# `actionchartheader.paach` Format

## Purpose

`character/binaryactionchart/actionchartheader.paach` holds a few flag bytes
for every action chart, so the client can read them without loading the
`.paac` itself. Each entry is keyed by the chart's path hash: lookup3
`hashlittle` with seed `810718` (`0xC5EDE`, the seed of
`_common/string_hash.py`) over the chart path relative to
`character/binaryactionchart/`, lower case, without `.paac`
(`pc/3_pew/elfaction_noweapon`). The charts are described in
[`*.paac`](actionchart_paac.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes   | Records     | Row bytes                 |
| ------ | -------------- | ------------------------- | ------- | ----------- | ------------------------- |
| 1      | 1784 and later | `actionchartheader.paach` | 389,222 | 8,071 Entry | 7 to 2,507, 48 on average |

| Layout | File                      | Known            | Unknown           |
| ------ | ------------------------- | ---------------- | ----------------- |
| 1      | `actionchartheader.paach` | 48,452 B (12.4%) | 340,770 B (87.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `c8d4818193aa`  |
| 3258   | Layout 1 | `c8d4818193aa`  |
| 2919   | Layout 1 | `c8d4818193aa`  |
| 2335   | Layout 1 | `c8d4818193aa`  |
| 1784   | Layout 1 | `c8d4818193aa`  |

<!-- versions:end -->

## Companion Files

None. The keys point at the [`*.paac`](actionchart_paac.md) charts by path
hash.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                | Type                | Field         | Notes |
| --------------------- | ------------------- | ------------- | ----- |
| `+0x00`               | char[4]             | magic         | ASCII `PABR` |
| `+0x04`               | u32                 | version       | `1`; the 1784 client loader skips it without a check |
| `+0x08`               | u16                 | entry_count   | `8,071` on client 3483 |
| `+0x0A`               | Entry[entry_count]  | entries       | See Entry |
| `entries+0x00`        | u32                 | version_end   | `1`, skipped like `version` |
| `entries+0x04`        | String Table        | string_table  | See String Table; no strings |
| `EOF-0x08`            | u32                 | table_start   | Offset of the string table |
| `EOF-0x04`            | u32                 | zero          | Always `0` |

### Entry (variable: 6 bytes + flags)

| Offset  | Type             | Field         | Notes |
| ------- | ---------------- | ------------- | ----- |
| `+0x00` | u32              | chart_hash    | Path hash of a `.paac`, see Purpose. On client 3483, 8,002 of the 8,071 keys match a live chart path; the other 69 name no chart |
| `+0x04` | u16              | flag_count    | Number of flag bytes; `1` on 5,022 entries, `101` on 609, `11` on 576 (client 3483) |
| `+0x06` | u8[flag_count]   | unknown_flags | One byte per index; see Flag Bytes |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Flag Bytes

The 1784 client reads the bytes in `0x1418eec80`: it looks up the chart's
key, takes byte `[index]` (byte `0` when the index is past the end of the
list) and falls back to byte `+0x185` of the loaded chart object when the
header has no entry. It then splits the byte: bit 0 and bit 6 each go into a
flag of their own, and a third flag is set when bit 0 is clear, bits 6 and 7
are not both set and bits 4 and 5 are not both set. What the flags do is not
known.

Byte values on client 3483, over every entry: `16` (174,784 bytes), `255`
(149,504), `1` (7,481), `17` (4,729), `144` (1,967), `208` (1,130), `64`
(750), `80` (288), and 13 more values below 50 bytes each.

## Notes

- The 1784 loader reads an entry's `flag_count` and bytes only for a key it
  has not seen yet, so a repeated key would shift every later entry. Client
  3483 has no repeated key.
- Every chart of the 33 class folders under `pc/` has a 1-byte entry on
  client 3483. The 29 charts without an entry include
  `pc/pc_actionchartpackagepcraw.paac`, 12 `npc/` and 4 `summon/` charts.

## Open Questions

### What the Flags Mean

The three flags the 1784 client derives from a flag byte (see Flag Bytes)
have no known use yet, and what the byte index counts (actions, packages or
something else) is not tied to the chart contents: the class charts have
one byte for 139 packages and over 20,000 actions.
