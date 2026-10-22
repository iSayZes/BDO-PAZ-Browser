# `specialpass.bss` Format

## Purpose

The Special Pass events of the event window: per pass its period, the end
of the pass sale, string table indices of its Korean title, period text
and description, and its content type (Daily, Solare, Combat, Sailing or
Gathering Special). A reward track per pass follows the rows, 14 steps of
a basic item, a pass item and the Pass Points that unlock the step.
`panel_event_specialpass_all_1.luac` picks a pass through
`ToClient_GetCurrentSpecialPassKey(passType)` and reads it through
`ToClient_GetSpecialPassTitle`, `ToClient_GetSpecialPassPeriod`,
`ToClient_GetSpecialPassDesc`, `ToClient_GetSpecialPassItemEnchantKey(passKey,
isPass, index)`, `ToClient_GetSpecialPassItemCount(passKey, isPass, index)`
and `ToClient_GetSpecialPassItemRewardPoint(passKey, index)`, for index `0`
to `__eSPECIALPASS_MAX_COUNT - 1`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes  | Records                           | Row bytes |
| ------ | -------------- | ------- | ----------------- | ------ | --------------------------------- | --------- |
| 2      | 3002 and later | 3482    | `specialpass.bss` | 39,107 | 31 Row, 434 Step, 31 Reward Track | 34        |
| 1      | 2107 to 2765   | 2765    | `specialpass.bss` | 15,493 | 12 Row, 168 Step, 12 Reward Track | 26        |

| Layout | File              | Known            | Unknown      |
| ------ | ----------------- | ---------------- | ------------ |
| 2      | `specialpass.bss` | 38,908 B (99.5%) | 199 B (0.5%) |
| 1      | `specialpass.bss` | 15,445 B (99.7%) | 48 B (0.3%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset                      | Type                      | Field                | Notes                                                       |
| --------------------------- | ------------------------- | -------------------- | ----------------------------------------------------------- |
| `+0x00`                     | char[4]                   | magic                | ASCII `PABR`                                                |
| `+0x04`                     | u32                       | row_count            | Number of rows                                              |
| `+0x08`                     | Row[row_count]            | rows                 | See Row                                                     |
| `rows+0x00`                 | u32                       | track_count          | Number of `tracks`; equals `row_count` (clients 2107 to 3482) |
| `rows+0x04`                 | Reward Track[track_count] | tracks               | One per row, in row order; see Reward Track                 |
| `tracks+0x00`               | u32[..table_start]        | unknown_after_tracks | 0 bytes up to client 3002, 48 on 3251, 168 on 3482; see Open Questions |
| `unknown_after_tracks+0x00` | String Table              | string_table         | See String Table                                            |
| `EOF-0x08`                  | u32                       | table_start          | Offset of the string table                                  |
| `EOF-0x04`                  | u32                       | zero                 | Always `0`                                                  |

### Row (43 bytes)

| Offset  | Type | Field             | Notes                                                                                     |
| ------- | ---- | ----------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | pass_key          | Row key, `1` to `31` on client 3482; `ToClient_GetCurrentSpecialPassKey()`                  |
| `+0x02` | u64  | start_time        | Unix seconds (UTC); the start date of the period text on 30 of 31 rows (client 3482)       |
| `+0x0A` | u64  | end_time          | Unix seconds (UTC); the end date of the period text on 30 of 31 rows                       |
| `+0x12` | u64  | sale_end_time     | Unix seconds (UTC), between the two; the end of the `패스 판매 기간` (pass sale) the description names, 31 of 31 |
| `+0x1A` | u32  | title_index       | String table index of the title (`스페셜 패스 - 솔라레 스페셜`); `ToClient_GetSpecialPassTitle` |
| `+0x1E` | u32  | period_index      | String table index of the period text (`2026년 4월 30일 ~ 2026년 5월 28일`); `ToClient_GetSpecialPassPeriod` |
| `+0x22` | u32  | description_index | String table index of the description; `ToClient_GetSpecialPassDesc`                       |
| `+0x26` | u32  | content_type      | `__eSpecialPassContentType_*`; see Content Types                                           |
| `+0x2A` | u8   | unknown_2a        | `0` on every row (clients 3002 to 3482)                                                    |

### Reward Track (variable: 4 bytes + steps)

| Offset  | Type             | Field      | Notes                                                        |
| ------- | ---------------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u32              | step_count | Number of `steps`; `14` on every track (clients 2107 to 3482) |
| `+0x04` | Step[step_count] | steps      | See Step                                                     |

### Step (34 bytes)

| Offset  | Type | Field            | Notes                                                                           |
| ------- | ---- | ---------------- | ------------------------------------------------------------------------------- |
| `+0x00` | u16  | pass_key         | The `pass_key` of the track's row, on every step                                |
| `+0x02` | u32  | basic_item_key   | Free reward, packed as `enchant_level << 24 \| item_id`; `ToClient_GetSpecialPassItemEnchantKey(key, false, i)` |
| `+0x06` | u64  | basic_item_count | Amount of `basic_item_key`; `ToClient_GetSpecialPassItemCount(key, false, i)`    |
| `+0x0E` | u32  | pass_item_key    | Reward of pass holders, packed the same way; `isPass` `true`                     |
| `+0x12` | u64  | pass_item_count  | Amount of `pass_item_key`                                                        |
| `+0x1A` | u64  | reward_point     | Pass Points that unlock the step, rising step by step; `ToClient_GetSpecialPassItemRewardPoint` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                   |
| ------- | ------------------ | ------------ | --------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; 68 on client 3482    |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE Korean texts the rows index    |

## Layout 1

### Row (42 bytes)

| Offset  | Type | Field             | Notes                                      |
| ------- | ---- | ----------------- | ------------------------------------------ |
| `+0x00` | u16  | pass_key          |                                            |
| `+0x02` | u64  | start_time        |                                            |
| `+0x0A` | u64  | end_time          |                                            |
| `+0x12` | u64  | sale_end_time     |                                            |
| `+0x1A` | u32  | title_index       |                                            |
| `+0x1E` | u32  | period_index      |                                            |
| `+0x22` | u32  | description_index |                                            |
| `+0x26` | u32  | unknown_26        | `0` on every row (clients 2107 to 2765)    |

### Step (26 bytes)

| Offset  | Type | Field            | Notes                              |
| ------- | ---- | ---------------- | ---------------------------------- |
| `+0x00` | u16  | pass_key         |                                    |
| `+0x02` | u32  | basic_item_key   |                                    |
| `+0x06` | u64  | basic_item_count |                                    |
| `+0x0E` | u32  | pass_item_key    |                                    |
| `+0x12` | u64  | pass_item_count  | No `reward_point`: a step is a day |

## Content Types

The Lua lists the five `__eSpecialPassContentType_*` values in this order
for the window's type buttons; the titles of the rows give the numbers
(client 3482):

| Value | Lua enum  | Title of the rows        | English (LOC type 0 pass item) | Rows |
| ----- | --------- | ------------------------ | ------------------------------ | ---- |
| 1     | `Daily`   | (스페셜 패스 -) 데일리 스페셜 | Daily Special Pass           | 21   |
| 2     | `Solare`  | 스페셜 패스 - 솔라레 스페셜  | Solare Special Pass            | 5    |
| 3     | `Monster` | 스페셜 패스 - 사냥 스페셜    | Combat Special Pass            | 3    |
| 4     | `Barter`  | 스페셜 패스 - 항해 스페셜    | Sailing Special Pass           | 1    |
| 5     | `Collect` | 스페셜 패스 - 채집 스페셜    | Gathering Special Pass         | 1    |

The Daily tracks count days (`reward_point` `1` to `14`), the others
Pass Points: `2` to `70` (Solare), `500` to `16000` (Combat), `10` to
`400` (Sailing) and `50` to `5000` (Gathering) on client 3482. The LOC
type 0 text of the Gathering pass item says "Earn Pass Points through
gathering activities", that of the Sailing pass "Earn Pass Points from
bartering".

## Field Names

The Special Pass is newer than client 1784: the file is not in its archives
and no sheet of a private server's `DataSheets.bexcel` on that client
covers it. The names follow the getters of
`panel_event_specialpass_all_1.luac` (client 3482); the free item is the
`isPass` `false` slot because every step's second item is the better one
(Black Friday Box I and II, a 7-day Value Pack and a Classic Outfit Box).
The three times are named by the texts the row indexes: the period text
holds the dates of `start_time` and `end_time`, and every description
ends with the pass sale period, whose last day is `sale_end_time` on all
31 rows. Pass 5 starts at 2023-08-22 21:01 UTC, the evening before its
text's 23 August; pass 16 ends a week after its text's 27 November 2025.

## Notes

- Client 2107 has 1 pass, 2519 has 9, 2765 has 12 (Layout 1); 3002 has
  15, 3251 has 18 and 3474 and 3482 have 31 (Layout 2). Client 3251
  is the first with a type other than Daily (one Solare pass).
- The handler (`_bss/specialpass/`) shows one row per step, in file order:
  the pass key, type, title, the three times, the step number, Pass
  Points, both reward items with their counts and the description.

## Open Questions

### What the u32 Values After the Tracks Hold

`unknown_after_tracks` grows with the content types in use. Client 3251
(Daily and Solare) holds `0 0 0 0 1 | 0 0 0 0 5 2 3`, client 3482 (all
five types) `0 0 0 0 0 0 0 1 | 0 0 0 0 0 0 0 5 2 3 | 0 0 0 0 0 0 0 1 |
0 0 0 0 0 0 0 1 | 0 0 0 0 0 0 0 1`: one group per type in value order,
each a run of zeros (4 on 3251, 7 on 3482) and a `1`, the Solare group
`5 2 3`. Pass Points per action (one per day, monster, barter or
gathering, and per Solare result) fit the values, but no Lua getter reads
them and the zero runs do not match a count in the file.

### What `unknown_2a` and Layout 1 `unknown_26` Hold

The u8 at the end of a Layout 2 row is `0` on all 31 rows; Layout 1 has a
u32 `0` where Layout 2 has `content_type`. Whether the old u32 is the
content type before Daily was numbered `1` is open.
