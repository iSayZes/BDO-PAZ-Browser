# `petupgraderesult.bss` Format

## Purpose

The outcome of Tier 5 Pet Training per pet: which Tier 5 pet a Tier 4 pet
trains into, and the talent (base skill) the pet shows while it is the
alpha. The file holds two maps with no PABR magic and no trailer: Tier 4
pet to result, then Tier 5 pet to alpha talent. Pet keys are `pet_id`s of
[`pet.dbss`](pet_dbss.md); talents are Section 2 `equip_skill_id`s of
[`petequipskill.bss`](petequipskill_bss.md), the keys `pet.dbss` stores as
`base_skill_id`. The training cost is in [`petupgrade.bss`](petupgrade_bss.md)
and the alpha's loot cooldown bonus in
[`petleaderbuff.bss`](petleaderbuff_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ---------------------------- | --------- |
| 1      | 1927 and later | 3483    | `petupgraderesult.bss` | 7,112 | 444 Result, 444 Leader Skill | 10        |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 1      | `petupgraderesult.bss` | 7,112 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 1 |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3464   | Layout 1 |
| 3458   | Layout 1 |
| 3454   | Layout 1 |
| 3444   | Layout 1 |
| 3435   | Layout 1 |
| 3426   | Layout 1 |
| 3418   | Layout 1 |
| 3412   | Layout 1 |
| 3402   | Layout 1 |
| 3396   | Layout 1 |
| 3387   | Layout 1 |
| 3381   | Layout 1 |
| 3373   | Layout 1 |
| 3364   | Layout 1 |
| 3356   | Layout 1 |
| 3349   | Layout 1 |
| 3342   | Layout 1 |
| 3335   | Layout 1 |
| 3326   | Layout 1 |
| 3321   | Layout 1 |
| 3314   | Layout 1 |
| 3303   | Layout 1 |
| 3302   | Layout 1 |
| 3293   | Layout 1 |
| 3283   | Layout 1 |
| 3275   | Layout 1 |
| 3267   | Layout 1 |
| 3258   | Layout 1 |
| 3251   | Layout 1 |
| 3242   | Layout 1 |
| 3235   | Layout 1 |
| 3229   | Layout 1 |
| 3212   | Layout 1 |
| 3203   | Layout 1 |
| 3193   | Layout 1 |
| 3186   | Layout 1 |
| 3177   | Layout 1 |
| 3169   | Layout 1 |
| 3158   | Layout 1 |
| 3151   | Layout 1 |
| 3144   | Layout 1 |
| 3133   | Layout 1 |
| 3125   | Layout 1 |
| 3118   | Layout 1 |
| 3111   | Layout 1 |
| 3103   | Layout 1 |
| 3095   | Layout 1 |
| 3086   | Layout 1 |
| 3072   | Layout 1 |
| 3062   | Layout 1 |
| 3052   | Layout 1 |
| 3045   | Layout 1 |
| 3037   | Layout 1 |
| 3030   | Layout 1 |
| 3021   | Layout 1 |
| 3012   | Layout 1 |
| 3002   | Layout 1 |
| 2995   | Layout 1 |
| 2987   | Layout 1 |
| 2978   | Layout 1 |
| 2970   | Layout 1 |
| 2959   | Layout 1 |
| 2951   | Layout 1 |
| 2942   | Layout 1 |
| 2935   | Layout 1 |
| 2932   | Layout 1 |
| 2923   | Layout 1 |
| 2919   | Layout 1 |
| 2907   | Layout 1 |
| 2900   | Layout 1 |
| 2891   | Layout 1 |
| 2882   | Layout 1 |
| 2872   | Layout 1 |
| 2863   | Layout 1 |
| 2855   | Layout 1 |
| 2849   | Layout 1 |
| 2844   | Layout 1 |
| 2834   | Layout 1 |
| 2825   | Layout 1 |
| 2819   | Layout 1 |
| 2811   | Layout 1 |
| 2803   | Layout 1 |
| 2794   | Layout 1 |
| 2783   | Layout 1 |
| 2774   | Layout 1 |
| 2765   | Layout 1 |
| 2756   | Layout 1 |
| 2750   | Layout 1 |
| 2743   | Layout 1 |
| 2736   | Layout 1 |
| 2726   | Layout 1 |
| 2717   | Layout 1 |
| 2709   | Layout 1 |
| 2703   | Layout 1 |
| 2695   | Layout 1 |
| 2684   | Layout 1 |
| 2672   | Layout 1 |
| 2665   | Layout 1 |
| 2657   | Layout 1 |
| 2649   | Layout 1 |
| 2644   | Layout 1 |
| 2637   | Layout 1 |
| 2629   | Layout 1 |
| 2619   | Layout 1 |
| 2612   | Layout 1 |
| 2606   | Layout 1 |
| 2602   | Layout 1 |
| 2601   | Layout 1 |
| 2592   | Layout 1 |
| 2583   | Layout 1 |
| 2575   | Layout 1 |
| 2567   | Layout 1 |
| 2560   | Layout 1 |
| 2553   | Layout 1 |
| 2545   | Layout 1 |
| 2538   | Layout 1 |
| 2529   | Layout 1 |
| 2519   | Layout 1 |
| 2513   | Layout 1 |
| 2510   | Layout 1 |
| 2507   | Layout 1 |
| 2503   | Layout 1 |
| 2498   | Layout 1 |
| 2492   | Layout 1 |
| 2487   | Layout 1 |
| 2480   | Layout 1 |
| 2474   | Layout 1 |
| 2468   | Layout 1 |
| 2460   | Layout 1 |
| 2453   | Layout 1 |
| 2444   | Layout 1 |
| 2438   | Layout 1 |
| 2434   | Layout 1 |
| 2429   | Layout 1 |
| 2421   | Layout 1 |
| 2414   | Layout 1 |
| 2407   | Layout 1 |
| 2401   | Layout 1 |
| 2397   | Layout 1 |
| 2393   | Layout 1 |
| 2384   | Layout 1 |
| 2378   | Layout 1 |
| 2372   | Layout 1 |
| 2358   | Layout 1 |
| 2352   | Layout 1 |
| 2347   | Layout 1 |
| 2343   | Layout 1 |
| 2335   | Layout 1 |
| 2327   | Layout 1 |
| 2324   | Layout 1 |
| 2319   | Layout 1 |
| 2313   | Layout 1 |
| 2308   | Layout 1 |
| 2302   | Layout 1 |
| 2295   | Layout 1 |
| 2290   | Layout 1 |
| 2284   | Layout 1 |
| 2276   | Layout 1 |
| 2269   | Layout 1 |
| 2259   | Layout 1 |
| 2250   | Layout 1 |
| 2243   | Layout 1 |
| 2235   | Layout 1 |
| 2229   | Layout 1 |
| 2224   | Layout 1 |
| 2218   | Layout 1 |
| 2215   | Layout 1 |
| 2207   | Layout 1 |
| 2203   | Layout 1 |
| 2196   | Layout 1 |
| 2192   | Layout 1 |
| 2189   | Layout 1 |
| 2183   | Layout 1 |
| 2179   | Layout 1 |
| 2171   | Layout 1 |
| 2163   | Layout 1 |
| 2156   | Layout 1 |
| 2151   | Layout 1 |
| 2147   | Layout 1 |
| 2142   | Layout 1 |
| 2138   | Layout 1 |
| 2134   | Layout 1 |
| 2130   | Layout 1 |
| 2122   | Layout 1 |
| 2107   | Layout 1 |
| 2098   | Layout 1 |
| 2089   | Layout 1 |
| 2081   | Layout 1 |
| 2073   | Layout 1 |
| 2067   | Layout 1 |
| 2063   | Layout 1 |
| 2059   | Layout 1 |
| 2052   | Layout 1 |
| 2044   | Layout 1 |
| 2039   | Layout 1 |
| 2032   | Layout 1 |
| 2025   | Layout 1 |
| 2011   | Layout 1 |
| 2005   | Layout 1 |
| 2000   | Layout 1 |
| 1996   | Layout 1 |
| 1991   | Layout 1 |
| 1985   | Layout 1 |
| 1980   | Layout 1 |
| 1969   | Layout 1 |
| 1964   | Layout 1 |
| 1958   | Layout 1 |
| 1950   | Layout 1 |
| 1945   | Layout 1 |
| 1937   | Layout 1 |
| 1933   | Layout 1 |
| 1927   | Layout 1 |
| 1921   | No file  |
| 1914   | No file  |
| 1908   | No file  |
| 1897   | No file  |
| 1892   | No file  |
| 1886   | No file  |
| 1881   | No file  |
| 1871   | No file  |
| 1866   | No file  |
| 1862   | No file  |
| 1854   | No file  |
| 1846   | No file  |
| 1838   | No file  |
| 1832   | No file  |
| 1826   | No file  |
| 1822   | No file  |
| 1818   | No file  |
| 1804   | No file  |
| 1794   | No file  |
| 1790   | No file  |
| 1784   | No file  |
| 1774   | No file  |
| 1771   | No file  |
| 1762   | No file  |
| 1759   | No file  |
| 1754   | No file  |
| 1749   | No file  |
| 1743   | No file  |
| 1737   | No file  |
| 1731   | No file  |
| 1725   | No file  |
| 1717   | No file  |
| 1710   | No file  |
| 1704   | No file  |
| 1698   | No file  |
| 1690   | No file  |
| 1685   | No file  |
| 1680   | No file  |
| 1674   | No file  |
| 1668   | No file  |
| 1659   | No file  |
| 1649   | No file  |
| 1642   | No file  |
| 1636   | No file  |
| 1628   | No file  |
| 1622   | No file  |
| 1614   | No file  |
| 1608   | No file  |
| 1602   | No file  |
| 1598   | No file  |
| 1594   | No file  |
| 1590   | No file  |
| 1587   | No file  |
| 1584   | No file  |
| 1579   | No file  |
| 1572   | No file  |
| 1565   | No file  |
| 1559   | No file  |
| 1554   | No file  |
| 1547   | No file  |
| 1537   | No file  |
| 1529   | No file  |
| 1524   | No file  |
| 1519   | No file  |
| 1509   | No file  |
| 1506   | No file  |
| 1504   | No file  |
| 1500   | No file  |
| 1493   | No file  |
| 1489   | No file  |
| 1485   | No file  |
| 1481   | No file  |
| 1474   | No file  |
| 1466   | No file  |
| 1462   | No file  |
| 1459   | No file  |
| 1453   | No file  |
| 1450   | No file  |
| 1445   | No file  |
| 1439   | No file  |
| 1433   | No file  |
| 1430   | No file  |
| 1426   | No file  |
| 1421   | No file  |
| 1417   | No file  |
| 1416   | No file  |
| 1409   | No file  |
| 1405   | No file  |
| 1401   | No file  |
| 1396   | No file  |
| 1391   | No file  |
| 1390   | No file  |
| 1386   | No file  |
| 1381   | No file  |
| 1379   | No file  |
| 1372   | No file  |
| 1366   | No file  |
| 1364   | No file  |
| 1363   | No file  |
| 1360   | No file  |
| 1358   | No file  |
| 1355   | No file  |
| 1351   | No file  |
| 1348   | No file  |
| 1346   | No file  |
| 1341   | No file  |
| 1340   | No file  |
| 1338   | No file  |
| 1335   | No file  |
| 1333   | No file  |
| 1329   | No file  |
| 1327   | No file  |
| 1324   | No file  |
| 1321   | No file  |
| 1319   | No file  |
| 1318   | No file  |
| 1316   | No file  |
| 1313   | No file  |
| 1311   | No file  |
| 1309   | No file  |
| 1304   | No file  |
| 1292   | No file  |
| 1286   | No file  |
| 1280   | No file  |
| 1276   | No file  |
| 1267   | No file  |
| 1261   | No file  |
| 1256   | No file  |
| 1250   | No file  |
| 1246   | No file  |
| 1239   | No file  |
| 1230   | No file  |
| 1226   | No file  |
| 1220   | No file  |
| 1217   | No file  |
| 1211   | No file  |
| 1210   | No file  |
| 1208   | No file  |
| 1203   | No file  |
| 1197   | No file  |
| 1194   | No file  |
| 1192   | No file  |
| 1187   | No file  |
| 1183   | No file  |
| 1177   | No file  |
| 1173   | No file  |
| 1167   | No file  |
| 1164   | No file  |
| 1156   | No file  |
| 1149   | No file  |
| 1144   | No file  |
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

None. The handler names the pets and the talents from
[`pet.dbss`](pet_dbss.md) (with `petoffset.dbss`) and
[`petequipskill.bss`](petequipskill_bss.md) when they are present.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset          | Type                          | Field              | Notes                                         |
| --------------- | ----------------------------- | ------------------ | --------------------------------------------- |
| `+0x00`         | u32                           | result_count       | Number of Result rows                         |
| `+0x04`         | Result[result_count]          | results            | See Result                                    |
| `results+0x00`  | u32                           | leader_skill_count | Number of Leader Skill rows; equals `result_count` on client 3474 |
| `results+0x04`  | Leader Skill[leader_skill_count] | leader_skills   | See Leader Skill                              |

On client 3474 the file is 4 + 444 x 10 + 4 + 444 x 6 = 7,112 bytes.

### Result (10 bytes)

| Offset  | Type | Field                | Notes                                                                                     |
| ------- | ---- | -------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id               | Map key: the Tier 4 pet (`tier` `3` in [`pet.dbss`](pet_dbss.md))                         |
| `+0x02` | u16  | pet_id_dup           | Equals `pet_id` on every row                                                              |
| `+0x04` | u16  | result_pet_id        | The Tier 5 pet the training gives (`tier` `4` in `pet.dbss`)                              |
| `+0x06` | u32  | leader_base_skill_id | Talent of the trained pet as the alpha: a Section 2 `equip_skill_id` of [`petequipskill.bss`](petequipskill_bss.md) |

### Leader Skill (6 bytes)

| Offset  | Type | Field                | Notes                                                           |
| ------- | ---- | -------------------- | --------------------------------------------------------------- |
| `+0x00` | u16  | pet_id               | Map key: a Tier 5 pet, the `result_pet_id` of one Result row     |
| `+0x02` | u32  | leader_base_skill_id | Equals `leader_base_skill_id` of that Result row                 |

## Training Results

On client 3474 every Tier 4 pet of `pet.dbss` has a Result row except the
five fairy records (`pet_type` 1), and every Tier 5 pet is the
`result_pet_id` of exactly one row. 431 of the 444 rows give a pet with the
same LOC name; the other 13 give the Tier 5 record of the same pet where
the Tier 4 record has no LOC name (`아토락시온 타르케스_T4` to Tarkhes,
`반려동물 쪼쪼_교역_T4` to Jojo).

`leader_base_skill_id` is the talent one level above the Tier 4 pet's own
`base_skill_id`, keyed by that base skill on all 444 rows:

| Tier 4 `base_skill_id` | `leader_base_skill_id` | Talent as the alpha (LOC type 10) | Rows (client 3474) |
| ---------------------- | ---------------------- | --------------------------------- | ------------------ |
| 18                     | 99                     | Skill EXP +5%                     | 118                |
| 38                     | 101                    | Durability Reduction Resistance +5% | 100              |
| 23                     | 100                    | Life EXP +5%                      | 99                 |
| 58                     | 103                    | Weight Limit +60 LT               | 31                 |
| 43                     | 102                    | Normal and Higher Grade Gain Chance Lv. 5 | 30         |
| 78                     | 106                    | Death Penalty Resistance +5%      | 28                 |
| 73                     | 105                    | Combat EXP +5%                    | 24                 |
| 82                     | 107                    | Item Drop Rate +5%                | 5                  |
| 68                     | 104                    | Max HP +125                       | 5                  |
| 86                     | 108                    | Mount EXP +5%                     | 2                  |
| 98                     | 111                    | Big Ship Inventory Weight +250 LT | 1                  |
| 94                     | 110                    | Barter EXP +5%                    | 1                  |

The Tier 5 pet's own record in `pet.dbss` keeps the Tier 4 `base_skill_id`
on every row.

## Field Names

No reference source has the table: the file is not in the client 1784
archive, a private server's `DataSheets.bexcel` on client 1784 has no sheet
with `Upgrade` and `Pet` in its name, and the 2016 client's debug symbols
have no pet upgrade type. The names come from the client Lua of client
3474 and the official Black Desert wiki:

- `pet_id` and `result_pet_id`: the Tier 5 Pet Training window
  (`panel_dialog_petleader_all_1.luac`) calls
  `ToClient_getPetUpgradeSimulationResult(characterKey)` with the character
  key of the Tier 4 pet in the slot and reads the tier of the pet it
  returns (`newPetStaticStatus:getPetTier()`) for the alpha bonus. Every
  key of Result is a Tier 4 pet and every `result_pet_id` a Tier 5 one.
- `leader_base_skill_id`: the same window, the pet list
  (`panel_window_petlist_all_2.luac`) and the pet info window
  (`panel_window_petinfo_all_1.luac`) show the talent of an alpha pet with
  `ToClient_getPetBaseSkillStaticStatus(ToClient_getLeaderBaseSkill(petNo))`,
  and of any other pet with `getPetBaseSkillIndex()`. The official Black
  Desert wiki page "Tier 5 Pet Training/Alpha Appointment" says "The Alpha
  Pet's Talent gains one additional level", with the examples "Combat EXP
  +4% -> +5%" and "HP +100 -> +125", and that other Tier 5 pets "share the
  same stats as a Tier 4 pet". That is the step from `base_skill_id` to
  `leader_base_skill_id` in Training Results (`73` Combat EXP +5% and `104`
  Max HP +125).
- `pet_id_dup`: equal to the key on all 444 rows, as `plantupgradeparam.bss`
  stores its map key again as the first member of the value.

## Notes

- Clients 2107, 2519, 3002 and 3251 ship the file too; client 1784 does
  not.
- The rows of neither map are sorted by key, and the two maps
  list the pets in different orders.
- `ToClient_getLeaderBaseSkill` takes a pet number, not a key, so the Lua
  does not show which of the two maps it reads. The training window calls
  it for a Tier 4 pet (a Result key), the pet list for an alpha, which is a
  Tier 5 pet (a Leader Skill key).

## Open Questions

### Why the Second Map

Leader Skill repeats the talent of every Result row under the Tier 5 pet's
key. The client could look the talent up through either key; which call
reads which map is not in the client Lua, and the client 3474 executable
does not name the table's loader.
