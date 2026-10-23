# `itemgroupingstaticstatus.bss` Format

## Purpose

The item group types of the high-end gear lines: per group type the items
of one line and slot kind, such as the 50 Blackstar main weapons or the 93
Sovereign awakening weapons. The client Lua asks for an item's type with
`ToClient_getItemKeyGroupTypeByTItemKey(itemKey)` and compares it with the
`__eItemGroupType_*` values: the Sovereign weapon creation window
(`panel_makegoonwang_all.luac`) filters its material slots by type, the dye
window (`panel_widget_dye_all_2.luac`) offers the glow dyes of
[`itemeffectgroupstaticstatus.bss`](itemeffectgroupstaticstatus_bss.md)
by it, and the item tooltip (`panel_tooltip_item.luac`) hides the dye lines
of the Sovereign types.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records  | Row bytes                 |
| ------ | -------------- | ------- | ------------------------------ | ----- | -------- | ------------------------- |
| 1      | 3177 and later | 3482    | `itemgroupingstaticstatus.bss` | 2,612 | 12 Group | 21 to 377, 217 on average |

| Layout | File                           | Known            | Unknown    |
| ------ | ------------------------------ | ---------------- | ---------- |
| 1      | `itemgroupingstaticstatus.bss` | 2,612 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3454   | Layout 1 |
| 3412   | Layout 1 |
| 3381   | Layout 1 |
| 3349   | Layout 1 |
| 3314   | Layout 1 |
| 3283   | Layout 1 |
| 3251   | Layout 1 |
| 3212   | Layout 1 |
| 3177   | Layout 1 |
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

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type               | Field       | Notes                                            |
| ------- | ------------------ | ----------- | ------------------------------------------------ |
| `+0x00` | u32                | group_count | Number of groups; no PABR magic, no string table |
| `+0x04` | Group[group_count] | groups      | See Group; from the highest type down            |

### Group (variable: 5 bytes + item IDs)

| Offset  | Type             | Field           | Notes                                                    |
| ------- | ---------------- | --------------- | -------------------------------------------------------- |
| `+0x00` | u8               | item_group_type | Group type, `0` to `11` on client 3482; see Group Types  |
| `+0x01` | u32              | item_count      | Number of `item_ids`                                     |
| `+0x05` | u32[item_count]  | item_ids        | Item IDs (enhancement level `0` in the high byte on every entry of client 3482) |

## Group Types

The items of each group on client 3482, and the `__eItemGroupType_*` name
of the client 3482 Lua whose use fits them (see Open Questions).

| Type | Items (client 3482)                                       | Lua name that fits       |
| ---- | --------------------------------------------------------- | ------------------------ |
| 0    | 50 Blackstar main weapons (Blackstar Longsword)           | `BlackStarMain`          |
| 1    | 50 Kzarka main weapons                                    | `KzakaMain`              |
| 2    | 50 Offin Tett's Radiant main weapons                      | `OpinMain`               |
| 3    | 62 Blackstar awakening weapons                            | `BlackStarAwaken`        |
| 4    | 62 Dandelion awakening weapons                            | `DandelionAwaken`        |
| 5    | 48 Blackstar sub-weapons                                  | `BlackStarSub`           |
| 6    | 48 Nouver sub-weapons                                     | `NuverSub`               |
| 7    | 48 Kutum sub-weapons                                      | `KutumSub`               |
| 8    | 50 Sovereign main weapons, Fiery Sovereign included       | `GoonWangMain`           |
| 9    | 72 Sovereign sub-weapons, Fiery Sovereign included        | `GoonWangSub`            |
| 10   | 93 Sovereign awakening weapons, Storm Devoured included   | `GoonWangAwaken`         |
| 11   | 4 Edana armor items (Edana - Heavensmite, Abyssveil, Oathgrip, Furystride) | `EdanaArmor` |

## Notes

- Types `8` to `11` are the group keys of
  [`itemeffectgroupstaticstatus.bss`](itemeffectgroupstaticstatus_bss.md),
  the item groups that take a glow dye; the dye window checks for
  `GoonWangMain`, `GoonWangSub`, `GoonWangAwaken` and `EdanaArmor`.
- The file is not in the client 1784 PAZ.
- The handler (`_bss/itemgroupingstaticstatus/`) shows one row per group
  with its items.

## Open Questions

### Which `__eItemGroupType_` Value Each Type Is

The client Lua uses the `__eItemGroupType_*` names but never their numbers,
which come from the game client. The order of the Group Types table puts
each Lua name on the group whose items it names; no Lua or file value
confirms the numbers.
