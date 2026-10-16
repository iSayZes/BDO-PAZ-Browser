# `titlebufflist.dbss` Format

## Purpose

Stores the title collection bonus/effect list shown in-game under **Title Effects**. Each record maps a required title count threshold to the bonus effects unlocked at that tier. This file is **not** responsible for individual title name colors.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records       | Row bytes                  |
| ------ | -------------- | ------- | -------------------------- | ----- | ------------- | -------------------------- |
| 1      | 1784 and later | 3473    | `titlebufflist.dbss`       | 5,972 | 18 Block      | 140 to 410, 332 on average |
| 1      | 1784 and later | 3473    | `titlebufflistoffset.dbss` | 220   | 18 Offset Row | 12                         |

| Layout | File                       | Known           | Unknown      |
| ------ | -------------------------- | --------------- | ------------ |
| 1      | `titlebufflist.dbss`       | 5,828 B (97.6%) | 144 B (2.4%) |
| 1      | `titlebufflistoffset.dbss` | 220 B (100.0%)  | 0 B (0.0%)   |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                               |
| -------------------------- | -------- | ---------------------------------- |
| `titlebufflistoffset.dbss` | Required | Provides block offsets and sizes   |
| `stringtable.bss`          | Optional | Key hash of the tooltip text in LOC, see Localised Text |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A block count, then the blocks back to back.

| Offset  | Type         | Field  | Notes                                |
| ------- | ------------ | ------ | ------------------------------------ |
| `+0x00` | u32          | count  | Number of blocks, 18 on client 3458  |
| `+0x04` | Block[count] | blocks | See Block                            |

### Block (variable: 32 bytes + texts)

| Offset             | Type  | Field           | Confidence | Notes                                                                                             |
| ------------------ | ----- | --------------- | ---------- | ------------------------------------------------------------------------------------------------- |
| `+0x00`            | u32   | internal_id     | High       | Zero-based buff/effect row ID, same as the offset file entry_id                                   |
| `+0x04`            | u32   | required_titles | High       | Title count to unlock this tier                                                                   |
| `+0x08`            | u8    | unknown_08      | High       | `1` on all 18 tiers                                                                               |
| `+0x09`            | u8    | unknown_09      | High       | `0` on all 18 tiers                                                                               |
| `+0x0A`            | u16   | unknown_0a      | High       | `58501 + internal_id` on all 18 tiers, see Open Questions                                         |
| `+0x0C`            | str16 | label_kr        | High       | Korean tier label, `칭호 50개 습득 : ` ("50 titles acquired: "); the u64 counts UTF-16 code units |
| `label_kr+0x00`    | str16 | effect_kr       | High       | Korean effects with PAColor markup, `행운 잠재력 <PAColor0xFF00BAFF>+1단계<PAOldColor>`           |
| `effect_kr+0x00`   | u32   | unknown_end     | High       | `0` on all 18 tiers; the block ends here                                                          |

Checked on all 18 blocks of client 3458: each one ends exactly after `unknown_end`. An earlier version of this doc left everything after `required_titles` as one text payload, and the parser read only from the first PAColor tag, so the Korean fallback showed just `+1단계`.

#### internal_id / Display Level

The offset file's `entry_id` and block `internal_id` identify the same row. Display level is usually `internal_id + 1`:

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

### `titlebufflistoffset.dbss`

| Offset  | Type              | Field | Notes          |
| ------- | ----------------- | ----- | -------------- |
| `+0x00` | u32               | count | Entry count    |
| `+0x04` | Offset Row[count] | rows  | See Offset Row |

Observed entry IDs are zero-based and align with `internal_id` inside each block.

Observed entries: 18 in the pre-2026-09-27 test fixture and in the 2026-09-27 client.

### Offset Row (12 bytes)

| Offset  | Type | Field    | Notes                                 |
| ------- | ---- | -------- | ------------------------------------- |
| `+0x00` | u32  | entry_id | Zero-based buff/effect row ID         |
| `+0x04` | u32  | offset   | Byte offset into `titlebufflist.dbss` |
| `+0x08` | u32  | size     | Block size in bytes                   |

## Embedded Korean Text

The DBSS block contains Korean text directly, `label_kr` followed by `effect_kr`:

```text
칭호 50개 습득 : 행운 잠재력 <PAColor0xFF00BAFF>+1단계<PAOldColor>
```

### PAColor Tags

Effect values use PA color markup:

```text
<PAColor0xFF00BAFF>+1단계<PAOldColor>
```

| Color      | Meaning                                           |
| ---------- | ------------------------------------------------- |
| `FF00BAFF` | Blue/cyan highlight used for numeric bonus values |

These tags color the bonus numbers in the Title Effects tooltip, not individual title name colors.

## Localised Text

The tooltip in the user's language is one multiline UI string, `GAME` sheet key `LUA_CHARACTERINFO_TITLE_TOOLTIP_DESC` (key hash `3723587620`, LOC `str_type=37`, `str_id1=3723587620`, `str_id2=1`). `stringtable.bss` gives the hash and keeps the same Korean text; `RESOURCE` key `PANEL_CHARACTERINFO_TITLE_TOOLTIP_DESC` holds a copy. Each line is one tier, in `internal_id` order (18 lines, 18 tiers):

```text
Acquire x50: Luck <PAColor0xff00baff>+1<PAOldColor>
Acquire x60: Luck <PAColor0xff00baff>+2<PAOldColor>
Acquire x70: Luck <PAColor0xff00baff>+2<PAOldColor> / Max Energy <PAColor0xff00baff>+1<PAOldColor>
```

Pick the line by `internal_id`, not by matching the `Acquire x50:` prefix, since other languages word the prefix differently.

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

## Open Questions

### What do `unknown_08`, `unknown_09` and `unknown_0a` encode?

`unknown_0a` counts up from `58501` with the tier. Buffs `58501` to `58503` are the title Luck buffs (`(칭호) 행운 1레벨` to `3레벨`, Luck +1 to +3), but tier 3 (`58503`) gives Luck +2 / Max Energy +1, so it is not the tier's buff. `unknown_08` is always `1` and `unknown_09` always `0`.
