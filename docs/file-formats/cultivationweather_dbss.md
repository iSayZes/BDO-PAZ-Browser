# `cultivationweather.dbss` Format

## Purpose

How weather changes the growth speed of a farming crop. Each record is one
crop, keyed by its exchange key (the `itemexchangesource.bss` key that
`characterobject.dbss` stores as the crop's `product_recipe_key`), and holds
the five weather kinds of the 2016 `gc::WeatherKind` (water, temperature,
humidity, pruning, birds). Per kind a list of ranges gives the growth speed
change while the weather value lies in that range. The farm info window
reads it through `getCultivationWeatherStaticStatusWrapper()` and shows the
change next to the temperature, humidity and groundwater bars. Companion
`cultivationweatheroffset.dbss` lists where every record's payload sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes  | Records                                             | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ------ | --------------------------------------------------- | --------- |
| 2      | 2726 and later | 3483    | `cultivationweather.dbss`       | 77,916 | 5,247 Range, 2,020 Weather, 404 Payload, 404 Record | 12        |
| 2      | 2726 and later | 3483    | `cultivationweatheroffset.dbss` | 4,852  | 404 Offset Row                                      | 12        |
| 1      | 1346 to 2717   | 2717    | `cultivationweather.dbss`       | 64,771 | 4,454 Range, 1,715 Weather, 343 Payload, 343 Record | 12        |
| 1      | 1346 to 2717   | 2717    | `cultivationweatheroffset.dbss` | 3,434  | 343 Offset Row                                      | 10        |

| Layout | File                            | Known             | Unknown    |
| ------ | ------------------------------- | ----------------- | ---------- |
| 2      | `cultivationweather.dbss`       | 77,916 B (100.0%) | 0 B (0.0%) |
| 2      | `cultivationweatheroffset.dbss` | 4,852 B (100.0%)  | 0 B (0.0%) |
| 1      | `cultivationweather.dbss`       | 64,771 B (100.0%) | 0 B (0.0%) |
| 1      | `cultivationweatheroffset.dbss` | 3,434 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 2             |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3464   | Layout 2             |
| 3458   | Layout 2             |
| 3454   | Layout 2             |
| 3444   | Layout 2             |
| 3435   | Layout 2             |
| 3426   | Layout 2             |
| 3418   | Layout 2             |
| 3412   | Layout 2             |
| 3402   | Layout 2             |
| 3396   | Layout 2             |
| 3387   | Layout 2             |
| 3381   | Layout 2             |
| 3373   | Layout 2             |
| 3364   | Layout 2             |
| 3356   | Layout 2             |
| 3349   | Layout 2             |
| 3342   | Layout 2             |
| 3335   | Layout 2             |
| 3326   | Layout 2             |
| 3321   | Layout 2             |
| 3314   | Layout 2             |
| 3303   | Layout 2             |
| 3302   | Layout 2             |
| 3293   | Layout 2             |
| 3283   | Layout 2             |
| 3275   | Layout 2             |
| 3267   | Layout 2             |
| 3258   | Layout 2             |
| 3251   | Layout 2             |
| 3242   | Layout 2             |
| 3235   | Layout 2             |
| 3229   | Layout 2             |
| 3212   | Layout 2             |
| 3203   | Layout 2             |
| 3193   | Layout 2             |
| 3186   | Layout 2             |
| 3177   | Layout 2             |
| 3169   | Layout 2             |
| 3158   | Layout 2             |
| 3151   | Layout 2             |
| 3144   | Layout 2             |
| 3133   | Layout 2             |
| 3125   | Layout 2             |
| 3118   | Layout 2             |
| 3111   | Layout 2             |
| 3103   | Layout 2             |
| 3095   | Layout 2             |
| 3086   | Layout 2             |
| 3072   | Layout 2             |
| 3062   | Layout 2             |
| 3052   | Layout 2             |
| 3045   | Layout 2             |
| 3037   | Layout 2             |
| 3030   | Layout 2             |
| 3021   | Layout 2             |
| 3012   | Layout 2             |
| 3002   | Layout 2             |
| 2995   | Layout 2             |
| 2987   | Layout 2             |
| 2978   | Layout 2             |
| 2970   | Layout 2             |
| 2959   | Layout 2             |
| 2951   | Layout 2             |
| 2942   | Layout 2             |
| 2935   | Layout 2             |
| 2932   | Layout 2             |
| 2923   | Layout 2             |
| 2919   | Layout 2             |
| 2907   | Layout 2             |
| 2900   | Layout 2             |
| 2891   | Layout 2             |
| 2882   | Layout 2             |
| 2872   | Layout 2             |
| 2863   | Layout 2             |
| 2855   | Layout 2             |
| 2849   | Layout 2             |
| 2844   | Layout 2             |
| 2834   | Layout 2             |
| 2825   | Layout 2             |
| 2819   | Layout 2             |
| 2811   | Layout 2             |
| 2803   | Layout 2             |
| 2794   | Layout 2             |
| 2783   | Layout 2             |
| 2774   | Layout 2             |
| 2765   | Layout 2             |
| 2756   | Layout 2             |
| 2750   | Layout 2             |
| 2743   | Layout 2             |
| 2736   | Layout 2             |
| 2726   | Layout 2             |
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
| 1690   | Layout 1             |
| 1685   | Layout 1             |
| 1680   | Layout 1             |
| 1674   | Layout 1             |
| 1668   | Layout 1             |
| 1659   | Layout 1             |
| 1649   | Layout 1             |
| 1642   | Layout 1             |
| 1636   | Layout 1             |
| 1628   | Layout 1             |
| 1622   | Layout 1             |
| 1614   | Layout 1             |
| 1608   | Layout 1             |
| 1602   | Layout 1             |
| 1598   | Layout 1             |
| 1594   | Layout 1             |
| 1590   | Layout 1             |
| 1587   | Layout 1             |
| 1584   | Layout 1             |
| 1579   | Layout 1             |
| 1572   | Layout 1             |
| 1565   | Layout 1             |
| 1559   | Layout 1             |
| 1554   | Layout 1             |
| 1547   | Layout 1             |
| 1537   | Layout 1             |
| 1529   | Layout 1             |
| 1524   | Layout 1             |
| 1519   | Layout 1             |
| 1509   | Layout 1             |
| 1506   | Layout 1             |
| 1504   | Layout 1             |
| 1500   | Layout 1             |
| 1493   | Layout 1             |
| 1489   | Layout 1             |
| 1485   | Layout 1             |
| 1481   | Layout 1             |
| 1474   | Layout 1             |
| 1466   | Layout 1             |
| 1462   | Layout 1             |
| 1459   | Layout 1             |
| 1453   | Layout 1             |
| 1450   | Layout 1             |
| 1445   | Layout 1             |
| 1439   | Layout 1             |
| 1433   | Layout 1             |
| 1430   | Layout 1             |
| 1426   | Layout 1             |
| 1421   | Layout 1             |
| 1417   | Layout 1             |
| 1416   | Layout 1             |
| 1409   | Layout 1             |
| 1405   | Layout 1             |
| 1401   | Layout 1             |
| 1396   | Layout 1             |
| 1391   | Layout 1             |
| 1390   | Layout 1             |
| 1386   | Layout 1             |
| 1381   | Layout 1             |
| 1379   | Layout 1             |
| 1372   | Layout 1             |
| 1366   | Layout 1             |
| 1364   | Layout 1             |
| 1363   | Layout 1             |
| 1360   | Layout 1             |
| 1358   | Layout 1             |
| 1355   | Layout 1             |
| 1351   | Layout 1             |
| 1348   | Layout 1             |
| 1346   | Layout 1             |
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
| 1256   | No file              |
| 1250   | No file              |
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

| File                            | Required | Role                                                                                     |
| ------------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `cultivationweatheroffset.dbss` | Optional | `exchange_key -> (data_offset, data_size)` of every payload; the parser walks the main file without it |

The handler links each exchange key to its `itemexchangesource.bss` row
through the `EXCHANGE_NAME_KR` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A record count, then the records back
to back; the file ends after the last record.

| Offset  | Type          | Field | Notes             |
| ------- | ------------- | ----- | ----------------- |
| `+0x00` | u32           | count | Number of records |
| `+0x04` | Record[count] | records | See Record      |

### Record (variable: 4 bytes + payload)

| Offset  | Type    | Field      | Notes                                             |
| ------- | ------- | ---------- | ------------------------------------------------- |
| `+0x00` | u32     | key_prefix | Equals `exchange_key`                             |
| `+0x04` | Payload | payload    | The offset row points at this field               |

### Payload (variable: 8 bytes + weathers)

| Offset  | Type                    | Field         | Notes                                                                 |
| ------- | ----------------------- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u32                     | exchange_key  | Crop exchange key; `57001` to `58000` on client 3474                  |
| `+0x04` | u32                     | weather_count | `5` on every record of clients 1784 and 3474                          |
| `+0x08` | Weather[weather_count]  | weathers      | See Weather                                                           |

### Weather (variable: 5 bytes + ranges)

| Offset  | Type               | Field        | Notes                                                       |
| ------- | ------------------ | ------------ | ----------------------------------------------------------- |
| `+0x00` | u8                 | weather_kind | See Weather Kinds; `1` to `5` in that order on every record |
| `+0x01` | u32                | range_count  | `1` to `3`                                                  |
| `+0x05` | Range[range_count] | ranges       | See Range                                                   |

### Range (12 bytes)

| Offset  | Type | Field              | Notes                                                                        |
| ------- | ---- | ------------------ | ---------------------------------------------------------------------------- |
| `+0x00` | f32  | weather_start_rate | Lower bound of the weather value, in percent; `-100.0` on temperature        |
| `+0x04` | f32  | weather_end_rate   | Upper bound                                                                  |
| `+0x08` | i32  | product_speed_rate | Growth speed change on the 1,000,000 = 100% scale; `-16668` to `1000000` on client 3474 |

The ranges of a kind follow in ascending order. On water, temperature and
humidity each range starts where the one before ends; the pruning ranges
leave gaps (`0` to `4`, `5` to `7`, `8` to `10`).

### `cultivationweatheroffset.dbss`

Bare offset table into `cultivationweather.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `cultivationweather.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field        | Notes                                                                       |
| ------- | ---- | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32  | exchange_key | Key of the record it points at                                              |
| `+0x04` | u32  | data_offset  | Absolute offset in `cultivationweather.dbss` of the payload, past the key prefix |
| `+0x08` | u32  | data_size    | Payload size in bytes, without the key prefix; `177` to `189` on client 3474 |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
offset rows are not in file order; on clients 1784 and 3474 every one points
at the payload of the record with its key.

## Layout 1

The keys are u16; the rest is as in Layout 2.

### Record (variable: 2 bytes + payload)

| Offset  | Type    | Field      | Notes |
| ------- | ------- | ---------- | ----- |
| `+0x00` | u16     | key_prefix |       |
| `+0x02` | Payload | payload    |       |

### Payload (variable: 6 bytes + weathers)

| Offset  | Type                   | Field         | Notes                              |
| ------- | ---------------------- | ------------- | ---------------------------------- |
| `+0x00` | u16                    | exchange_key  | `57001` to `58000` on client 1784  |
| `+0x02` | u32                    | weather_count |                                    |
| `+0x06` | Weather[weather_count] | weathers      |                                    |

### `cultivationweatheroffset.dbss`

| Offset  | Type              | Field | Notes |
| ------- | ----------------- | ----- | ----- |
| `+0x00` | u32               | count |       |
| `+0x04` | Offset Row[count] | rows  |       |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                       |
| ------- | ---- | ------------ | ----------------------------------------------------------- |
| `+0x00` | u16  | exchange_key |                                                             |
| `+0x02` | u32  | data_offset  |                                                             |
| `+0x06` | u32  | data_size    | `175` to `187` on client 1784                               |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`.

## Weather Kinds

`weather_kind` is the 2016 `gc::WeatherKind` (an unsigned char). The farm
info window (`panel_housing_farminfo_all_1.luac`) asks for kinds `Water`,
`Temperature` and `Humidity` by these names through `CppEnums.WeatherKind`.

| Value | `gc::WeatherKind`         | Bounds (client 3474) | Ranges per record (client 3474) |
| ----- | ------------------------- | -------------------- | ------------------------------- |
| 1     | `WeatherKind_Water`       | `0` to `100`         | 3                               |
| 2     | `WeatherKind_Temperature` | `-100` to `100`      | 3                               |
| 3     | `WeatherKind_Humidity`    | `0` to `100`         | 2                               |
| 4     | `WeatherKind_NeedLop`     | `0` to `10`          | 3                               |
| 5     | `WeatherKind_BirdsAttack` | `0` to `100`         | 2, or 1 on 5 records            |

## Field Names

The `CultivationWeather_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `ExchangeKey`,
`WeatherKind`, `WeatherStartRate`, `WeatherEndRate` and `ProductSpeedRate`,
one sheet row per range. Grouped by key and kind, its 3,870 rows match the
298 records of client 1784 on every range and value, 298 of 298. The sheet
lives in `datasheet_collectdatatable.xlsm`, whose `#Nodename` note column
names key `57001` `재배용 후추` (pepper for farming); `characterobject.dbss`
documents character `1201` Pepper Crop with `product_recipe_key` `57001`.

The 2016 client has no table of this name. Its debug symbols have
`gc::PlantZoneStaticStatus::WeatherRate` as `_maxRate` (f32) and
`_productRate` (f32), and an `unordered_map` from `gc::WeatherKind` to a
`pa_map<float, WeatherRate>`: the same range-to-rate shape.

## Notes

- The farm info window prints `getRateByWeather(kind, value) * 1.0E-4` as a
  percent, so `product_speed_rate` `10000` shows as `1.00%`. For water it
  shows the value with its sign flipped.
- It marks the best temperature with `getTopValue(Temperature)` and the best
  humidity with `getBottomValue(Humidity)`.
- Client 3474 holds 404 records, client 1784 298. 290 keys are in both,
  every one with changed values; `57238` to `57242`, `57442`, `57622` and
  `57722` are only in client 1784.
