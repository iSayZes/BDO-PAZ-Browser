# `itembuildkit.bss` Format

## Purpose

The siege build kits: per kit item the structures it can place in a Node
or Conquest War (fences, barricades, the fort and command post annexes),
each with the condition script that allows it, a contents event, its icon
and its Korean description. Clients 1784 and 3482 have one kit, item 59791
`[Guild] Node/Conquest War Annex Assembly Tool`. The siege installation
window (`panel_house_installationmode_siege_all_1.luac`) lists the
structures with `ToClient_getSiegeInstallableListSize()` and
`ToClient_getSiegeInstallableListByIndex(index)` and places one with
`ToClient_requestSiegeInstallationStart(itemEnchantKey, characterKey)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records   | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------ | --------- | --------- |
| 3      | 2519 and later | 3482    | `itembuildkit.bss` | 41,439 | 103 Entry | 35        |
| 2      | 1717 to 2498   | 2498    | `itembuildkit.bss` | 56,950 | 56 Entry  | 26        |
| 1      | 1698           | 1698    | `itembuildkit.bss` | 2,770  | 56 Entry  | 22        |

| Layout | File               | Known             | Unknown      |
| ------ | ------------------ | ----------------- | ------------ |
| 3      | `itembuildkit.bss` | 40,512 B (97.8%)  | 927 B (2.2%) |
| 2      | `itembuildkit.bss` | 56,950 B (100.0%) | 0 B (0.0%)   |
| 1      | `itembuildkit.bss` | 2,770 B (100.0%)  | 0 B (0.0%)   |

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
| 2923   | Layout 3 |
| 2900   | Layout 3 |
| 2872   | Layout 3 |
| 2834   | Layout 3 |
| 2803   | Layout 3 |
| 2765   | Layout 3 |
| 2736   | Layout 3 |
| 2703   | Layout 3 |
| 2665   | Layout 3 |
| 2637   | Layout 3 |
| 2606   | Layout 3 |
| 2583   | Layout 3 |
| 2545   | Layout 3 |
| 2519   | Layout 3 |
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
| 1749   | Layout 2 |
| 1717   | Layout 2 |
| 1698   | Layout 1 |
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
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                      |
| ---------------------------- | -------- | ------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a structure without a row shows as plain text |
| `languagedata_en.loc`        | Optional | Item names (LOC type 0) and structure names (LOC type 6)                  |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field        | Notes                                        |
| ------------------- | -------------- | ------------ | -------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                 |
| `+0x04`             | u32            | kit_count    | Number of kits; `1` on clients 1784 and 3482 |
| `+0x08`             | Kit[kit_count] | kits         | See Kit                                      |
| `kits+0x00`         | String Table   | string_table | See String Table                             |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `kits` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                   |

### Kit (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                       |
| ------- | ------------------ | ----------- | ------------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; 103 on client 3482     |
| `+0x04` | Entry[entry_count] | entries     | See Entry; one per structure the kit places |

### Entry (35 bytes)

| Offset  | Type | Field                 | Notes                                                                                     |
| ------- | ---- | --------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key              | The kit, a packed item key; the same in every entry of a kit                               |
| `+0x04` | u16  | character_key         | The structure placed (`2046` Wooden Fence, `12606` Barricade); unique within a kit          |
| `+0x06` | u32  | use_condition         | Index into `strings`: the condition script (`checksiegetower(0);checkInstallTentLevel(5);`) |
| `+0x0A` | u32  | contents_event_type   | `1` on every entry of clients 1784 and 3482                                                |
| `+0x0E` | u32  | contents_event_param1 | `15000` on every entry of client 1784, `5000` on client 3482                               |
| `+0x12` | u32  | icon_image_file       | Index into `strings`: the icon path (`New_Icon/03_ETC/06_Housing/00056071.dds`)            |
| `+0x16` | u32  | description           | Index into `strings`: the Korean description, with `<PAColor>` tags and `\n` escapes        |
| `+0x1A` | u32  | unknown_1a            | `0`, `30000000` or `50000000` on client 3482; see Open Questions                           |
| `+0x1E` | u32  | unknown_1e            | `0` on every entry of client 3482                                                          |
| `+0x22` | u8   | unknown_22            | `0`, `1` or `2` on client 3482; see Open Questions                                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                       |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; 73 on client 3482                                        |
| `+0x04` | pstr[string_count] | strings      | Condition scripts and descriptions UTF-16LE (`is_wide` 1), icon paths UTF-8; each text stored once |

## Layout 2

The entry ends after `description`. Only the Entry differs from Layout 3.

### Entry (26 bytes)

| Offset  | Type | Field                 | Notes |
| ------- | ---- | --------------------- | ----- |
| `+0x00` | u32  | item_key              |       |
| `+0x04` | u16  | character_key         |       |
| `+0x06` | u32  | use_condition         |       |
| `+0x0A` | u32  | contents_event_type   |       |
| `+0x0E` | u32  | contents_event_param1 |       |
| `+0x12` | u32  | icon_image_file       |       |
| `+0x16` | u32  | description           |       |

## Layout 1

The entry ends after `icon_image_file`: no description. Only the Entry
differs from Layout 2.

### Entry (22 bytes)

| Offset  | Type | Field                 | Notes |
| ------- | ---- | --------------------- | ----- |
| `+0x00` | u32  | item_key              |       |
| `+0x04` | u16  | character_key         |       |
| `+0x06` | u32  | use_condition         |       |
| `+0x0A` | u32  | contents_event_type   |       |
| `+0x0E` | u32  | contents_event_param1 |       |
| `+0x12` | u32  | icon_image_file       |       |

## Field Names

The `SiegeItemInstallation` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `ItemKey`, `CharacterKey`, `UseCondition`,
`ContentsEventType`, `ContentsEventParam1`, `IconImageFile` and
`Description`, one sheet row per entry, in another order than the file.
Matched on (`ItemKey`, `CharacterKey`):

| Field                 | Column                | Same value (client 1784) | Same value (client 3482) |
| --------------------- | --------------------- | ------------------------ | ------------------------ |
| item_key              | `ItemKey`             | 56 of 56                 | 52 of 103                |
| character_key         | `CharacterKey`        | 56 of 56                 | 52 of 52                 |
| use_condition         | `UseCondition`        | 56 of 56                 | 28 of 52                 |
| contents_event_type   | `ContentsEventType`   | 56 of 56                 | 52 of 52                 |
| contents_event_param1 | `ContentsEventParam1` | 56 of 56                 | 0 of 52                  |
| icon_image_file       | `IconImageFile`       | 56 of 56                 | 52 of 52                 |
| description           | `Description`         | 56 of 56                 | 5 of 52                  |

The client 3482 misses are changed conditions and descriptions and the
parameter `5000` in place of `15000`. The sheet has no column for the three
fields Layout 3 adds.

## Notes

- `use_condition` calls `checksiegetower`, `checksiegetowercharacter`,
  `checkInstallTentLevel`, `checkiskingguild` and, on client 3482,
  `checksiege2024groupno`.
- On client 3482, `unknown_1a` is `30000000` on 6 entries and `50000000` on
  9, all of them with `unknown_22` `1`; these 15 entries (characters `12759`
  to `12790`) are the ones whose condition calls `checksiege2024groupno`.
- The handler (`_bss/itembuildkit/`) shows one row per entry: the kit, the
  structure with its name, the condition, the contents event, the icon and
  the description.

## Open Questions

### What the Three Fields Layout 3 Adds Hold

`unknown_1a` (`0`, `30000000`, `50000000`), `unknown_1e` (`0`) and
`unknown_22` (`0`, `1`, `2`) are new on client 2519 and match no sheet
column. `unknown_1a` may be a Silver cost of the 15 newer structures; the
client 3482 Lua reads no cost from the installable list.
