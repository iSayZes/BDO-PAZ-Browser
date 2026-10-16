# `questgroup.dbss` Format

## Purpose

Quest grouping table. Each record names a quest chain/group in Korean and lists the `quest.dbss` quest IDs that belong to that group.

Example:

```text
group_id: 1022
name: 소서러, 여정의 시작
quests: 66558, 132094, 197630
```

## Companion Files

| File          | Required | Role                                             |
| ------------- | -------- | ------------------------------------------------ |
| `quest.dbss`  | Optional | Provides full quest records for listed quest IDs |

All multi-byte values are little-endian.

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                                       |
| ------- | ---- | ----- | ------------------------------------------- |
| `+0x00` | u32  | count | Number of quest group records; `110` in the pre-2026-09-27 fixture and in the 2026-09-27 client |

### Record Stream

Records start immediately after the header at `+0x04`. Records are variable length because each group name and child quest list can have different sizes.

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
| varies  | u32               | unknown_end | Observed `0` in all 110 records; record terminator/padding sentinel |

### Quest Link (4 bytes)

| Offset  | Type | Field    | Notes                                             |
| ------- | ---- | -------- | ------------------------------------------------- |
| `+0x00` | u16  | group_id | Child quest group ID; normally matches parent     |
| `+0x02` | u16  | quest_no | 1-based quest number within the group             |

The corresponding `quest.dbss` `quest_id` is the same 4 bytes interpreted as a little-endian `u32`:

```text
quest_id = (quest_no << 16) | group_id
```

## Observed Records

Pre-2026-09-27 fixture:

| File Offset | Group ID | Name KR                  | Quest Count | Quest IDs                         |
| ----------- | -------- | ------------------------ | ----------- | --------------------------------- |
| `0x000004`  | `1022`   | `소서러, 여정의 시작`    | `3`         | `66558`, `132094`, `197630`       |
| `0x000038`  | `1014`   | `워리어, 여정의 시작`    | `3`         | `66550`, `132086`, `197622`       |
| `0x00006C`  | `1055`   | `해적이 숨겨 놓은 보물`  | `6`         | `66591` .. `394271`               |
| `0x0000AE`  | `503`    | `소서러의 기술`          | `4`         | `66039`, `131575`, `197111`, `262647` |
| `0x0000DE`  | `3100`   | `칼페온의 레이트 가문`   | `4`         | `68636`, `134172`, `199708`, `265244` |

## Notes

- Observed decompressed size is `6,038` bytes in the pre-2026-09-27 fixture and `5,918` in the 2026-09-27 client.
- `(file_size - 4) / count` is not integral, confirming variable-length records.
- All 504 child quest IDs were found as little-endian `u32` values in the extracted `quest.dbss` sample. All are `allquestlist.bss` entries: 504 of 504 in the pre-2026-09-27 fixture, 474 of 474 in the 2026-09-27 client.
- Child links are stored as `(group_id, quest_no)` pairs, not as standalone `u32` fields, but the byte representation is identical to the derived `quest_id`.
- `quest_count` ranges from `0` to `21` in both files. Two groups are empty in the fixture and nine in the 2026-09-27 client, which emptied group `1022` (Sorceress, Beginning of the Journey) among others.
- `name_len` ranges from `3` to `15` UTF-16 code units.

## Open Questions

### Localization

Group names are stored inline as Korean UTF-16 text. LOC type `18` rows keyed by `str_id1=group_id` provide child quest titles, not group names. The handler reads English group names from LOC type `25` keyed by `str_id1=group_id` (group `1022` `소서러, 여정의 시작` is "Sorceress, Beginning of the Journey"); all 110 groups have one in both the pre-2026-09-27 fixture and the 2026-09-27 client.
