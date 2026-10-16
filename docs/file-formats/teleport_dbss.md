# `teleport.dbss` Format

## Purpose

The destinations of teleport buffs: world positions grouped into sections and
keyed within each section. A `buff.dbss` effect type 23 buff stores the
section in `param_1` and the key in `param_2`; using the item moves the player
to that point. The file holds positions only, no names.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                        |
| ---------------------- | -------- | ----------------------------------------------------------- |
| `teleportoffset.dbss`  | Optional | Positional index of the records, see below; not needed to read this file |
| `mapdata_realexplore2.bwp` | Optional | Worldmap nodes in the same coordinate frame, to place a point |
| `buff.dbss`            | Optional | The type 23 buffs that teleport to each point, through the `TELEPORT_BUFFS` lookup index |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The file is a list of sections, each a counted run of fixed 18-byte records.
It walks exactly to its last byte on client 3458 (11,206 bytes).

| Offset  | Type                   | Field         | Notes                                       |
| ------- | ---------------------- | ------------- | ------------------------------------------- |
| `+0x00` | u32                    | section_count | `6` on client 3458                          |
| `+0x04` | Section[section_count] | sections      | Sections in order 0, 1, 2, ...; see Section |

### Section (variable: 4 bytes + records)

| Offset  | Type          | Field   | Notes                             |
| ------- | ------------- | ------- | --------------------------------- |
| `+0x00` | u32           | count   | Number of records; `0` is allowed |
| `+0x04` | Record[count] | records | See Record                        |

### Record (18 bytes)

| Offset  | Type | Field       | Notes |
| ------- | ---- | ----------- | ----- |
| `+0x00` | u32  | key         | Unique within its section, not across sections; not sorted in section 0 and 5 (section 0 runs 0 to 1034 over 426 records) |
| `+0x04` | u8   | section     | Always the index of the section the record sits in |
| `+0x05` | f32  | x           | World position, the frame of `exploration.bss` and `mapdata_realexplore2.bwp` (centimetres) |
| `+0x09` | f32  | y           | Height |
| `+0x0D` | f32  | z           | |
| `+0x11` | u8   | unknown_11  | `0` on 612 of 621 records; see Open Questions |

### `teleportoffset.dbss`

The same sections as `teleport.dbss`, in the same order, each a counted list
of 12-byte rows. Unlike `teleport.dbss` it has no section count: the first
section starts at `+0x00` and the sections run to the end of the file, which
they fill exactly (7,476 bytes).

| Offset  | Type                  | Field    | Notes                                         |
| ------- | --------------------- | -------- | --------------------------------------------- |
| `+0x00` | Offset Section[..end] | sections | Up to the end of the file; see Offset Section |

### Offset Section (variable: 4 bytes + rows)

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the record count of the same section |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field  | Notes |
| ------- | ---- | ------ | ----- |
| `+0x00` | u32  | index  | Position of the record within its section, `0` to `count - 1` |
| `+0x04` | u32  | offset | `teleport.dbss` offset of that record: section start + `18 * index` on every row |
| `+0x08` | u32  | size   | Always `18` |

The rows are in a hash order (section 0 starts `399, 0, 1, 393, 2, 3, 387,
4`), and `index` is a position, not the record's `key`. The two agree only
where a section's keys run `0` to `count - 1` in order (sections 1 and 2).
Read as a key, the section 0 rows point 14.5 km (median) away from the places
the buff texts name, against 73 m through the inline keys, so readers look
records up by the inline `key` and do not need this file.

## Sections on Client 3458

| Section | Records | Used by (buff type 23, Korean names) |
| ------- | ------: | ------------------------------------ |
| 0       | 426     | 470 buffs: travel items and quest moves, `발자국 : 잔해의 해안` ("footprints: Shore of Ruins", `Move to Shore of Ruins`), `출입 통과 : 오르의 요람` ("entry pass: Orze's Cradle") |
| 1       | 9       | 1 buff, `발렌시아 파트2 던전 무작위 순간이동` ("Valencia part 2 dungeon random teleport") |
| 2       | 3       | No buff                              |
| 3       | 0       | 1 buff, `단방향(마을) 귀환석` ("one-way (town) return stone"), key 0 |
| 4       | 0       | 1 buff, `벨리아 마을 귀환석` ("Velia town return stone"), key 5 |
| 5       | 183     | 181 buffs: boss rooms, event gimmicks and unstuck moves, `하둠 보스용 블랙홀 1번` ("Hadum boss black hole 1"), `이벤트 선물상자 끼이는 현상 방지 텔레포트` ("teleport against getting stuck in the event gift box") |

652 of the 654 type 23 buffs name a record that exists; the other two are the
return stones on the empty sections 3 and 4, whose destination is resolved
elsewhere. 22 of the 621 records are used by no buff.

## Notes

- Positions were checked against the type 23 buffs whose English text names
  a worldmap node: `Footprints: Flower-sunken Swamp`, `Mongryong's Exile` and
  `Martial God Tournament` lie within 1 m of their node, `Holbon Entrance`
  3 m, and 8 of 14 such points lie within 100 m. Points inside instanced
  areas (Orzekea, `Instantly teleport to Orze's Garden`) lie kilometres from
  any node.
- `mapdata_realteleport.xml` / `.bwp` in `gamecommondata/waypoint/` is a
  different set: its 293 waypoints have numeric names, and only 3 lie within
  5 m of a teleport point.
- `magnuseasyteleport.bss` (1.1 KB, PABR) holds the Abyss One Magnus teleport
  map; not read here.

## Open Questions

### What does `unknown_11` mark?

Nine section 0 records set it: keys 1 and 23 store `1` (buffs to the Ancient
Stone Chamber), 2 and 24 store `2` (Valencia, Gyfin Rhasia Temple), and 260,
231, 253, 257 and 259 store `85`, `90`, `99`, `32` and `96` (an indoor point
after a street battle, Muzgar Village, a watchtower, the Northern Wheat
Plantation and a troll defence base). No
other field or buff parameter follows it.

### What do sections 1 and 2 serve?

Section 1 has one buff, a random teleport in the second Valencia dungeon,
whose `param_2` `0` picks one of nine points; section 2 has no buff. Some
other system (a dungeon script, an action chart) may pick points from them.
