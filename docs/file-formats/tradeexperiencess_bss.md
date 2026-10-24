# `tradeexperiencess.bss` Format

## Purpose

The base Trading EXP of one sold trade item, per Trading level: a u32 count
and 180 u64 values, with no `PABR` magic and no string table. Row `r` is
`trade_exp` at Trading level `r + 1`. A sale scales it by the trade
distance and by the item's trade EXP rate (see Trading EXP of a Sale). The
file first ships in client 3473, the same client that replaced the Trading
EXP curve of [`lifeexp.dbss`](lifeexp_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 1      | 3473 and later | 3483    | `tradeexperiencess.bss` | 1,444 | 180 Row | 8         |

| Layout | File                    | Known            | Unknown    |
| ------ | ----------------------- | ---------------- | ---------- |
| 1      | `tradeexperiencess.bss` | 1,444 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 1 |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3464   | No file  |
| 3458   | No file  |
| 3454   | No file  |
| 3444   | No file  |
| 3435   | No file  |
| 3426   | No file  |
| 3418   | No file  |
| 3412   | No file  |
| 3402   | No file  |
| 3396   | No file  |
| 3387   | No file  |
| 3381   | No file  |
| 3373   | No file  |
| 3364   | No file  |
| 3356   | No file  |
| 3349   | No file  |
| 3342   | No file  |
| 3335   | No file  |
| 3326   | No file  |
| 3321   | No file  |
| 3314   | No file  |
| 3303   | No file  |
| 3302   | No file  |
| 3293   | No file  |
| 3283   | No file  |
| 3275   | No file  |
| 3267   | No file  |
| 3258   | No file  |
| 3251   | No file  |
| 3242   | No file  |
| 3235   | No file  |
| 3229   | No file  |
| 3212   | No file  |
| 3203   | No file  |
| 3193   | No file  |
| 3186   | No file  |
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

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3483 the file is 4 + 180 x 8 = 1,444 bytes.

### Row (8 bytes)

| Offset  | Type | Field     | Notes                                                                                     |
| ------- | ---- | --------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u64  | trade_exp | Base Trading EXP of one sold item at Trading level row + 1; `1` to `100308581` (client 3483) |

## Field Names

`trade_exp` is the 2016 PDB member `_tradeExp` of `gc::ActionExpStaticStatus`
(`+0x40`, see [`actionexp.dbss`](actionexp_dbss.md)), filled from the
`%Trade` column of the `ActionEXP_Table` sheet. In a private server's
`datasheet_pcdatatable.xlsm` on client 1784 that column runs from level 1
to 130 and is the same for all 31 classes. The sheet value at level `n`
matches row `n - 1` of the file:

- Level 41 is 133,805.76 in the sheet and row 40 is `133806`.
- On client 3483, 88 of the 180 rows equal the sheet value rounded to a
  whole number: every row from 49 to 129 (levels 50 to 130, the sheet's
  end), and rows 16, 26, 38, 40, 43, 44 and 45 below them.
- The other rows from 0 to 48 differ (row 48 is `403929`, the sheet
  403,144.30). These levels were retuned with the client 3473 Trading curve
  of `lifeexp.dbss`: the Trading EXP of each of them is a whole number of
  rows (see Rows and Trading Levels).
- Rows 130 to 179 (levels 131 to 180) lie past the sheet's end and hold `3`.

`CalcTradeSellRewards` reads `_tradeExp` from the row of the seller's
Trading level, and my readings below fit the result.

## Trading EXP of a Sale

`CalcTradeSellRewards` (VA `0x1412413f0`) in a private server's server dump
on client 1784 computes the Trading EXP of a sale. With `d` the trade
distance and `trade_exp` the row of the seller's Trading level:

```
g   = 0.95 * sqrt(d / 1000)          when d <= 500
g   = 0.3 + 0.7 * sqrt(d / 1000)     when d > 500
E1  = max(1, trunc(g * trade_exp))
EXP = max(1, trunc(GetSellingTradeExpRate / 1000000 * E1)) * item count
```

| Part | Source |
| ---- | ------ |
| `d` | The distance the trade window shows as Distance Bonus: the bonus is `68` millionths per unit of `d` (0.0068%), up to `1500000` (150%). These are `trade_bonus_gold_percent` and `max_distance_bonus` of [`gameoption.bss`](gameoption_bss.md), read by the bonus function at VA `0x140a99cb0`. |
| `g` | The function cuts `g` to six decimals before the multiplication. `g` is `1.0` at `d = 1000`, a 6.8% bonus. The square root is a call to a redirected CRT function in the dump, so it rests on my readings below. |
| `GetSellingTradeExpRate` | Per item, in millionths: the server-only `%GetSellingTradeExpRate` column of `SellingToNpc_Table` in a private server's `datasheet_tradedatatable.xlsm` on client 1784 (developer comment 무역경험치습득비율, trade EXP gain rate). 149 of the 199 fish there have `100000` (0.1) and 50 rarer fish `1000000` (1.0). The client file [`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md) has the member, but it is `0` in every entry on client 1784 and inside the all-zero `unknown_6d` on client 3474. |

The item's price and grade do not enter the formula. At a 0% bonus `g` is
`0`, and the two `max(1, ...)` steps leave 1 EXP per item. The EXP
multiplier of the life skill window (A x (100% + B) x (C + (100% + D) + E))
applies on top. I assume it comes after the formula (see Open Questions).

## Readings on Client 3483

My character had Trading at Artisan 1 (level 41: 47,501,047 EXP to the next
level, `trade_exp` 133,806) and the window multiplier x1.49 (only D,
Character Applied Stats, at 49%). I sold one item per sale to the Heidel
trade manager with a 100% bargain. The seven named fish have rate 0.1 in
the client 1784 sheet. The bar started at 86.49%.

| Sale | Item                 | Silver  | Distance bonus | Predicted EXP | Predicted gain | Bar after | Predicted bar |
| ---- | -------------------- | ------- | -------------- | ------------- | -------------- | --------- | ------------- |
| 1    | a green fish         | -       | 7.7%           | 20,831        | 0.0439%        | 86.53%    | 86.5391%      |
| 2    | a fish               | -       | 7.7%           | 20,831        | 0.0439%        | 86.58%    | 86.5830%      |
| 3    | Grayling (green)     | 26,853  | 7.7%           | 20,831        | 0.0439%        | 86.62%    | 86.6268%      |
| 4    | Barbel Steed (green) | 17,185  | 7.7%           | 20,831        | 0.0439%        | 86.67%    | 86.6707%      |
| 5    | Arowana (blue)       | 125,210 | 7.7%           | 20,831        | 0.0439%        | 86.71%    | 86.7146%      |
| 6    | Arowana (blue)       | 124,925 | 7.7%           | 20,831        | 0.0439%        | 86.75%    | 86.7584%      |
| 7    | Bitterling (green)   | 19,317  | 7.7%           | 20,831        | 0.0439%        | 86.80%    | 86.8023%      |
| 8    | Carp (blue)          | 100,401 | 7.7%           | 20,831        | 0.0439%        | 86.84%    | 86.8461%      |
| 9    | Terrapin (green)     | 21,840  | 0%             | 1             | 0.0000%        | 86.84%    | 86.8461%      |
| 10   | Sweetfish (green)    | 28,505  | 2.3%           | 11,014        | 0.0232%        | 86.86%    | 86.8693%      |
| 11   | Grayling (green)     | 37,339  | 47.1%          | 42,709        | 0.0899%        | 86.95%    | 86.9592%      |

I did not note the names and prices of the first two fish. Predicted EXP is
the formula at the shown bonus (`d` = bonus / 0.000068), with rate 0.1, times
1.49 and cut to a whole number. The shown bonus is rounded, so 7.7% stands
for `d` from 1,125 to 1,140 and gains from 20,782 to 20,879 EXP (0.0438% to
0.0440%). The predicted bar starts at 41,086,165 EXP (86.4953%). Any start
from 41,085,834 to 41,086,496 EXP gives all eleven shown values when the bar
cuts to two decimals, and a start from 41,083,656 to 41,084,121 does when it
rounds.

The Terrapin and Sweetfish sales rule out a flat EXP per sale, and the
Arowana and Barbel Steed sales a gain that follows the price. A gain
linear in the bonus, through the 0.0439% of the 7.7% sales, would be 0.27%
at 47.1%. The bar moved 0.09%, as the square root predicts.

## Rows and Trading Levels

Counted on client 3473 against the Trading row of
[`lifeexp.dbss`](lifeexp_dbss.md) from the same client, where the row for
level `n` holds the EXP to go from `n` to `n + 1`. The ratio is the number
of rate 1.0 items sold at 1,000 distance that level `n` takes:

| Trading levels | Rows      | Trading EXP of level `n` / row `n - 1`                                                                               |
| -------------- | --------- | -------------------------------------------------------------------------------------------------------------------- |
| 1 to 49        | 0 to 48   | A whole number `N` to within rounding, and the row is `round(EXP / N)`                                               |
| 50 to 61       | 49 to 60  | No whole number: 522.3 on level 50, then 1.3 times larger per level (1.385 from level 59 to 60), 9,969.2 on level 61 |
| 62 to 180      | 61 to 179 | No relation: the rows shrink, `lifeexp.dbss` keeps its sentinels                                                     |

`N` is 5, 5, 6, 9, 10, 11, 13, 16, 19 and 23 on Beginner 1 to 10, and
then grows by 4 to 22 per level up to 514 on level 49 (Artisan 9). On level 61,
the 9,969.2 divides the `999,999,999,999` sentinel that stops Trading at
Master 11.

Level 0 (20 EXP, no rank) has no row, row 60 is Master 11, the highest
level Trading can reach, and row 179 is Guru 100, the Trading max level of
[`lifeexpmaxlevel.bss`](lifeexpmaxlevel_bss.md).

## Notes

- The values on client 3474, by row index from 0: `1`, `1`, `2`, `5`,
  `16`, `43`, `91` and up to `210540` at row 45, then a steep rise to the
  largest value, `100308581`, at row 60. From there each value is about
  13/18 and 10/13 of the one before in turn (`72445086`, `55726989`,
  ...), down to `1023` at row 99, then `34` less per row to `3` at row
  129, and `3` on rows 129 to 179.
- Client 3473 (2026-10-15 build) is the first client with the file; 3473,
  3474 and 3482 ship the same 1,444 bytes. Client 3464 (2026-10-08) has no
  such file, and its Trading row of `lifeexp.dbss` is the older curve
  (20 EXP for Beginner 1, 212,980,644 for level 60). Its level 4 needs 33
  EXP, 6.6 times row 3, so the whole-number fit holds only for the new
  curve.
- The client file [`actionexp.dbss`](actionexp_dbss.md) holds the same
  `ActionExpStaticStatus` grid with every EXP byte `0`. This file carries
  the Trading column alone.
- No client Lua of client 3482 names the table or calls a getter for it;
  the trade dialog Lua reads only `getLifeExperienceLevel` for item level
  requirements.

## Open Questions

### Live Trade EXP Rates

The per-item `GetSellingTradeExpRate` values come from the client 1784
sheet of a private server. `itemtradegrouptonpc.dbss` of client 3474 holds
no non-zero copy of the value, so the rates of client 3483 are assumed to
be the same. My readings fit rate 0.1 for the seven fish I sold.

### Where the EXP Multiplier Applies

I assume the window multiplier scales the result of the formula. Applying it
to `trade_exp` before the two cuts changes the result by at most a few EXP
per item, which the bar does not show at Artisan 1.

## In-Game Checks

### Rate 1.0 Fish

Needs item (any one):

- [Grass Carp](https://bdocodex.com/us/item/8368/)
- [Diamond Minnow](https://bdocodex.com/us/item/8353/)
- [Spotted Barbel](https://bdocodex.com/us/item/8351/)

Needs skill: Trading at Artisan 1, with the x1.49 multiplier of my readings

This check settles whether the live rate of these fish is 1.0, as in the
client 1784 sheet.

1. Carry one of the fish to a trade manager where the trade window shows
   about 7.7% Distance Bonus.
2. Note the Trading bar in the life skill window.
3. Sell the one fish.
4. Note the Trading bar again.

Expected: the bar moves by about 0.44% (208,318 EXP), ten times the 0.0439%
of a rate 0.1 fish. A move of about 0.04% means the fish has rate 0.1 on the
live client, and the 1784 sheet rates do not hold.
