# titlecategory.bss Format

## Purpose

Maps titles to categories.

## Structure

| Offset | Type | Name        | Description      | Confidence |
| ------ | ---- | ----------- | ---------------- | ---------- |
| +0x00  | u32  | title_id    | Title identifier | High       |
| +0x04  | u32  | category_id | Category         | Medium     |

## Known Categories

| ID  | Name       |
| --- | ---------- |
| 0   | World      |
| 1   | Combat     |
| 2   | Life Skill |
| 3   | Fishing    |

## Notes

- Used to group titles in output JSON

## Open Questions

- None
