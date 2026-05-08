# `titlebufflist.dbss` Format

## Purpose

Stores the title collection bonus/effect list shown in-game under **Title Effects**. Each record maps a required title count threshold to the bonus effects unlocked at that tier. This file is **not** responsible for individual title name colors.

Example:

```text
Acquire x50: Luck +1
Acquire x60: Luck +2
Acquire x70: Luck +2 / Max Energy +1
```

## Graph

### Tags

- file format
- dbss
- title
- title buff
- title effects
- collection bonus

### Connections

- [titlebufflistoffset.dbss](#titlebufflistoffsetdbss) — required; provides block offsets and sizes
- [title.dbss](title_dbss.md) — source of individual title data
- [languagedata_en.loc](languagedata_loc.md) — English multiline Title Effects tooltip (str_type=37)

---

## Companion Files

| File                       | Required | Role                               |
| -------------------------- | -------- | ---------------------------------- |
| `titlebufflistoffset.dbss` | Required | Provides block offsets and sizes   |
| `languagedata_en.loc`      | Optional | English display text for each tier |

All multi-byte values are little-endian.

---

## File Layout

### titlebufflistoffset.dbss

- 4-byte header: u32 entry count
- Repeating 12-byte records:

| Offset  | Type | Name     | Description                           |
| ------- | ---- | -------- | ------------------------------------- |
| `+0x00` | u32  | entry_id | Zero-based buff/effect row ID         |
| `+0x04` | u32  | offset   | Byte offset into `titlebufflist.dbss` |
| `+0x08` | u32  | size     | Block size in bytes                   |

Observed entry IDs are zero-based and align with `internal_id` inside each block.

---

## Record Structure

### Block Layout

| Offset   | Type   | Name            | Description                                                      | Confidence |
| -------- | ------ | --------------- | ---------------------------------------------------------------- | ---------- |
| `+0x00`  | u32    | internal_id     | Zero-based buff/effect row ID — same as the offset file entry_id | High       |
| `+0x04`  | u32    | required_titles | Title count to unlock this tier                                  | High       |
| `+0x08+` | varies | text_payload    | Embedded UTF-16LE Korean effect text and PAColor markup          | High       |

#### internal_id / Display Level

The offset file's `entry_id` and block `internal_id` represent the same row. Display level is usually `internal_id + 1`:

| Display Level | internal_id |
| ------------- | ----------- |
| 1             | 0           |
| 2             | 1           |
| 3             | 2           |

#### required_titles Examples

| internal_id | required_titles | Meaning            |
| ----------- | --------------- | ------------------ |
| 0           | 50              | Acquire x50 titles |
| 1           | 60              | Acquire x60 titles |
| 2           | 70              | Acquire x70 titles |

---

## Embedded Korean Text

The DBSS block contains Korean text directly:

```text
칭호 50개 습득 : 행운 잠재력 <PAColor0xFF00BAFF>+1단계<PAOldColor>
```

Decode the payload as UTF-16LE. The leading binary/header bytes should not be displayed as text.

### PAColor Tags

Effect values use PA color markup:

```text
<PAColor0xFF00BAFF>+1단계<PAOldColor>
```

| Color      | Meaning                                           |
| ---------- | ------------------------------------------------- |
| `FF00BAFF` | Blue/cyan highlight used for numeric bonus values |

These tags color the bonus numbers in the Title Effects tooltip, not individual title name colors.

---

## English Text

The official English text appears in `languagedata_en.loc` as one multiline tooltip entry containing all Title Effects lines:

```text
str_type: 37, str_id1: 3723587620, str_id2: 1, str_id3: 0, str_id4: 0
```

Example content:

```text
Acquire x50: Luck <PAColor0xff00baff>+1<PAOldColor>
Acquire x60: Luck <PAColor0xff00baff>+2<PAOldColor>
Acquire x70: Luck <PAColor0xff00baff>+2<PAOldColor> / Max Energy <PAColor0xff00baff>+1<PAOldColor>
```

Recommended lookup:

1. Parse `languagedata_en.loc`.
2. Find the multiline entry containing `Acquire x50: Luck`.
3. Split it into lines.
4. Map each line by the `Acquire x{required_titles}:` prefix.
5. Use `required_titles` from the DBSS row to select the matching English line.

---

## Suggested UI Layout

| Column          | Source                                                    |
| --------------- | --------------------------------------------------------- |
| Level           | `internal_id + 1`                                         |
| Required Titles | `required_titles`                                         |
| Text            | Parsed from `languagedata_en.loc` by required title count |
| Offset          | From offset file                                          |

---

## Reference Data

### Known Effect Progression

| Required Titles | Effects                                               |
| --------------- | ----------------------------------------------------- |
| 50              | Luck +1                                               |
| 60              | Luck +2                                               |
| 70              | Luck +2 / Max Energy +1                               |
| 80              | Luck +2 / Max Energy +2                               |
| 90              | Luck +2 / Max Energy +3                               |
| 100             | Luck +2 / Max Energy +3 / EXP +3%                     |
| 150             | Luck +3 / Max Energy +3 / EXP +3%                     |
| 200             | Luck +3 / Max Energy +4 / EXP +3%                     |
| 300             | Luck +3 / Max Energy +4 / EXP +6% / Max Stamina +50   |
| 400             | Luck +3 / Max Energy +5 / EXP +6% / Max Stamina +50   |
| 500             | Luck +3 / Max Energy +5 / EXP +9% / Max Stamina +50   |
| 600             | Luck +3 / Max Energy +5 / EXP +9% / Max Stamina +100  |
| 700             | Luck +3 / Max Energy +6 / EXP +9% / Max Stamina +100  |
| 800             | Luck +3 / Max Energy +6 / EXP +9% / Max Stamina +150  |
| 900             | Luck +3 / Max Energy +6 / EXP +12% / Max Stamina +150 |
| 1,000           | Luck +3 / Max Energy +7 / EXP +12% / Max Stamina +150 |
| 1,500           | Luck +3 / Max Energy +8 / EXP +12% / Max Stamina +150 |
| 2,000           | Luck +3 / Max Energy +8 / EXP +12% / Max Stamina +200 |

---

## Open Questions

### Unknown Payload Bytes

Exact meaning of the bytes after `required_titles` (`+0x08`) and before the first visible Korean text marker.
