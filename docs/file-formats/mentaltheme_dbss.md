# `mentaltheme.dbss` Format

## Purpose

Defines the knowledge group/category tree. Each theme record stores a group ID, Korean inline group name, parent group, energy reward thresholds, the theme's bookshelf item, direct knowledge entries, and child theme IDs.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes   | Records                       | Row bytes                   |
| ------ | -------------- | ------- | ------------------------ | ------- | ----------------------------- | --------------------------- |
| 1      | 3473 and later | 3473    | `mentaltheme.dbss`       | 108,785 | 939 Theme Payload, 939 Record | 45 to 1,587, 114 on average |
| 1      | 3473 and later | 3473    | `mentalthemeoffset.dbss` | 9,394   | 939 Offset Row                | 10                          |

| Layout | File                     | Known             | Unknown        |
| ------ | ------------------------ | ----------------- | -------------- |
| 1      | `mentaltheme.dbss`       | 104,090 B (95.7%) | 4,695 B (4.3%) |
| 1      | `mentalthemeoffset.dbss` | 9,394 B (100.0%)  | 0 B (0.0%)     |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                  |
| ------------------------ | -------- | ----------------------------------------------------- |
| `mentalthemeoffset.dbss` | Required | Provides theme ID, payload offset, and payload size   |
| `mentalcard.dbss`        | Optional | Confirms entry ID -> theme ID membership              |
| `languagedata_en.loc`    | Optional | Provides localized English names for themes, entries and bookshelf items |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                            |
| ------- | ------------- | ------- | ------------------------------------------------ |
| `+0x00` | u32           | count   | Number of records; matches `mentalthemeoffset`   |
| `+0x04` | Record[count] | data    | Record stream: 2-byte lead ID, then the payloads; see Record |

Each payload is preceded by a 2-byte `theme_id` lead in the main stream. The offset file points two bytes later, to a payload that begins with the same `theme_id` again.

`name_len` is an `i64` code-unit count, the same string prefix used by `mentalcard.dbss`. The field was earlier read as a u16 followed by six reserved zero bytes; bytes `+0x04..+0x09` are zero on all 931 records, so both reads give the same length. The `i64` reading matches the notes of [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor), which call `theme_id` and `parent_id` `themeKey` and `parentTheme`.

### Record (variable: 2 bytes + payload)

| Offset  | Type          | Field   | Notes                                                    |
| ------- | ------------- | ------- | -------------------------------------------------------- |
| `+0x00` | u16           | lead_id | Equals the payload's `theme_id`                          |
| `+0x02` | Theme Payload | payload | `payload_size` bytes; the offset row points at this field |

### Theme Payload (variable: 41 bytes + name and lists)

The fields from `parent_id` to `entry_count` are the 23-byte theme stats; their offsets count from the end of `name_kr`.

| Offset           | Type             | Field                   | Notes                                                                                    |
| ---------------- | ---------------- | ----------------------- | ---------------------------------------------------------------------------------------- |
| `+0x00`          | u16              | theme_id                | Knowledge group/category ID; matches offset row                                          |
| `+0x02`          | str16            | name_kr                 | Inline Korean theme name; the i64 count is `name_len`, the number of UTF-16LE code units |
| `name_kr+0x00`   | u16              | parent_id               | Parent theme ID, or `0` for root themes                                                  |
| `name_kr+0x02`   | u16              | increase_wp             | First energy reward amount                                                               |
| `name_kr+0x04`   | u32              | need_count              | Entries needed for first reward                                                          |
| `name_kr+0x08`   | u16              | increase_wp_2           | Second energy reward amount                                                              |
| `name_kr+0x0A`   | u32              | need_count_2            | Entries needed for second reward                                                         |
| `name_kr+0x0E`   | u8               | unknown_0e              | Observed `0` or `1`; see Open Questions                                                  |
| `name_kr+0x0F`   | u32              | bookshelf_item          | Item ID of the theme's bookshelf (LOC type 0), or `0`                                    |
| `name_kr+0x13`   | u32              | entry_count             | Number of direct `entries` that follow                                                   |
| `name_kr+0x17`   | u32[entry_count] | entries                 | Direct knowledge entry IDs; LOC `str_type=34`, `str_id1`                                 |
| `entries+0x00`   | u32              | child_count             | Number of direct child theme IDs                                                         |
| `entries+0x04`   | u16[child_count] | child_ids               | Child theme IDs in binary/UI order                                                       |
| `child_ids+0x00` | u32              | unknown_after_child_ids | Always observed as `0`                                                                   |

Earlier versions of this doc called `unknown_0e` `unknown_flag`, `bookshelf_item` `unknown_value`, then `unknown_0f`, and `unknown_after_child_ids` `terminator`.

The entries are stored in the order the Knowledge window lists them. Checked in game (2026-09-28) on People of Olvia Academy (`145`): all 20 entries show in stored order, from Cedrio to Gray Biants, which is not card ID order (Merv `14703` second, Justin Bartali `14675` second to last).

### `mentalthemeoffset.dbss`

| Offset  | Type              | Field | Notes             |
| ------- | ----------------- | ----- | ----------------- |
| `+0x00` | u32               | count | Number of records |
| `+0x04` | Offset Row[count] | rows  | See Offset Row    |

### Offset Row (10 bytes)

| Offset  | Type | Field          | Notes                                                             |
| ------- | ---- | -------------- | ----------------------------------------------------------------- |
| `+0x00` | u16  | theme_id       | Knowledge group/category ID                                       |
| `+0x02` | u32  | payload_offset | Byte offset into `mentaltheme.dbss`; points to the duplicate ID    |
| `+0x06` | u32  | payload_size   | Size of the payload at `payload_offset`, excluding the 2-byte lead |

## Bookshelf Item

`bookshelf_item` names an item whose LOC type 0 name is "Bookshelf with Knowledge on" plus the theme's subject: Refugee Camp (`10319`) holds `2532` "Bookshelf with Knowledge on Monsters of the Refugee Camp", Quarry (`10318`) holds `2531`, Beasts (Balenos) (`10101`) holds `2501` "Bookshelf with Knowledge on Beast Monsters (Balenos)". The item's description (LOC type 0 `str_id4=1`) reads "A bookshelf filled with knowledge on monsters in the Refugee Camp."

On client 3464, 33 themes carry a bookshelf item and the rest store `0`. The items are `2501` to `2533`, one per theme, in theme ID order: 4 themes under Ecology of Eastern Balenos (`10010`), 11 under Ecology of Serendia (`10020`), 17 under Ecology of Calpheon (`10030`) and Steppe (Kamasylvia) (`10601`) under Ecology of Kamasylvia (`10065`). All 33 have `unknown_0e = 1`. calpheonlabs reads the field the same way (`bookshelfItemId`).

## Confirmed Examples

Sample records confirmed from `mentaltheme.dbss`, `mentalthemeoffset.dbss`, `mentalcard.dbss`, and LOC lookups:

| Theme ID | LOC Name              | Parent  | Energy Reward 1 | Energy Reward 2  | Entry Count |
| -------- | --------------------- | ------- | --------------- | ---------------- | ----------- |
| `10001`  | Ecology               | `0`     | `-`             | `+0 at 10 entries` | `0`       |
| `10030`  | Ecology of Calpheon   | `10001` | `-`             | `+0 at 10 entries` | `0`       |
| `10319`  | Refugee Camp          | `10030` | `+1 at 5 entries` | `+2 at 13 entries` | `14`     |
| `10318`  | Quarry                | `10030` | `+1 at 6 entries` | `+2 at 15 entries` | `15`     |
| `15000`  | Fish Species          | `10001` | `+2 at 3 entries` | `+2 at 13 entries` | `3`      |

## Notes

- `mentaltheme.dbss` and `mentalthemeoffset.dbss` both start with the same count: `939` after the 2026-09-27 client update, `931` before it, `902` in the test fixture.
- `mentalthemeoffset.dbss` has no `PABR` magic and no trailer; it ends exactly at `4 + count * 10`.
- `parent_id` links form a tree: 11 roots (`parent_id = 0`, e.g. `1` People, `5001` Topography, `10001` Ecology, `10399` None), maximum depth 3, no cycles, and every parent exists. The 920 non-root themes each appear exactly once in their parent's `child_ids`.
- The direct `entries` of all themes together list each of the 12,502 cards once, and each listed card's u16 `theme_id` in `mentalcard.dbss` names the theme that lists it.
- All 931 themes have an LOC `str_type=9` name; LOC has 12 more type 9 IDs that match no theme.
- `mentalthemeoffset.dbss` uses 10-byte rows, unlike the 12-byte offset records used by `mentalcardoffset.dbss` and `knowledgelearningoffset.dbss`.
- `child_ids` are stored in binary/UI order.
- The Knowledge window (client Lua `panel_knowledge_main`) lists a root only when its `circularColorValue` table has a colour for the key: `1`, `5001`, `5020`, `10001`, `20001`, `25001`, `30001`, `31300` and `31310`. The other two roots, `10399` None and `10320` Bosses (Calpheon), have no colour and are not listed. Under a listed root the window adds every child theme, then the theme's cards.
- The window appends `getIncreaseWp() / getMaxIncreaseWp()` to a theme's name (`Lua_Knowledge_TalkingPowerUp`). Read as the two tiers, `increase_wp_2` is the theme's total energy, not an amount on top of `increase_wp`: Refugee Camp (`10319`, +1 at 5, +2 at 13) reads `x/2`.
- "People of the Black Desert" (`19`) and "First Mate" (`33`, child `295`) are children of Characters (`1`) here, but the Knowledge window does not show them (in-game check 2026-10-13), and `panel_knowledge_main` has no filter for them. No field in this file marks them. Theme `19` holds retired NPCs (Eden Marsella, Lavodhim), the crop cards (`7236` to `7255`, `7821` to `7827`), cards without an LOC name and card `19` "NPC Pathfind Preventive Knowledge"; `33` holds one card without an LOC name.
- The DBSS files should be treated as the source of truth for this format.

## Open Questions

### `unknown_0e` Meaning

`unknown_0e` is a u8 at stats offset `+0x0E`, `0` or `1`. On client 3464 it is `1` on 232 themes (94 of them under Trade), the 33 themes with a `bookshelf_item` among them. calpheonlabs reads it as a switch for the C/B/A/A+/S knowledge grades; that reading is not confirmed here. The Knowledge window Lua (`panel_knowledge_main`, `panel_window_knowledge_renew`) has no theme getter for it: its only grade switch is the per-user display option `__eKnowledgeGrade`. The value also shows no link to the cards' `unknown_description_kr_02` in `mentalcard.dbss`.
