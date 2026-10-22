# `challengerewardlist.bss` Format

## Purpose

A sorted list of every item a challenge (the Rewards tab of the character
window, `panel_characterinfo_challenge_all`) hands out: one packed item key
(`enchant_level << 24 | item_id`) per entry, ascending, with no
repeats. The challenges themselves are in `challenge.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | -------------- | --------- |
| 1      | 1348 and later | 3482    | `challengerewardlist.bss` | 3,564 | 1 String Table | 4         |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `challengerewardlist.bss` | 3,564 B (100.0%) | 0 B (0.0%) |

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
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset             | Type             | Field        | Notes                                              |
| ------------------ | ---------------- | ------------ | -------------------------------------------------- |
| `+0x00`            | char[4]          | magic        | ASCII `PABR`                                       |
| `+0x04`            | u32              | item_count   | Number of `item_keys`                              |
| `+0x08`            | u32[item_count]  | item_keys    | Packed item keys, ascending; the first is `0`      |
| `item_keys+0x00`   | String Table     | string_table | See String Table                                   |
| `EOF-0x08`         | u32              | table_start  | Offset of the string table, where `item_keys` ends |
| `EOF-0x04`         | u32              | zero         | Always `0`                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The keys are the reward items of the challenges: the `BaseReward` and
`SelectReward` columns (`item(7,0,100);`, item, level, count) of the
`Challenge_Table` sheet of a private server's `DataSheets.bexcel` on client
1784 hold 655 item keys, and 652 of the 653 keys of that client's file are
among them. The one left over is `0`; three sheet keys (`18461`, `50142`,
`750022`) are not in the file. The `WorldChallenge_Table` of a private
server on client 519 has the challenge columns (`Key`, `BaseReward`,
`SelectReward`): it is the twin of `challenge.dbss`, and this file is
derived from its rewards.

## Notes

- On client 3482 the 886 keys hold 885 items (one key is `0`); the
  highest keys are the four Capotia accessories at level 3 (`50343893`
  is Capotia Belt (3)). Client 1784 holds 653 keys, including Tuvala Earring
  at level 5 (`84580190`), which client 3482 no longer lists.
- No Lua function of client 3482 names the file; the challenge window
  reads its rewards through `ToClient_GetChallengeRewardInfoWrapper()`.
- The handler (`_bss/challengerewardlist/`) shows one row per key with
  its item ID, level and the item's icon and name.
