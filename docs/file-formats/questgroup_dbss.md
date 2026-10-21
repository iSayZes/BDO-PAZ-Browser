# `questgroup.dbss` Format

## Purpose

Quest grouping table. Each record names a quest chain/group in Korean and lists the `quest.dbss` quest IDs that belong to that group.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records                                | Row bytes |
| ------ | -------------- | ------- | ----------------- | ----- | -------------------------------------- | --------- |
| 1      | 1485 and later | 3474    | `questgroup.dbss` | 5,918 | 110 Quest Group Record, 474 Quest Link | 4         |

| Layout | File              | Known           | Unknown      |
| ------ | ----------------- | --------------- | ------------ |
| 1      | `questgroup.dbss` | 5,478 B (92.6%) | 440 B (7.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File          | Required | Role                                             |
| ------------- | -------- | ------------------------------------------------ |
| `quest.dbss`  | Optional | Provides full quest records for listed quest IDs |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                      | Field   | Notes                                       |
| ------- | ------------------------- | ------- | ------------------------------------------- |
| `+0x00` | u32                       | count   | Number of quest group records; `110` in the pre-2026-09-27 fixture and in the 2026-09-27 client |
| `+0x04` | Quest Group Record[count] | records | See Quest Group Record                      |

Records start immediately after the header at `+0x04`. Records are variable length because each group name and child quest list can have different sizes.

### Quest Group Record (variable: 18 bytes + name and quest links)

| Offset         | Type                    | Field       | Notes                                                              |
| -------------- | ----------------------- | ----------- | ------------------------------------------------------------------ |
| `+0x00`        | u16                     | group_id    | Quest group identifier; also appears in child quest IDs            |
| `+0x02`        | str16                   | name_kr     | Korean quest group title, not NUL-terminated; see Field Names      |
| `name_kr+0x00` | u32                     | quest_count | Number of child quest IDs                                          |
| `name_kr+0x04` | Quest Link[quest_count] | quests      | `quest_count` child quest references                               |
| `quests+0x00`  | u32                     | unknown_end | Observed `0` in all 110 records; see Field Names                   |

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

## Field Names

The record is the `Group_Quest` sheet of a private server on client 1784
(`QuestGroup`, `GroupName`). That server's dump (`Instance_dumpFull.exe`)
reads the client record (row reader at VA `0x140c18560`) as a u16 group key,
a wide string, a u32 count with that many u32 quest links, and a closing u32,
and rejects a record whose bytes it does not consume exactly. Its string
reader takes a u64 code unit count (VA `0x140510d78`), so `+0x02` to `+0x09`
is one count and the text starts at `+0x0A`. Earlier versions of this doc
read those 8 bytes as a u16 `name_len`, a u32 `unknown_04` and a u16
`unknown_08`; the upper six bytes are `0` because no title has 65,536 code
units. The sheet loader builds each quest list as `(group, 1)`, `(group,
2)`, ... for as long as the quest exists.

`unknown_end` has no sheet column and no member in the 2016 PDB's
`gc::QuestGroupStaticStatus`. The loader sets it to `0`; the only code that
reads it passes it with LOC type 25 to a lookup that skips `0` and otherwise
reads an 8-byte entry at `value * 8` of a `Head_LanguageData_` file, the
same use as the `newquest.bss` group trailer ([`newquest_bss.md`](newquest_bss.md)
Open Questions). Nothing names it.

The sheet and the private server's own file hold the same 114 groups with
the same names; client 3474 shares 110 of them, all with the same name.

## Notes

- Observed decompressed size is `6,038` bytes in the pre-2026-09-27 fixture and `5,918` in the 2026-09-27 client.
- `(file_size - 4) / count` is not integral, confirming variable-length records.
- All 504 child quest IDs were found as little-endian `u32` values in the extracted `quest.dbss` sample. All are `allquestlist.bss` entries: 504 of 504 in the pre-2026-09-27 fixture, 474 of 474 in the 2026-09-27 client.
- Child links are stored as `(group_id, quest_no)` pairs, not as standalone `u32` fields, but the byte representation is identical to the derived `quest_id`.
- `quest_count` ranges from `0` to `21` in both files. Two groups are empty in the fixture and nine in the 2026-09-27 client, which emptied group `1022` (Sorceress, Beginning of the Journey) among others.
- The `name_kr` count ranges from `3` to `15` UTF-16 code units.

## Open Questions

### Localization

Group names are stored inline as Korean UTF-16 text. LOC type `18` rows keyed by `str_id1=group_id` provide child quest titles, not group names. The handler reads English group names from LOC type `25` keyed by `str_id1=group_id` (group `1022` `소서러, 여정의 시작` is "Sorceress, Beginning of the Journey"); all 110 groups have one in both the pre-2026-09-27 fixture and the 2026-09-27 client.
