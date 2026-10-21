# `simplesequence.bss` Format

## Purpose

A keyed table of 13-byte rows. Each u32 key is two u16 halves: the high
half groups the rows (238 groups, `1` to `424`, on client 3474) and the
low half numbers the rows of a group from `1` with no gap. Both halves
repeat in the row, and a last byte is `0` or `1` per group. No client Lua,
sheet or server text names the table, so what a group and its rows stand
for is open. The file is a u32 count and fixed rows, with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | --------- |
| 1      | 2519 and later | 3474    | `simplesequence.bss` | 6,946 | 534 Row | 13        |

| Layout | File                 | Known           | Unknown         |
| ------ | -------------------- | --------------- | --------------- |
| 1      | `simplesequence.bss` | 2,140 B (30.8%) | 4,806 B (69.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (13 bytes)

| Offset  | Type | Field      | Notes                                                       |
| ------- | ---- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32  | key        | Unique; high u16 the group, low u16 the row in the group     |
| `+0x04` | u16  | unknown_04 | The key's low half                                          |
| `+0x06` | u16  | unknown_06 | The key's high half                                         |
| `+0x08` | u16  | unknown_08 | The key's high half                                         |
| `+0x0A` | u16  | unknown_0a | The key's low half                                          |
| `+0x0C` | u8   | unknown_0c | `0` or `1`; the same on every row of a group (client 3474)   |

The rows of a group sit together; neither the groups nor the rows within
a group are sorted by key (the file opens `0x00AD0002`, `0x00AD0001`,
`0x00AC0004`).

## Groups

On client 3474 the 534 rows form 238 groups: 86 of one row, 83 of two, 35
of three, 22 of four and 12 larger ones up to 22 rows (group `11` has 14,
the largest 22). `unknown_0c` is `0` on all rows of 53 groups (`1` to `40`,
`400` to `407` and `420` to `424`) and `1` on all rows of the other 185.

## Notes

- The file is not in client 1784. The 2016 client's debug symbols, the
  sheets of a private server's `DataSheets.bexcel` on client 1784 and its
  server dump hold no `SimpleSequence` name; the only `sequence` sheet
  column there is `sequenceFilePath` of `Emoticon_Table`.
- The client Lua plays cutscenes ("sequences") through `ToClient_*Sequence*`
  calls such as `ToClient_isPlayingSequence`, none with a key.

## Open Questions

### What a Group Stands For

The key's high half (`1` to `424`, 238 values) and low half (`1` to N)
match no table read so far, and `unknown_0c` splits the groups into 53
and 185 by key ranges. Whether a group is a cutscene, a quest step chain or
something else is open.
