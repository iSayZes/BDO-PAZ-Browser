# `audioinfo.bss` Format

## Purpose

The world's background music and ambience by area: per area colour of
the audio map image (`AudioMap.bmp`, the `audio_map_index` `7` of
[`fieldinfo.bss`](fieldinfo_bss.md)) the four Wwise `BGM` states
the area plays and its ambience index. Since the Wwise sound system
(client 1866) the file also lists the `BGM` states of a few special
situations and the radio channels of the radio player. Client 1784 holds
the older layout with sound bank and music numbers per situation.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes   | Records                                   | Row bytes |
| ------ | -------------- | ------- | --------------- | ------- | ----------------------------------------- | --------- |
| 6      | 2665 and later | 3482    | `audioinfo.bss` | 40,977  | 1,256 Row, 10 State Entry, 10 Radio Entry | 28        |
| 5      | 2011 to 2637   | 2637    | `audioinfo.bss` | 36,534  | 1,113 Row, 10 State Entry, 10 Radio Entry | 28        |
| 4      | 1969 to 1996   | 1996    | `audioinfo.bss` | 28,374  | 831 Row, 9 State Entry, 10 Radio Entry    | 28        |
| 3      | 1914 to 3482   | 3482    | `audioinfo.bss` | 40,977  | 1,256 Row, 10 State Entry, 10 Radio Entry | 28        |
| 2      | 1866 to 1937   | 1937    | `audioinfo.bss` | 27,671  | 831 Row, 8 State Entry                    | 28        |
| 1      | 1109 to 1838   | 1838    | `audioinfo.bss` | 132,980 | 831 Row                                   | 160       |

| Layout | File            | Known             | Unknown        |
| ------ | --------------- | ----------------- | -------------- |
| 6      | `audioinfo.bss` | 40,846 B (99.7%)  | 131 B (0.3%)   |
| 5      | `audioinfo.bss` | 36,443 B (99.8%)  | 91 B (0.2%)    |
| 4      | `audioinfo.bss` | 28,285 B (99.7%)  | 89 B (0.3%)    |
| 3      | `audioinfo.bss` | 40,846 B (99.7%)  | 131 B (0.3%)   |
| 2      | `audioinfo.bss` | 27,655 B (99.9%)  | 16 B (0.1%)    |
| 1      | `audioinfo.bss` | 129,656 B (97.5%) | 3,324 B (2.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 6             |
| 3474   | Layout 6             |
| 3454   | Layout 6             |
| 3412   | Layout 6             |
| 3381   | Layout 6             |
| 3349   | Layout 6             |
| 3314   | Layout 6             |
| 3283   | Layout 6             |
| 3251   | Layout 6             |
| 3212   | Layout 6             |
| 3177   | Layout 6             |
| 3144   | Layout 6             |
| 3103   | Layout 6             |
| 3062   | Layout 6             |
| 3037   | Layout 6             |
| 3002   | Layout 6             |
| 2959   | Layout 6             |
| 2923   | Layout 6             |
| 2900   | Layout 6             |
| 2872   | Layout 6             |
| 2834   | Layout 6             |
| 2803   | Layout 6             |
| 2765   | Layout 6             |
| 2736   | Layout 6             |
| 2703   | Layout 6             |
| 2665   | Layout 6             |
| 2637   | Layout 5             |
| 2606   | Layout 5             |
| 2583   | Layout 5             |
| 2545   | Layout 5             |
| 2519   | Layout 5             |
| 2498   | Layout 5             |
| 2468   | Layout 5             |
| 2438   | Layout 5             |
| 2414   | Layout 5             |
| 2384   | Layout 5             |
| 2358   | Layout 5             |
| 2335   | Layout 5             |
| 2313   | Layout 5             |
| 2290   | Layout 5             |
| 2250   | Layout 5             |
| 2224   | Layout 5             |
| 2203   | Layout 5             |
| 2179   | Layout 5             |
| 2151   | Layout 5             |
| 2134   | Layout 5             |
| 2107   | Layout 5             |
| 2073   | Layout 5             |
| 2052   | Layout 5             |
| 2011   | Layout 5             |
| 1996   | Layout 4             |
| 1969   | Layout 4             |
| 1937   | Layout 3             |
| 1914   | Layout 3             |
| 1886   | Layout 2             |
| 1866   | Layout 2             |
| 1838   | Layout 1             |
| 1818   | Layout 1             |
| 1794   | Layout 1             |
| 1784   | Layout 1             |
| 1749   | Layout 1             |
| 1717   | Layout 1             |
| 1698   | Layout 1             |
| 1674   | Layout 1             |
| 1636   | Layout 1             |
| 1608   | Layout 1             |
| 1587   | Layout 1             |
| 1565   | Layout 1             |
| 1537   | Layout 1             |
| 1509   | Layout 1             |
| 1485   | Layout 1             |
| 1466   | Layout 1             |
| 1445   | Layout 1             |
| 1426   | Layout 1             |
| 1409   | Layout 1             |
| 1390   | Layout 1             |
| 1372   | Layout 1             |
| 1360   | Layout 1             |
| 1348   | Layout 1             |
| 1338   | Layout 1             |
| 1324   | Layout 1             |
| 1316   | Layout 1             |
| 1309   | Layout 1             |
| 1286   | Layout 1             |
| 1256   | Layout 1             |
| 1230   | Layout 1             |
| 1211   | Layout 1             |
| 1194   | Layout 1             |
| 1177   | Layout 1             |
| 1156   | Layout 1             |
| 1127   | Layout 1             |
| 1109   | Layout 1             |
| 1076   | No file              |
| 1058   | No file              |
| 1016   | No file              |
| 990    | No file              |
| 955    | No file              |
| 911    | No file              |
| 885    | No file              |
| 855    | No file              |
| 822    | No documented layout |
| 794    | No documented layout |
| 748    | No documented layout |
| 711    | No documented layout |
| 683    | No documented layout |
| 656    | No documented layout |
| 630    | No documented layout |
| 606    | No documented layout |
| 577    | No documented layout |
| 542    | No documented layout |
| 526    | No documented layout |
| 508    | No documented layout |
| 485    | No documented layout |
| 457    | No documented layout |
| 435    | No documented layout |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 6

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[10]          | state_entries      | No count in the file; see State Entry Count             |
| `rows+0x64`               | u32                      | radio_count        | Number of `radio_entries`                                |
| `rows+0x68`               | Radio Entry[radio_count] | radio_entries      | See Radio Entry                                          |
| `radio_entries+0x00`      | u32                      | unknown_tail_count | Number of `unknown_tail` bytes                           |
| `radio_entries+0x04`      | u8[unknown_tail_count]   | unknown_tail       | 17 values from `0` to `60` in rising order on client 3482 |
| `unknown_tail+0x00`       | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table, where `unknown_tail` ends    |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

### Row (28 bytes)

| Offset  | Type   | Field               | Notes                                                                                     |
| ------- | ------ | ------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32    | color               | Area colour as `0x00RRGGBB`; each colour once                                             |
| `+0x04` | u32    | color_dup           | Equals `color` on every row                                                               |
| `+0x08` | u32[4] | bgm_states          | Indexes into `strings`: four states of the Wwise `BGM` state group (`W01_Balenos_Exploration_Motivated`); see BGM State Slots |
| `+0x18` | u32    | bank_no_environment | Ambience: the Wwise `ENV_INDEX_<n>` state; `0` on 226 of 1,256 rows (client 3482)         |

The rows are in no colour order.

### State Entry (10 bytes)

| Offset  | Type | Field       | Notes                                                                             |
| ------- | ---- | ----------- | --------------------------------------------------------------------------------- |
| `+0x00` | u8   | unknown_00  | `0` to `9`, each once, in no order (client 3482)                                  |
| `+0x01` | u8   | unknown_01  | `51` to `55`, or `255` on four entries                                             |
| `+0x02` | u32  | state_group | Index into `strings`: the Wwise state group, `BGM` on every entry                 |
| `+0x06` | u32  | state_name  | Index into `strings`: the state (`W00_ArenaOfSolare_Round_Start`)                 |

### Radio Entry (17 bytes)

| Offset  | Type | Field        | Notes                                                                                   |
| ------- | ---- | ------------ | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00   | `1` to `10` in file order on client 3482                                                |
| `+0x04` | u32  | unknown_04   | Index into `strings`: `Game_Start`, `Radio_Off` or an empty string                      |
| `+0x08` | u32  | channel_name | Index into `strings`: the channel title (`City Jazz Vibes (feat. Jazz in Black Desert)`), UTF-16LE; empty for entries 1 and 2 |
| `+0x0C` | u32  | event_name   | Index into `strings`: the Wwise event (`BGM_Radio_Chanel_01`, `BGM_Radio_off`)           |
| `+0x10` | u8   | unknown_10   | `1` on the eight channels, `0` on entries 1 and 2                                       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                  |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                      |
| `+0x04` | pstr[string_count] | strings      | State and event names, UTF-8; the channel titles and one empty string UTF-16LE; a string several rows use is stored once |

## Layout 5

The radio entries have no leading `unknown_00`. Only the Radio Entry
differs from Layout 6.

### Radio Entry (13 bytes)

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u32  | unknown_04   | Index into `strings`: `Game_Start`, `Radio_Off` or empty |
| `+0x04` | u32  | channel_name | Index into `strings`: the channel title                  |
| `+0x08` | u32  | event_name   | Index into `strings`: the Wwise event                    |
| `+0x0C` | u8   | unknown_10   | `1` on the eight channels                                |

## Layout 4

Nine state entries. Only the File Layout differs from Layout 5.

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[9]           | state_entries      | No count in the file; keys `0` to `8`                    |
| `rows+0x5A`               | u32                      | radio_count        | Number of `radio_entries`                                |
| `rows+0x5E`               | Radio Entry[radio_count] | radio_entries      | See Radio Entry                                          |
| `radio_entries+0x00`      | u32                      | unknown_tail_count | Number of `unknown_tail` bytes                           |
| `radio_entries+0x04`      | u8[unknown_tail_count]   | unknown_tail       | The same 17 values as on client 3482                     |
| `unknown_tail+0x00`       | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table                               |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

## Layout 3

Eight state entries and no radio entries or tail. Only the File Layout
differs from Layout 4.

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[8]           | state_entries      | No count in the file; keys `0` to `7`                    |
| `rows+0x50`               | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table                               |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

## Layout 2

Five state entries and no radio entries or tail. Only the File Layout
differs from Layout 3.

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[5]           | state_entries      | No count in the file; keys `0` to `4`                    |
| `rows+0x32`               | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table                               |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

## Layout 1

The sound bank system before Wwise: per area colour a sound bank and a
music number for each of 18 situations, and no state entries. The string
table is empty. The File Layout and the Row differ from Layout 2.

### File Layout

| Offset              | Type           | Field              | Notes                                   |
| ------------------- | -------------- | ------------------ | --------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                            |
| `+0x04`             | u32            | row_count          | Number of area colours                  |
| `+0x08`             | Row[row_count] | rows               | See Row                                 |
| `rows+0x00`         | String Table   | string_table       | `string_count` `0` on client 1784       |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table              |
| `string_table+0x04` | u32            | zero               | `0`                                     |

### Row (160 bytes)

| Offset  | Type    | Field               | Notes                                                           |
| ------- | ------- | ------------------- | --------------------------------------------------------------- |
| `+0x00` | u32     | color               | Area colour as `0x00RRGGBB`; each colour once                   |
| `+0x04` | u32     | color_dup           | Equals `color` on every row                                     |
| `+0x08` | u32[18] | bank_nos            | Sound bank per situation, in the order of Situations            |
| `+0x50` | u32[18] | music_indexes       | Music number in that bank per situation, same order             |
| `+0x98` | u32     | unknown_98          | `1` on every row of client 1784                                 |
| `+0x9C` | u32     | bank_no_environment | Ambience bank                                                   |

## Situations

The order of `bank_nos` and `music_indexes` in Layout 1, with the column
pair of the client 1784 sheet each slot matches:

| Slot | Columns                                              |
| ---- | ---------------------------------------------------- |
| 0    | `BankNo_NormaiDay`, `MusicIdx_NormaiDay`             |
| 1    | `BankNo_NormaiNight`, `MusicIdx_NormaiNight`         |
| 2    | `BankNo_CombatLv1`, `MusicIdx_CombatLv1`             |
| 3    | `BankNo_CombatLv2`, `MusicIdx_CombatLv2`             |
| 4    | `BankNo_CombatNightLv1`, `MusicIdx_CombatNightLv1`   |
| 5    | `BankNo_CombatNightLv2`, `MusicIdx_CombatNightLv2`   |
| 6    | `BankNo_CombatBoss`, `MusicIdx_CombatBoss`           |
| 7    | `BankNo_CombatHpLow`, `MusicIdx_CombatHpLow`         |
| 8    | `BankNo_Riding`, `MusicIdx_Riding`                   |
| 9    | `BankNo_Racing`, `MusicIdx_Racing`                   |
| 10   | `BankNo_VillageSiege`, `MusicIdx_VillageSiege`       |
| 11   | `BankNo_Siegewarfare`, `MusicIdx_Siegewarfare`       |
| 12   | `BankNo_GuildTeamBattle`, `MusicIdx_GuildTeamBattle` |
| 13   | `BankNo_BattleRoyale`, `MusicIdx_BattleRoyale`       |
| 14   | `BankNo_BattleRoyaleLobby`, `MusicIdx_BattleRoyaleLobby` |
| 15   | `BankNo_BattleRoyaleLostRegion`, `MusicIdx_BattleRoyaleLostRegion` |
| 16   | `BankNo_NationSiegeStart`, `MusicIdx_NationSiegeStart` |
| 17   | `BankNo_Undersea`, `MusicIdx_Undersea`               |

## State Entry Count

No field holds the number of state entries; it grew from 5 (clients 1866
and 1886) to 8, 9 and 10 (client 2107 and later), one entry per new key,
so each count is its own layout. A reader can only check a count by
walking the rest of the file to the string table.

## BGM State Slots

The names the four `bgm_states` slots hold most often on client 3482
(the part after the area prefix, `W01_Balenos_`):

| Slot | Most frequent names                                                        |
| ---- | -------------------------------------------------------------------------- |
| 0    | `Exploration_Motivated` (294 rows), `Exploration_Peaceful` (105)           |
| 1    | `Exploration_Motivated` (293), `Exploration_Peaceful` (105), `Battle_General` (84) |
| 2    | `Battle_Boss` (866)                                                        |
| 3    | `Exploration_Motivated` (293), `Exploration_Peaceful` (105), `Diving` (83) |

Areas with combat or underwater music fill slot 1 with a `Battle_General`
and slot 3 with a `Diving` state; elsewhere slots 0, 1 and 3 hold the same
state.

## Field Names

The `AudioMap_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Index`, `RegionGroupKey`, `R`, `G`, `B`,
`AreaName`, `BankNo_Environment` and a `BankNo_` and `MusicIdx_` pair per
situation. Joined on `R`, `G`, `B` = `color`, 811 of 811 sheet rows have a
Layout 1 row (client 1784). `bank_no_environment` matches on 811 of 811,
the 18 `music_indexes` on 811 of 811 each. `bank_nos` slot 7 matches on
811 of 811 and the other 17 slots on 810: the sheet row `1087` holds bank
`109` in them where the file holds `110`.
`Index`, `RegionGroupKey` and the `AreaName` note are not in the file.

In Layout 3, `bank_no_environment` equals the client 1784 value on 810 of
the 811 colours both clients have (client 3482), and every value is an
`ENV_INDEX_<n>` state of `sound2022/wwise_ids.h`. That header lists the
`bgm_states` and `state_name` strings under the `BGM` state group, and
the radio `event_name` strings under its events. The `AudioRenewal_Table`
sheet of client 1784 has the columns `Index`, `AudioStateGroupName`,
`AudioStateName` and `ContentsGroupKey` and no rows; it fits the State
Entry, but with no rows no value can confirm it.

## Open Questions

### BGM State Slot Meaning

Which situation each `bgm_states` slot plays is not confirmed. The names
point at normal play (slot 0), combat (slot 1), boss fights (slot 2) and
underwater (slot 3), the Layout 1 situations `NormaiDay`, `CombatLv1`,
`CombatBoss` and `Undersea`.

### State Entry Keys

`unknown_00` of the state entries runs `0` to `9` and `unknown_01` holds
`51` to `55` or `255`. The states (`W00_ArenaOfSolare_Round_Start`,
`W00_Ocean_Battle_PVP`, `W01_PapuCrioWar_Default`) suggest a key per
special situation (an arena round, a sea battle); `unknown_01` may be a
contents group or a priority.

### Radio Tail

`unknown_tail` (17 rising values up to `60`) follows the radio entries and
matches no key in the file.

### Layout Before Client 1109

Clients 435 to 822 hold a file no layout reads (85,652 bytes on client
822); clients 855 to 1076 have none. Its rows are larger than the Layout 1
row.
