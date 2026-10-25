# Empty BSS Tables Format

## Purpose

PABR `.bss` tables the client ships with no records. Each is 20 bytes: the
`PABR` magic, a record count of `0`, a string table with no strings and the
8-byte PABR trailer. Every file below is that on client 3474. On the two
older clients checked it is the same 20 bytes, not in the archive, or (four
files) a table with records that this doc does not cover:

| File                                  | Client 1784 | Client 1485 |
| ------------------------------------- | ----------- | ----------- |
| `audiorenewal.bss`                    | empty       | empty       |
| `beginnerroadmaplinkurldata.bss`      | absent      | absent      |
| `cashproduct_discountperiodcheck.bss` | empty       | empty       |
| `cashproductcachedata.bss`            | records     | records     |
| `charactertrigger.bss`                | records     | records     |
| `commonskill.bss`                     | empty       | empty       |
| `dropuiurlinfo.bss`                   | absent      | absent      |
| `enchantlightstone.bss`               | absent      | absent      |
| `equipitemchanage.bss`                | records     | absent      |
| `fishinginfo.bss`                     | empty       | empty       |
| `instancefieldenteroption.bss`        | empty       | absent      |
| `instancefieldmanagement.bss`         | empty       | empty       |
| `itembundle.bss`                      | empty       | empty       |
| `lightstoneenchantgroup.bss`          | absent      | absent      |
| `naktype.bss`                         | empty       | records     |
| `normalgroupquest.bss`                | empty       | empty       |
| `openuiwhennak.bss`                   | absent      | absent      |
| `preloadpcactioncharacter.bss`        | empty       | empty       |
| `shadowarenalist.bss`                 | empty       | empty       |
| `skillselectuiinfo.bss`               | absent      | absent      |
| `spawngroup.bss`                      | empty       | empty       |
| `tempcashstaticstatus.bss`            | absent      | absent      |

The Lightstone names point at Lightstone enhancement and Lightstone
enhancement groups, but no record, Lua function or reference source shows
what a row would hold. `normalgroupquest.bss` is the quest list of the
quest widget's group quest line, a feature the live client keeps off; see
[Normal Group Quests](#normal-group-quests).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                  | Bytes | Records        | Row bytes |
| ------ | -------------- | ------------------------------------- | ----- | -------------- | --------- |
| 1      | 1208 and later | `audiorenewal.bss`                    | 20    | 1 String Table | 4         |
| 1      | 3144 and later | `beginnerroadmaplinkurldata.bss`      | 20    | 1 String Table | 4         |
| 1      | 1784 and later | `cashproduct_discountperiodcheck.bss` | 20    | 1 String Table | 4         |
| 1      | 3144 and later | `cashproductcachedata.bss`            | 20    | 1 String Table | 4         |
| 1      | 822 and later  | `charactertrigger.bss`                | 20    | 1 String Table | 4         |
| 1      | 1784 and later | `commonskill.bss`                     | 20    | 1 String Table | 4         |
| 1      | 3144 and later | `dropuiurlinfo.bss`                   | 20    | 1 String Table | 4         |
| 1      | 3144 and later | `enchantlightstone.bss`               | 20    | 1 String Table | 4         |
| 1      | 3144 and later | `equipitemchanage.bss`                | 20    | 1 String Table | 4         |
| 1      | 805 and later  | `fishinginfo.bss`                     | 20    | 1 String Table | 4         |
| 1      | 1784 and later | `instancefieldenteroption.bss`        | 20    | 1 String Table | 4         |
| 1      | 1784 and later | `instancefieldmanagement.bss`         | 20    | 1 String Table | 4         |
| 1      | 805 and later  | `itembundle.bss`                      | 20    | 1 String Table | 4         |
| 1      | 3144 and later | `lightstoneenchantgroup.bss`          | 20    | 1 String Table | 4         |
| 1      | 3144 and later | `naktype.bss`                         | 20    | 1 String Table | 4         |
| 1      | 1784 and later | `normalgroupquest.bss`                | 20    | 1 String Table | 4         |
| 1      | 3144 and later | `openuiwhennak.bss`                   | 20    | 1 String Table | 4         |
| 1      | 1784 and later | `preloadpcactioncharacter.bss`        | 20    | 1 String Table | 4         |
| 1      | 1784 and later | `shadowarenalist.bss`                 | 20    | 1 String Table | 4         |
| 1      | 3144 and later | `skillselectuiinfo.bss`               | 20    | 1 String Table | 4         |
| 1      | 805 and later  | `spawngroup.bss`                      | 20    | 1 String Table | 4         |
| 1      | 3144 and later | `tempcashstaticstatus.bss`            | 20    | 1 String Table | 4         |

| Layout | File                                  | Known         | Unknown    |
| ------ | ------------------------------------- | ------------- | ---------- |
| 1      | `audiorenewal.bss`                    | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `beginnerroadmaplinkurldata.bss`      | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `cashproduct_discountperiodcheck.bss` | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `cashproductcachedata.bss`            | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `charactertrigger.bss`                | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `commonskill.bss`                     | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `dropuiurlinfo.bss`                   | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `enchantlightstone.bss`               | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `equipitemchanage.bss`                | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `fishinginfo.bss`                     | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `instancefieldenteroption.bss`        | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `instancefieldmanagement.bss`         | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `itembundle.bss`                      | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `lightstoneenchantgroup.bss`          | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `naktype.bss`                         | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `normalgroupquest.bss`                | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `openuiwhennak.bss`                   | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `preloadpcactioncharacter.bss`        | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `shadowarenalist.bss`                 | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `skillselectuiinfo.bss`               | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `spawngroup.bss`                      | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `tempcashstaticstatus.bss`            | 20 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `0b6f6b5b003f`  |
| 3482   | Layout 1             | `0b6f6b5b003f`  |
| 3474   | Layout 1             | `0b6f6b5b003f`  |
| 3473   | Layout 1             | `0b6f6b5b003f`  |
| 3464   | Layout 1             | `0b6f6b5b003f`  |
| 3458   | Layout 1             | `0b6f6b5b003f`  |
| 3454   | Layout 1             | `0b6f6b5b003f`  |
| 3444   | Layout 1             | `0b6f6b5b003f`  |
| 3435   | Layout 1             | `0b6f6b5b003f`  |
| 3426   | Layout 1             | `0b6f6b5b003f`  |
| 3418   | Layout 1             | `0b6f6b5b003f`  |
| 3412   | Layout 1             | `0b6f6b5b003f`  |
| 3402   | Layout 1             | `0b6f6b5b003f`  |
| 3396   | Layout 1             | `0b6f6b5b003f`  |
| 3387   | Layout 1             | `0b6f6b5b003f`  |
| 3381   | Layout 1             | `0b6f6b5b003f`  |
| 3373   | Layout 1             | `0b6f6b5b003f`  |
| 3364   | Layout 1             | `0b6f6b5b003f`  |
| 3356   | Layout 1             | `0b6f6b5b003f`  |
| 3349   | Layout 1             | `0b6f6b5b003f`  |
| 3342   | Layout 1             | `0b6f6b5b003f`  |
| 3335   | Layout 1             | `0b6f6b5b003f`  |
| 3326   | Layout 1             | `0b6f6b5b003f`  |
| 3321   | Layout 1             | `0b6f6b5b003f`  |
| 3314   | Layout 1             | `0b6f6b5b003f`  |
| 3303   | Layout 1             | `0b6f6b5b003f`  |
| 3302   | Layout 1             | `0b6f6b5b003f`  |
| 3293   | Layout 1             | `0b6f6b5b003f`  |
| 3283   | Layout 1             | `0b6f6b5b003f`  |
| 3275   | Layout 1             | `0b6f6b5b003f`  |
| 3267   | Layout 1             | `0b6f6b5b003f`  |
| 3258   | Layout 1             | `0b6f6b5b003f`  |
| 3251   | Layout 1             | `0b6f6b5b003f`  |
| 3242   | Layout 1             | `0b6f6b5b003f`  |
| 3235   | Layout 1             | `0b6f6b5b003f`  |
| 3229   | Layout 1             | `0b6f6b5b003f`  |
| 3212   | Layout 1             | `0b6f6b5b003f`  |
| 3203   | Layout 1             | `0b6f6b5b003f`  |
| 3193   | Layout 1             | `0b6f6b5b003f`  |
| 3186   | Layout 1             | `0b6f6b5b003f`  |
| 3177   | Layout 1             | `0b6f6b5b003f`  |
| 3169   | Layout 1             | `0b6f6b5b003f`  |
| 3158   | Layout 1             | `0b6f6b5b003f`  |
| 3151   | Layout 1             | `0b6f6b5b003f`  |
| 3144   | Layout 1             | `0b6f6b5b003f`  |
| 3133   | No documented layout | `0b6f6b5b003f`  |
| 3125   | No documented layout | `0b6f6b5b003f`  |
| 3118   | No documented layout | `0b6f6b5b003f`  |
| 3111   | No documented layout | `0b6f6b5b003f`  |
| 3103   | No documented layout | `0b6f6b5b003f`  |
| 3095   | No documented layout | `0b6f6b5b003f`  |
| 3086   | No documented layout | `0b6f6b5b003f`  |
| 3072   | No documented layout | `0b6f6b5b003f`  |
| 3062   | No documented layout | `0b6f6b5b003f`  |
| 3052   | No documented layout | `0b6f6b5b003f`  |
| 3045   | No documented layout | `0b6f6b5b003f`  |
| 3037   | No documented layout | `0b6f6b5b003f`  |
| 3030   | No documented layout | `0b6f6b5b003f`  |
| 3021   | No documented layout | `0b6f6b5b003f`  |
| 3012   | No documented layout | `0b6f6b5b003f`  |
| 3002   | No documented layout | `0b6f6b5b003f`  |
| 2995   | No documented layout | `0b6f6b5b003f`  |
| 2987   | No documented layout | `0b6f6b5b003f`  |
| 2978   | No documented layout | `0b6f6b5b003f`  |
| 2970   | No documented layout | `0b6f6b5b003f`  |
| 2959   | No documented layout | `0b6f6b5b003f`  |
| 2951   | No documented layout | `0b6f6b5b003f`  |
| 2942   | No documented layout | `0b6f6b5b003f`  |
| 2935   | No documented layout | `0b6f6b5b003f`  |
| 2932   | No documented layout | `0b6f6b5b003f`  |
| 2923   | No documented layout | `0b6f6b5b003f`  |
| 2919   | No documented layout | `0b6f6b5b003f`  |
| 2907   | No documented layout | `0b6f6b5b003f`  |
| 2900   | No documented layout | `0b6f6b5b003f`  |
| 2891   | No documented layout | `0b6f6b5b003f`  |
| 2882   | No documented layout | `0b6f6b5b003f`  |
| 2872   | No documented layout | `0b6f6b5b003f`  |
| 2863   | No documented layout | `0b6f6b5b003f`  |
| 2855   | No documented layout | `0b6f6b5b003f`  |
| 2849   | No documented layout | `0b6f6b5b003f`  |
| 2844   | No documented layout | `0b6f6b5b003f`  |
| 2834   | No documented layout | `0b6f6b5b003f`  |
| 2825   | No documented layout | `0b6f6b5b003f`  |
| 2819   | No documented layout | `0b6f6b5b003f`  |
| 2811   | No documented layout | `0b6f6b5b003f`  |
| 2803   | No documented layout | `0b6f6b5b003f`  |
| 2794   | No documented layout | `0b6f6b5b003f`  |
| 2783   | No documented layout | `0b6f6b5b003f`  |
| 2774   | No documented layout | `0b6f6b5b003f`  |
| 2765   | No documented layout | `0b6f6b5b003f`  |
| 2756   | No documented layout | `0b6f6b5b003f`  |
| 2750   | No documented layout | `0b6f6b5b003f`  |
| 2743   | No documented layout | `0b6f6b5b003f`  |
| 2736   | No documented layout | `0b6f6b5b003f`  |
| 2726   | No documented layout | `0b6f6b5b003f`  |
| 2717   | No documented layout | `0b6f6b5b003f`  |
| 2709   | No documented layout | `0b6f6b5b003f`  |
| 2703   | No documented layout | `0b6f6b5b003f`  |
| 2695   | No documented layout | `0b6f6b5b003f`  |
| 2684   | No documented layout | `0b6f6b5b003f`  |
| 2672   | No documented layout | `0b6f6b5b003f`  |
| 2665   | No documented layout | `0b6f6b5b003f`  |
| 2657   | No documented layout | `0b6f6b5b003f`  |
| 2649   | No documented layout | `0b6f6b5b003f`  |
| 2644   | No documented layout | `0b6f6b5b003f`  |
| 2637   | No documented layout | `0b6f6b5b003f`  |
| 2629   | No documented layout | `0b6f6b5b003f`  |
| 2619   | No documented layout | `0b6f6b5b003f`  |
| 2612   | No documented layout | `0b6f6b5b003f`  |
| 2606   | No documented layout | `0b6f6b5b003f`  |
| 2602   | No documented layout | `0b6f6b5b003f`  |
| 2601   | No documented layout | `0b6f6b5b003f`  |
| 2592   | No documented layout | `0b6f6b5b003f`  |
| 2583   | No documented layout | `0b6f6b5b003f`  |
| 2575   | No documented layout | `0b6f6b5b003f`  |
| 2567   | No documented layout | `0b6f6b5b003f`  |
| 2560   | No documented layout | `0b6f6b5b003f`  |
| 2553   | No documented layout | `0b6f6b5b003f`  |
| 2545   | No documented layout | `0b6f6b5b003f`  |
| 2538   | No documented layout | `0b6f6b5b003f`  |
| 2529   | No documented layout | `0b6f6b5b003f`  |
| 2519   | No documented layout | `0b6f6b5b003f`  |
| 2513   | No documented layout | `0b6f6b5b003f`  |
| 2510   | No documented layout | `0b6f6b5b003f`  |
| 2507   | No documented layout | `0b6f6b5b003f`  |
| 2503   | No documented layout | `0b6f6b5b003f`  |
| 2498   | No documented layout | `0b6f6b5b003f`  |
| 2492   | No documented layout | `0b6f6b5b003f`  |
| 2487   | No documented layout | `0b6f6b5b003f`  |
| 2480   | No documented layout | `0b6f6b5b003f`  |
| 2474   | No documented layout | `0b6f6b5b003f`  |
| 2468   | No documented layout | `0b6f6b5b003f`  |
| 2460   | No documented layout | `0b6f6b5b003f`  |
| 2453   | No documented layout | `0b6f6b5b003f`  |
| 2444   | No documented layout | `0b6f6b5b003f`  |
| 2438   | No documented layout | `0b6f6b5b003f`  |
| 2434   | No documented layout | `0b6f6b5b003f`  |
| 2429   | No documented layout | `0b6f6b5b003f`  |
| 2421   | No documented layout | `0b6f6b5b003f`  |
| 2414   | No documented layout | `0b6f6b5b003f`  |
| 2407   | No documented layout | `0b6f6b5b003f`  |
| 2401   | No documented layout | `0b6f6b5b003f`  |
| 2397   | No documented layout | `0b6f6b5b003f`  |
| 2393   | No documented layout | `0b6f6b5b003f`  |
| 2384   | No documented layout | `0b6f6b5b003f`  |
| 2378   | No documented layout | `0b6f6b5b003f`  |
| 2372   | No documented layout | `0b6f6b5b003f`  |
| 2358   | No documented layout | `0b6f6b5b003f`  |
| 2352   | No documented layout | `0b6f6b5b003f`  |
| 2347   | No documented layout | `0b6f6b5b003f`  |
| 2343   | No documented layout | `0b6f6b5b003f`  |
| 2335   | No documented layout | `0b6f6b5b003f`  |
| 2327   | No documented layout | `0b6f6b5b003f`  |
| 2324   | No documented layout | `0b6f6b5b003f`  |
| 2319   | No documented layout | `0b6f6b5b003f`  |
| 2313   | No documented layout | `0b6f6b5b003f`  |
| 2308   | No documented layout | `0b6f6b5b003f`  |
| 2302   | No documented layout | `0b6f6b5b003f`  |
| 2295   | No documented layout | `0b6f6b5b003f`  |
| 2290   | No documented layout | `0b6f6b5b003f`  |
| 2284   | No documented layout | `0b6f6b5b003f`  |
| 2276   | No documented layout | `0b6f6b5b003f`  |
| 2269   | No documented layout | `0b6f6b5b003f`  |
| 2259   | No documented layout | `0b6f6b5b003f`  |
| 2250   | No documented layout | `0b6f6b5b003f`  |
| 2243   | No documented layout | `0b6f6b5b003f`  |
| 2235   | No documented layout | `0b6f6b5b003f`  |
| 2229   | No documented layout | `0b6f6b5b003f`  |
| 2224   | No documented layout | `0b6f6b5b003f`  |
| 2218   | No documented layout | `0b6f6b5b003f`  |
| 2215   | No documented layout | `0b6f6b5b003f`  |
| 2207   | No documented layout | `0b6f6b5b003f`  |
| 2203   | No documented layout | `0b6f6b5b003f`  |
| 2196   | No documented layout | `0b6f6b5b003f`  |
| 2192   | No documented layout | `0b6f6b5b003f`  |
| 2189   | No documented layout | `0b6f6b5b003f`  |
| 2183   | No documented layout | `0b6f6b5b003f`  |
| 2179   | No documented layout | `0b6f6b5b003f`  |
| 2171   | No documented layout | `0b6f6b5b003f`  |
| 2163   | No documented layout | `0b6f6b5b003f`  |
| 2156   | No documented layout | `0b6f6b5b003f`  |
| 2151   | No documented layout | `0b6f6b5b003f`  |
| 2147   | No documented layout | `0b6f6b5b003f`  |
| 2142   | No documented layout | `0b6f6b5b003f`  |
| 2138   | No documented layout | `0b6f6b5b003f`  |
| 2134   | No documented layout | `0b6f6b5b003f`  |
| 2130   | No documented layout | `0b6f6b5b003f`  |
| 2122   | No documented layout | `0b6f6b5b003f`  |
| 2107   | No documented layout | `0b6f6b5b003f`  |
| 2098   | No documented layout | `0b6f6b5b003f`  |
| 2089   | No documented layout | `0b6f6b5b003f`  |
| 2081   | No documented layout | `0b6f6b5b003f`  |
| 2073   | No documented layout | `0b6f6b5b003f`  |
| 2067   | No documented layout | `0b6f6b5b003f`  |
| 2063   | No documented layout | `0b6f6b5b003f`  |
| 2059   | No documented layout | `0b6f6b5b003f`  |
| 2052   | No documented layout | `0b6f6b5b003f`  |
| 2044   | No documented layout | `0b6f6b5b003f`  |
| 2039   | No documented layout | `0b6f6b5b003f`  |
| 2032   | No documented layout | `0b6f6b5b003f`  |
| 2025   | No documented layout | `0b6f6b5b003f`  |
| 2011   | No documented layout | `0b6f6b5b003f`  |
| 2005   | No documented layout | `0b6f6b5b003f`  |
| 2000   | No documented layout | `0b6f6b5b003f`  |
| 1996   | No documented layout | `0b6f6b5b003f`  |
| 1991   | No documented layout | `0b6f6b5b003f`  |
| 1985   | No documented layout | `0b6f6b5b003f`  |
| 1980   | No documented layout | `0b6f6b5b003f`  |
| 1969   | No documented layout | `0b6f6b5b003f`  |
| 1964   | No documented layout | `0b6f6b5b003f`  |
| 1958   | No documented layout | `0b6f6b5b003f`  |
| 1950   | No documented layout | `0b6f6b5b003f`  |
| 1945   | No documented layout | `0b6f6b5b003f`  |
| 1937   | No documented layout | `0b6f6b5b003f`  |
| 1933   | No documented layout | `0b6f6b5b003f`  |
| 1927   | No documented layout | `0b6f6b5b003f`  |
| 1921   | No documented layout | `0b6f6b5b003f`  |
| 1914   | No documented layout | `0b6f6b5b003f`  |
| 1908   | No documented layout | `0b6f6b5b003f`  |
| 1897   | No documented layout | `0b6f6b5b003f`  |
| 1892   | No documented layout | `0b6f6b5b003f`  |
| 1886   | No documented layout | `0b6f6b5b003f`  |
| 1881   | No documented layout | `0b6f6b5b003f`  |
| 1871   | No documented layout | `0b6f6b5b003f`  |
| 1866   | No documented layout | `0b6f6b5b003f`  |
| 1862   | No documented layout | `0b6f6b5b003f`  |
| 1854   | No documented layout | `0b6f6b5b003f`  |
| 1846   | No documented layout | `0b6f6b5b003f`  |
| 1838   | No documented layout | `0b6f6b5b003f`  |
| 1832   | No documented layout | `0b6f6b5b003f`  |
| 1826   | No documented layout | `0b6f6b5b003f`  |
| 1822   | No documented layout | `0b6f6b5b003f`  |
| 1818   | No documented layout | `0b6f6b5b003f`  |
| 1804   | No documented layout | `0b6f6b5b003f`  |
| 1794   | No documented layout | `0b6f6b5b003f`  |
| 1790   | No documented layout | `0b6f6b5b003f`  |
| 1784   | No documented layout | `0b6f6b5b003f`  |
| 1774   | No documented layout | `0b6f6b5b003f`  |
| 1771   | No documented layout | `0b6f6b5b003f`  |
| 1762   | No documented layout | `0b6f6b5b003f`  |
| 1759   | No documented layout | `0b6f6b5b003f`  |
| 1754   | No documented layout | `0b6f6b5b003f`  |
| 1749   | No documented layout | `0b6f6b5b003f`  |
| 1743   | No documented layout | `0b6f6b5b003f`  |
| 1737   | No documented layout | `0b6f6b5b003f`  |
| 1731   | No documented layout | `0b6f6b5b003f`  |
| 1725   | No documented layout | `0b6f6b5b003f`  |
| 1717   | No documented layout | `0b6f6b5b003f`  |
| 1710   | No documented layout | `0b6f6b5b003f`  |
| 1704   | No documented layout | `0b6f6b5b003f`  |
| 1698   | No documented layout | `0b6f6b5b003f`  |
| 1690   | No documented layout | `0b6f6b5b003f`  |
| 1685   | No documented layout | `0b6f6b5b003f`  |
| 1680   | No documented layout | `0b6f6b5b003f`  |
| 1674   | No documented layout | `0b6f6b5b003f`  |
| 1668   | No documented layout | `0b6f6b5b003f`  |
| 1659   | No documented layout | `0b6f6b5b003f`  |
| 1649   | No documented layout | `0b6f6b5b003f`  |
| 1642   | No documented layout | `0b6f6b5b003f`  |
| 1636   | No documented layout | `0b6f6b5b003f`  |
| 1628   | No documented layout | `0b6f6b5b003f`  |
| 1622   | No documented layout | `0b6f6b5b003f`  |
| 1614   | No documented layout | `0b6f6b5b003f`  |
| 1608   | No documented layout | `0b6f6b5b003f`  |
| 1602   | No documented layout | `0b6f6b5b003f`  |
| 1598   | No documented layout | `0b6f6b5b003f`  |
| 1594   | No documented layout | `0b6f6b5b003f`  |
| 1590   | No documented layout | `0b6f6b5b003f`  |
| 1587   | No documented layout | `0b6f6b5b003f`  |
| 1584   | No documented layout | `0b6f6b5b003f`  |
| 1579   | No documented layout | `0b6f6b5b003f`  |
| 1572   | No documented layout | `0b6f6b5b003f`  |
| 1565   | No documented layout | `0b6f6b5b003f`  |
| 1559   | No documented layout | `0b6f6b5b003f`  |
| 1554   | No documented layout | `0b6f6b5b003f`  |
| 1547   | No documented layout | `0b6f6b5b003f`  |
| 1537   | No documented layout | `0b6f6b5b003f`  |
| 1529   | No documented layout | `0b6f6b5b003f`  |
| 1524   | No documented layout | `0b6f6b5b003f`  |
| 1519   | No documented layout | `0b6f6b5b003f`  |
| 1509   | No documented layout | `0b6f6b5b003f`  |
| 1506   | No documented layout | `0b6f6b5b003f`  |
| 1504   | No documented layout | `0b6f6b5b003f`  |
| 1500   | No documented layout | `0b6f6b5b003f`  |
| 1493   | No documented layout | `0b6f6b5b003f`  |
| 1489   | No documented layout | `0b6f6b5b003f`  |
| 1485   | No documented layout | `0b6f6b5b003f`  |
| 1481   | No documented layout | `0b6f6b5b003f`  |
| 1474   | No documented layout | `0b6f6b5b003f`  |
| 1466   | No documented layout | `0b6f6b5b003f`  |
| 1462   | No documented layout | `0b6f6b5b003f`  |
| 1459   | No documented layout | `0b6f6b5b003f`  |
| 1453   | No documented layout | `0b6f6b5b003f`  |
| 1450   | No documented layout | `0b6f6b5b003f`  |
| 1445   | No documented layout | `0b6f6b5b003f`  |
| 1439   | No documented layout | `0b6f6b5b003f`  |
| 1433   | No documented layout | `0b6f6b5b003f`  |
| 1430   | No documented layout | `0b6f6b5b003f`  |
| 1426   | No documented layout | `0b6f6b5b003f`  |
| 1421   | No documented layout | `0b6f6b5b003f`  |
| 1417   | No documented layout | `0b6f6b5b003f`  |
| 1416   | No documented layout | `0b6f6b5b003f`  |
| 1409   | No documented layout | `0b6f6b5b003f`  |
| 1405   | No documented layout | `0b6f6b5b003f`  |
| 1401   | No documented layout | `0b6f6b5b003f`  |
| 1396   | No documented layout | `0b6f6b5b003f`  |
| 1391   | No documented layout | `0b6f6b5b003f`  |
| 1390   | No documented layout | `0b6f6b5b003f`  |
| 1386   | No documented layout | `0b6f6b5b003f`  |
| 1381   | No documented layout | `0b6f6b5b003f`  |
| 1379   | No documented layout | `0b6f6b5b003f`  |
| 1372   | No documented layout | `0b6f6b5b003f`  |
| 1366   | No documented layout | `0b6f6b5b003f`  |
| 1364   | No documented layout | `0b6f6b5b003f`  |
| 1363   | No documented layout | `0b6f6b5b003f`  |
| 1360   | No documented layout | `0b6f6b5b003f`  |
| 1358   | No documented layout | `0b6f6b5b003f`  |
| 1355   | No documented layout | `0b6f6b5b003f`  |
| 1351   | No documented layout | `0b6f6b5b003f`  |
| 1348   | No documented layout | `0b6f6b5b003f`  |
| 1346   | No documented layout | `0b6f6b5b003f`  |
| 1341   | No documented layout | `0b6f6b5b003f`  |
| 1340   | No documented layout | `0b6f6b5b003f`  |
| 1338   | No documented layout | `0b6f6b5b003f`  |
| 1335   | No documented layout | `0b6f6b5b003f`  |
| 1333   | No documented layout | `0b6f6b5b003f`  |
| 1329   | No documented layout | `0b6f6b5b003f`  |
| 1327   | No documented layout | `0b6f6b5b003f`  |
| 1324   | No documented layout | `0b6f6b5b003f`  |
| 1321   | No documented layout | `0b6f6b5b003f`  |
| 1319   | No documented layout | `0b6f6b5b003f`  |
| 1318   | No documented layout | `0b6f6b5b003f`  |
| 1316   | No documented layout | `0b6f6b5b003f`  |
| 1313   | No documented layout | `0b6f6b5b003f`  |
| 1311   | No documented layout | `0b6f6b5b003f`  |
| 1309   | No documented layout | `0b6f6b5b003f`  |
| 1304   | No documented layout | `0b6f6b5b003f`  |
| 1292   | No documented layout | `0b6f6b5b003f`  |
| 1286   | No documented layout | `0b6f6b5b003f`  |
| 1280   | No documented layout | `0b6f6b5b003f`  |
| 1276   | No documented layout | `0b6f6b5b003f`  |
| 1267   | No documented layout | `0b6f6b5b003f`  |
| 1261   | No documented layout | `0b6f6b5b003f`  |
| 1256   | No documented layout | `0b6f6b5b003f`  |
| 1250   | No documented layout | `0b6f6b5b003f`  |
| 1246   | Layout 1             | `0b6f6b5b003f`  |
| 1239   | Layout 1             | `0b6f6b5b003f`  |
| 1230   | Layout 1             | `0b6f6b5b003f`  |
| 1226   | Layout 1             | `0b6f6b5b003f`  |
| 1220   | Layout 1             | `0b6f6b5b003f`  |
| 1217   | Layout 1             | `0b6f6b5b003f`  |
| 1211   | Layout 1             | `0b6f6b5b003f`  |
| 1210   | Layout 1             | `0b6f6b5b003f`  |
| 1208   | Layout 1             | `0b6f6b5b003f`  |
| 1203   | Layout 1             | `0b6f6b5b003f`  |
| 1197   | Layout 1             | `0b6f6b5b003f`  |
| 1194   | Layout 1             | `0b6f6b5b003f`  |
| 1192   | Layout 1             | `0b6f6b5b003f`  |
| 1187   | Layout 1             | `0b6f6b5b003f`  |
| 1183   | Layout 1             | `0b6f6b5b003f`  |
| 1177   | Layout 1             | `0b6f6b5b003f`  |
| 1173   | Layout 1             | `0b6f6b5b003f`  |
| 1167   | Layout 1             | `0b6f6b5b003f`  |
| 1164   | Layout 1             | `0b6f6b5b003f`  |
| 1156   | Layout 1             | `0b6f6b5b003f`  |
| 1149   | Layout 1             | `0b6f6b5b003f`  |
| 1144   | No documented layout | `0b6f6b5b003f`  |
| 1137   | No documented layout | `0b6f6b5b003f`  |
| 1132   | No documented layout | `0b6f6b5b003f`  |
| 1127   | No documented layout | `0b6f6b5b003f`  |
| 1122   | No documented layout | `0b6f6b5b003f`  |
| 1118   | No documented layout | `0b6f6b5b003f`  |
| 1114   | No documented layout | `0b6f6b5b003f`  |
| 1109   | No documented layout | `0b6f6b5b003f`  |
| 1102   | No file              | `0b6f6b5b003f`  |
| 1096   | No file              | `0b6f6b5b003f`  |
| 1088   | No file              | `0b6f6b5b003f`  |
| 1081   | No file              | `0b6f6b5b003f`  |
| 1076   | No file              | `0b6f6b5b003f`  |
| 1069   | No file              | `0b6f6b5b003f`  |
| 1064   | No file              | `0b6f6b5b003f`  |
| 1058   | No file              | `0b6f6b5b003f`  |
| 1051   | No file              | `0b6f6b5b003f`  |
| 1044   | No file              | `0b6f6b5b003f`  |
| 1036   | No file              | `0b6f6b5b003f`  |
| 1026   | No file              | `0b6f6b5b003f`  |
| 1016   | No file              | `0b6f6b5b003f`  |
| 1009   | No file              | `0b6f6b5b003f`  |
| 1005   | No file              | `0b6f6b5b003f`  |
| 1000   | No file              | `0b6f6b5b003f`  |
| 998    | No file              | `0b6f6b5b003f`  |
| 990    | No file              | `0b6f6b5b003f`  |
| 979    | No file              | `0b6f6b5b003f`  |
| 972    | No file              | `0b6f6b5b003f`  |
| 963    | No file              | `0b6f6b5b003f`  |
| 955    | No file              | `0b6f6b5b003f`  |
| 946    | No file              | `0b6f6b5b003f`  |
| 938    | No file              | `0b6f6b5b003f`  |
| 927    | No file              | `0b6f6b5b003f`  |
| 911    | No file              | `0b6f6b5b003f`  |
| 904    | No file              | `0b6f6b5b003f`  |
| 899    | No file              | `0b6f6b5b003f`  |
| 894    | No file              | `0b6f6b5b003f`  |
| 885    | No file              | `0b6f6b5b003f`  |
| 879    | No file              | `0b6f6b5b003f`  |
| 872    | No file              | `0b6f6b5b003f`  |
| 864    | No file              | `0b6f6b5b003f`  |
| 855    | No file              | `0b6f6b5b003f`  |
| 853    | No file              | `0b6f6b5b003f`  |
| 845    | No file              | `0b6f6b5b003f`  |
| 837    | No file              | `0b6f6b5b003f`  |
| 829    | Layout 1             | `0b6f6b5b003f`  |
| 822    | Layout 1             | `0b6f6b5b003f`  |
| 814    | No documented layout | `0b6f6b5b003f`  |
| 805    | Layout 1             | `0b6f6b5b003f`  |
| 794    | No documented layout | `0b6f6b5b003f`  |
| 787    | No documented layout | `0b6f6b5b003f`  |
| 780    | No documented layout | `0b6f6b5b003f`  |
| 771    | No documented layout | `0b6f6b5b003f`  |
| 760    | No documented layout | `0b6f6b5b003f`  |
| 748    | No documented layout | `0b6f6b5b003f`  |
| 741    | No documented layout | `0b6f6b5b003f`  |
| 736    | No documented layout | `0b6f6b5b003f`  |
| 731    | No documented layout | `0b6f6b5b003f`  |
| 723    | No documented layout | `0b6f6b5b003f`  |
| 711    | No documented layout | `0b6f6b5b003f`  |
| 707    | No documented layout | `0b6f6b5b003f`  |
| 697    | No documented layout | `0b6f6b5b003f`  |
| 689    | No documented layout | `0b6f6b5b003f`  |
| 683    | No documented layout | `0b6f6b5b003f`  |
| 678    | No documented layout | `0b6f6b5b003f`  |
| 670    | No documented layout | `0b6f6b5b003f`  |
| 661    | No documented layout | `0b6f6b5b003f`  |
| 656    | No documented layout | `0b6f6b5b003f`  |
| 652    | No documented layout | `0b6f6b5b003f`  |
| 643    | No documented layout | `0b6f6b5b003f`  |
| 637    | No documented layout | `0b6f6b5b003f`  |
| 630    | No documented layout | `0b6f6b5b003f`  |
| 627    | No documented layout | `0b6f6b5b003f`  |
| 621    | No documented layout | `0b6f6b5b003f`  |
| 617    | No documented layout | `0b6f6b5b003f`  |
| 615    | No documented layout | `0b6f6b5b003f`  |
| 606    | No documented layout | `0b6f6b5b003f`  |
| 599    | No documented layout | `0b6f6b5b003f`  |
| 592    | No documented layout | `0b6f6b5b003f`  |
| 586    | No documented layout | `0b6f6b5b003f`  |
| 577    | No documented layout | `0b6f6b5b003f`  |
| 569    | No documented layout | `0b6f6b5b003f`  |
| 561    | No documented layout | `0b6f6b5b003f`  |
| 554    | No documented layout | `0b6f6b5b003f`  |
| 542    | No documented layout | `0b6f6b5b003f`  |
| 532    | No documented layout | `0b6f6b5b003f`  |
| 531    | No documented layout | `0b6f6b5b003f`  |
| 526    | No documented layout | `0b6f6b5b003f`  |
| 521    | No documented layout | `0b6f6b5b003f`  |
| 517    | No documented layout | `0b6f6b5b003f`  |
| 510    | No documented layout | `0b6f6b5b003f`  |
| 508    | No documented layout | `0b6f6b5b003f`  |
| 504    | No documented layout | `0b6f6b5b003f`  |
| 497    | No documented layout | `0b6f6b5b003f`  |
| 491    | No documented layout | `0b6f6b5b003f`  |
| 485    | No documented layout | `0b6f6b5b003f`  |
| 478    | No documented layout | `0b6f6b5b003f`  |
| 472    | No documented layout | `0b6f6b5b003f`  |
| 466    | No documented layout | `0b6f6b5b003f`  |
| 457    | No documented layout | `0b6f6b5b003f`  |
| 452    | No documented layout | `0b6f6b5b003f`  |
| 449    | No documented layout | `0b6f6b5b003f`  |
| 435    | No documented layout | `0b6f6b5b003f`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The PABR string table layout of `buffsimply.bss` (`_common/pabr_strings.py`)
with no rows. No record structure can be inferred because the files hold no
records.

| Offset              | Type         | Field        | Notes                                              |
| ------------------- | ------------ | ------------ | -------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                       |
| `+0x04`             | u32          | count        | Number of records; `0` in every file               |
| `+0x08`             | String Table | string_table | See String Table                                   |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x08` in every file   |
| `string_table+0x04` | u32          | zero         | Always 0                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | `0` in every file    |
| `+0x04` | pstr[string_count] | strings      | Empty                |

## Normal Group Quests

The client Lua on client 3474 reads `normalgroupquest.bss` through four
functions, all behind one switch: `global_contentsoptions.luac` sets
`_ContentsGroup_NormalGroupQuest = ToClient_IsContentsGroupOpen("1684")`,
and contents group `1684` is closed on client 3474
([`contentsgroupoptionstaticstatusmanager.bss`](contentsgroupoptionstaticstatusmanager_bss.md)).
The two quest widgets, `panel_widget_checkedquest.luac` and
`panel_widget_questlist_abyssone.luac`, use them the same way:

| Lua function                                 | Use in the quest widget                                                                                       |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `ToClient_GetNormalGroupQuestCount(group, quest)` | Quest count of the quest's group; the first recent quest with a count other than `0` becomes the group quest |
| `ToClient_GetNormalGroupQuestIndex(group, quest)` | The quest's position in its group, from `0`; shown as `index + 1` of the count                           |
| `ToClient_GetNormalGroupName(group, quest)`  | The group name in the `LUA_GROUPQUEST_WORDS_TITLE` line (`group_quest_name`, `group_quest_now`, `group_quest_total`) |
| `ToClient_GetGroupQuestInfo(group, quest)`   | On `FromClient_ClearNormalGroupQuestInformation`, the next quest of the group; `(0, 0)` ends the line         |

While a group quest is set, the widget shows the next quest under
`ToClient_GetGroupQuestTitle(group, quest)` as acceptable and hides it again
on `FromClient_AcceptNormalGroupQuestInformation` for that quest.

On client 1784 the source sheet and the struct name agree with that:

- The `New_Group_Quest` sheet of a private server's
  `DataSheet_QuestRecommendationTable.xlsm` on client 1784 has the columns
  `QuestGroupKey`, `GroupName`, `QuestGroup`, `QuestID` and
  `ContentsGroupKey`, the note columns `#~Title` and `#^E_Merge Index`, and
  no rows. The same sheet in its `DataSheets.bexcel` holds the five compiled
  columns and 0 rows, and its compiled `binary/normalgroupquest.bss` is the
  20 bytes above. The loader's file list names the workbook, which also
  holds the sheets `NewQuest_Table`, `MainQuest_Table`,
  `RecommendationQuest_Table` and `RepetitionQuest_Table`.
- The server dump of that build has four load errors for
  `NormalGroupQuestStaticStatus`: quest `(%#, %#)` has no group name, has a
  wrong key, has a wrong `QuestNo(%#, %#)`, and has no data. A row so holds a
  group name and a quest number `(group, quest)`.
- The same dump's list of string sheet names puts `NormalGroupQuestName`
  between `YachtDiceHandRank` and `SeasonPassQuickQuest`, then
  `SiegeBuildKit` and `YachtGameBoardString`. On client 3474 LOC type 105
  holds the Yar! hand names (`Straight Shot`, `Double Trouble`), 108 the
  Conquest War object descriptions and 109 the Yar! mode descriptions, which
  puts `NormalGroupQuestName` at type 106. The English LOC on client 3474 has
  no type 106 entry.

## Notes

- Raw bytes of every file on client 3474, and of every file marked empty on
  clients 1784 and 1485:
  `50 41 42 52 00 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00`.
- The list comes from a scan of every `.bss` under `gamecommondata/binary/`
  on client 3474 for files of at most 40 bytes. The spawn grid files under
  `mapdata_*/spawnplacementfieldgrid/` are left out.
- Four files with these 20 bytes on client 3474 hold records on an older
  client: `cashproductcachedata.bss` (1,509,235 bytes on client 1784,
  1,097.1 KB on client 1485), `charactertrigger.bss` (307 bytes, count 9, on
  clients 1784 and 1485), `equipitemchanage.bss` (464 bytes, count 37, on
  client 1784) and `naktype.bss` (empty on client 1784, 455 bytes and count 4
  on client 1485). The handler reads the live empty layout and rejects the
  older files; their record layouts wait for multi-version support.
- Two 20-byte PABR files are not empty tables: `cashproduct_newbieproduct.bss`
  holds `0x18CAD` at `+0x04` and `petfeedcount.bss` holds `10` there, each
  with no row bytes before the string table, so the u32 is a single value.
  They have their own docs,
  [cashproduct_newbieproduct](cashproduct_newbieproduct_bss.md) and
  [petfeedcount](petfeedcount_bss.md).
- Neither Lightstone file is in the client 1784 archive. The 2016 PDB, a
  private server's `DataSheets.bexcel`, `.xlsm` sheets, compiled `binary/`
  folder and server dump on client 1784 hold no table, file, struct or
  loader with `LightStone` in its name. That `ContentsGroupOption` sheet has
  no key between `1795` and `2000`, so contents group `1801` (below) is newer
  than client 1784 too.
- The installed `BlackDesert64.exe` (client 3473) holds neither Lightstone
  file name as ASCII or UTF-16 text, so it does not show the loader or its
  struct.
- The client Lua on client 3473 (3,073 `.luac` files) names neither
  Lightstone file. `global_contentsoptions.luac` sets
  `_ContentsGroup_EnchantLightStone = ToClient_IsContentsGroupOpen("1801")`,
  and no other Lua file reads `_ContentsGroup_EnchantLightStone`. The
  Lightstone bag (`_ContentsGroup_LightStoneBag`, contents group `1815`) and
  the set lookups (`ToClient_getLightStoneSet`, read from
  [`lightstoneset.bss`](lightstoneset_bss.md)) are separate features.
- The 2016 PDB has no `NormalGroupQuest` type.
- calpheonlabs lists `normalgroupquest.bss` with a decoder but no field
  ledger, so it gives no layout to compare.
- One handler class (`EmptyTableHandler`, `_common/empty_table.py`) with the
  PABR reader in `_bss/empty_tables/parser.py` previews every file in
  `_bss/empty_tables/tables.py`. A file that declares a record or a string
  raises an error, so a client that fills one of these tables shows up as a
  parse error and in the tests.
- The zero-count `.dbss` tables have their own doc:
  [empty](../dbss/empty_dbss.md).

## Open Questions

### Record Layout

No client checked has a record in any of these files, so every row layout
is unknown. When a client ships `count > 0`, the file moves to its own doc
and handler, with rows starting at `+0x08` and ending at `table_start`. For
`normalgroupquest.bss` the five compiled `New_Group_Quest` columns are the
lead (`QuestGroupKey`, `GroupName`, `QuestGroup`, `QuestID`,
`ContentsGroupKey`); their types and order in the file are unknown. Whether
the group names come from LOC type 106 keyed by `QuestGroupKey`, as the
group names of the four quest lists of [`newquest.bss`](newquest_bss.md)
come from their own LOC types, is open too.

### Contents Group 1801

The Lua defines `_ContentsGroup_EnchantLightStone` for contents group `1801`
but never reads it. Whether that group gates whatever reads these two tables
is unknown.
