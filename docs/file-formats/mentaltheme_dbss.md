# `mentaltheme.dbss` Format

## Purpose

Defines the knowledge group/category tree. Each theme record stores a group ID, Korean inline group name, parent group, energy reward thresholds, direct knowledge entries, and child theme IDs.

Example:

```text
theme_id: 10319 -> parent: 10030 -> "Refugee Camp"
entries: 4327, 4325, 4324, ... -> knowledge entries in that group
```

## Graph

### Tags

- file format
- dbss
- knowledge

### Connections

- [mentalcard.dbss](mentalcard_dbss.md) - maps knowledge entry IDs to the same theme IDs
- [languagedata_en.loc](languagedata_loc.md) - English theme names (`str_type=9`) and knowledge entry names (`str_type=34`)

---

## Companion Files

| File                     | Required | Role                                                  |
| ------------------------ | -------- | ----------------------------------------------------- |
| `mentalthemeoffset.dbss` | Required | Provides theme ID, payload offset, and payload size   |
| `mentalcard.dbss`        | Optional | Confirms entry ID -> theme ID membership              |
| `languagedata_en.loc`    | Optional | Provides localized English names for themes/entries   |

All multi-byte values are little-endian.

---

## File Layout

### mentalthemeoffset.dbss

| Offset  | Type | Name  | Description       |
| ------- | ---- | ----- | ----------------- |
| `+0x00` | u32  | count | Number of records |
| `+0x04` | ...  | rows  | 10-byte rows      |

### Offset Row (10 bytes, repeated `count` times)

| Offset  | Type | Name           | Description                                                       |
| ------- | ---- | -------------- | ----------------------------------------------------------------- |
| `+0x00` | u16  | theme_id       | Knowledge group/category ID                                       |
| `+0x02` | u32  | payload_offset | Byte offset into `mentaltheme.dbss`; points to the duplicate ID    |
| `+0x06` | u32  | payload_size   | Size of the payload at `payload_offset`, excluding the 2-byte lead |

### mentaltheme.dbss

| Offset  | Type | Name  | Description                                      |
| ------- | ---- | ----- | ------------------------------------------------ |
| `+0x00` | u32  | count | Number of records; matches `mentalthemeoffset`   |
| `+0x04` | ...  | data  | Record stream: 2-byte lead ID, then the payloads |

Each payload is preceded by a 2-byte `theme_id` lead in the main stream. The offset file points two bytes later, to a payload that begins with the same `theme_id` again.

---

## Record Structure

### Theme Payload (variable size)

| Offset        | Type             | Name            | Description                                                |
| ------------- | ---------------- | --------------- | ---------------------------------------------------------- |
| `+0x00`       | u16              | theme_id        | Knowledge group/category ID; matches offset row            |
| `+0x02`       | u16              | name_len        | Number of UTF-16LE code units in `name_ko`                 |
| `+0x04`       | u32              | reserved_0      | Always observed as `0`                                     |
| `+0x08`       | u16              | reserved_1      | Always observed as `0`                                     |
| `+0x0A`       | utf16le[]        | name_ko         | Inline Korean theme name, `name_len * 2` bytes             |
| after name    | Theme Stats      | stats           | Parent and energy reward thresholds                        |
| after stats   | u32[]            | entries         | Direct knowledge entry IDs                                 |
| after entries | Child Theme List | children        | Direct child theme IDs                                     |

### Theme Stats (23 bytes)

| Offset  | Type | Name            | Description                                           |
| ------- | ---- | --------------- | ----------------------------------------------------- |
| `+0x00` | u16  | parent_id       | Parent theme ID, or `0` for root themes               |
| `+0x02` | u16  | increase_wp     | First energy reward amount                            |
| `+0x04` | u32  | need_count      | Entries needed for first reward                       |
| `+0x08` | u16  | increase_wp_2   | Second energy reward amount                           |
| `+0x0A` | u32  | need_count_2    | Entries needed for second reward                      |
| `+0x0E` | u8   | unknown_flag    | Unknown; observed `0` or `1` in common records         |
| `+0x0F` | u32  | unknown_value   | Unknown; often `0`, otherwise small UI-like values    |
| `+0x13` | u32  | entry_count     | Number of direct `entries` that follow                 |

### Entries (`entry_count * 4` bytes)

| Offset  | Type | Name     | Description                                      |
| ------- | ---- | -------- | ------------------------------------------------ |
| `+0x00` | u32  | entry_id | Knowledge entry ID; LOC `str_type=34`, `str_id1` |

### Child Theme List (variable size)

| Offset                 | Type  | Name        | Description                                      |
| ---------------------- | ----- | ----------- | ------------------------------------------------ |
| `+0x00`                | u32   | child_count | Number of direct child theme IDs                 |
| `+0x04`                | u16[] | child_ids   | Child theme IDs in binary/UI order               |
| `+0x04 + child_count*2` | u32   | terminator  | Always observed as `0`                           |

---

## Confirmed Examples

Sample records confirmed from `mentaltheme.dbss`, `mentalthemeoffset.dbss`, `mentalcard.dbss`, and LOC lookups:

| Theme ID | LOC Name              | Parent  | Energy Reward 1 | Energy Reward 2  | Entry Count |
| -------- | --------------------- | ------- | --------------- | ---------------- | ----------- |
| `10001`  | Ecology               | `0`     | `—`             | `+0 at 10 entries` | `0`       |
| `10030`  | Ecology of Calpheon   | `10001` | `—`             | `+0 at 10 entries` | `0`       |
| `10319`  | Refugee Camp          | `10030` | `+1 at 5 entries` | `+2 at 13 entries` | `14`     |
| `10318`  | Quarry                | `10030` | `+1 at 6 entries` | `+2 at 15 entries` | `15`     |
| `15000`  | Fish Species          | `10001` | `+2 at 3 entries` | `+2 at 13 entries` | `3`      |

---

## Suggested UI Layout

| Column          | Type | Notes                                                     |
| --------------- | ---- | --------------------------------------------------------- |
| Theme ID        | num  | Primary key                                               |
| Name            | text | LOC `str_type=9`; fallback to `name_ko`                   |
| Parent ID       | num  | Link to parent theme                                      |
| Parent Name     | text | LOC `str_type=9` for `parent_id`                          |
| Energy Reward 1 | text | Render as `+{increase_wp} at {need_count} entries`        |
| Energy Reward 2 | text | Render as `—` when it duplicates reward 1; otherwise `+{increase_wp_2} at {need_count_2} entries` |
| Entries         | num  | `entry_count`                                             |
| Children Groups | num  | `child_count`                                             |

---

## Notes

- `mentaltheme.dbss` and `mentalthemeoffset.dbss` both start with count `902`.
- `mentalthemeoffset.dbss` uses 10-byte rows, unlike the 12-byte offset records used by `mentalcardoffset.dbss` and `knowledgelearningoffset.dbss`.
- Direct `entries` match `mentalcard.dbss` memberships and LOC `str_type=34` names.
- `child_ids` are stored in binary/UI order.
- The DBSS files should be treated as the source of truth for this format.

---

## Open Questions

### Unknown Stats Tail

The 5 bytes at stats offsets `+0x0E..+0x12` look like `unknown_flag: u8` plus `unknown_value: u32`; values may be UI/display metadata, but this is not confirmed.
