# `sha_weburl.bss` Format

## Purpose

The web addresses of Shadow Arena: seven string-table indexes in one
PABR row, each pointing at a URL template with `{branch}`, `{region}`,
`{lang}` and `{pos}` placeholders, such as
`https://{branch}payment.pearlabyss.com`. The row has no count and no key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | -------------- | --------- |
| 4      | 1485 and later | 3482    | `sha_weburl.bss` | 438   | 1 String Table | 398       |
| 3      | 1481           | 1481    | `sha_weburl.bss` | 391   | 1 String Table | 355       |
| 2      | 1358 to 1474   | 1474    | `sha_weburl.bss` | 329   | 1 String Table | 297       |
| 1      | 1355           | 1355    | `sha_weburl.bss` | 92    | 1 String Table | 76        |

| Layout | File             | Known         | Unknown     |
| ------ | ---------------- | ------------- | ----------- |
| 4      | `sha_weburl.bss` | 426 B (97.3%) | 12 B (2.7%) |
| 3      | `sha_weburl.bss` | 379 B (96.9%) | 12 B (3.1%) |
| 2      | `sha_weburl.bss` | 317 B (96.4%) | 12 B (3.6%) |
| 1      | `sha_weburl.bss` | 92 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 4 |
| 3474   | Layout 4 |
| 3464   | Layout 4 |
| 3458   | Layout 4 |
| 3454   | Layout 4 |
| 3444   | Layout 4 |
| 3435   | Layout 4 |
| 3426   | Layout 4 |
| 3418   | Layout 4 |
| 3412   | Layout 4 |
| 3402   | Layout 4 |
| 3396   | Layout 4 |
| 3387   | Layout 4 |
| 3381   | Layout 4 |
| 3373   | Layout 4 |
| 3364   | Layout 4 |
| 3356   | Layout 4 |
| 3349   | Layout 4 |
| 3342   | Layout 4 |
| 3335   | Layout 4 |
| 3326   | Layout 4 |
| 3321   | Layout 4 |
| 3314   | Layout 4 |
| 3303   | Layout 4 |
| 3302   | Layout 4 |
| 3293   | Layout 4 |
| 3283   | Layout 4 |
| 3275   | Layout 4 |
| 3267   | Layout 4 |
| 3258   | Layout 4 |
| 3251   | Layout 4 |
| 3242   | Layout 4 |
| 3235   | Layout 4 |
| 3229   | Layout 4 |
| 3212   | Layout 4 |
| 3203   | Layout 4 |
| 3193   | Layout 4 |
| 3186   | Layout 4 |
| 3177   | Layout 4 |
| 3169   | Layout 4 |
| 3158   | Layout 4 |
| 3151   | Layout 4 |
| 3144   | Layout 4 |
| 3133   | Layout 4 |
| 3125   | Layout 4 |
| 3118   | Layout 4 |
| 3111   | Layout 4 |
| 3103   | Layout 4 |
| 3095   | Layout 4 |
| 3086   | Layout 4 |
| 3072   | Layout 4 |
| 3062   | Layout 4 |
| 3052   | Layout 4 |
| 3045   | Layout 4 |
| 3037   | Layout 4 |
| 3030   | Layout 4 |
| 3021   | Layout 4 |
| 3012   | Layout 4 |
| 3002   | Layout 4 |
| 2995   | Layout 4 |
| 2987   | Layout 4 |
| 2978   | Layout 4 |
| 2970   | Layout 4 |
| 2959   | Layout 4 |
| 2951   | Layout 4 |
| 2942   | Layout 4 |
| 2935   | Layout 4 |
| 2932   | Layout 4 |
| 2923   | Layout 4 |
| 2919   | Layout 4 |
| 2907   | Layout 4 |
| 2900   | Layout 4 |
| 2891   | Layout 4 |
| 2882   | Layout 4 |
| 2872   | Layout 4 |
| 2863   | Layout 4 |
| 2855   | Layout 4 |
| 2849   | Layout 4 |
| 2844   | Layout 4 |
| 2834   | Layout 4 |
| 2825   | Layout 4 |
| 2819   | Layout 4 |
| 2811   | Layout 4 |
| 2803   | Layout 4 |
| 2794   | Layout 4 |
| 2783   | Layout 4 |
| 2774   | Layout 4 |
| 2765   | Layout 4 |
| 2756   | Layout 4 |
| 2750   | Layout 4 |
| 2743   | Layout 4 |
| 2736   | Layout 4 |
| 2726   | Layout 4 |
| 2717   | Layout 4 |
| 2709   | Layout 4 |
| 2703   | Layout 4 |
| 2695   | Layout 4 |
| 2684   | Layout 4 |
| 2672   | Layout 4 |
| 2665   | Layout 4 |
| 2657   | Layout 4 |
| 2649   | Layout 4 |
| 2644   | Layout 4 |
| 2637   | Layout 4 |
| 2629   | Layout 4 |
| 2619   | Layout 4 |
| 2612   | Layout 4 |
| 2606   | Layout 4 |
| 2602   | Layout 4 |
| 2601   | Layout 4 |
| 2592   | Layout 4 |
| 2583   | Layout 4 |
| 2575   | Layout 4 |
| 2567   | Layout 4 |
| 2560   | Layout 4 |
| 2553   | Layout 4 |
| 2545   | Layout 4 |
| 2538   | Layout 4 |
| 2529   | Layout 4 |
| 2519   | Layout 4 |
| 2513   | Layout 4 |
| 2510   | Layout 4 |
| 2507   | Layout 4 |
| 2503   | Layout 4 |
| 2498   | Layout 4 |
| 2492   | Layout 4 |
| 2487   | Layout 4 |
| 2480   | Layout 4 |
| 2474   | Layout 4 |
| 2468   | Layout 4 |
| 2460   | Layout 4 |
| 2453   | Layout 4 |
| 2444   | Layout 4 |
| 2438   | Layout 4 |
| 2434   | Layout 4 |
| 2429   | Layout 4 |
| 2421   | Layout 4 |
| 2414   | Layout 4 |
| 2407   | Layout 4 |
| 2401   | Layout 4 |
| 2397   | Layout 4 |
| 2393   | Layout 4 |
| 2384   | Layout 4 |
| 2378   | Layout 4 |
| 2372   | Layout 4 |
| 2358   | Layout 4 |
| 2352   | Layout 4 |
| 2347   | Layout 4 |
| 2343   | Layout 4 |
| 2335   | Layout 4 |
| 2327   | Layout 4 |
| 2324   | Layout 4 |
| 2319   | Layout 4 |
| 2313   | Layout 4 |
| 2308   | Layout 4 |
| 2302   | Layout 4 |
| 2295   | Layout 4 |
| 2290   | Layout 4 |
| 2284   | Layout 4 |
| 2276   | Layout 4 |
| 2269   | Layout 4 |
| 2259   | Layout 4 |
| 2250   | Layout 4 |
| 2243   | Layout 4 |
| 2235   | Layout 4 |
| 2229   | Layout 4 |
| 2224   | Layout 4 |
| 2218   | Layout 4 |
| 2215   | Layout 4 |
| 2207   | Layout 4 |
| 2203   | Layout 4 |
| 2196   | Layout 4 |
| 2192   | Layout 4 |
| 2189   | Layout 4 |
| 2183   | Layout 4 |
| 2179   | Layout 4 |
| 2171   | Layout 4 |
| 2163   | Layout 4 |
| 2156   | Layout 4 |
| 2151   | Layout 4 |
| 2147   | Layout 4 |
| 2142   | Layout 4 |
| 2138   | Layout 4 |
| 2134   | Layout 4 |
| 2130   | Layout 4 |
| 2122   | Layout 4 |
| 2107   | Layout 4 |
| 2098   | Layout 4 |
| 2089   | Layout 4 |
| 2081   | Layout 4 |
| 2073   | Layout 4 |
| 2067   | Layout 4 |
| 2063   | Layout 4 |
| 2059   | Layout 4 |
| 2052   | Layout 4 |
| 2044   | Layout 4 |
| 2039   | Layout 4 |
| 2032   | Layout 4 |
| 2025   | Layout 4 |
| 2011   | Layout 4 |
| 2005   | Layout 4 |
| 2000   | Layout 4 |
| 1996   | Layout 4 |
| 1991   | Layout 4 |
| 1985   | Layout 4 |
| 1980   | Layout 4 |
| 1969   | Layout 4 |
| 1964   | Layout 4 |
| 1958   | Layout 4 |
| 1950   | Layout 4 |
| 1945   | Layout 4 |
| 1937   | Layout 4 |
| 1933   | Layout 4 |
| 1927   | Layout 4 |
| 1921   | Layout 4 |
| 1914   | Layout 4 |
| 1908   | Layout 4 |
| 1897   | Layout 4 |
| 1892   | Layout 4 |
| 1886   | Layout 4 |
| 1881   | Layout 4 |
| 1871   | Layout 4 |
| 1866   | Layout 4 |
| 1862   | Layout 4 |
| 1854   | Layout 4 |
| 1846   | Layout 4 |
| 1838   | Layout 4 |
| 1832   | Layout 4 |
| 1826   | Layout 4 |
| 1822   | Layout 4 |
| 1818   | Layout 4 |
| 1804   | Layout 4 |
| 1794   | Layout 4 |
| 1790   | Layout 4 |
| 1784   | Layout 4 |
| 1774   | Layout 4 |
| 1771   | Layout 4 |
| 1762   | Layout 4 |
| 1759   | Layout 4 |
| 1754   | Layout 4 |
| 1749   | Layout 4 |
| 1743   | Layout 4 |
| 1737   | Layout 4 |
| 1731   | Layout 4 |
| 1725   | Layout 4 |
| 1717   | Layout 4 |
| 1710   | Layout 4 |
| 1704   | Layout 4 |
| 1698   | Layout 4 |
| 1690   | Layout 4 |
| 1685   | Layout 4 |
| 1680   | Layout 4 |
| 1674   | Layout 4 |
| 1668   | Layout 4 |
| 1659   | Layout 4 |
| 1649   | Layout 4 |
| 1642   | Layout 4 |
| 1636   | Layout 4 |
| 1628   | Layout 4 |
| 1622   | Layout 4 |
| 1614   | Layout 4 |
| 1608   | Layout 4 |
| 1602   | Layout 4 |
| 1598   | Layout 4 |
| 1594   | Layout 4 |
| 1590   | Layout 4 |
| 1587   | Layout 4 |
| 1584   | Layout 4 |
| 1579   | Layout 4 |
| 1572   | Layout 4 |
| 1565   | Layout 4 |
| 1559   | Layout 4 |
| 1554   | Layout 4 |
| 1547   | Layout 4 |
| 1537   | Layout 4 |
| 1529   | Layout 4 |
| 1524   | Layout 4 |
| 1519   | Layout 4 |
| 1509   | Layout 4 |
| 1506   | Layout 4 |
| 1504   | Layout 4 |
| 1500   | Layout 4 |
| 1493   | Layout 4 |
| 1489   | Layout 4 |
| 1485   | Layout 4 |
| 1481   | Layout 3 |
| 1474   | Layout 2 |
| 1466   | Layout 2 |
| 1462   | Layout 2 |
| 1459   | Layout 2 |
| 1453   | Layout 2 |
| 1450   | Layout 2 |
| 1445   | Layout 2 |
| 1439   | Layout 2 |
| 1433   | Layout 2 |
| 1430   | Layout 2 |
| 1426   | Layout 2 |
| 1421   | Layout 2 |
| 1417   | Layout 2 |
| 1416   | Layout 2 |
| 1409   | Layout 2 |
| 1405   | Layout 2 |
| 1401   | Layout 2 |
| 1396   | Layout 2 |
| 1391   | Layout 2 |
| 1390   | Layout 2 |
| 1386   | Layout 2 |
| 1381   | Layout 2 |
| 1379   | Layout 2 |
| 1372   | Layout 2 |
| 1366   | Layout 2 |
| 1364   | Layout 2 |
| 1363   | Layout 2 |
| 1360   | Layout 2 |
| 1358   | Layout 2 |
| 1355   | Layout 1 |
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

None.

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset              | Type         | Field             | Notes                                                                 |
| ------------------- | ------------ | ----------------- | --------------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                                                          |
| `+0x04`             | u32          | record_client_ref | String table index of the record client API URL                       |
| `+0x08`             | u32          | unknown_08        | String table index; the event banner URL on every client checked      |
| `+0x0C`             | u32          | unknown_0c        | String table index; the in-game banner URL on every client checked    |
| `+0x10`             | u32          | cash_shop_ref     | String table index of the cash shop (in-game banner) URL              |
| `+0x14`             | u32          | unknown_14        | String table index; the in-game banner URL on every client checked    |
| `+0x18`             | u32          | replay_ref        | String table index of the replay API URL                              |
| `+0x1C`             | u32          | payment_ref       | String table index of the payment URL                                 |
| `+0x20`             | String Table | string_table      | See String Table                                                      |
| `string_table+0x00` | u32          | table_start       | Offset of the string table; `0x20` on every client checked            |
| `string_table+0x04` | u32          | zero              | Always `0`                                                            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `5` on every client checked           |
| `+0x04` | pstr[string_count] | strings      | UTF-8 URL templates in first-use order; see URLs         |

## Layout 3

### File Layout

| Offset              | Type         | Field             | Notes                                           |
| ------------------- | ------------ | ----------------- | ----------------------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                                    |
| `+0x04`             | u32          | record_client_ref | As in Layout 4                                  |
| `+0x08`             | u32          | unknown_08        | As in Layout 4                                  |
| `+0x0C`             | u32          | unknown_0c        | As in Layout 4                                  |
| `+0x10`             | u32          | cash_shop_ref     | As in Layout 4                                  |
| `+0x14`             | u32          | unknown_14        | As in Layout 4                                  |
| `+0x18`             | u32          | replay_ref        | As in Layout 4                                  |
| `+0x1C`             | String Table | string_table      | See String Table                                |
| `string_table+0x00` | u32          | table_start       | Offset of the string table, `0x1C`              |
| `string_table+0x04` | u32          | zero              | Always `0`                                      |

## Layout 2

### File Layout

| Offset              | Type         | Field             | Notes                                           |
| ------------------- | ------------ | ----------------- | ----------------------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                                    |
| `+0x04`             | u32          | record_client_ref | As in Layout 4                                  |
| `+0x08`             | u32          | unknown_08        | As in Layout 4                                  |
| `+0x0C`             | u32          | unknown_0c        | As in Layout 4                                  |
| `+0x10`             | u32          | cash_shop_ref     | As in Layout 4                                  |
| `+0x14`             | u32          | unknown_14        | As in Layout 4                                  |
| `+0x18`             | String Table | string_table      | See String Table                                |
| `string_table+0x00` | u32          | table_start       | Offset of the string table, `0x18`              |
| `string_table+0x04` | u32          | zero              | Always `0`                                      |

## Layout 1

### File Layout

| Offset              | Type         | Field             | Notes                                           |
| ------------------- | ------------ | ----------------- | ----------------------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                                    |
| `+0x04`             | u32          | record_client_ref | As in Layout 4                                  |
| `+0x08`             | String Table | string_table      | See String Table                                |
| `string_table+0x00` | u32          | table_start       | Offset of the string table, `0x08`              |
| `string_table+0x04` | u32          | zero              | Always `0`                                      |

## URLs

Client 3482:

| Field               | URL                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `record_client_ref` | `https://{branch}{region}recordclient-api-shadowarena.pearlabyss.com`                         |
| `unknown_08`        | `https://{branch}{region}game-shadowarena.pearlabyss.com/InGameBanner/Home/EventBanner?language={lang}` |
| `unknown_0c`        | `https://{branch}{region}game-shadowarena.pearlabyss.com/InGameBanner/Home/Index?language={lang}&position={pos}` |
| `cash_shop_ref`     | the same as `unknown_0c`                                                                      |
| `unknown_14`        | the same as `unknown_0c`                                                                      |
| `replay_ref`        | `https://{branch}api-shadowarena.pearlabyss.com/Replay`                                       |
| `payment_ref`       | `https://{branch}payment.pearlabyss.com`                                                      |

## Field Names

The `SA_Web_URL` sheet of a private server's `DataSheets.bexcel` on
client 1784 has seven columns, `RecordClient`, `RecordServer`,
`EventBanner`, `CashShop`, `Policy`, `Replay` and `Payment`, and one row.
The client 1784 file is the same 438 bytes as the client 3482 file. Its
seven fields match the sheet by column position and value on four
columns, which name them: `RecordClient` (`+0x04`), `CashShop`
(`+0x10`), `Replay` (`+0x18`) and `Payment` (`+0x1C`).

The other three do not match. At `+0x08` the sheet has the
`RecordServer` URL (`recordserver-api-shadowarena`), which the file does
not hold; the file has the sheet's `EventBanner` URL there. At `+0x0C`
the sheet has `EventBanner`, the file the `CashShop` URL. At `+0x14` the
sheet has the `Policy` URL (`.../Policy?language={lang}`), which the
file does not hold; the file has the `CashShop` URL again. They stay
`unknown_*`.

## Notes

- The file is the same on clients 1784, 2107, 2765, 3002 and 3482. The
  older layouts hold the first fields only: Layout 1 `record_client_ref`,
  Layout 2 up to `unknown_14`, Layout 3 up to `replay_ref`.
- The `SA` prefix of the sheet and of [`bgmstatesa.bss`](bgmstatesa_bss.md)
  reads as Shadow Arena, the `*-shadowarena.pearlabyss.com` hosts of the
  URLs.
- No client Lua file of client 3482 names the table, a Shadow Arena URL
  or a `{branch}` placeholder.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/client_tables.py`, with
  the four named URLs.

## Open Questions

### The Three Unmatched URLs

The file was compiled from a sheet other than the client 1784 one: its
`+0x08`, `+0x0C` and `+0x14` URLs are not the sheet's `RecordServer`,
`EventBanner` and `Policy` values. Whether those are the three columns
of the file, with other values, or the file stores its URLs in another
order, is open.
