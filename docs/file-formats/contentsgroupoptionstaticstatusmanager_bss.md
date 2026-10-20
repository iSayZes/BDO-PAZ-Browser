# `contentsgroupoptionstaticstatusmanager.bss` Format

## Purpose

The contents group switches of the client's service: which feature groups
are open. A contents group is a decimal key string such as `"330"`, the
argument of the client Lua's `ToClient_IsContentsGroupOpen("330")`. The file
holds the sorted key hashes of the open groups, then every group key the
client knows with its hash. On client 3474 that is 1,492 open groups out of
2,463, keys `0` to `10043`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                         | Bytes  | Records     | Row bytes               |
| ------ | -------------- | ------- | -------------------------------------------- | ------ | ----------- | ----------------------- |
| 1      | 3474 and later | 3474    | `contentsgroupoptionstaticstatusmanager.bss` | 53,048 | 2,463 Group | 14 to 22, 19 on average |

| Layout | File                                         | Known             | Unknown    |
| ------ | -------------------------------------------- | ----------------- | ---------- |
| 1      | `contentsgroupoptionstaticstatusmanager.bss` | 53,048 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

The handler reads no companion files.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                 | Type               | Field           | Notes                                                                    |
| ---------------------- | ------------------ | --------------- | ------------------------------------------------------------------------ |
| `+0x00`                | u32                | open_count      | Number of open groups; `1492` on client 3474                             |
| `+0x04`                | u32[open_count]    | open_key_hashes | `key_hash` of each open group, ascending, unique                         |
| `open_key_hashes+0x00` | u32                | group_count     | Number of groups; `2463` on client 3474                                  |
| `open_key_hashes+0x04` | Group[group_count] | groups          | See Group; the last one ends at the end of the file                      |

### Group (variable: 12 bytes + key text)

| Offset  | Type  | Field              | Notes                                                                       |
| ------- | ----- | ------------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32   | key_hash           | Hash of `contents_group_key`, see [Key Hash](#key-hash)                     |
| `+0x04` | str16 | contents_group_key | Decimal group key (`"49"`, `"2295"`); the string `ToClient_IsContentsGroupOpen` takes |

## Key Hash

`key_hash` is the client's string-key hash (`_common/string_hash.py`):
lookup3 `hashlittle` over the UTF-16LE bytes of `contents_group_key` with
seed `0xC5EDE`, the hash of the `stringtable.bss` keys. It reproduces all
2,463 `key_hash` values of client 3474, and every `open_key_hashes` entry is
the `key_hash` of one group.

## Field Names

`contents_group_key` is the `ContentsGroupKey` column of the
`ContentsGroupOption` sheet in a private server's `DataSheets.bexcel` on
client 1784. The sheet has one `0`/`1` column per service (`DEV`,
`KOR_REAL`, `JPN_REAL`, `RUS_REAL`, `NA_REAL`, `TW_REAL`, `SA_REAL`,
`KOR_2`, `TH_REAL`, `ID_REAL`, `TR_REAL`, `XB_REAL`, `PS_REAL`, `GT_REAL`,
`CS_REAL`, `LV_REAL`, `DD_SERVER`) and a `TranslationRegionKey`. 1,551 of
its 1,561 keys are groups of the client 3474 file. Over those 1,551 keys,
membership in `open_key_hashes` agrees with `NA_REAL` on 1,468, more than
any other column (`TW_REAL` 1,446, `KOR_REAL` 1,391, `DEV` 1,050). That and
the Lua function name give `open_key_hashes` its name: the groups whose
service column is `1` for the client's service.

## Notes

- `global_contentsoptions.luac` (client 3474) sets 476 globals as
  `_ContentsGroup_<Name> = ToClient_IsContentsGroupOpen("<key>")`. Every
  key is a group of the file and 386 of them are open, among them
  `330` `_ContentsGroup_DuelCharacter`, `345` `_ContentsGroup_3DMiniMapOpen`
  and `357` `_ContentsGroup_isFairy`. Closed ones include `383`
  `_ContentsGroup_DamageMeter`, `1145` `_ContentsGroup_PearlShopGift` and
  `1151` `_ContentsGroup_PearlShopMileage`.
- `groups` is sorted neither by key nor by hash; `open_key_hashes` is
  sorted by hash, so a lookup can binary-search it.
- Of the 83 keys where the list and `NA_REAL` disagree, 51 are open on
  client 3474 and `0` in the sheet, 32 the reverse. The sheet is a
  private server's copy from early 2022, so these rows are not evidence
  against the reading.
- The client 1784 test client has no `contentsgroupoptionstaticstatusmanager.bss`.
  The 2016 client names `gc::GameOptionManager::isContentsGroupOpen` and
  `ToClient_IsContentsGroupOpen`, but no loader for this file.

## Open Questions

### Which Service the Open List Follows

The list matches the `NA_REAL` column best, and the checked client is the
NA/EU client. Whether a client of another service ships the same `groups`
with its own `open_key_hashes`, and whether NA and EU share one list, needs
a file from another service's client.
