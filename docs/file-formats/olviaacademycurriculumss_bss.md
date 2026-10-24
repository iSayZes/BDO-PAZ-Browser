# `olviaacademycurriculumss.bss` Format

## Purpose

The curricula and family rewards of the Olvia Academy main window
(`panel_window_olviaacademy_main_all*.luac`). A curriculum (Combat, Life
Skill) holds subjects; a subject holds its quest list, its start quest, its
texts and, for the Life Skill subjects, a preview page. A family reward
(Combat, Life Skill) holds reward groups of quests. Every title, description
and preview text is a key of the `RESOURCE` string sheet, every quest a
packed quest ID `(quest_id << 16) | quest_chain_id`. The file has no PABR
magic and no string table. The quests are those of
[`olviaacademycurriculumquestlist.bss` and `olviaacademyrewardquestlist.bss`](olviaacademyquestlist_bss.md);
the pass tabs are in
[`olviaacademypassstaticstatusmanager.bss`](olviaacademypassstaticstatusmanager_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records                                                                           | Row bytes               |
| ------ | -------------- | ------- | ------------------------------ | ------ | --------------------------------------------------------------------------------- | ----------------------- |
| 1      | 3186 and later | 3483    | `olviaacademycurriculumss.bss` | 17,166 | 142 Subject Quest, 11 Subject, 2 Curriculum, 9 Preview, 10 Reward Group, 2 Reward | 46 to 49, 47 on average |

| Layout | File                           | Known             | Unknown    |
| ------ | ------------------------------ | ----------------- | ---------- |
| 1      | `olviaacademycurriculumss.bss` | 17,166 B (100.0%) | 0 B (0.0%) |

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
| 3177   | No file  |
| 3169   | No file  |
| 3158   | No file  |
| 3151   | No file  |
| 3144   | No file  |
| 3133   | No file  |
| 3125   | No file  |
| 3118   | No file  |
| 3111   | No file  |
| 3103   | No file  |
| 3095   | No file  |
| 3086   | No file  |
| 3072   | No file  |
| 3062   | No file  |
| 3052   | No file  |
| 3045   | No file  |
| 3037   | No file  |
| 3030   | No file  |
| 3021   | No file  |
| 3012   | No file  |
| 3002   | No file  |
| 2995   | No file  |
| 2987   | No file  |
| 2978   | No file  |
| 2970   | No file  |
| 2959   | No file  |
| 2951   | No file  |
| 2942   | No file  |
| 2935   | No file  |
| 2932   | No file  |
| 2923   | No file  |
| 2919   | No file  |
| 2907   | No file  |
| 2900   | No file  |
| 2891   | No file  |
| 2882   | No file  |
| 2872   | No file  |
| 2863   | No file  |
| 2855   | No file  |
| 2849   | No file  |
| 2844   | No file  |
| 2834   | No file  |
| 2825   | No file  |
| 2819   | No file  |
| 2811   | No file  |
| 2803   | No file  |
| 2794   | No file  |
| 2783   | No file  |
| 2774   | No file  |
| 2765   | No file  |
| 2756   | No file  |
| 2750   | No file  |
| 2743   | No file  |
| 2736   | No file  |
| 2726   | No file  |
| 2717   | No file  |
| 2709   | No file  |
| 2703   | No file  |
| 2695   | No file  |
| 2684   | No file  |
| 2672   | No file  |
| 2665   | No file  |
| 2657   | No file  |
| 2649   | No file  |
| 2644   | No file  |
| 2637   | No file  |
| 2629   | No file  |
| 2619   | No file  |
| 2612   | No file  |
| 2606   | No file  |
| 2602   | No file  |
| 2601   | No file  |
| 2592   | No file  |
| 2583   | No file  |
| 2575   | No file  |
| 2567   | No file  |
| 2560   | No file  |
| 2553   | No file  |
| 2545   | No file  |
| 2538   | No file  |
| 2529   | No file  |
| 2519   | No file  |
| 2513   | No file  |
| 2510   | No file  |
| 2507   | No file  |
| 2503   | No file  |
| 2498   | No file  |
| 2492   | No file  |
| 2487   | No file  |
| 2480   | No file  |
| 2474   | No file  |
| 2468   | No file  |
| 2460   | No file  |
| 2453   | No file  |
| 2444   | No file  |
| 2438   | No file  |
| 2434   | No file  |
| 2429   | No file  |
| 2421   | No file  |
| 2414   | No file  |
| 2407   | No file  |
| 2401   | No file  |
| 2397   | No file  |
| 2393   | No file  |
| 2384   | No file  |
| 2378   | No file  |
| 2372   | No file  |
| 2358   | No file  |
| 2352   | No file  |
| 2347   | No file  |
| 2343   | No file  |
| 2335   | No file  |
| 2327   | No file  |
| 2324   | No file  |
| 2319   | No file  |
| 2313   | No file  |
| 2308   | No file  |
| 2302   | No file  |
| 2295   | No file  |
| 2290   | No file  |
| 2284   | No file  |
| 2276   | No file  |
| 2269   | No file  |
| 2259   | No file  |
| 2250   | No file  |
| 2243   | No file  |
| 2235   | No file  |
| 2229   | No file  |
| 2224   | No file  |
| 2218   | No file  |
| 2215   | No file  |
| 2207   | No file  |
| 2203   | No file  |
| 2196   | No file  |
| 2192   | No file  |
| 2189   | No file  |
| 2183   | No file  |
| 2179   | No file  |
| 2171   | No file  |
| 2163   | No file  |
| 2156   | No file  |
| 2151   | No file  |
| 2147   | No file  |
| 2142   | No file  |
| 2138   | No file  |
| 2134   | No file  |
| 2130   | No file  |
| 2122   | No file  |
| 2107   | No file  |
| 2098   | No file  |
| 2089   | No file  |
| 2081   | No file  |
| 2073   | No file  |
| 2067   | No file  |
| 2063   | No file  |
| 2059   | No file  |
| 2052   | No file  |
| 2044   | No file  |
| 2039   | No file  |
| 2032   | No file  |
| 2025   | No file  |
| 2011   | No file  |
| 2005   | No file  |
| 2000   | No file  |
| 1996   | No file  |
| 1991   | No file  |
| 1985   | No file  |
| 1980   | No file  |
| 1969   | No file  |
| 1964   | No file  |
| 1958   | No file  |
| 1950   | No file  |
| 1945   | No file  |
| 1937   | No file  |
| 1933   | No file  |
| 1927   | No file  |
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

None. The handler names each `RESOURCE` key with its LOC type 37 text (the
key's hash, sheet `str_id2` 2) and each quest with its LOC type 18 title
from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset           | Type                         | Field            | Notes                                     |
| ---------------- | ---------------------------- | ---------------- | ----------------------------------------- |
| `+0x00`          | u32                          | curriculum_count | `ToClient_RequestOlviaAcademyCurriculumCount()` |
| `+0x04`          | Curriculum[curriculum_count] | curricula        | `ToClient_RequestOlviaAcademyCurriculumAt(index)`, index from `0` |
| `curricula+0x00` | u32                          | reward_count     | `ToClient_RequestOlviaAcademyRewardCount()` |
| `curricula+0x04` | Reward[reward_count]         | rewards          | `ToClient_RequestOlviaAcademyRewardAt(index)`, index from `0`; end at the last byte |

### Curriculum (variable: 20 bytes + texts and subjects)

| Offset                  | Type                   | Field            | Notes                                                       |
| ----------------------- | ---------------------- | ---------------- | ----------------------------------------------------------- |
| `+0x00`                 | str16                  | curriculum_title | `RESOURCE` key; `PANEL_OLVIA_ACADEMY_CURRICULM_BATTLE_TITLE` "Combat" |
| `curriculum_title+0x00` | str8                   | curriculum_icon  | Texture ID of the list icon (`Combine_Etc_OlviaSchoolAcademy_01_List_Icon_03_Normal`) |
| `curriculum_icon+0x00`  | u32                    | subject_count    | `getSubjectCount()`                                         |
| `curriculum_icon+0x04`  | Subject[subject_count] | subjects         | `getSubjectAt(index)`, index from `0`                       |

### Subject (variable: 28 bytes + texts and quests)

| Offset               | Type                                | Field              | Notes                                                       |
| -------------------- | ----------------------------------- | ------------------ | ----------------------------------------------------------- |
| `+0x00`              | u32                                 | preview_text_count | `getPreviewTextCount()`; `0` on the Combat subjects, `4` on the Life Skill subjects |
| `+0x04`              | str16[preview_text_count]           | preview_texts      | `getPreviewTextAt(index)`; `RESOURCE` keys (`PANEL_OLVIA_ACADEMY_SUBJECT_LIFE_PREVIEW_TEXT_1_01` "Key Point: ...") |
| `preview_texts+0x00` | Preview if preview_text_count != 0  | preview            | See Preview                                                 |
| `preview+0x00`       | u32                                 | start_quest        | `getStartQuestNo()`; packed quest ID, the first quest of `quests` on every subject |
| `preview+0x04`       | str16                               | subject_title      | `getSubjectTitle()`; `RESOURCE` key (`PANEL_OLVIA_ACADEMY_SUBJECT_LIFE_TITLE_1` "Gathering") |
| `subject_title+0x00` | str16                               | subject_desc       | `getSubjectDesc()`; `RESOURCE` key                          |
| `subject_desc+0x00`  | u32                                 | quest_count        | `getQuestCount()`                                           |
| `subject_desc+0x04`  | Subject Quest[quest_count]          | quests             | See Subject Quest                                           |

### Preview (variable: 24 bytes + texts)

The page the window opens before a subject's start quest is cleared
(`updateQuestInfoPage`); the window opens it only when
`getPreviewTextAt(0)` is not `nil`.

| Offset               | Type  | Field              | Notes                                                    |
| -------------------- | ----- | ------------------ | -------------------------------------------------------- |
| `+0x00`              | str16 | preview_title      | `getPreviewTitle()`; `RESOURCE` key (`PANEL_OLVIA_ACADEMY_SUBJECT_LIFE_PREVIEW_TITLE_1` "Nature's Goodies") |
| `preview_title+0x00` | str16 | preview_desc       | `getPreviewDesc()`; `RESOURCE` key                       |
| `preview_desc+0x00`  | str8  | preview_texture_id | `getPreviewTextureID()`; the page background (`Combine_Etc_OlviaSchoolAcademy_BG_11`) |

### Subject Quest (variable: 12 bytes + texture ID)

| Offset  | Type | Field            | Notes                                                              |
| ------- | ---- | ---------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | quest            | `getQuestNoAt(index)`; packed quest ID                             |
| `+0x04` | str8 | quest_texture_id | `getQuestTextureIDAt(index)`; the roadmap slot image, `OlviaSchoolAcademy_<Course>_Quest_<sub ID>` |

### Reward (variable: 36 bytes + texts and groups)

| Offset                  | Type                             | Field              | Notes                                                 |
| ----------------------- | -------------------------------- | ------------------ | ----------------------------------------------------- |
| `+0x00`                 | str16                            | reward_title       | `getRewardTitle()`; `RESOURCE` key (`PANEL_OLVIA_ACADEMY_FAMILYREWARD_TITLE_BATTLE` "Family Rewards - Combat") |
| `reward_title+0x00`     | str16                            | reward_sub_title   | `getRewardSubTitle()`; `RESOURCE` key                 |
| `reward_sub_title+0x00` | str16                            | reward_desc        | `getRewardDesc()`; `RESOURCE` key                     |
| `reward_desc+0x00`      | str8                             | reward_icon        | `getRewardIcon()`; texture ID of the tab icon         |
| `reward_icon+0x00`      | u32                              | reward_group_count | `getRewardGroupCount()`                               |
| `reward_icon+0x04`      | Reward Group[reward_group_count] | reward_groups      | `getRewardGroupAt(index)`, index from `0`             |

### Reward Group (variable: 12 bytes + title and quests)

| Offset                    | Type             | Field              | Notes                                                |
| ------------------------- | ---------------- | ------------------ | ---------------------------------------------------- |
| `+0x00`                   | str16            | reward_group_title | `getRewardGroupTitle()`; `RESOURCE` key, the Life Skill groups reuse the subject titles (`PANEL_OLVIA_ACADEMY_SUBJECT_LIFE_TITLE_1` "Gathering") |
| `reward_group_title+0x00` | u32              | quest_count        | `getQuestCount()`                                    |
| `reward_group_title+0x04` | u32[quest_count] | quests             | `getQuestNoAt(index)`; packed quest IDs              |

## Curricula and Rewards

On client 3482 the file holds two curricula with 2 and 9 subjects and two
family rewards with 1 and 9 groups. Every text resolves to an English LOC
type 37 text.

| Curriculum | Subject        | Quest chain | Quests | Preview texts |
| ---------- | -------------- | ----------: | -----: | ------------: |
| Combat     | Basic Tactics  | 2310        | 12     | 0             |
| Combat     | Field Tactics  | 2310        | 19     | 0             |
| Life Skill | Gathering      | 2325        | 10     | 4             |
| Life Skill | Fishing        | 2316        | 13     | 4             |
| Life Skill | Hunting        | 2314        | 13     | 4             |
| Life Skill | Cooking        | 2313        | 13     | 4             |
| Life Skill | Alchemy        | 2311        | 12     | 4             |
| Life Skill | Processing     | 2317        | 11     | 4             |
| Life Skill | Training       | 2312        | 14     | 4             |
| Life Skill | Farming        | 2318        | 12     | 4             |
| Life Skill | Sailing/Barter | 2315        | 13     | 4             |

| Reward                      | Group                    | Quests of chain 2323 |
| --------------------------- | ------------------------ | -------------------- |
| Family Rewards - Combat     | Combat                   | 1 to 36              |
| Family Rewards - Life Skill | Gathering                | 101 to 106           |
| Family Rewards - Life Skill | Fishing                  | 161 to 166           |
| Family Rewards - Life Skill | Hunting                  | 141 to 145           |
| Family Rewards - Life Skill | Cooking                  | 111 to 116           |
| Family Rewards - Life Skill | Alchemy                  | 121 to 126           |
| Family Rewards - Life Skill | Processing               | 171 to 175           |
| Family Rewards - Life Skill | Training                 | 131 to 135           |
| Family Rewards - Life Skill | Farming                  | 181 to 185           |
| Family Rewards - Life Skill | Sailing/Barter           | 151 to 155           |

## Field Names

No reference source has the file: it first appears on client 3186
(absent on client 3177), and a private server's `DataSheets.bexcel` on
client 1784 has no sheet with `Olvia` or `Academy` in its name. Every name
comes from the getter the client Lua (client 3482) calls on the object the
field belongs to: `panel_window_olviaacademy_main_all_1.luac` and
`_2.luac` call `getCurriculumTitle()`, `getCurriculumIcon()`,
`getSubjectCount()` and `getSubjectAt()` on a curriculum;
`getPreviewTextCount()`, `getPreviewTextAt()`, `getPreviewTitle()`,
`getPreviewDesc()`, `getPreviewTextureID()`, `getStartQuestNo()`,
`getSubjectTitle()`, `getSubjectDesc()`, `getQuestCount()`,
`getQuestNoAt()` and `getQuestTextureIDAt()` on a subject;
`getRewardTitle()`, `getRewardSubTitle()`, `getRewardDesc()`,
`getRewardIcon()`, `getRewardGroupCount()` and `getRewardGroupAt()` on a
reward; `getRewardGroupTitle()`, `getQuestCount()` and `getQuestNoAt()` on
a reward group. The texts go through `PAGetString(Defines.StringSheet_RESOURCE, ...)`
and the icons and textures through `ChangeTextureInfoTextureIDAsync()`,
which matches the `RESOURCE` keys and texture IDs the strings hold.

## Notes

- Decompressed size on client 3482: `17166` bytes; the walk ends at the
  last byte.
- The 142 subject quests are all in
  `olviaacademycurriculumquestlist.bss` (client 3482). The list holds 26
  more: `2308/1` and `2309/1` (the enrollment and graduation quests of
  [`olviaacademyseasonss.bss`](olviaacademyseasonss_bss.md)) and the 24
  `Material Support` and `Ship Support` quests at sub IDs 53 to 62, which
  no subject lists. Quest `2310/19` is in neither.
- The 85 reward group quests are exactly the quests of
  `olviaacademyrewardquestlist.bss` (client 3482).
- Each `quest_texture_id` ends in its quest's sub ID with two digits
  (`OlviaSchoolAcademy_Battle_Quest_13` on `2310/13`).
- The handler shows one row per subject and one per reward group, each
  with the fields of its curriculum or reward. The row key `row_ref`
  (`curriculum:1:0`, `reward:1:3`: section, then the two Lua indexes from
  `0`) is what the quest list views link to; each quest links to its row
  in the quest list file.

## Open Questions

### A Subject With Preview Texts but No Preview Page

The preview title, description and texture follow only when
`preview_text_count` is not `0`: the two Combat subjects store `0` and go
straight on to `start_quest`, the nine Life Skill subjects store `4` texts
and the three preview fields. Whether the client writes the three fields
for a subject on its own flag (and a subject could have a preview page with
no texts) or with the text list is open, since every subject on client 3482
has both or neither.
