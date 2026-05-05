# `questgroup.dbss` Format

## Purpose

Quest grouping table. Each record names a quest chain/group in Korean and lists the `quest.dbss` quest IDs that belong to that group.

Example:

```text
group_id: 1022
name: 소서러, 여정의 시작
quests: 66558, 132094, 197630
```

## Graph

### Tags

- file format
- dbss
- quest

### Connections

- [quest.dbss](quest_dbss.md) — child quest IDs resolve to `quest.dbss` record IDs

---

## Companion Files

| File          | Required | Role                                             |
| ------------- | -------- | ------------------------------------------------ |
| `quest.dbss`  | Optional | Provides full quest records for listed quest IDs |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                                       |
| ------- | ---- | ----- | ------------------------------------------- |
| `+0x00` | u32  | count | Number of quest group records; observed `110` |

### Record Stream

Records start immediately after the header at `+0x04`. Records are variable length because each group name and child quest list can have different sizes.

---

## Record Structure

### Quest Group Record (variable length)

| Offset  | Type              | Field       | Notes                                                              |
| ------- | ----------------- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u16               | group_id    | Quest group identifier; also appears in child quest IDs            |
| `+0x02` | u16               | name_len    | UTF-16 code unit count for `name_kr`                               |
| `+0x04` | u32               | unknown_04  | Observed `0` in all 110 records                                    |
| `+0x08` | u16               | unknown_08  | Observed `0` in all 110 records                                    |
| `+0x0A` | utf16le[name_len] | name_kr     | Korean quest group title, not NUL-terminated                       |
| varies  | u32               | quest_count | Number of child quest IDs                                          |
| varies  | Quest Link[]      | quests      | `quest_count` child quest references                               |
| varies  | u32               | tail_zero   | Observed `0` in all 110 records; record terminator/padding sentinel |

### Quest Link (4 bytes)

| Offset  | Type | Field    | Notes                                             |
| ------- | ---- | -------- | ------------------------------------------------- |
| `+0x00` | u16  | group_id | Child quest group ID; normally matches parent     |
| `+0x02` | u16  | quest_no | 1-based quest number within the group             |

The corresponding `quest.dbss` `quest_id` is the same 4 bytes interpreted as a little-endian `u32`:

```text
quest_id = (quest_no << 16) | group_id
```

---

## Observed Records

| File Offset | Group ID | Name KR                  | Quest Count | Quest IDs                         |
| ----------- | -------- | ------------------------ | ----------- | --------------------------------- |
| `0x000004`  | `1022`   | `소서러, 여정의 시작`    | `3`         | `66558`, `132094`, `197630`       |
| `0x000038`  | `1014`   | `워리어, 여정의 시작`    | `3`         | `66550`, `132086`, `197622`       |
| `0x00006C`  | `1055`   | `해적이 숨겨 놓은 보물`  | `6`         | `66591` .. `394271`               |
| `0x0000AE`  | `503`    | `소서러의 기술`          | `4`         | `66039`, `131575`, `197111`, `262647` |
| `0x0000DE`  | `3100`   | `칼페온의 레이트 가문`   | `4`         | `68636`, `134172`, `199708`, `265244` |

---

## Suggested UI Layout

| Column      | Type | Notes                                                       |
| ----------- | ---- | ----------------------------------------------------------- |
| Group ID    | num  | `group_id`; right-aligned                                   |
| Name        | text | Raw Korean `name_kr`; use localization if a mapping is found |
| Quests      | num  | Number of linked child quests                               |
| Quest IDs   | text | Comma-separated derived `quest.dbss` IDs                    |
| Group:No    | text | Compact raw child links as `group_id:quest_no`              |

---

## Notes

- Observed decompressed size is `6,038` bytes.
- `(file_size - 4) / count` is not integral, confirming variable-length records.
- All 504 child quest IDs were found as little-endian `u32` values in the extracted `quest.dbss` sample.
- Child links are stored as `(group_id, quest_no)` pairs, not as standalone `u32` fields, but the byte representation is identical to the derived `quest_id`.
- `quest_count` ranges from `0` to `21`.
- `name_len` ranges from `3` to `15` UTF-16 code units.

---

## Open Questions

### Localization

Group names are stored inline as Korean UTF-16 text. No LOC mapping has been confirmed yet, so an English preview should display raw Korean unless a later localization relationship is found.
