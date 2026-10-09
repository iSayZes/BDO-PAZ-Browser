# `instancefield.dbss` Format

## Purpose

The instance fields: separate copies of a world area that a group enters
(Solare arenas, Atoraxion, node and siege war maps, horse race tracks, guild
matches, test fields). Each record has a key, an area of the world given in
sectors, and an internal ASCII name. `buff.dbss` effect type 176 stores the
key in `param_3` (`Teleport to Instance Field The Magnus: The Great Single
Path (A1_001)`).

Example:

```text
key 150   Atoraxion_Desert   x 46..52  y -2..5  z -33..-28
  sector 56, 2, -35 holds the teleport.dbss point of buff 42791
  "아토락시온 포탈 : 사막 : 2구역 입장" ("Atoraxion portal: desert: enter zone 2")
```

## Companion Files

| File                       | Required | Role                                                         |
| -------------------------- | -------- | ------------------------------------------------------------ |
| `instancefieldoffset.dbss` | Optional | Index of the records by key, see below; not needed to read this file |

All multi-byte values are little-endian.

## File Layout

A count followed by variable-size records. No PABR magic and no trailer; the
records fill the file exactly (199 records, 10,736 bytes on client 3464).

| Offset  | Type | Field   | Notes                         |
| ------- | ---- | ------- | ----------------------------- |
| `+0x00` | u32  | count   | Number of records             |
| `+0x04` | ...  | records | `count` x record, not sorted by key |

### Record (40 bytes + name)

| Offset      | Type    | Field         | Notes |
| ----------- | ------- | ------------- | ----- |
| `+0x00`     | u16     | key           | Unique; `0` to `9876` |
| `+0x02`     | i32     | min_x         | Sector box, lower corner; one sector is 12,800 world units (128 m), see Notes |
| `+0x06`     | i32     | min_y         | Height |
| `+0x0A`     | i32     | min_z         | |
| `+0x0E`     | i32     | max_x         | Sector box, upper corner; never below the matching `min_*` |
| `+0x12`     | i32     | max_y         | |
| `+0x16`     | i32     | max_z         | |
| `+0x1A`     | u32     | unknown_1a    | `1`, `2` or `3`; see Open Questions |
| `+0x1E`     | u64     | name_length   | Byte length of `name` |
| `+0x26`     | char[n] | name          | ASCII, not null-terminated |
| `+0x26 + n` | u16     | unknown_tail  | `1`, or the record's own key on the `A1_` fields; see Open Questions |

Names are not unique: on client 3464 the 199 records carry 163 names, and
`Edania_Field` / `Edania_Field_1vs1` (10 each), `CrimsonField` (6),
`CrimsonField2` (6), `CrimsonField3` (4), `Solare_Arena_Common` (4) and `ABSO`
(3) repeat with different keys.

## `instancefieldoffset.dbss`

A u32 count followed by `count` 10-byte rows, no header or trailer (1,994
bytes on client 3464).

| Offset  | Type | Field  | Notes |
| ------- | ---- | ------ | ----- |
| `+0x00` | u16  | key    | Record key |
| `+0x02` | u32  | offset | `instancefield.dbss` offset of the record with this key |
| `+0x06` | u32  | size   | Byte size of that record, `40 + name_length` |

The rows are in a hash order (`80, 16, 4053, 0, 4035, ...`), not file
order. Every row points at the start of the record with the same key and
gives its exact size, so the index adds nothing to a sequential read.

## Suggested UI Layout

| Column    | Type | Notes                                             |
| --------- | ---- | ------------------------------------------------- |
| Key       | num  | `key`; right-aligned; what buff type 176 stores  |
| Name      | text | `name`                                            |
| Title     | text | The `instancefieldmapinfo.bss` title in the loaded language (`INSTANCE_FIELD_TITLE`); dash without one |
| Sector X  | num  | `min_x..max_x` (`46..52`); sorts by `min_x`       |
| Sector Y  | num  | `min_y..max_y`; sorts by `min_y`                  |
| Sector Z  | num  | `min_z..max_z`; sorts by `min_z`                  |

## Notes

- The box unit is a 12,800-unit sector of the world frame that
  `teleport.dbss` and `mapdata_realexplore2.bwp` use. Divided by 12,800 and
  floored, the `teleport.dbss` points of the Atoraxion portal buffs
  (`아토락시온 포탈 : 사막 : 2구역 입장`, `아토락시온 포탈 : 해저 : 3구역
  입장`) fall inside the `Atoraxion_*` boxes, `벨리아 > 수궁` ("Velia > Sea
  Palace") inside `Yonggung`, and point 277 (`x -1460010, z 1419360`, sector
  `-114, 110`) inside `Solare_Arena_Janghwa` (`-117..-113, 109..113`) in the
  Land of the Morning Light. At 25,600 or 6,400 per sector those points
  leave their boxes. The check counted both bounds as inside.
- Boxes overlap the open world and each other: an instance field is a copy
  of a world area, so many open-world teleport points also fall in a box.
  The `MajorSiege_*` boxes cover whole territories (`MajorSiege_Valencia`
  `x 25..100`).
- The `INSTANCE_FIELD_NAME` lookup index maps each key to its name, so the
  `buff.dbss` Effect text of type 176 names the field without opening this
  file, after the `instancefieldmapinfo.bss` title: `Teleport to Instance
  Field The Magnus: The Great Single Path (A1_001)`.
- The 66 `A1_` fields (keys 4001 to 4066, names `A1_001` to `A1_066`) share
  the box `-3..3` on every axis, around the world origin. Items and skills
  named `A1_001` to `A1_054` apply the type 176 buffs that send a player
  there (`buff_dbss.md`).
- [instancefieldmapinfo.bss](instancefieldmapinfo_bss.md) holds the map
  data under the same keys: a `GAME` sheet name and description
  (`A1_001` is "The Magnus: The Great Single Path"), a map image, a centre
  point, an entry item and team spawn points. The other
  `instancefield*` tables (`instancefieldcommon.bss`,
  `instancefieldranking.bss`, `instancefieldreward.dbss`,
  `instancefieldcommonlimitentertime.bss`) have their own layouts.

## Open Questions

### What does `unknown_1a` mark?

On client 3464 it is `1` on 189 records, `3` on `Shadow_Ser_Main` (key 1)
and `2` on nine: keys 2 to 8 (`1`, `3_Ser_CentralGuardCamp`,
`4_Bal_Ehwaz`, `5_Cal_CalpheonCastle`, `6_Cal_SounilFortress`,
`7_Val_Desert`, `8_Kam_Naban`) and 98 / 99 (`Practice1`, `Practice`). None
of these ten has an `instancefieldmapinfo.bss` record, while every field with
`1` has one except `PlayGround` (9), `InfinityDefence_Sub_Main` (888),
`InfinityDefence_Main` (999) and `SiegeofThornCastle` (9876). The `2` names
read like node war maps per territory, which suggests a field kind, but no
client enum names the values. The Lua calls
`ToClient_GetInstanceFieldMapKeyInfoByTypeAndIndex` and
`ToClient_InstanceFieldRoomInfoWrapperWithType` take a type, which may be
this field.

### What does `unknown_tail` hold?

It is `1` on the 133 named fields and equals the record's own key on all 66
`A1_` fields (4001 to 4066). The Lua function `getInstanceFieldMapKey` hints
at a map key separate from the field key, but `instancefieldmapinfo.bss` is
keyed by the field key itself and has no record 1, so it is not that map
key.
