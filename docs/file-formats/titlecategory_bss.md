# titlecategory.bss

Maps title IDs to their category. A flat array of fixed-size records with no
file header — record count is derived from file size.

---

## Structure

### Record (8 bytes, repeated for each entry)

| Offset | Type | Field       | Notes                          |
| ------ | ---- | ----------- | ------------------------------ |
| 0x00   | u32  | title_id    | Unique title identifier        |
| 0x04   | u32  | category_id | Category code (see table below)|

Record count = `file_size / 8`.

### Known category IDs

| ID | Name       |
| -- | ---------- |
| 0  | World      |
| 1  | Combat     |
| 2  | Life Skill |
| 3  | Fishing    |

---

## Notes

- Little-endian throughout.
- No file header — parsing relies solely on file size being a multiple of 8.
- Category IDs outside 0–3 are decoded as `Unknown (N)` by the preview handler.
