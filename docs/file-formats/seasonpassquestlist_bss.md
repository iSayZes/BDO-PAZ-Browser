# `seasonpassquestlist.bss` Format

## Purpose

Quest lists of the Black Spirit Pass (season pass) window. Three files share one layout, the packed quest ID list of [`allquestlist.bss`](allquestlist_bss.md), and one handler:

| File                               | Holds                                                         |
| ---------------------------------- | ------------------------------------------------------------- |
| `seasonpassquestlistfornormal.bss` | The free quest of each pass row                               |
| `seasonpassquestlistforcash.bss`   | The Black Spirit Pass (premium) quest of each pass row        |
| `seasonpassquestlist.bss`          | Both: every quest of the two files above, in another order    |

Example (client 3464):

```text
fornormal: quest 50000 / 1 -> [Summer Season] Leveling Up, One Step at a Time! 1
forcash:   quest 50000 / 2 -> [Summer Season] Leveling Up, One Step at a Time! 1 (Black Spirit Pass)
```

All multi-byte values are little-endian.

## File Layout

### Header (8 bytes)

| Offset  | Type  | Field | Notes                                   |
| ------- | ----- | ----- | --------------------------------------- |
| `+0x00` | u8[4] | magic | `PABR` (ASCII)                          |
| `+0x04` | u32   | count | Number of entries                       |

### Entry (4 bytes, repeated `count` times)

| Offset  | Type | Field           | Notes                                                       |
| ------- | ---- | --------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | packed_quest_id | `(quest_id << 16) \| quest_chain_id`; LOC type 18 title key |

### Trailer (12 bytes)

| Offset  | Type | Field          | Notes                                  |
| ------- | ---- | -------------- | -------------------------------------- |
| `+0x00` | u32  | reserved_a     | `0`                                    |
| `+0x04` | u32  | end_of_entries | `8 + count * 4`, where the trailer starts |
| `+0x08` | u32  | reserved_b     | `0`                                    |

## Pass Rows

`panel_window_blackspiritpass_1.luac` walks `ToClient_SeasonPassQuestCount()` rows and asks for two quests per row: `ToClient_GetSeasonPassQuestAt(listIdx, __eSeasonPassQuest_Normal)` for the free reward and `ToClient_GetSeasonPassQuestAt(listIdx, __eSeasonPassQuest_SeasonPass)` for the premium reward. A premium reward counts as claimable only when the player's `isSeasonPass()` is true (`panel_window_blackspiritpass_2.luac`). The two type values match the two files:

- Each free quest `(chain, n)` in `fornormal` has its premium quest `(chain, n + 1)` in `forcash`. Free quests have odd sub IDs, premium quests even ones.
- Every `forcash` title ends in `(Black Spirit Pass)`; no `fornormal` title does.
- `seasonpassquestlist.bss` holds exactly the quests of both files, none twice.

The file order is not the row order: index `i` of `fornormal` and index `i` of `forcash` belong to the same row on only 6 of 205 indexes (client 3464).

On client 3464 both side files hold 205 quests and the full list 410, all with a LOC type 18 title. The quest chains fall in three blocks: 50000 to 50057 (titles start `[Summer Season]`), 50100 to 50146, and 50150 to 50152 (74, 74 and 52 quests in the full list).

## Suggested UI Layout

Same as [`allquestlist.bss`](allquestlist_bss.md):

| Column  | Type | Notes                                                                    |
| ------- | ---- | ------------------------------------------------------------------------ |
| Main ID | num  | `packed_quest_id & 0xFFFF`; LOC type 18 `str_id1`                         |
| Sub ID  | num  | `packed_quest_id >> 16`; LOC type 18 `str_id2`                            |
| Icon    | text | Quest icon resolved from `packed_quest_id` through the quest icon index  |
| Title   | text | LOC type 18 row with matching main/sub ID and `str_id4=0`, in its game colours |

The title already names the track (`(Black Spirit Pass)`), so there is no separate Free / Premium column.

## Notes

- Decompressed sizes on client 3464: `1,660` bytes for `seasonpassquestlist.bss`, `840` bytes for each side file; all match `8 + count * 4 + 12`.
- calpheonlabs (`seasonpassquestlist.bss.ts`, capture PAZ 3595) reads the same layout: a u32-counted array of (u16 quest group, u16 quest number) and a 12-byte pad. It names the cash file's quests "paid Season Pass quest IDs".
- `seasonpass.dbss` (7.6 KB, not documented yet) is the next file to check for the row order and the season period.
- `test_pass_lists.py` asserts that the full list is the two side files together and that every free quest has its premium quest at sub ID + 1.

## Open Questions

### Row Order

The window's row order (`listIdx`) does not follow the order of any of the three files. `seasonpass.dbss` is the first candidate for it.
