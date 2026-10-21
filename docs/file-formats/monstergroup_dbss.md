# `monstergroup.dbss` Format

## Purpose

Monster groups: per group key a list of monster character keys, each with a
`percent` on the 1,000,000 = 100% scale. The groups are hunting zones: on
client 3474, 29 of the 35 groups with members have every member in one
[`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) hunting ground
(see Notes). `monstergroupoffset.dbss` is required to address the
variable-length records.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records                                | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | -------------------------------------- | --------- |
| 1      | 1784 and later | 3474    | `monstergroup.dbss`       | 1,402 | 185 Member, 36 Group Record, 36 Record | 6         |
| 1      | 1784 and later | 3474    | `monstergroupoffset.dbss` | 364   | 36 Offset Row                          | 10        |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `monstergroup.dbss`       | 1,402 B (100.0%) | 0 B (0.0%) |
| 1      | `monstergroupoffset.dbss` | 364 B (100.0%)   | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                      |
| ------------------------- | -------- | --------------------------------------------------------- |
| `monstergroupoffset.dbss` | Required | Bare u16-keyed index: group key -> record offset and size |
| `languagedata_en.loc`     | Optional | Monster names, LOC type 6 at `str_id1` = `character_key`  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                  |
| ------- | ------------- | ------- | -------------------------------------- |
| `+0x00` | u32           | count   | Same count as the offset table         |
| `+0x04` | Record[count] | records | See Record; in offset-table order      |

The records end exactly at the end of the file.

### Record (variable: 2 bytes + group)

Each record is preceded by a copy of its u16 key. The offset of a row points
past that copy, at the group's own key, as in
[`worldmapmonster.dbss`](worldmapmonster_dbss.md).

| Offset  | Type         | Field      | Notes                                                    |
| ------- | ------------ | ---------- | -------------------------------------------------------- |
| `+0x00` | u16          | key_prefix | Copy of the group's `group_key`                          |
| `+0x02` | Group Record | group      | `size` bytes of the offset row; the offset row points here |

### Group Record (variable: 6 bytes + members)

| Offset  | Type                  | Field        | Notes                                              |
| ------- | --------------------- | ------------ | -------------------------------------------------- |
| `+0x00` | u16                   | group_key    | Same as the offset row `group_key`                 |
| `+0x02` | u32                   | member_count | Number of members; `0` on group 18 (client 3474)   |
| `+0x06` | Member[member_count]  | members      | See Member; ascending `character_key` in every group |

`6 + 6 * member_count` equals the offset row `size` on every record.

### Member (6 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | Monster character key; LOC type 6 names it                            |
| `+0x02` | u32  | percent       | On the 1,000,000 = 100% scale; `1,000,000` on the last member of every group, see `percent` Values |

### `monstergroupoffset.dbss`

No magic and no trailer (`parse_bare_offset_rows()`).

| Offset  | Type              | Field | Notes          |
| ------- | ----------------- | ----- | -------------- |
| `+0x00` | u32               | count | Number of rows |
| `+0x04` | Offset Row[count] | rows  | See Offset Row |

The rows are in file order, which is not key order: on client 3474 the keys
run 36 to 32, 15 to 1, then 31 to 16.

### Offset Row (10 bytes)

| Offset  | Type | Field     | Notes                                                        |
| ------- | ---- | --------- | ------------------------------------------------------------ |
| `+0x00` | u16  | group_key | Group key                                                    |
| `+0x02` | u32  | offset    | Start of the group record in `monstergroup.dbss`, past the key copy |
| `+0x06` | u32  | size      | Length of the group record, the key copy left out           |

## `percent` Values

Each member's `percent` is `1,000,000 / k` rounded, where `k` counts the
members from this one to the end of the group (within 2 on all 185 members,
client 3474). A group of five stores `200,000`, `250,000`, `333,334`,
`500,001`, `1,000,000`. Picking each member in list order with its own
chance, and moving on when it is not picked, gives every member the same
chance of `1 / member_count`. Read as cumulative chances, the values would
have to rise by equal steps (`200,000`, `400,000` ...); they do not.

## Field Names

The fields are named from the `MonsterGroup` sheet of a private server's
`DataSheets.bexcel` on client 1784 (columns `Group`, `Character`,
`Percent`). All 185 (group, character) pairs of client 3474 are sheet rows,
and all 185 have the same `Percent`. The sheet has 188 rows; the 3 extra are
group 18 (`21035` to `21037`, the Basilisk Den monsters), which has no
members in the client file on clients 1784 and 3474. None of the three keys
has a `characterstatic.dbss` row on either client, so the client build leaves
out members whose character it does not ship.

The `.xlsm` copy of the sheet has two note columns that are not compiled:
`#GroupName`, a hunting zone name per group (`폐철광산`, Abandoned Iron Mine,
for group 2; group 1 is `세렌디아 북부 평원 (테스트용)`, marked as a test
group), and `#MonsterName`. The 2016 client has no monster group table: its
PDB holds `gc::KillMonsterGroup` (the quest condition) but no
`gc::MonsterGroup*` struct or loader.

## Regions per Group

The regions whose `MonsterGroupForTotem` column in the `Region_Table` sheet
(client 1784) names each group. Region names and territories come from
[`regioninfo.bss`](regioninfo_bss.md) on client 3474. No region names groups
1 (the Altar Imp test group), 5 (Helm) or 9 (Shultz Guard).

| Group | Regions                                                                                         | Territory  | Members                                     |
| ----: | ----------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------- |
| 2     | 211 Abandoned Iron Mine, 555 Rhutum District, 556 Saunil District, 557 Entrance (same mine)     | Mediah     | Rhutum, Red Orc, Saunil and Khuruto (11)    |
| 3     | 35 Northern Plain of Serendia (Serendia), 213 Manes Hideout                                     | Mediah     | Manes (4)                                   |
| 4     | 214 Wandering Rogue Den                                                                         | Mediah     | Wandering Rogues, Servant of Darkness (4)   |
| 6     | 210 Canyon of Corruption                                                                        | Mediah     | Elric cultists, Decayed Swamp Monster (6)   |
| 7     | 417 Soldier's Cemetery                                                                          | Mediah     | Frenzied and Grudged Skeletons (6)          |
| 8     | 327 Sausan Garrison, 415 Sausan Garrison Wharf                                                  | Mediah     | Sausan soldiers (8)                         |
| 10    | 216 Hasrah Cliff                                                                                | Mediah     | Kamol, Balten, Kukuri, Buruko, Kamel (5)    |
| 11    | 241 Bashim Base, 585 and 674 Pujiya Canyon                                                      | Valencia   | Ohonsey, Terruda and Khala (10)             |
| 12    | 623 Titium Valley                                                                               | Valencia   | Desert Fogans (4)                           |
| 13    | 607 Desert Naga Temple                                                                          | Valencia   | Desert Nagas (3)                            |
| 14    | 603 and 678 Gahaz Bandits' Lair                                                                 | Valencia   | Sandstorm bandits (4)                       |
| 15    | 579 and 631 Cadry Ruins                                                                         | Valencia   | Cadry Fighter, Black Mage, Armored Fighter  |
| 16    | 622 Crescent Shrine, 625 Crescent Mountains                                                     | Valencia   | Crescent Watcher, Follower, Guardian        |
| 17    | 243 Taphtar Plain                                                                               | Valencia   | Centaurus (3)                               |
| 18    | 578 and 630 Gorgo Rock Belt, 632 Basilisk Den, 655 Basilisk Cave                                | Valencia   | none in the client file                     |
| 19    | 691 Pila Ku Jail                                                                                | Valencia   | Pila Ku Jail inmates and warders (6)        |
| 20    | 420 Roud Sulfur Works, 690 Roud Sulfur Mine                                                     | Valencia   | Lava monsters (6)                           |
| 21    | 688 Aakman Temple                                                                               | Valencia   | Aakman (7)                                  |
| 22    | 689 Hystria Ruins                                                                               | Valencia   | Kalqueesh, Vodkhan, Tukars and others (8)   |
| 23    | 736 and 747 Polly's Forest                                                                      | Kamasylvia | Poison mushrooms (5)                        |
| 24    | 728 and 746 Loopy Tree Forest                                                                   | Kamasylvia | Fadus (5)                                   |
| 25    | 708 Navarn Steppe                                                                               | Kamasylvia | Belladonna Elephant, Feather Wolf and others (5) |
| 26    | 711 Manshaum Forest, 723 Manshaum Forest Path                                                   | Kamasylvia | Manshaum (5)                                |
| 27    | 729 and 745 Tooth Fairy Forest                                                                  | Kamasylvia | Forest Ronaros (4)                          |
| 28    | 712 Mirumok Ruins, 722 Mirumok Ruins Entrance                                                   | Kamasylvia | Mirumok, Treants, Voraro (5)                |
| 29    | 739 and 755 Gyfin Rhasia Temple                                                                 | Kamasylvia | Gyfin Rhasia (4)                            |
| 30    | 895 and 934 Tshira Ruins                                                                        | Drieghan   | Tree Hermit, Keepers and others (7)         |
| 31    | 876 and 930 Blood Wolf Settlement                                                               | Drieghan   | Kagtum (6)                                  |
| 32    | 875 and 927 Sherekhan Necropolis                                                                | Drieghan   | Garud, Lateh, Belcadas, Nybrica, Federik    |
| 33    | 948 Protty Cave                                                                                 | Balenos    | Protty, Zera Protty, Kaz Protty             |
| 34    | 952 Sycraia Underwater Ruins                                                                    | Balenos    | Damaged Pirash, Lykin, Kureba               |
| 35    | 949 Sycraia Underwater Ruins                                                                    | Balenos    | Pirash, Lykin, Kureba, Elmermol             |
| 36    | 971 and 977 Star's End                                                                          | Calpheon   | Apostles and Harbingers (6)                 |

Group 3 is the only one that spans two territories: region 35 is in
Serendia, region 213 in Mediah.

## Notes

- The `Region_Table` sheet of the same `DataSheets.bexcel` points 57 regions
  at 33 groups (all but 1, 5 and 9) through its `MonsterGroupForTotem`
  column; see Regions per Group. That column is not in the client
  [`regioninfo.bss`](regioninfo_bss.md), so on the client nothing links a
  region to its group.
- Group to hunting ground, matched by members against
  [`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) on client
  3474: 29 of the 35 non-empty groups have every member in one hunting ground
  (group 2 in `Lv.51 폐철광산`, 11 of 11). Groups 4 and 12 have all but one
  member in one hunting ground (3 of 4). Groups 1 (Altar Imp and four
  more), 34 (Damaged Pirash and two more), 35 (Pirash and three more) and 36
  (Apostle of Corruption and five more) share no member with any hunting
  ground.
- `<Violent>` monsters: LOC type 6 gives 111 characters the title prefix
  `<Violent>` (`str_id4` = 1, client 3474), each a separate character key
  with the name of a regular monster. Every member of groups 13, 14, 16,
  19, 21 and 22 has a `<Violent>` character with the same name, and 3 of 4
  members of group 12 do. These seven groups belong to the seven zones that
  LOC type 10 lists as `[Hardcore] Violent ... Teleport` (49502 to 49507,
  49523): Titium Valley, Desert Naga Temple, Gahaz Bandits' Lair, Crescent
  Shrine, Pila Ku Jail, Aakman Temple and Hystria Ruins. In the other groups
  at most 2 members have one.
- The client Lua does not name the file: no `.luac` file of client 3474
  holds the string `monstergroup` or `totem`.
- The bytes are the same on clients 1784 and 3474 (1,402 and 364 bytes).
- The quest condition `killMonsterGroup(group, count)` does not read this
  file: its key is the `character_group` of
  [`characterstatic.dbss`](characterstatic_dbss.md#character-group). The
  2016 `gc::KillMonsterGroup` stores the first argument as
  `_characterGroupKey` (`gc::KeyType<short,-1>`, the type of the
  character's `_groupKey`), and on client 3474 every key of the 878
  `killMonsterGroup` calls in `quest.dbss` and the 16 in
  [`guildquest.dbss`](guildquest_dbss.md) (`84` and `125`) is a
  `character_group` value. The two key sets overlap without matching: Star's
  End is group 36 here and character group 116, and character group 36 is
  the Calpheon Shrine.

## Open Questions

### What Reads the Groups

The server column `MonsterGroupForTotem` says a region uses its group for a
totem, and the `percent` values make one member pick with equal chances.
Nothing on the client names the feature: the Lua never names the file, and
the first 40 English LOC matches for `totem` are item names (Manshaum Totem,
Totem of the Sea). Which monster a region's totem spawns or targets, and
whether the client uses the file at all, is open.
