# `seasonreward.dbss` Format

## Purpose

The rewards of the Season server: one row per season with its number, the
`GAME` string sheet keys of its name and description, and the items a
graduated Season character picks from. `panel_window_seasonreward_all.luac`
lists the seasons (`ToClient_getSeasonCount()`), reads a row through
`getSeasonRewardStaticStatus(seasonNo)` (`getSeasonName()`,
`getDescription()`) and its items through
`ToClient_getRewardByIndex(seasonNo, index)`. Season `254` is the
repeatable reward (`_seasonNoRewardRepeatable = 254` in the same Lua).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes                  |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | -------------------------- |
| 1      | 1485 and later | 3482    | `seasonreward.dbss` | 1,749 | 15 Row  | 115 to 119, 116 on average |

| Layout | File                | Known            | Unknown    |
| ------ | ------------------- | ---------------- | ---------- |
| 1      | `seasonreward.dbss` | 1,749 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                       |
| --------------------- | -------- | -------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Season names and descriptions (LOC type 37 under the key hash), item names (type 0) |

The handler hashes each key itself (`_common/string_hash.py`), so it needs
no `stringtable.bss`. All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 21 bytes + keys and rewards)

| Offset                 | Type              | Field            | Notes                                                                                   |
| ---------------------- | ----------------- | ---------------- | --------------------------------------------------------------------------------------- |
| `+0x00`                | u8                | season_no        | Row key; `1` to `14` and `254` on client 3482                                            |
| `+0x01`                | str16             | season_name_key  | `GAME` sheet key of the season name, `LUA_SEASONSERVER_NAME<n>`; `getSeasonName()`       |
| `season_name_key+0x00` | str16             | description_key  | `GAME` sheet key of the reward condition text, `LUA_SEASONSERVER_DESC<n>`; `getDescription()` |
| `description_key+0x00` | u32               | reward_count     | Number of `reward_item_keys`; `ToClient_getRewardCountBySeason(seasonNo)`                |
| `description_key+0x04` | u32[reward_count] | reward_item_keys | Packed item keys (`enchant_level << 24 \| item_id`); `ToClient_getRewardByIndex()`        |

## Seasons

Client 3482; the names are the LOC type 37 text of `season_name_key`. Every
row holds `LUA_SEASONSERVER_DESC14` ("Reach Lv. 10, get from ... Evergreen
Season Pass"); seasons `1` to `14` name `LUA_SEASONSERVER_NAME<n+1>` and
season `254` names `LUA_SEASONSERVER_NAME254`.

| Season | Name                          | Rewards                                |
| ------ | ----------------------------- | -------------------------------------- |
| 1      | Summer Season                 | Capotia Earring (5), Capotia Ring (5)  |
| 2      | Autumn Season                 | Perilla's Star                         |
| 3      | Winter Season                 | Capotia Belt (5)                       |
| 4      | 2021 Summer Season            | Capotia Necklace (5)                   |
| 5      | 2021 Season+                  | Advice of Valks (+100)                 |
| 6 to 12 | 2021 Winter Season to 2023 Summer Season | Advice of Valks (+100) Box  |
| 13     | 2023 Evergreen Season         | Advice of Valks (+150)                 |
| 14     | Evergreen Season Special Gift | Advice of Valks (+150) Box             |
| 254    | [Repeat] Season Special Gift  | Advice of Valks (+100) Box             |

## Field Names

The `SeasonReward` sheet (`SeasonNo`, `ItemKey`, `EnchantLevel`, one sheet
row per item) and the `SeasonName` sheet (`SeasonNo`, one key column per
service, `Desc`) of a private server's `DataSheets.bexcel` on client 1784
match the file of that client on all 5 seasons: the 6 items with their
levels, the `NA_REAL` name key (season 1 names `LUA_SEASONSERVER_NAME2`
there too) and the `Desc` key (`LUA_SEASONSERVER_DESC1` to `DESC5`). The
getters come from `panel_window_seasonreward_all_1.luac` and `_2.luac` of
client 3482.

## Notes

- A quest reward of type `18` (`eRewardSeasonReward`,
  [`quest.dbss`](quest_dbss.md) Reward Entry) carries a `season_no`.
- The window lists seasons `1` to `count - 1` and then `254` when
  `ToClient_isRewardRepeatableSeasonExist()` is true; a season whose reward
  was taken is locked, except `254`.
- The handler (`_dbss/seasonreward/`) shows one row per season with the
  LOC name and description of the two keys (the key itself when LOC has
  none) and the reward items with their icons and levels.
