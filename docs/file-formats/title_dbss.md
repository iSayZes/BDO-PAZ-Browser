# `title.dbss` Format

## Purpose

Stores title metadata, the raw Korean title text, raw Korean requirement text,
category, and optional inline PAColor markup for special title names.

`title.dbss` is block-addressed by `titleoffset.dbss`; it is not a flat fixed
record table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes   | Records          | Row bytes                  |
| ------ | -------------- | ------- | ------------------ | ------- | ---------------- | -------------------------- |
| 1      | 1698 and later | 3483    | `title.dbss`       | 870,292 | 3,179 Record     | 200 to 870, 274 on average |
| 1      | 1698 and later | 3483    | `titleoffset.dbss` | 38,152  | 3,179 Offset Row | 12                         |

| Layout | File               | Known             | Unknown           |
| ------ | ------------------ | ----------------- | ----------------- |
| 1      | `title.dbss`       | 704,984 B (81.0%) | 165,308 B (19.0%) |
| 1      | `titleoffset.dbss` | 38,152 B (100.0%) | 0 B (0.0%)        |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 1             |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3473   | Layout 1             |
| 3464   | Layout 1             |
| 3458   | Layout 1             |
| 3454   | Layout 1             |
| 3444   | Layout 1             |
| 3435   | Layout 1             |
| 3426   | Layout 1             |
| 3418   | Layout 1             |
| 3412   | Layout 1             |
| 3402   | Layout 1             |
| 3396   | Layout 1             |
| 3387   | Layout 1             |
| 3381   | Layout 1             |
| 3373   | Layout 1             |
| 3364   | Layout 1             |
| 3356   | Layout 1             |
| 3349   | Layout 1             |
| 3342   | Layout 1             |
| 3335   | Layout 1             |
| 3326   | Layout 1             |
| 3321   | Layout 1             |
| 3314   | Layout 1             |
| 3303   | Layout 1             |
| 3302   | Layout 1             |
| 3293   | Layout 1             |
| 3283   | Layout 1             |
| 3275   | Layout 1             |
| 3267   | Layout 1             |
| 3258   | Layout 1             |
| 3251   | Layout 1             |
| 3242   | Layout 1             |
| 3235   | Layout 1             |
| 3229   | Layout 1             |
| 3212   | Layout 1             |
| 3203   | Layout 1             |
| 3193   | Layout 1             |
| 3186   | Layout 1             |
| 3177   | Layout 1             |
| 3169   | Layout 1             |
| 3158   | Layout 1             |
| 3151   | Layout 1             |
| 3144   | Layout 1             |
| 3133   | Layout 1             |
| 3125   | Layout 1             |
| 3118   | Layout 1             |
| 3111   | Layout 1             |
| 3103   | Layout 1             |
| 3095   | Layout 1             |
| 3086   | Layout 1             |
| 3072   | Layout 1             |
| 3062   | Layout 1             |
| 3052   | Layout 1             |
| 3045   | Layout 1             |
| 3037   | Layout 1             |
| 3030   | Layout 1             |
| 3021   | Layout 1             |
| 3012   | Layout 1             |
| 3002   | Layout 1             |
| 2995   | Layout 1             |
| 2987   | Layout 1             |
| 2978   | Layout 1             |
| 2970   | Layout 1             |
| 2959   | Layout 1             |
| 2951   | Layout 1             |
| 2942   | Layout 1             |
| 2935   | Layout 1             |
| 2932   | Layout 1             |
| 2923   | Layout 1             |
| 2919   | Layout 1             |
| 2907   | Layout 1             |
| 2900   | Layout 1             |
| 2891   | Layout 1             |
| 2882   | Layout 1             |
| 2872   | Layout 1             |
| 2863   | Layout 1             |
| 2855   | Layout 1             |
| 2849   | Layout 1             |
| 2844   | Layout 1             |
| 2834   | Layout 1             |
| 2825   | Layout 1             |
| 2819   | Layout 1             |
| 2811   | Layout 1             |
| 2803   | Layout 1             |
| 2794   | Layout 1             |
| 2783   | Layout 1             |
| 2774   | Layout 1             |
| 2765   | Layout 1             |
| 2756   | Layout 1             |
| 2750   | Layout 1             |
| 2743   | Layout 1             |
| 2736   | Layout 1             |
| 2726   | Layout 1             |
| 2717   | Layout 1             |
| 2709   | Layout 1             |
| 2703   | Layout 1             |
| 2695   | Layout 1             |
| 2684   | Layout 1             |
| 2672   | Layout 1             |
| 2665   | Layout 1             |
| 2657   | Layout 1             |
| 2649   | Layout 1             |
| 2644   | Layout 1             |
| 2637   | Layout 1             |
| 2629   | Layout 1             |
| 2619   | Layout 1             |
| 2612   | Layout 1             |
| 2606   | Layout 1             |
| 2602   | Layout 1             |
| 2601   | Layout 1             |
| 2592   | Layout 1             |
| 2583   | Layout 1             |
| 2575   | Layout 1             |
| 2567   | Layout 1             |
| 2560   | Layout 1             |
| 2553   | Layout 1             |
| 2545   | Layout 1             |
| 2538   | Layout 1             |
| 2529   | Layout 1             |
| 2519   | Layout 1             |
| 2513   | Layout 1             |
| 2510   | Layout 1             |
| 2507   | Layout 1             |
| 2503   | Layout 1             |
| 2498   | Layout 1             |
| 2492   | Layout 1             |
| 2487   | Layout 1             |
| 2480   | Layout 1             |
| 2474   | Layout 1             |
| 2468   | Layout 1             |
| 2460   | Layout 1             |
| 2453   | Layout 1             |
| 2444   | Layout 1             |
| 2438   | Layout 1             |
| 2434   | Layout 1             |
| 2429   | Layout 1             |
| 2421   | Layout 1             |
| 2414   | Layout 1             |
| 2407   | Layout 1             |
| 2401   | Layout 1             |
| 2397   | Layout 1             |
| 2393   | Layout 1             |
| 2384   | Layout 1             |
| 2378   | Layout 1             |
| 2372   | Layout 1             |
| 2358   | Layout 1             |
| 2352   | Layout 1             |
| 2347   | Layout 1             |
| 2343   | Layout 1             |
| 2335   | Layout 1             |
| 2327   | Layout 1             |
| 2324   | Layout 1             |
| 2319   | Layout 1             |
| 2313   | Layout 1             |
| 2308   | Layout 1             |
| 2302   | Layout 1             |
| 2295   | Layout 1             |
| 2290   | Layout 1             |
| 2284   | Layout 1             |
| 2276   | Layout 1             |
| 2269   | Layout 1             |
| 2259   | Layout 1             |
| 2250   | Layout 1             |
| 2243   | Layout 1             |
| 2235   | Layout 1             |
| 2229   | Layout 1             |
| 2224   | Layout 1             |
| 2218   | Layout 1             |
| 2215   | Layout 1             |
| 2207   | Layout 1             |
| 2203   | Layout 1             |
| 2196   | Layout 1             |
| 2192   | Layout 1             |
| 2189   | Layout 1             |
| 2183   | Layout 1             |
| 2179   | Layout 1             |
| 2171   | Layout 1             |
| 2163   | Layout 1             |
| 2156   | Layout 1             |
| 2151   | Layout 1             |
| 2147   | Layout 1             |
| 2142   | Layout 1             |
| 2138   | Layout 1             |
| 2134   | Layout 1             |
| 2130   | Layout 1             |
| 2122   | Layout 1             |
| 2107   | Layout 1             |
| 2098   | Layout 1             |
| 2089   | Layout 1             |
| 2081   | Layout 1             |
| 2073   | Layout 1             |
| 2067   | Layout 1             |
| 2063   | Layout 1             |
| 2059   | Layout 1             |
| 2052   | Layout 1             |
| 2044   | Layout 1             |
| 2039   | Layout 1             |
| 2032   | Layout 1             |
| 2025   | Layout 1             |
| 2011   | Layout 1             |
| 2005   | Layout 1             |
| 2000   | Layout 1             |
| 1996   | Layout 1             |
| 1991   | Layout 1             |
| 1985   | Layout 1             |
| 1980   | Layout 1             |
| 1969   | Layout 1             |
| 1964   | Layout 1             |
| 1958   | Layout 1             |
| 1950   | Layout 1             |
| 1945   | Layout 1             |
| 1937   | Layout 1             |
| 1933   | Layout 1             |
| 1927   | Layout 1             |
| 1921   | Layout 1             |
| 1914   | Layout 1             |
| 1908   | Layout 1             |
| 1897   | Layout 1             |
| 1892   | Layout 1             |
| 1886   | Layout 1             |
| 1881   | Layout 1             |
| 1871   | Layout 1             |
| 1866   | Layout 1             |
| 1862   | Layout 1             |
| 1854   | Layout 1             |
| 1846   | Layout 1             |
| 1838   | Layout 1             |
| 1832   | Layout 1             |
| 1826   | Layout 1             |
| 1822   | Layout 1             |
| 1818   | Layout 1             |
| 1804   | Layout 1             |
| 1794   | Layout 1             |
| 1790   | Layout 1             |
| 1784   | Layout 1             |
| 1774   | Layout 1             |
| 1771   | Layout 1             |
| 1762   | Layout 1             |
| 1759   | Layout 1             |
| 1754   | Layout 1             |
| 1749   | Layout 1             |
| 1743   | Layout 1             |
| 1737   | Layout 1             |
| 1731   | Layout 1             |
| 1725   | Layout 1             |
| 1717   | Layout 1             |
| 1710   | Layout 1             |
| 1704   | Layout 1             |
| 1698   | Layout 1             |
| 1690   | No documented layout |
| 1685   | No documented layout |
| 1680   | No documented layout |
| 1674   | No documented layout |
| 1668   | No documented layout |
| 1659   | No documented layout |
| 1649   | No documented layout |
| 1642   | No documented layout |
| 1636   | No documented layout |
| 1628   | No documented layout |
| 1622   | No documented layout |
| 1614   | No documented layout |
| 1608   | No documented layout |
| 1602   | No documented layout |
| 1598   | No documented layout |
| 1594   | No documented layout |
| 1590   | No documented layout |
| 1587   | No documented layout |
| 1584   | No documented layout |
| 1579   | No documented layout |
| 1572   | No documented layout |
| 1565   | No documented layout |
| 1559   | No documented layout |
| 1554   | No documented layout |
| 1547   | No documented layout |
| 1537   | No documented layout |
| 1529   | No documented layout |
| 1524   | No documented layout |
| 1519   | No documented layout |
| 1509   | No documented layout |
| 1506   | No documented layout |
| 1504   | No documented layout |
| 1500   | No documented layout |
| 1493   | No documented layout |
| 1489   | No documented layout |
| 1485   | No documented layout |
| 1481   | No documented layout |
| 1474   | No documented layout |
| 1466   | No documented layout |
| 1462   | No documented layout |
| 1459   | No documented layout |
| 1453   | No documented layout |
| 1450   | No documented layout |
| 1445   | No documented layout |
| 1439   | No documented layout |
| 1433   | No documented layout |
| 1430   | No documented layout |
| 1426   | No documented layout |
| 1421   | No documented layout |
| 1417   | No documented layout |
| 1416   | No documented layout |
| 1409   | No documented layout |
| 1405   | No documented layout |
| 1401   | No documented layout |
| 1396   | No documented layout |
| 1391   | No documented layout |
| 1390   | No documented layout |
| 1386   | No documented layout |
| 1381   | No documented layout |
| 1379   | No documented layout |
| 1372   | No documented layout |
| 1366   | No documented layout |
| 1364   | No documented layout |
| 1363   | No documented layout |
| 1360   | No documented layout |
| 1358   | No documented layout |
| 1355   | No documented layout |
| 1351   | No documented layout |
| 1348   | No documented layout |
| 1346   | No documented layout |
| 1341   | No documented layout |
| 1340   | No documented layout |
| 1338   | No documented layout |
| 1335   | No documented layout |
| 1333   | No documented layout |
| 1329   | No documented layout |
| 1327   | No documented layout |
| 1324   | No documented layout |
| 1321   | No documented layout |
| 1319   | No documented layout |
| 1318   | No documented layout |
| 1316   | No documented layout |
| 1313   | No documented layout |
| 1311   | No documented layout |
| 1309   | No documented layout |
| 1304   | No documented layout |
| 1292   | No documented layout |
| 1286   | No documented layout |
| 1280   | No documented layout |
| 1276   | No documented layout |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
| 1246   | No file              |
| 1239   | No file              |
| 1230   | No file              |
| 1226   | No file              |
| 1220   | No file              |
| 1217   | No file              |
| 1211   | No file              |
| 1210   | No file              |
| 1208   | No file              |
| 1203   | No file              |
| 1197   | No file              |
| 1194   | No file              |
| 1192   | No file              |
| 1187   | No file              |
| 1183   | No file              |
| 1177   | No file              |
| 1173   | No file              |
| 1167   | No file              |
| 1164   | No file              |
| 1156   | No file              |
| 1149   | No file              |
| 1144   | No file              |
| 1137   | No file              |
| 1132   | No file              |
| 1127   | No file              |
| 1122   | No file              |
| 1118   | No file              |
| 1114   | No file              |
| 1109   | No file              |
| 1102   | No file              |
| 1096   | No file              |
| 1088   | No file              |
| 1081   | No file              |
| 1076   | No file              |
| 1069   | No file              |
| 1064   | No file              |
| 1058   | No file              |
| 1051   | No file              |
| 1044   | No file              |
| 1036   | No file              |
| 1026   | No file              |
| 1016   | No file              |
| 1009   | No file              |
| 1005   | No file              |
| 1000   | No file              |
| 998    | No file              |
| 990    | No file              |
| 979    | No file              |
| 972    | No file              |
| 963    | No file              |
| 955    | No file              |
| 946    | No file              |
| 938    | No file              |
| 927    | No file              |
| 911    | No file              |
| 904    | No file              |
| 899    | No file              |
| 894    | No file              |
| 885    | No file              |
| 879    | No file              |
| 872    | No file              |
| 864    | No file              |
| 855    | No file              |
| 853    | No file              |
| 845    | No file              |
| 837    | No file              |
| 829    | No file              |
| 822    | No file              |
| 814    | No file              |
| 805    | No file              |
| 794    | No file              |
| 787    | No file              |
| 780    | No file              |
| 771    | No file              |
| 760    | No file              |
| 748    | No file              |
| 741    | No file              |
| 736    | No file              |
| 731    | No file              |
| 723    | No file              |
| 711    | No file              |
| 707    | No file              |
| 697    | No file              |
| 689    | No file              |
| 683    | No file              |
| 678    | No file              |
| 670    | No file              |
| 661    | No file              |
| 656    | No file              |
| 652    | No file              |
| 643    | No file              |
| 637    | No file              |
| 630    | No file              |
| 627    | No file              |
| 621    | No file              |
| 617    | No file              |
| 615    | No file              |
| 606    | No file              |
| 599    | No file              |
| 592    | No file              |
| 586    | No file              |
| 577    | No file              |
| 569    | No file              |
| 561    | No file              |
| 554    | No file              |
| 542    | No file              |
| 532    | No file              |
| 531    | No file              |
| 526    | No file              |
| 521    | No file              |
| 517    | No file              |
| 510    | No file              |
| 508    | No file              |
| 504    | No file              |
| 497    | No file              |
| 491    | No file              |
| 485    | No file              |
| 478    | No file              |
| 472    | No file              |
| 466    | No file              |
| 457    | No file              |
| 452    | No file              |
| 449    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

- `titleoffset.dbss` - required. Provides `title_id -> (offset, size)` block
  lookup.
- `languagedata_en.loc` - optional for English title/requirement display.

## Layout 1

### File Layout

A record count, then the records back to back; `titleoffset.dbss` addresses
each one.

| Offset  | Type          | Field   | Notes                                           |
| ------- | ------------- | ------- | ----------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; equals the `titleoffset.dbss` count |
| `+0x04` | Record[count] | records | See Record                                      |

### Record (variable: 100 bytes + text)

All inspected records fit one generalized header. The older A/B/C layouts are
just `key_count` values 1, 2, and 3. The tail after `requirement_text_kr`
reads the same on all 3,177 records of client 3473; the tail names count from
the end of `requirement_text_kr`.

| Offset                     | Type           | Field                     | Notes                                                             |
| -------------------------- | -------------- | ------------------------- | ----------------------------------------------------------------- |
| `+0x00`                    | u32            | key_count                 | Number of 32-bit key/hash/group fields before `title_id`          |
| `+0x04`                    | u32[key_count] | key_values                | `key_count` values                                                |
| `key_values+0x00`          | u32            | title_id                  | Matches offset entry and loc string ID                            |
| `key_values+0x04`          | str16          | title_text_kr             | Korean title; PAColor-tagged on the styled title records, see Styled Title Records |
| `title_text_kr+0x00`       | str16          | requirement_text_kr       | Korean requirement, usually with PAColor tags                     |
| `requirement_text_kr+0x00` | u32            | unknown_tail_00           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x04` | u32            | category_id               | See Category IDs; `0` on 1,321 records, `1` on 900, `2` on 197, `3` on 759 (client 3473) |
| `requirement_text_kr+0x08` | bytes[20]      | unknown_tail_08           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x1C` | u32            | unknown_tail_1c           | `0` on 3,102 records; else `3600` to `7776000`, all multiples of 3,600 (`2592000` on 37) (client 3473) |
| `requirement_text_kr+0x20` | u32            | unknown_tail_20           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x24` | u32            | unknown_tail_24           | `0` on 3,082 records; else `604800` to `15552000`, all multiples of 3,600 (`2592000` on 50) (client 3473) |
| `requirement_text_kr+0x28` | u32            | unknown_tail_28           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x2C` | str8           | effect_name               | Aura/effect name, e.g. `vCalsutain_Buff_Aura_02A`; empty on 3,105 records (client 3473) |
| `effect_name+0x00`         | str8           | color_argb                | ASCII hex, e.g. `FFFF7124`; 8 characters on 365 records, else empty (client 3473) |
| `color_argb+0x00`          | u32            | color_value               | Same value as little-endian integer; `0` when `color_argb` is empty |
| `color_argb+0x04`          | bytes[12]      | unknown_after_color_value | Always `0` (client 3473)                                          |

Observed `key_count` distribution:

| key_count | Count | Former Layout  |
| --------- | ----- | -------------- |
| 1         | 2,844 | A              |
| 2         | 175   | B              |
| 3         | 15    | C              |
| 4         | 1     | Previously `?` |
| 6         | 13    | Previously `?` |

Earlier versions of this doc read the count of `title_text_kr` as a u32
`style_or_title_len` and a u32 `zero`, and the count of
`requirement_text_kr` as a u16 `requirement_text_length` and three u16 `0`.
Both are the u64 count of a `str16`.

### `titleoffset.dbss`

| Offset  | Type              | Field | Notes       |
| ------- | ----------------- | ----- | ----------- |
| `+0x00` | u32               | count | Entry count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row |

Observed entries: 3,048 in the pre-2026-09-27 test fixture, 3,172 in the
2026-09-27 client. The largest `offset + size` equals the `title.dbss` byte
length, so the offset table accounts for the full file.

### Offset Row (12 bytes)

| Offset  | Type | Field    | Notes                                                |
| ------- | ---- | -------- | ---------------------------------------------------- |
| `+0x00` | u32  | title_id | Title ID                                             |
| `+0x04` | u32  | offset   | Offset into `title.dbss`, at the record's `key_count` |
| `+0x08` | u32  | size     | Block size                                           |

## Text Payload

Most records have a plain Korean title followed by the Korean requirement
string.

The count of `requirement_text_kr` is the UTF-16 code-unit length of the tagged
requirement string, not the visible text length after stripping PA tags.

Example, title ID `44`:

| Field                     | Value                    |
| ------------------------- | ------------------------ |
| English title             | `Stoneback Crab Artisan` |
| Korean title              | `돌멘게 공예가`          |
| Requirement length marker | `66`                     |
| Tagged requirement length | `66`                     |
| Plain requirement length  | `35`                     |
| Category                  | `1` / Combat             |

## Styled Title Records

Thirty records, title IDs `3645..3674`, begin their text payload with a PAColor
tag. These are class "MASTER ..." titles. For these records, as for every
other, the header field after `title_id` is the count of `title_text_kr`, here
the length of the styled title payload.

Example, title ID `3645`:

| Field                            | Value                   |
| -------------------------------- | ----------------------- |
| Header field                     | `231`                   |
| Styled title payload length      | `231` UTF-16 code units |
| Plain title after stripping tags | `MASTER WARRIOR`        |
| Requirement length marker        | `115`                   |
| Category                         | `0` / World             |

An earlier version of this doc read the styled title payload as 232 code units,
the header field plus one, with the requirement length marker as its final code
unit. That last unit is the low half of the `requirement_text_kr` count.

## Category IDs

`title.dbss` itself carries a category field after the requirement text.

| ID  | Name       |
| --- | ---------- |
| 0   | World      |
| 1   | Combat     |
| 2   | Life Skill |
| 3   | Fishing    |

## Extra Payload And Title Color

Most default-color titles have no non-zero payload after the category field.
Most non-default-color titles have a 64-byte or 88-byte extra payload. The title
color is encoded near the end of that payload as both an ASCII `AARRGGBB`
string and the same value as a little-endian u32.

The extra payload is the Record tail from `unknown_tail_08` to
`unknown_after_color_value` with its trailing zeros cut: 64 bytes when
`effect_name` is empty and `color_argb` holds 8 characters, 88 bytes when
`effect_name` holds 24. `color_argb` is the `color_len` and `color_argb` of
earlier versions of this doc, and `effect_name` their `effect_len` and
`effect_name`.

Example:

```text
46 46 46 46 37 31 32 34 24 71 ff ff
F  F  F  F  7  1  2  4  packed 0xFFFF7124
```

This decodes to `0xFFFF7124`, displayed in CSS as `#FF7124`.

88-byte payloads add an aura/effect string before the color. The name is
probably misspelled data (`Calsutain` instead of `Calustian` or similar), so
parsers should preserve it exactly.

In the current extracted sample, 335 records decode a title color from this
payload. For example, title ID `3451` (`Fisher`) has the same `0xFFAFEEEE`
payload color as `Angel`. This was visually confirmed in-game.

Other visual confirmations:

| Titles                                                           | Payload Color | Result                                |
| ---------------------------------------------------------------- | ------------- | ------------------------------------- |
| `The Greatest Guardian`, `#BDORemastered`, `One of the Greatest` | `0xFFFF7124`  | Same color                            |
| `REBOOT`                                                         | `0xFFFF7124`  | Same color family as the titles above |
| `Nouverikant`                                                    | `0xFFFFB400`  | Not the same as `REBOOT`              |

These confirmations support using the DBSS payload color as the precise source
for individual non-default title display.

## PAColor Tags

Requirement text commonly starts with:

```text
<PAColor0xFFf32200>칭호 조건<PAOldColor>:
```

This default requirement label color is not the visible title-name color.
The English requirement (LOC type 1, `str_id4` 1) carries the same tag on its
`Title Requirement` label in all 3,322 rows on client 3458. The parser keeps the
tags in `requirement_text_kr`, and the table draws them.

Special "MASTER ..." title names are different: their title payload itself is
PAColor-tagged, so those PAColor tags are part of the displayed title name. The
tags draw a gradient, one colour per letter pair: `MASTER WARRIOR` goes from
`0xffffffff` on `MA` down to `0xff424242` on `R`, as in game. The parser keeps
the tags in `title_text_kr`, and the English LOC name (type 1) carries the same
tags. Two more LOC names are tagged without a styled payload (`Seasonal
Sensation!`, `Rise Above the Disorder`); 1348 `Lights, Camera, Action!` has a
stored payload colour and a different LOC tag colour; the table draws the tag
colour (unchecked in game).

## Style Field

Earlier versions of this doc read the header field after `title_id`
(`style_or_title_len`) as a style/category-like value for normal records, with
common values `2..17`, rare values through `28` and `43`, and a few high values
used only by styled title records. It is the count of `title_text_kr`: the
title's length in UTF-16 code units.

It does not identify the final visible title color. Counterexample: three
titles of 7 code units each.

| Title ID | Title                      | Header Field | Visual Result |
| -------- | -------------------------- | ------------ | ------------- |
| `2117`   | The Greatest Guardian      | `7`          | Special color |
| `44`     | Stoneback Crab Artisan     | `7`          | Normal blue   |
| `45`     | Stoneback Crab Philosopher | `7`          | Normal blue   |

## Optional Extra Payload

Some color payloads also include small non-zero integers at `unknown_tail_1c`
and `unknown_tail_24` (`+0x14` and `+0x1C` of the extra payload). These look
like grouping/effect parameters, not the title color itself.

## Recommended Parser Behavior

1. Use `titleoffset.dbss` to slice blocks.
2. Read `key_count`, then `key_values` and `title_id`.
3. Read `title_text_kr` and `requirement_text_kr` through their u64 counts.
4. Read `category_id`, then `effect_name`, `color_argb` and `color_value` at
   their Record offsets.
5. A `title_text_kr` that starts with a PAColor tag is a styled title.
6. Strip PA tags only for readable display; keep raw PA tags for debugging.
7. Look up English name/requirement from `languagedata_en.loc`:
   - Name: `str_type=1, str_id1=title_id, str_id4=0`
   - Requirement: `str_type=1, str_id1=title_id, str_id4=1`

## Notes

- The previously unknown `?` layouts are now explained by `key_count` values 4
  and 6.
- The old `u32_14`, `u32_18`, and similar columns can be UTF-16 text fragments,
  not structured integers.
- `titlecategory.bss` is not needed for category display; `title.dbss` carries
  the category after the requirement string.

## Open Questions

### Extra Payload Parameters

The color value and optional aura/effect name are now decoded, but
`unknown_tail_1c` and `unknown_tail_24` in the extra payload are still
unresolved.

### Normal Title Name Color

For titles without an extra color payload, the default visible color is still
not stored as a per-record RGB value in `title.dbss`. Disproven candidates:

- Requirement `_PA_COLOR_MARKER`
- `style_or_title_len` alone (the count of `title_text_kr`)
- A fixed early `u32` field after the title text

Likely sources still to investigate:

- client-side title color table
- UI scripts / title rendering logic
- another DBSS file related to title grade/type/color
- implicit default color chosen by title category/UI code
