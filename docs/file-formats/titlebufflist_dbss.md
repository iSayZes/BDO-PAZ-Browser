# titlebufflist.dbss Format

## Purpose

Stores the title collection bonus/effect list shown in-game under **Title Effects**.

This file is **not** responsible for individual title name colors.

Example in-game display:

```text
Acquire x50: Luck +1
Acquire x60: Luck +2
Acquire x70: Luck +2 / Max Energy +1
...
```

## Companion Files

- `titlebufflistoffset.dbss` — required. Provides block offsets and sizes.
- `languagedata_en.loc` — optional but useful. Contains the official English multiline Title Effects tooltip.

## Offset File Format: titlebufflistoffset.dbss

| Offset           | Type | Description                      |
| ---------------- | ---- | -------------------------------- |
| `+0x00`          | u32  | Entry count                      |
| `+0x04 + n*0x0C` | u32  | Entry index / id                 |
| `+0x08 + n*0x0C` | u32  | Offset into `titlebufflist.dbss` |
| `+0x0C + n*0x0C` | u32  | Block size                       |

Observed entry IDs are zero-based and align with `u32_00` inside each block.

## Block Structure

Observed block structure:

| Offset   | Type   | Name                               | Description                                           | Confidence |
| -------- | ------ | ---------------------------------- | ----------------------------------------------------- | ---------- |
| `+0x00`  | u32    | internal_id                        | Zero-based buff/effect row id                         | High       |
| `+0x04`  | u32    | required_titles                    | Number of titles required to unlock this effect tier  | High       |
| `+0x08+` | varies | KR text / PA tags / effect payload | Embedded UTF-16 Korean effect text and PAColor markup | High       |

## Key Fields

### internal_id / offset id

The offset-file entry id and block `u32_00` represent the same row, with display level usually shown as `internal_id + 1`.

Example:

| Display Level | internal_id (`u32_00`) |
| ------------- | ---------------------- |
| 1             | 0                      |
| 2             | 1                      |
| 3             | 2                      |

### required_titles

`u32_04` is the title count requirement.

Examples:

| internal_id | required_titles | Meaning            |
| ----------- | --------------- | ------------------ |
| 0           | 50              | Acquire x50 titles |
| 1           | 60              | Acquire x60 titles |
| 2           | 70              | Acquire x70 titles |

## Embedded Korean Text

The DBSS block contains Korean text directly, such as:

```text
칭호 50개 습득 : 행운 잠재력 <PAColor0xFF00BAFF>+1단계<PAOldColor>
```

This can be decoded from the first `<PAColor...` area or by decoding the payload as UTF-16LE. The leading binary/header bytes should not be displayed as text.

## PAColor Tags

The effect values use PA color markup:

```text
<PAColor0xFF00BAFF>+1단계<PAOldColor>
```

Observed color:

| Color      | Meaning                                           |
| ---------- | ------------------------------------------------- |
| `FF00BAFF` | Blue/cyan highlight used for numeric bonus values |

These tags color the **bonus numbers** in the Title Effects tooltip.

They do not control individual title name colors.

## English Text

The official English text is not row-by-row inside `titlebufflist.dbss`.

It appears in `languagedata_en.loc` as one multiline tooltip entries containing all Title Effects lines.

type: 37, id1=3723587620, id2=1, id3=0, id4=0

for example:

```text
Acquire x50: Luck <PAColor0xff00baff>+1<PAOldColor>
Acquire x60: Luck <PAColor0xff00baff>+2<PAOldColor>
Acquire x70: Luck <PAColor0xff00baff>+2<PAOldColor> / Max Energy <PAColor0xff00baff>+1<PAOldColor>
...
```

Recommended lookup:

1. Parse `languagedata_en.loc`.
2. Find the multiline entry containing `Acquire x50: Luck`.
3. Split it into lines.
4. Map each line by the `Acquire x{required_titles}:` prefix.
5. Use `u32_04` from the DBSS row to select the matching English line.

## Recommended Handler Columns

Suggested UI columns:

| Column           | Source                                                    |
| ---------------- | --------------------------------------------------------- |
| Level            | `u32_00 + 1`                                              |
| Required Titles  | `u32_04`                                                  |
| EN Buff Text     | parsed from `languagedata_en.loc` by required title count |
| KR Buff Text     | decoded from DBSS block                                   |
| Offset           | offset file                                               |
| Debug u32 Fields | first few u32 values for investigation                    |

## Example Rows

| Level | Required Titles | EN Meaning                           |
| ----- | --------------- | ------------------------------------ |
| 1     | 50              | Acquire x50: Luck +1                 |
| 2     | 60              | Acquire x60: Luck +2                 |
| 3     | 70              | Acquire x70: Luck +2 / Max Energy +1 |

## Known Effect Progression

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

## Open Questions

- Exact meaning of unknown payload bytes after `u32_04` and before the first visible text marker.
