# `textbind.dbss` Format

## Purpose

The Korean text of every TextBind name. LOC and inline text can name a text
instead of holding it, as `{TextBind:NAME}` or
`{StringTableBind(TextBind:NAME)}` (see `languagedata_loc.md`, Type 59). Each
record holds the text of one name in four variants. The English and other
translations are LOC type 59 with the same key; this file is the Korean source
and the fallback without LOC.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes     | Records          | Row bytes                      |
| ------ | -------------- | ------- | --------------------- | --------- | ---------------- | ------------------------------ |
| 1      | 1784 and later | 3473    | `textbind.dbss`       | 1,952,118 | 1,167 Record     | 64 to 12,716, 1,673 on average |
| 1      | 1784 and later | 3473    | `textbindoffset.dbss` | 14,008    | 1,167 Offset Row | 12                             |

| Layout | File                  | Known               | Unknown        |
| ------ | --------------------- | ------------------- | -------------- |
| 1      | `textbind.dbss`       | 1,947,450 B (99.8%) | 4,668 B (0.2%) |
| 1      | `textbindoffset.dbss` | 14,008 B (100.0%)   | 0 B (0.0%)     |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `textbindoffset.dbss` | Optional | `key -> (offset, size)` index; records also read in order without it |
| `languagedata_*.loc`  | Optional | Type 59: the same texts in the user language, `str_id4` = variant |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                |
| ------- | ------------- | ------- | ------------------------------------ |
| `+0x00` | u32           | count   | `1,166` on client 3464               |
| `+0x04` | Record[count] | records | Back to back, no padding; see Record |

The records tile the file: the first starts at `0x04` and the last ends at
the end of the file (1,951,374 bytes on client 3464).

### Record (variable: 40 bytes + texts)

| Offset           | Type  | Field                 | Notes |
| ---------------- | ----- | --------------------- | ----- |
| `+0x00`          | u32   | key                   | `key_hash()` of the TextBind name: lookup3 `hashlittle` over the UTF-16LE name, seed `0xC5EDE`, the `stringtable.bss` key hash. LOC type 59 `str_id1` |
| `+0x04`          | str16 | variant_0             | PC text, see Variants |
| `variant_0+0x00` | str16 | variant_1             | PlayStation text, see Variants |
| `variant_1+0x00` | str16 | variant_2             | Console text, see Variants |
| `variant_2+0x00` | u32   | unknown_pre_variant_3 | `0` on all 1,166 records (client 3464) |
| `variant_2+0x04` | str16 | variant_3             | See Variants |

Each string is a u64 length in UTF-16 code units followed by that many
UTF-16LE units, no terminator (`RecordReader.text(wide=True)`). The
`unknown_pre_variant_3` u32 has no fixed offset; it follows the end of
`variant_2`.

### `textbindoffset.dbss`

| Offset  | Type              | Field | Notes                         |
| ------- | ----------------- | ----- | ----------------------------- |
| `+0x00` | u32               | count | Same count as `textbind.dbss` |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                |

No PABR magic. The rows are not in file order or key order; sorted by
`offset` they tile `textbind.dbss` from `0x04` to its end. Read with
`parse_bare_u32_offset_rows()`.

### Offset Row (12 bytes)

| Offset  | Type | Field  | Notes                                        |
| ------- | ---- | ------ | -------------------------------------------- |
| `+0x00` | u32  | key    | Record key, repeated per row                 |
| `+0x04` | u32  | offset | Byte offset of the record in `textbind.dbss` |
| `+0x08` | u32  | size   | Byte size of the record                      |

## Variants

Counted on client 3464:

| Variant | Platform     | Evidence |
| ------- | ------------ | -------- |
| 0       | PC           | Key hints name the mouse actions (`{KeyBind:Attack1}` 235 times, `{KeyBind:Attack2}` 173, `{KeyBind:Confirm}` once). The `TextBind_Table` of a private server on client 519 has `Key`, `PC` and `Console` columns; its `PC` text equals variant 0 on 233 of the 258 names both hold, and the other 25 differ by later wording changes (`말` to `탑승물`) |
| 1       | PlayStation  | The only variant with `컨트롤러` (12 records, the others say `게임 패드`), `DUALSHOCK` and PlayStation names (4 records), and never `xbox` (variants 0, 2 and 3 have it in 11 records each). Key hints use `{KeyBind:Confirm}` 106 times |
| 2       | Console      | Differs from variant 1 in 82 records: it says `게임 패드` where variant 1 says `컨트롤러` or `DUALSHOCK™4`, and holds `xbox` in 11 records. Key hints use `{KeyBind:Confirm}` 104 times |
| 3       | Not known    | Equal to variant 0 in 1,010 records and to variant 1 in 777; see Open Questions |

All four variants are equal in 635 records. Every record has a non-empty
variant 0. 452 variants hold another TextBind placeholder.

## Notes

- The TextBind name is not stored; only its hash is. Names appear in the
  placeholders that use them, such as `GROWTHPASS_PC_CONSOLE_SEP1` in quest
  4470 / 3.
- LOC type 59 holds 1,203 names on client 3464: all 1,166 of this file and 37
  more with no Korean record.
- The `TEXT_BIND_KR` lookup index maps `key` to the Korean variant 0 text.
  `resolve_text_binds()` in `_common/loc.py` falls back to it when LOC is not
  loaded or has no type 59 text for a name.
- No client Lua script mentions TextBind or picks a variant; the game fills
  placeholders itself.

## Open Questions

### Variant 3

Variant 3 matches variant 0 in 1,010 records, but in 14 records it swaps the
mouse hints for pad buttons (`{KeyBind:Dash}+{KeyBind:Attack2}` becomes
`{KeyBind:Symbol_LT}+{KeyBind:Symbol_X}`), and the chat tip record says
`눌러보세요` ("press") where variant 0 says `클릭해보세요` ("click"). It may be the PC text
for a gamepad player, or the Xbox text with variant 2 being something else.

### `unknown_pre_variant_3`

The u32 between variants 2 and 3 is `0` on every record of client 3464, so
its meaning cannot be read from the data.
