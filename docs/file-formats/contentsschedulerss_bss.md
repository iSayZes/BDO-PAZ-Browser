# `contentsschedulerss.bss` Format

## Purpose

The contents of the Contents Schedule window (`Panel_Window_ContentsSchedule_All`)
that a player can add to the list: per content type the `RESOURCE` sheet
key of its title, the texture key of its icon and the contents groups that
must be open. On client 3482 the four rows are the Black Shrine (Donghae
solo and Hwanghae party, the `MorningLand` keys), the Altar of Blood and
the War of the Roses, as LOC titles them. The file is a
u32 count and variable rows, with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | ----------------------- |
| 1      | 3454 and later | 3482    | `contentsschedulerss.bss` | 318   | 4 Row   | 69 to 83, 78 on average |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 1      | `contentsschedulerss.bss` | 318 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3454   | Layout 1 |
| 3412   | No file  |
| 3381   | No file  |
| 3349   | No file  |
| 3314   | No file  |
| 3283   | No file  |
| 3251   | No file  |
| 3212   | No file  |
| 3177   | No file  |
| 3144   | No file  |
| 3103   | No file  |
| 3062   | No file  |
| 3037   | No file  |
| 3002   | No file  |
| 2959   | No file  |
| 2923   | No file  |
| 2900   | No file  |
| 2872   | No file  |
| 2834   | No file  |
| 2803   | No file  |
| 2765   | No file  |
| 2736   | No file  |
| 2703   | No file  |
| 2665   | No file  |
| 2637   | No file  |
| 2606   | No file  |
| 2583   | No file  |
| 2545   | No file  |
| 2519   | No file  |
| 2498   | No file  |
| 2468   | No file  |
| 2438   | No file  |
| 2414   | No file  |
| 2384   | No file  |
| 2358   | No file  |
| 2335   | No file  |
| 2313   | No file  |
| 2290   | No file  |
| 2250   | No file  |
| 2224   | No file  |
| 2203   | No file  |
| 2179   | No file  |
| 2151   | No file  |
| 2134   | No file  |
| 2107   | No file  |
| 2073   | No file  |
| 2052   | No file  |
| 2011   | No file  |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
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

| File                                       | Required | Role |
| ------------------------------------------ | -------- | ---- |
| `stringtable.bss`                          | Optional | Hash of the `title` key, for its LOC type 37 text |
| `ui_texture/texturestringkey/texturestring_combine.xml` | Optional | Sprite sheet and rectangle of the `icon_texture` key |
| `languagedata_en.loc`                      | Optional | Title in the user's language |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 21 bytes + texts + groups)

| Offset               | Type                         | Field                 | Notes |
| -------------------- | ---------------------------- | --------------------- | ----- |
| `+0x00`              | u8                           | content_type          | Row key, `0` to `3` in file order (client 3482) |
| `+0x01`              | str8                         | title                 | `RESOURCE` sheet key (`PANEL_MORNINGLAND_PART1`, `PANEL_ROSEWAR_TITLE`) |
| `title+0x00`         | str8                         | icon_texture          | Texture key (`Combine_TitleIcon_RoseWar`) |
| `icon_texture+0x00`  | u32                          | contents_group_count  | Number of contents groups, `1` on every row |
| `icon_texture+0x04`  | u32[contents_group_count]    | contents_group_hashes | Contents group keys as the client's string hash of their decimal text, as in `characterstatic.dbss` |

## Rows (Client 3482)

| `content_type` | `title`                         | `icon_texture`                       | Contents group |
| -------------- | ------------------------------- | ------------------------------------ | -------------- |
| 0              | `PANEL_MORNINGLAND_PART1`       | `Combine_TitleIcon_MorningLandBoss`  | 9              |
| 1              | `PANEL_MORNINGLAND_PART2`       | `Combine_TitleIcon_MorningLandBoss`  | 863            |
| 2              | `PANEL_WINDOW_BLOODALTAR_TITLE` | `Combine_Title_Icon_BloodAltar`      | 2195           |
| 3              | `PANEL_ROSEWAR_TITLE`           | `Combine_TitleIcon_RoseWar`          | 1880           |

Every hash is the hash of a key that
[`contentsgroupoptionstaticstatusmanager.bss`](contentsgroupoptionstaticstatusmanager_bss.md)
lists.

## Field Names

The names follow the getters of the object that
`ToClient_GetContentsSchedulerStaticStatus(index)` returns in
`panel_window_contentsschedule_addcontents_1.luac` (client 3482):
`getContentType()`, `getTitle()` (shown with
`PAGetString(Defines.StringSheet_RESOURCE, ...)`), `getIconTexture()`
(passed to `ChangeTextureInfoTextureIDAsync`) and `isContentsGroupOpen()`.
The window loops `ToClient_GetContentsSchedulerCount()` rows from index 0.

## Notes

- The file is in client 3454 and later; clients 3412 and older do not have
  it.
- The Lua names three content types, `__eContentsScheduler_MorningLandBoss_Part`,
  `__eContentsScheduler_BloodAltar` and `__eContentsScheduler_RoseWar`. The
  client sets their values, so the Lua does not show which number each
  one is; the title keys of the rows match the three names in the order
  `0` and `1`, `2`, `3`.
