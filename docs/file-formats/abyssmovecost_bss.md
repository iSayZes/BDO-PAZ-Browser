# `abyssmovecost.bss` Format

## Purpose

Move costs between pairs of regions for the Magnus (`AbyssOne`): one row
per region, each a list of the same set of other regions with a u64 cost.
On client 3482 the table is 16 rows of 16 moves; every cost is `5000000`
except one `0` per row, where the two regions are near each other
(Bartali Farm and Velia, Erethea's Belt and Zvier Highlands). The
file has no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ---------------- | --------- |
| 1      | 2011 and later | 3482    | `abyssmovecost.bss` | 3,140 | 256 Move, 16 Row | 12        |

| Layout | File                | Known            | Unknown    |
| ------ | ------------------- | ---------------- | ---------- |
| 1      | `abyssmovecost.bss` | 3,140 B (100.0%) | 0 B (0.0%) |

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
| 3144   | Layout 1 |
| 3103   | Layout 1 |
| 3062   | Layout 1 |
| 3037   | Layout 1 |
| 3002   | Layout 1 |
| 2959   | Layout 1 |
| 2923   | Layout 1 |
| 2900   | Layout 1 |
| 2872   | Layout 1 |
| 2834   | Layout 1 |
| 2803   | Layout 1 |
| 2765   | Layout 1 |
| 2736   | Layout 1 |
| 2703   | Layout 1 |
| 2665   | Layout 1 |
| 2637   | Layout 1 |
| 2606   | Layout 1 |
| 2583   | Layout 1 |
| 2545   | Layout 1 |
| 2519   | Layout 1 |
| 2498   | Layout 1 |
| 2468   | Layout 1 |
| 2438   | Layout 1 |
| 2414   | Layout 1 |
| 2384   | Layout 1 |
| 2358   | Layout 1 |
| 2335   | Layout 1 |
| 2313   | Layout 1 |
| 2290   | Layout 1 |
| 2250   | Layout 1 |
| 2224   | Layout 1 |
| 2203   | Layout 1 |
| 2179   | Layout 1 |
| 2151   | Layout 1 |
| 2134   | Layout 1 |
| 2107   | Layout 1 |
| 2073   | Layout 1 |
| 2052   | Layout 1 |
| 2011   | Layout 1 |
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

None. The handler names both regions (LOC type 17) from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

### Row (variable: 4 bytes + moves)

| Offset  | Type              | Field      | Notes                                         |
| ------- | ----------------- | ---------- | --------------------------------------------- |
| `+0x00` | u32               | move_count | Number of `moves`; the same on every row      |
| `+0x04` | Move[move_count]  | moves      | See Move                                      |

### Move (12 bytes)

| Offset  | Type | Field        | Notes                                                                            |
| ------- | ---- | ------------ | -------------------------------------------------------------------------------- |
| `+0x00` | u64  | move_cost    | `5000000` or `0` on client 3482; `0` on exactly one move per row                 |
| `+0x08` | u16  | region_key_1 | `regioninfo.bss` region key (LOC type 17); the same on every move of a row, unique per row |
| `+0x0A` | u16  | region_key_2 | `regioninfo.bss` region key (LOC type 17); every row lists the same set                              |

## Free Moves

Client 3482: each row's region and the region of its `0` move.

| `region_key_1`             | `region_key_2`               |
| -------------------------- | ---------------------------- |
| 1733 Angavu Outpost        | 1741 Radiant Lands           |
| 1677 Olvia Academy Grounds | 1681 Olvia Academy Dining Hall |
| 1553 Hakinza Sanctuary     | 1574 Great White Spot        |
| 1121 Erethea's Belt        | 1122 Zvier Highlands         |
| 1420 Yukjo Street          | 1419 Seoul                   |
| 1375 Muzgar                | 1383 Turba Farm              |
| 1319 Chief's Home          | 1219 Nampo's Moodle Village  |
| 735 Grána                  | 1073 Lake Flondor            |
| 639 Erdal Farm             | 641 Fohalam Farm             |
| 1000 Oquilla's Eye         | 984 Oquilla's Eye            |
| 1023 Delmira Plantation    | 1022 Salanar Pond            |
| 903 Marak Farm             | 926 Duvencrune Farmland      |
| 236 Altinova Gateway       | 204 Stonebeak Shore          |
| 16 Bartali Farm            | 5 Velia                      |
| 300 Gabino Farm            | 267 Falres Dirt Farm         |
| 318 Moretti Plantation     | 36 Eastern Border            |

## Field Names

The Magnus is newer than client 1784: the file is not in its archives and
no sheet of a private server's `DataSheets.bexcel` on that client has
`Abyss` in its name. `move_cost` follows the file name; the two region
keys resolve to LOC type 17 names on every move. Which of the two is the
start of a move is not known, so they keep the numbers of their order in
the move.

## Notes

- Client 2107 holds 9 rows of 9 moves (1,012 bytes) with costs that grow
  with the distance between the two regions: from Erethea's Belt `0` to
  Zvier Highlands, `2100000` to Duvencrune Farmland and `11200000` to
  Fohalam Farm. Client 3482 has one cost for every move that is not free.
- Six of the 16 `region_key_1` regions (Angavu Outpost, Hakinza
  Sanctuary, Yukjo Street, Muzgar, Grána and Oquilla's Eye) are storage
  towns of [`abyssonewarehouse.bss`](abyssonewarehouse_bss.md) on client
  3482.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/abyssone_tables.py`: one
  row per region, each move as both regions with names and the cost.

## Open Questions

### What a Move Is

The rows pair 16 regions with 16 others and make one nearby pair per row
free. A move from the Magnus out to a vein
other than the one the character came in by would fit; no client Lua of
client 3482 names the file or a move cost getter. In game every move I
know of costs 5,000,000 silver in either direction, the same as the
`5000000` cost here, so the cost does not tell which region is the start.
