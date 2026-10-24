# `journalquest.dbss` Format

## Purpose

Adventure Log (bookshelf) data. Defines the journal groups shown in the in-game Adventure Log UI (e.g., "Igor Bartali's Adventures", "Shakatu Merchants' Archive"), the books (volumes) inside each group, and per-book metadata: Korean journal name, journal description, book name and unlock requirement, two bookshelf asset names, and the ordered list of quests that make up the book's pages.

Field names `journal_key`, `book_key` and the "book" terminology follow the notes of [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor); every field below was re-verified against our extracted files.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes  | Records                   | Row bytes                  |
| ------ | -------------- | ------- | ------------------- | ------ | ------------------------- | -------------------------- |
| 2      | 2142 and later | 3483    | `journalquest.dbss` | 48,566 | 117 Book Record, 13 Group | 258 to 774, 415 on average |
| 1      | 1286 to 2138   | 2138    | `journalquest.dbss` | 23,327 | 52 Book Record, 12 Group  | 205 to 639, 448 on average |

| Layout | File                | Known            | Unknown         |
| ------ | ------------------- | ---------------- | --------------- |
| 2      | `journalquest.dbss` | 48,098 B (99.0%) | 468 B (1.0%)    |
| 1      | `journalquest.dbss` | 20,580 B (88.2%) | 2,747 B (11.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 2 |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3464   | Layout 2 |
| 3458   | Layout 2 |
| 3454   | Layout 2 |
| 3444   | Layout 2 |
| 3435   | Layout 2 |
| 3426   | Layout 2 |
| 3418   | Layout 2 |
| 3412   | Layout 2 |
| 3402   | Layout 2 |
| 3396   | Layout 2 |
| 3387   | Layout 2 |
| 3381   | Layout 2 |
| 3373   | Layout 2 |
| 3364   | Layout 2 |
| 3356   | Layout 2 |
| 3349   | Layout 2 |
| 3342   | Layout 2 |
| 3335   | Layout 2 |
| 3326   | Layout 2 |
| 3321   | Layout 2 |
| 3314   | Layout 2 |
| 3303   | Layout 2 |
| 3302   | Layout 2 |
| 3293   | Layout 2 |
| 3283   | Layout 2 |
| 3275   | Layout 2 |
| 3267   | Layout 2 |
| 3258   | Layout 2 |
| 3251   | Layout 2 |
| 3242   | Layout 2 |
| 3235   | Layout 2 |
| 3229   | Layout 2 |
| 3212   | Layout 2 |
| 3203   | Layout 2 |
| 3193   | Layout 2 |
| 3186   | Layout 2 |
| 3177   | Layout 2 |
| 3169   | Layout 2 |
| 3158   | Layout 2 |
| 3151   | Layout 2 |
| 3144   | Layout 2 |
| 3133   | Layout 2 |
| 3125   | Layout 2 |
| 3118   | Layout 2 |
| 3111   | Layout 2 |
| 3103   | Layout 2 |
| 3095   | Layout 2 |
| 3086   | Layout 2 |
| 3072   | Layout 2 |
| 3062   | Layout 2 |
| 3052   | Layout 2 |
| 3045   | Layout 2 |
| 3037   | Layout 2 |
| 3030   | Layout 2 |
| 3021   | Layout 2 |
| 3012   | Layout 2 |
| 3002   | Layout 2 |
| 2995   | Layout 2 |
| 2987   | Layout 2 |
| 2978   | Layout 2 |
| 2970   | Layout 2 |
| 2959   | Layout 2 |
| 2951   | Layout 2 |
| 2942   | Layout 2 |
| 2935   | Layout 2 |
| 2932   | Layout 2 |
| 2923   | Layout 2 |
| 2919   | Layout 2 |
| 2907   | Layout 2 |
| 2900   | Layout 2 |
| 2891   | Layout 2 |
| 2882   | Layout 2 |
| 2872   | Layout 2 |
| 2863   | Layout 2 |
| 2855   | Layout 2 |
| 2849   | Layout 2 |
| 2844   | Layout 2 |
| 2834   | Layout 2 |
| 2825   | Layout 2 |
| 2819   | Layout 2 |
| 2811   | Layout 2 |
| 2803   | Layout 2 |
| 2794   | Layout 2 |
| 2783   | Layout 2 |
| 2774   | Layout 2 |
| 2765   | Layout 2 |
| 2756   | Layout 2 |
| 2750   | Layout 2 |
| 2743   | Layout 2 |
| 2736   | Layout 2 |
| 2726   | Layout 2 |
| 2717   | Layout 2 |
| 2709   | Layout 2 |
| 2703   | Layout 2 |
| 2695   | Layout 2 |
| 2684   | Layout 2 |
| 2672   | Layout 2 |
| 2665   | Layout 2 |
| 2657   | Layout 2 |
| 2649   | Layout 2 |
| 2644   | Layout 2 |
| 2637   | Layout 2 |
| 2629   | Layout 2 |
| 2619   | Layout 2 |
| 2612   | Layout 2 |
| 2606   | Layout 2 |
| 2602   | Layout 2 |
| 2601   | Layout 2 |
| 2592   | Layout 2 |
| 2583   | Layout 2 |
| 2575   | Layout 2 |
| 2567   | Layout 2 |
| 2560   | Layout 2 |
| 2553   | Layout 2 |
| 2545   | Layout 2 |
| 2538   | Layout 2 |
| 2529   | Layout 2 |
| 2519   | Layout 2 |
| 2513   | Layout 2 |
| 2510   | Layout 2 |
| 2507   | Layout 2 |
| 2503   | Layout 2 |
| 2498   | Layout 2 |
| 2492   | Layout 2 |
| 2487   | Layout 2 |
| 2480   | Layout 2 |
| 2474   | Layout 2 |
| 2468   | Layout 2 |
| 2460   | Layout 2 |
| 2453   | Layout 2 |
| 2444   | Layout 2 |
| 2438   | Layout 2 |
| 2434   | Layout 2 |
| 2429   | Layout 2 |
| 2421   | Layout 2 |
| 2414   | Layout 2 |
| 2407   | Layout 2 |
| 2401   | Layout 2 |
| 2397   | Layout 2 |
| 2393   | Layout 2 |
| 2384   | Layout 2 |
| 2378   | Layout 2 |
| 2372   | Layout 2 |
| 2358   | Layout 2 |
| 2352   | Layout 2 |
| 2347   | Layout 2 |
| 2343   | Layout 2 |
| 2335   | Layout 2 |
| 2327   | Layout 2 |
| 2324   | Layout 2 |
| 2319   | Layout 2 |
| 2313   | Layout 2 |
| 2308   | Layout 2 |
| 2302   | Layout 2 |
| 2295   | Layout 2 |
| 2290   | Layout 2 |
| 2284   | Layout 2 |
| 2276   | Layout 2 |
| 2269   | Layout 2 |
| 2259   | Layout 2 |
| 2250   | Layout 2 |
| 2243   | Layout 2 |
| 2235   | Layout 2 |
| 2229   | Layout 2 |
| 2224   | Layout 2 |
| 2218   | Layout 2 |
| 2215   | Layout 2 |
| 2207   | Layout 2 |
| 2203   | Layout 2 |
| 2196   | Layout 2 |
| 2192   | Layout 2 |
| 2189   | Layout 2 |
| 2183   | Layout 2 |
| 2179   | Layout 2 |
| 2171   | Layout 2 |
| 2163   | Layout 2 |
| 2156   | Layout 2 |
| 2151   | Layout 2 |
| 2147   | Layout 2 |
| 2142   | Layout 2 |
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
| 1921   | Layout 1 |
| 1914   | Layout 1 |
| 1908   | Layout 1 |
| 1897   | Layout 1 |
| 1892   | Layout 1 |
| 1886   | Layout 1 |
| 1881   | Layout 1 |
| 1871   | Layout 1 |
| 1866   | Layout 1 |
| 1862   | Layout 1 |
| 1854   | Layout 1 |
| 1846   | Layout 1 |
| 1838   | Layout 1 |
| 1832   | Layout 1 |
| 1826   | Layout 1 |
| 1822   | Layout 1 |
| 1818   | Layout 1 |
| 1804   | Layout 1 |
| 1794   | Layout 1 |
| 1790   | Layout 1 |
| 1784   | Layout 1 |
| 1774   | Layout 1 |
| 1771   | Layout 1 |
| 1762   | Layout 1 |
| 1759   | Layout 1 |
| 1754   | Layout 1 |
| 1749   | Layout 1 |
| 1743   | Layout 1 |
| 1737   | Layout 1 |
| 1731   | Layout 1 |
| 1725   | Layout 1 |
| 1717   | Layout 1 |
| 1710   | Layout 1 |
| 1704   | Layout 1 |
| 1698   | Layout 1 |
| 1690   | Layout 1 |
| 1685   | Layout 1 |
| 1680   | Layout 1 |
| 1674   | Layout 1 |
| 1668   | Layout 1 |
| 1659   | Layout 1 |
| 1649   | Layout 1 |
| 1642   | Layout 1 |
| 1636   | Layout 1 |
| 1628   | Layout 1 |
| 1622   | Layout 1 |
| 1614   | Layout 1 |
| 1608   | Layout 1 |
| 1602   | Layout 1 |
| 1598   | Layout 1 |
| 1594   | Layout 1 |
| 1590   | Layout 1 |
| 1587   | Layout 1 |
| 1584   | Layout 1 |
| 1579   | Layout 1 |
| 1572   | Layout 1 |
| 1565   | Layout 1 |
| 1559   | Layout 1 |
| 1554   | Layout 1 |
| 1547   | Layout 1 |
| 1537   | Layout 1 |
| 1529   | Layout 1 |
| 1524   | Layout 1 |
| 1519   | Layout 1 |
| 1509   | Layout 1 |
| 1506   | Layout 1 |
| 1504   | Layout 1 |
| 1500   | Layout 1 |
| 1493   | Layout 1 |
| 1489   | Layout 1 |
| 1485   | Layout 1 |
| 1481   | Layout 1 |
| 1474   | Layout 1 |
| 1466   | Layout 1 |
| 1462   | Layout 1 |
| 1459   | Layout 1 |
| 1453   | Layout 1 |
| 1450   | Layout 1 |
| 1445   | Layout 1 |
| 1439   | Layout 1 |
| 1433   | Layout 1 |
| 1430   | Layout 1 |
| 1426   | Layout 1 |
| 1421   | Layout 1 |
| 1417   | Layout 1 |
| 1416   | Layout 1 |
| 1409   | Layout 1 |
| 1405   | Layout 1 |
| 1401   | Layout 1 |
| 1396   | Layout 1 |
| 1391   | Layout 1 |
| 1390   | Layout 1 |
| 1386   | Layout 1 |
| 1381   | Layout 1 |
| 1379   | Layout 1 |
| 1372   | Layout 1 |
| 1366   | Layout 1 |
| 1364   | Layout 1 |
| 1363   | Layout 1 |
| 1360   | Layout 1 |
| 1358   | Layout 1 |
| 1355   | Layout 1 |
| 1351   | Layout 1 |
| 1348   | Layout 1 |
| 1346   | Layout 1 |
| 1341   | Layout 1 |
| 1340   | Layout 1 |
| 1338   | Layout 1 |
| 1335   | Layout 1 |
| 1333   | Layout 1 |
| 1329   | Layout 1 |
| 1327   | Layout 1 |
| 1324   | Layout 1 |
| 1321   | Layout 1 |
| 1319   | Layout 1 |
| 1318   | Layout 1 |
| 1316   | Layout 1 |
| 1313   | Layout 1 |
| 1311   | Layout 1 |
| 1309   | Layout 1 |
| 1304   | Layout 1 |
| 1292   | Layout 1 |
| 1286   | Layout 1 |
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

| File                         | Required | Role                                                                        |
| ---------------------------- | -------- | --------------------------------------------------------------------------- |
| `journalquestoffset.dbss`    | Required | Provides `(journal_key, book_key) → (byte_offset, byte_size)` record lookup |
| `quest.dbss`                 | Optional | Quest record for each page (conditions, objective, rewards)                 |
| `languagedata_en.loc`        | Optional | English journal/book text via LOC type=63; page quest text via LOC type=18  |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type               | Field       | Notes                                          |
| ------- | ------------------ | ----------- | ---------------------------------------------- |
| `+0x00` | u32                | group_count | Number of journal groups; `13` since the 2026-09-27 client update, `12` before |
| `+0x04` | Group[group_count] | groups      | See Group                                      |

### Group (variable: 4 bytes + book records)

| Offset  | Type                    | Field      | Notes                                                              |
| ------- | ----------------------- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | u32                     | book_count | Number of book records in this group; equals the offset-file count |
| `+0x04` | Book Record[book_count] | books      | See Book Record                                                    |

The value previously documented as header `unknown_1` (`15` at `+0x04`) is the `book_count` of the first group (journal 1 has 15 books). The 4-byte header, the `book_count` words and the indexed records tile the file exactly, with no gaps or overlaps (verified on the `49,206`-byte file after the 2026-09-27 update with 13 groups and 119 records, the `46,620`-byte file before it with 12 and 112, and the `46,476`-byte fixture). Groups are stored physically in offset-file order; inside group 6 the offset-file order of books differs from their physical order (see [journalquestoffset.dbss](journalquestoffset_dbss.md)).

### Book Record (variable: 65 bytes + strings and pages)

Strings are length-prefixed: a u64 character count followed by that many UTF-16LE (`str16`) or single-byte ASCII (`str8`) code units, with no terminator.

| Offset                          | Type            | Field                  | Notes                                                                                      |
| ------------------------------- | --------------- | ---------------------- | ------------------------------------------------------------------------------------------ |
| `+0x00`                         | u32             | journal_key            | Journal group key; equals the containing group in 112 of 112 records                       |
| `+0x04`                         | u32             | book_key               | Book key within the group; equals the offset-file key in 112 of 112 records                |
| `+0x08`                         | u8              | is_record_book         | `1` on record books, whose pages fill in from what the player has already done; 43 records (all books of journals 7, 10, 12 and 13, plus journal 6 book 8), see Notes |
| `+0x09`                         | str16           | journal_name_kr        | Korean journal name; identical for every book in a group except journal 6                  |
| `journal_name_kr+0x00`          | str16           | journal_description_kr | Korean journal description                                                                 |
| `journal_description_kr+0x00`   | str16           | book_name_kr           | Korean book (volume) name; may contain a `\n` and a second line                            |
| `book_name_kr+0x00`             | str16           | unlock_requirement_kr  | Korean unlock text with `<PAColor0x........>` markup; empty (`n=0`) in 51 of 112 books      |
| `unlock_requirement_kr+0x00`    | str8            | bookshelf_scene        | E.g. `Combine_Etc_Adventure_Bookshelf01`; 31 distinct values                               |
| `bookshelf_scene+0x00`          | str8            | book_model             | `Adventure_Bookshelf_Static_book_00` to `_06`                                              |
| `book_model+0x00`               | u32             | page_count             | Number of page quest IDs                                                                   |
| `book_model+0x04`               | u32[page_count] | page_quest_ids         | Packed quest IDs `(quest_id << 16) \| quest_chain_id`                                      |
| `page_quest_ids+0x00`           | u32             | unknown_end            | `0` in 112 of 112 records; the record ends exactly here                                   |

Earlier versions of this doc called `is_record_book` `flag_08` and then `unknown_08`. An even older reading of it as a u32 (`0x00000d00` etc.) was this byte plus the low bytes of the first string length. The "trailing `"` in `combine_model`" was the low byte of the next string's u64 length (`0x22` = 34 characters); it is not part of the stored value.

## Layout 1

Client 1784 book records have no `is_record_book`, `unlock_requirement_kr`,
`bookshelf_scene` or `book_model`. After `book_name_kr` they hold a u32 and
one ASCII icon path. The 12 groups hold 52 books on client 1784. Only the
Book Record differs from Layout 2.

### Book Record (variable: 52 bytes + strings and pages)

| Offset                        | Type            | Field                   | Notes                                                                 |
| ----------------------------- | --------------- | ----------------------- | --------------------------------------------------------------------- |
| `+0x00`                       | u32             | journal_key             |                                                                       |
| `+0x04`                       | u32             | book_key                |                                                                       |
| `+0x08`                       | str16           | journal_name_kr         |                                                                       |
| `journal_name_kr+0x00`        | str16           | journal_description_kr  |                                                                       |
| `journal_description_kr+0x00` | str16           | book_name_kr            |                                                                       |
| `book_name_kr+0x00`           | u32             | unknown_book_name_kr_00 | `1` to `6`, one value per journal on client 1784                      |
| `book_name_kr+0x04`           | str8            | unknown_icon_path       | A `.dds` path such as `Icon/Quest/Journal_BlackSpirit.dds`            |
| `unknown_icon_path+0x00`      | u32             | page_count              |                                                                       |
| `unknown_icon_path+0x04`      | u32[page_count] | page_quest_ids          |                                                                       |
| `page_quest_ids+0x00`         | u32             | unknown_end             | `0` in all 52 records (client 1784)                                   |

## Page Quest IDs

Every page is a single packed quest ID `(quest_id << 16) | quest_chain_id`, the same scheme as [quest.dbss](quest_dbss.md) and [allquestlist.bss](allquestlist_bss.md). There is only one encoding: the old "Type A / Type B" split does not occur in either file version (all 827 current pages decode with `lo16 = quest_chain_id`). All pages of one book belong to a single quest chain (112 of 112 books), and 110 books start at `quest_id = 1`.

Current file totals (after the 2026-09-27 update): 119 books, 901 pages, 901 distinct page quest IDs, all present in `allquestlist.bss`; one quest chain per book, 117 books start at `quest_id = 1`, and 51 books have no unlock text. Before the update: 112 books, 827 pages, all with a LOC type 18 `id4=0` title.

## Journal Group Table

Current client data (`files/journalquest.dbss`), offset-file order:

| Journal Key | Books | Pages | English Journal Name (LOC 63, `id4=0`) | Record books | Books with unlock text |
| ----------: | ----: | ----: | -------------------------------------- | ------------: | ---------------------: |
|           1 |    15 |    71 | Igor Bartali's Adventures              |             0 |                     15 |
|           2 |    11 |    51 | Shakatu Merchants' Archive             |             0 |                     11 |
|           3 |    10 |   105 | Storybook - Morning Bosses             |             0 |                      0 |
|           4 |     1 |    17 | Justin Bartali's Adventures            |             0 |                      1 |
|           5 |    13 |    66 | Crow Merchants' Records                |             0 |                     13 |
|           6 |     7 |    44 | Event Logs                             |             1 |                      4 |
|           7 |    15 |   180 | Storybook - Donghae                    |            15 |                      0 |
|           8 |     1 |    13 | Olvia Academy Journal                  |             0 |                      0 |
|           9 |    10 |    53 | Old Moon Logs                          |             0 |                     10 |
|          11 |     9 |    45 | The Eyes of Adventure                  |             0 |                      0 |
|          12 |    13 |   138 | Storybook - Hwanghae                   |            13 |                      0 |
|          10 |     7 |    44 | Outer Edania                           |             7 |                      7 |
|          13 |     7 |    74 | Inner Edania (added 2026-09-27)        |             7 |                      7 |

The older fixture (`PAZ-Parser/tests/fixtures/journalquest.dbss`, 815 pages) has the same books, except journal 8 was a one-page placeholder (chain 896) instead of the 13-page Olvia Academy Journal.

## Localization

Journal and book text is in LOC `str_type=63`. The LOC key's second u32 packs `str_id2`/`str_id3` (low 24 bits) and `str_id4` (high byte), so this is the same as "low 24 bits select the book, high byte selects the field":

| LOC Field  | Value                                                                    | Notes                                         |
| ---------- | ------------------------------------------------------------------------ | --------------------------------------------- |
| `str_type` | `63`                                                                     |                                               |
| `str_id1`  | `journal_key`                                                            |                                               |
| `str_id2`  | `book_key`                                                               | `str_id3` is always `0`                       |
| `str_id4`  | `0` = journal name, `1` = journal description, `2` = unlock requirement, `3` = book name |                               |

Checked against all 112 books: `id4=0`, `1` and `3` exist for every book; `id4=2` exists for exactly the 61 books whose Korean `unlock_requirement_kr` is non-empty. The English journal name for every book is LOC 63 `id4=0`.

LOC type 63 also holds rows the file does not reference: `str_id2=0` rows for journal keys 1 to 13 (older journal names such as "Rulupee's Travels" under key 2). Journal key 13 ("Inner Edania", books 1 to 7) had LOC rows before it had records; the 2026-09-27 update added its 7 books.

Page text is LOC `str_type=18` keyed by the page's packed quest ID, like any quest:

| LOC Field  | Value                              | Notes                                         |
| ---------- | ---------------------------------- | --------------------------------------------- |
| `str_type` | `18`                               |                                               |
| `str_id1`  | `page_quest_id & 0xFFFF`           | Quest chain ID                                |
| `str_id2`  | `page_quest_id >> 16`              | Quest ID within the chain; no off-by-one      |
| `str_id4`  | `0` = title, `1` = story text      | See [quest.dbss](quest_dbss.md) for `2`/`3`   |

## Notes

- All records are located through `journalquestoffset.dbss`; the book records are self-describing (length-prefixed strings, counted page list), so the file can also be walked sequentially using the per-group `book_count` words.
- Strings are length-prefixed, so the odd byte offset of the first string (`+0x09`, after two u32 and one u8) has no alignment meaning.
- Unlock text uses BDO rich-text markup: `<PAColor0xAARRGGBB>` to set color (e.g. `<PAColor0xFFf3d900>`), `<PAOldColor>` to reset, and backtick-delimited quest names.
- Journal 6 ("Event Logs") is the only group whose Korean journal name differs between books (two variants: event logs and 10th anniversary event logs). In game all seven books sit under one "Event Logs (6/7)" journal with the description "Special adventure logs available during events." (2026-09-28).
- The journal window shows the books as a shelf sorted by `book_key`, with the key printed on each cover and "?" for a book not obtained yet. Journal 6 shows 1, 2, 7, 8, 10, 11, 12 (checked in game, 2026-09-28), although the offset file lists 1, 2, 10, 7, 8, 11, 12 and the data file stores 1, 10, 2, 7, 8, 11, 12. So neither file order is the display order; bdo-data-extractor's claim that the index order is the UI order does not hold.
- The journals themselves are sorted by `journal_key` too: the main bookshelf fills columns of four, 1 to 4, 5 to 8 and 9 to 12, although the offset file lists journal 10 after 12. In my game (2026-09-28) the slot for journal 10 (Outer Edania) is empty and journal 13 (Inner Edania) does not show, on a family that has not started the Edania questline. In-Game Checks has the test for when they appear.
- `is_record_book` marks a record book: every page completes passively from what the player has already done, and the book reads as a story, with no Goal line, no reward and no claim button. Every page quest of a record book (448 pages, client 3458) has only a passive `action_script` check: `collectknowledge(...)` (318, Donghae and Hwanghae), `alreadyclearquest(...)` (118, the Edania journals) or `checkLevelUp(1)` (12, Event Logs book 8, objective "접속하기", log in). Other books are mostly real tasks (`meet` 134, `killmonster` 114, `gatheritem`, `exchangeitem` and others), with a few passive pages mixed in. Checked in game (2026-09-28): Event Logs book 8 reads as a long story ("An Adventurer's Story (1/4)") with no Goal line or reward, while book 2 shows "Goal: Find the note Reubens hid", "Upon Completion: Black Stone" and "This adventure log must be completed in order"; a Storybook - Donghae book has no Goal line or claim button either, and a page not earned yet shows as "???" ("Untold stories are waiting to be discovered. Embark on quests to uncover the hidden tales."). The flag does not pick the cover or the spine: book 8 has the same red cover as book 2, and Storybook - Donghae looks like Storybook - Morning Bosses (not a record book) on the shelf. bdo-data-extractor leaves the byte unnamed.
- Each page quest has a `quest.dbss` record whose `quest_category` is `11`; that value occurs on no other quest. [`specialquestlist.bss`](specialquestlist_bss.md) lists the same quests in `quest.dbss` record order. Page records hold the journal's permanent Family-stat rewards (see [quest.dbss](quest_dbss.md)).

## Open Questions

### Unreferenced LOC Type 63 Rows

LOC 63 has `str_id2=0` rows for journal keys 1 to 13 with names that do not match the current journals (key 2 is "Rulupee's Travels" in LOC but "Shakatu Merchants' Archive" in the file). Whether these are leftovers or something else is unknown. Journal 13 ("Inner Edania") was LOC-only until the 2026-09-27 update shipped its books, so LOC can run ahead of the data files.

## In-Game Checks

### Edania Journals on the Shelf

Needs quest (all):

- [[Edania] First Steps Toward the End Times](https://bdocodex.com/us/quest/9100/1/), the start of the Edania questline
- [[Edania] Into the Nightmare](https://bdocodex.com/us/quest/9100/5/), the unlock of journal 10 book 1
- [[Edania] The Two Keys](https://bdocodex.com/us/quest/9301/8/), the unlock of journal 13 book 1

On a family that has not started the Edania questline, the slot for journal 10 (Outer Edania) is empty and journal 13 (Inner Edania) is missing (2026-09-28). Open the main bookshelf after each quest. Journal 10 should fill the empty slot of the third column and journal 13 should start a fourth column, which confirms the shelf places journals by `journal_key`. If journal 10 shows after First Steps Toward the End Times, a journal joins the shelf when its questline starts; if it only shows after Into the Nightmare, it joins with its first book. Journal 13 showing only after The Two Keys fits the second reading.
