# `growthpassquestlist.bss` Format

## Purpose

Quest list of the Growth Pass window (`panel_window_growthpass*.luac`). Same layout and handler as [`allquestlist.bss`](allquestlist_bss.md): a `PABR` list of packed quest IDs.

Example (client 3464):

```text
quest 4464 / 1 -> [Main] Complete Embarking on an Adventure
quest 4472 / 1 -> [Olvia Academy] Academy Enrollment
```

All multi-byte values are little-endian.

## File Layout

### Header (8 bytes)

| Offset  | Type  | Field | Notes             |
| ------- | ----- | ----- | ----------------- |
| `+0x00` | u8[4] | magic | `PABR` (ASCII)    |
| `+0x04` | u32   | count | Number of entries |

### Entry (4 bytes, repeated `count` times)

| Offset  | Type | Field           | Notes                                                       |
| ------- | ---- | --------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | packed_quest_id | `(quest_id << 16) \| quest_chain_id`; LOC type 18 title key |

### Trailer (12 bytes)

| Offset  | Type | Field          | Notes                                     |
| ------- | ---- | -------------- | ----------------------------------------- |
| `+0x00` | u32  | reserved_a     | `0`                                       |
| `+0x04` | u32  | end_of_entries | `8 + count * 4`, where the trailer starts |
| `+0x08` | u32  | reserved_b     | `0`                                       |

## Quest Chains

On client 3464 the list holds 224 quests in nine chains, 4464 to 4472, and every quest of those chains that `allquestlist.bss` has. Some chains skip sub IDs (4471 runs to 47 with 20 quests); the skipped ones are not in `quest.dbss` either. Titles open with a topic tag such as `[Main]`, `[Buffs]`, `[Worker]`, `[Quest]`, `[Menu]` or `[Olvia Academy]`.

| Chain (client 3464) | Quests | Quest 1                                                 |
| ------------------- | ------ | ------------------------------------------------------- |
| 4464                | 28     | [Main] Complete Embarking on an Adventure               |
| 4465                | 28     | [Buffs] Eat a Simple Cron Meal                          |
| 4466                | 28     | [Buffs] Eat a Seafood Cron Meal                         |
| 4467                | 26     | [Worker] Hire a Worker in Velia and Check Worker List   |
| 4468                | 25     | [Quest] Complete Bee Hurts Farm                         |
| 4469                | 16     | [Quest] Complete Have You Ever... Tamed a Horse?        |
| 4470                | 40     | [Menu] Chat Groups                                      |
| 4471                | 20     | [Quest] Complete Old Moon Guild's Trade Offer           |
| 4472                | 13     | [Olvia Academy] Academy Enrollment                      |

The window does not read this list by index. It walks the categories of [`growthpasscategory.dbss`](growthpasscategory_dbss.md) and places each quest in a grid cell of the category's layout in [`uigrowthpasslayout.bss`](uigrowthpasslayout_bss.md). Each category names one quest chain, and its grid holds that chain's quests. On client 3464 only two chains have a category: 4470 (category 7, Game Tips, quests 1 to 40) and 4472 (category 9, HYPERBOOST, quests 1 to 13). The other seven chains are in this list with no category or grid. LOC type 107 still names categories 1 to 9.

## Notes

- Decompressed size on client 3464: `916` bytes, `8 + 224 * 4 + 12`.
- calpheonlabs (`growthpassquestlist.bss.mdx`) reads the same layout: a u32-counted array of (u16 quest group, u16 quest number) and a 12-byte pad.
- `test_pass_lists.py` checks this file next to the three [Black Spirit Pass lists](seasonpassquestlist_bss.md).
