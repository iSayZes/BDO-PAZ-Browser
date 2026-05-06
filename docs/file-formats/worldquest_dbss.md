# `worldquest.dbss` Format

## Purpose

World quest table placeholder. The observed client file contains only an empty DBSS record-count header and no record data.

Example:

```text
count: 0
records: none
```

## Graph

### Tags

- file format
- dbss
- quest
- world

### Connections

- [quest.dbss](quest_dbss.md) — related quest definition table; no direct field relationship observed in this empty file

---

## Companion Files

No required companion files were observed. The archive contains no `worldquestoffset.dbss` companion.

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                                   |
| ------- | ---- | ----- | --------------------------------------- |
| `+0x00` | u32  | count | Number of world quest records; observed `0` |

### Record Stream

No record stream is present in the observed file because `count` is `0` and file length is exactly `4` bytes.

---

## Record Structure

No record structure can be inferred from the observed sample because there are no records.

---

## Suggested UI Layout

| Column | Type | Notes                              |
| ------ | ---- | ---------------------------------- |
| Count  | num  | Header `count`; observed `0`       |
| Status | text | Display `No world quest records`   |

---

## Notes

- Observed decompressed size is `4` bytes.
- Raw bytes are `00 00 00 00`, interpreted as u32 `count = 0`.
- `python browser.py --list *worldquest*` found only `gamecommondata/binary/worldquest.dbss`.
- `python browser.py --list *world*quest*` found world-map quest UI assets and `worldquest.dbss`, but no same-stem DBSS/BSS/PAC companion.

---

## Open Questions

### Non-Empty Layout

No non-empty sample was available, so record fields remain unknown. If a future client build ships `count > 0`, inspect records starting at `+0x04`.
