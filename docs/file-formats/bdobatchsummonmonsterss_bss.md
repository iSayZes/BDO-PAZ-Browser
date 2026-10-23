# `bdobatchsummonmonsterss.bss` Format

## Purpose

A PABR table of the party summon scrolls: the party leader (or a player
with no party) summons with `ToClient_RequestBatchSummonMonster(summonKey,
summonLevel)` in `panel_batchsummonmonster.luac`, which shows the level
with the Ancient Ruins raid party text `LUA_ANCIENT_RUINS_RAID_PARTY_LEVEL`.
Each row is one summon level of one scroll: the summoned monster and the
AP, damage reduction, evasion, accuracy and HP added to it. On client 3482
it holds 20 rows of six scrolls, among them the Ancient Relic Crystal
Summon Scroll (`41583`, levels 1 to 5), Cartian Spell (`41587`), Pila Fe
Scroll (`41595`), Manshaum Narc's Stone (`41619`), Ibedor's Scroll
(`65771`) and Rift's Echo (`721058`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | ------- | --------- |
| 3      | 2959 and later | 3482    | `bdobatchsummonmonsterss.bss` | 700   | 20 Row  | 34        |
| 2      | 1784 to 2923   | 2923    | `bdobatchsummonmonsterss.bss` | 780   | 20 Row  | 38        |
| 1      | 1749           | 1749    | `bdobatchsummonmonsterss.bss` | 214   | 5 Row   | 38        |

| Layout | File                          | Known          | Unknown      |
| ------ | ----------------------------- | -------------- | ------------ |
| 3      | `bdobatchsummonmonsterss.bss` | 700 B (100.0%) | 0 B (0.0%)   |
| 2      | `bdobatchsummonmonsterss.bss` | 700 B (89.7%)  | 80 B (10.3%) |
| 1      | `bdobatchsummonmonsterss.bss` | 190 B (88.8%)  | 24 B (11.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 3 |
| 3474   | Layout 3 |
| 3454   | Layout 3 |
| 3412   | Layout 3 |
| 3381   | Layout 3 |
| 3349   | Layout 3 |
| 3314   | Layout 3 |
| 3283   | Layout 3 |
| 3251   | Layout 3 |
| 3212   | Layout 3 |
| 3177   | Layout 3 |
| 3144   | Layout 3 |
| 3103   | Layout 3 |
| 3062   | Layout 3 |
| 3037   | Layout 3 |
| 3002   | Layout 3 |
| 2959   | Layout 3 |
| 2923   | Layout 2 |
| 2900   | Layout 2 |
| 2872   | Layout 2 |
| 2834   | Layout 2 |
| 2803   | Layout 2 |
| 2765   | Layout 2 |
| 2736   | Layout 2 |
| 2703   | Layout 2 |
| 2665   | Layout 2 |
| 2637   | Layout 2 |
| 2606   | Layout 2 |
| 2583   | Layout 2 |
| 2545   | Layout 2 |
| 2519   | Layout 2 |
| 2498   | Layout 2 |
| 2468   | Layout 2 |
| 2438   | Layout 2 |
| 2414   | Layout 2 |
| 2384   | Layout 2 |
| 2358   | Layout 2 |
| 2335   | Layout 2 |
| 2313   | Layout 2 |
| 2290   | Layout 2 |
| 2250   | Layout 2 |
| 2224   | Layout 2 |
| 2203   | Layout 2 |
| 2179   | Layout 2 |
| 2151   | Layout 2 |
| 2134   | Layout 2 |
| 2107   | Layout 2 |
| 2073   | Layout 2 |
| 2052   | Layout 2 |
| 2011   | Layout 2 |
| 1996   | Layout 2 |
| 1969   | Layout 2 |
| 1937   | Layout 2 |
| 1914   | Layout 2 |
| 1886   | Layout 2 |
| 1866   | Layout 2 |
| 1838   | Layout 2 |
| 1818   | Layout 2 |
| 1794   | Layout 2 |
| 1784   | Layout 2 |
| 1749   | Layout 1 |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1137   | No file  |
| 1132   | No file  |
| 1127   | No file  |
| 1122   | No file  |
| 1118   | No file  |
| 1114   | No file  |
| 1109   | No file  |
| 1102   | No file  |
| 1096   | No file  |
| 1088   | No file  |
| 1081   | No file  |
| 1076   | No file  |
| 1069   | No file  |
| 1064   | No file  |
| 1058   | No file  |
| 1051   | No file  |
| 1044   | No file  |
| 1036   | No file  |
| 1026   | No file  |
| 1016   | No file  |
| 1009   | No file  |
| 1005   | No file  |
| 1000   | No file  |
| 998    | No file  |
| 990    | No file  |
| 979    | No file  |
| 972    | No file  |
| 963    | No file  |
| 955    | No file  |
| 946    | No file  |
| 938    | No file  |
| 927    | No file  |
| 911    | No file  |
| 904    | No file  |
| 899    | No file  |
| 894    | No file  |
| 885    | No file  |
| 879    | No file  |
| 872    | No file  |
| 864    | No file  |
| 855    | No file  |
| 853    | No file  |
| 845    | No file  |
| 837    | No file  |
| 829    | No file  |
| 822    | No file  |
| 814    | No file  |
| 805    | No file  |
| 794    | No file  |
| 787    | No file  |
| 780    | No file  |
| 771    | No file  |
| 760    | No file  |
| 748    | No file  |
| 741    | No file  |
| 736    | No file  |
| 731    | No file  |
| 723    | No file  |
| 711    | No file  |
| 707    | No file  |
| 697    | No file  |
| 689    | No file  |
| 683    | No file  |
| 678    | No file  |
| 670    | No file  |
| 661    | No file  |
| 656    | No file  |
| 652    | No file  |
| 643    | No file  |
| 637    | No file  |
| 630    | No file  |
| 627    | No file  |
| 621    | No file  |
| 617    | No file  |
| 615    | No file  |
| 606    | No file  |
| 599    | No file  |
| 592    | No file  |
| 586    | No file  |
| 577    | No file  |
| 569    | No file  |
| 561    | No file  |
| 554    | No file  |
| 542    | No file  |
| 532    | No file  |
| 531    | No file  |
| 526    | No file  |
| 521    | No file  |
| 517    | No file  |
| 510    | No file  |
| 508    | No file  |
| 504    | No file  |
| 497    | No file  |
| 491    | No file  |
| 485    | No file  |
| 478    | No file  |
| 472    | No file  |
| 466    | No file  |
| 457    | No file  |
| 452    | No file  |
| 449    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                          |
| --------------------- | -------- | --------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) and character names (LOC type 6) |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (34 bytes)

| Offset  | Type | Field         | Notes                                                                    |
| ------- | ---- | ------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | summon_key    | Row key, `summon_level << 24 \| item_key`                                 |
| `+0x04` | u32  | item_key      | The summon scroll, an `itemenchant.dbss` item ID                         |
| `+0x08` | u32  | summon_level  | `1` to `5`                                                               |
| `+0x0C` | f32  | added_dd      | AP added to the summoned monster                                         |
| `+0x10` | f32  | added_pv      | Damage reduction added                                                   |
| `+0x14` | f32  | added_dv      | Evasion added; equal to `added_pv` on every row of client 3482           |
| `+0x18` | f32  | added_hit     | Accuracy added                                                           |
| `+0x1C` | f32  | added_hp      | HP added                                                                 |
| `+0x20` | u16  | character_key | The summoned monster, a `characterstatic.dbss` key (LOC type 6 name)     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 2

### Row (38 bytes)

| Offset  | Type | Field                  | Notes                                                       |
| ------- | ---- | ---------------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | summon_key             | Row key, `summon_level << 24 \| item_key`                    |
| `+0x04` | u32  | item_key               | The summon scroll                                           |
| `+0x08` | u32  | summon_level           | `1` to `5`                                                  |
| `+0x0C` | f32  | added_dd               | AP added                                                    |
| `+0x10` | f32  | added_pv               | Damage reduction added                                      |
| `+0x14` | f32  | added_dv               | Evasion added; `0` on every row of client 1784              |
| `+0x18` | f32  | added_hit              | Accuracy added                                              |
| `+0x1C` | f32  | added_hp               | HP added                                                    |
| `+0x20` | f32  | unknown_after_added_hp | `0` on every row of client 1784; Layout 3 drops it          |
| `+0x24` | u16  | character_key          | The summoned monster                                        |

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                                 |
| ------------------- | -------------- | ------------ | ----------------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                          |
| `+0x04`             | u32            | unknown_04   | `5` on client 1749, equal to `row_count`              |
| `+0x08`             | u32            | row_count    | Number of rows                                        |
| `+0x0C`             | Row[row_count] | rows         | See Row                                               |
| `rows+0x00`         | String Table   | string_table | See String Table                                      |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends         |
| `string_table+0x04` | u32            | zero         | Always `0`                                            |

## Field Names

The names are the `BatchSummonMonsterStaticStatus` members that the
server dump of a private server on client 1784 names in its load checks
(`_addedDD`, `_addedPV`, `_addedDV`, `_addedHit`, `_addedHp`, `_itemKey`,
`_characterKey`, `_summonLevel`). The `BatchSpawnMonsterByItem` sheet of
that server's `DataSheets.bexcel` matches the client 1784 file by value on
6 of 6 rows: `TargetItemkey` is `item_key`, `SummonLevel` is
`summon_level`, `AddedDD`, `AddedPV`, `AddedHit` and `AddedHP` are the
fields of the same names, and `MonsterKey` is `character_key`. The live
file of client 3482 holds the same values for those 6 keys.

`AddedDV` and `AddedCri` are `0` on every sheet row, so the values do not
place them. `added_dv` is the f32 after `added_pv` by the member order of
the load checks (`_addedPV`, then `_addedDV`, then `_addedHit`), and
client 3482 sets it to the `added_pv` value. The f32 that Layout 2 holds
after `added_hp` is the one column left, `AddedCri`, but no client data
confirms it, so it stays `unknown_after_added_hp`. The sheet's
`MaxCount`, `DropGroupKey` and `GroupDrop0` to `GroupDrop4` columns are
not in the client file.

## Notes

- Layout 1 (client 1749, the first client with the file) stores a u32
  before `row_count` that equals it: 5 rows, levels 1 to 5 of `41583`.
- `summon_key` packs the level into the top byte of the item key, as
  [`elementalmonsterreward.bss`](elementalmonsterreward_bss.md) packs an
  enchant level: `0x0100A26F` is level 1 of item `41583`.
- The rows of one scroll can name different monsters per level: levels 1
  to 3 of `41583` summon Ancient Relic Crystal `22649`, levels 4 and 5 the
  Ancient Relic Crystal `22600`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`.

## Open Questions

### The Dropped Field of Layout 2

Layout 2 holds an f32 after `added_hp` that is `0` on every row of client
1784; it would be the sheet's `AddedCri` column, the one sheet stat with
no load check in the server dump. Layout 3 no longer has it.
