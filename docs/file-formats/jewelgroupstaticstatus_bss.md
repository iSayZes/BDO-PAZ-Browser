# `jewelgroupstaticstatus.bss` Format

## Purpose

The crystal groups: one fixed row per group with its group number, the most
crystals of that group a crystal preset may hold, and its Korean name. A
crystal names its group in the last two bytes of its
[`itemenchant.dbss`](itemenchant_dbss.md) block. LOC type 121 names each
group under its group number and limit.
[`jewelspecialslotsgroupstaticstatus.bss`](jewelspecialslotsgroupstaticstatus_bss.md)
lists the groups each special preset slot accepts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | ------------ | --------- |
| 1      | 3473 and later | 3474    | `jewelgroupstaticstatus.bss` | 980   | 42 Group Row | 8         |

| Layout | File                         | Known          | Unknown    |
| ------ | ---------------------------- | -------------- | ---------- |
| 1      | `jewelgroupstaticstatus.bss` | 980 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                   |
| --------------------- | -------- | ---------------------- |
| `languagedata_en.loc` | Optional | Group names (type 121) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block of fixed 8-byte rows, followed by the same counted string table
and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). On client 3473 the string table holds 42 wide
strings, one Korean group name per row.

| Offset              | Type             | Field              | Notes                            |
| ------------------- | ---------------- | ------------------ | -------------------------------- |
| `+0x00`             | char[4]          | magic              | ASCII `PABR`                     |
| `+0x04`             | u32              | count              | Number of rows; 42 on client 3473 |
| `+0x08`             | Group Row[count] | rows               | See Group Row                    |
| `rows+0x00`         | String Table     | string_table       | One Korean name per row          |
| `string_table+0x00` | u32              | string_table_start | Where the rows end               |
| `string_table+0x04` | u32              | zero               | Always `0`                       |

The rows are not sorted by group number.

### Group Row (8 bytes)

| Offset  | Type | Field     | Notes                                                                 |
| ------- | ---- | --------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | name_ref  | String table index of the Korean name; equal to the row index on client 3473 |
| `+0x04` | u16  | group     | Crystal group number; LOC type 121 `str_id1`                         |
| `+0x06` | u16  | max_count | Most crystals of this group one preset holds; LOC type 121 `str_id2`  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Groups

On client 3473:

| Group | Korean          | LOC type 121                    | Max count |
| ----- | --------------- | ------------------------------- | --------- |
| 1     | 게르비슈        | Gervish                         | 1000      |
| 2     | 마칼로드        | Macalod                         | 1000      |
| 3     | 훔              | Hoom                            | 1000      |
| 4     | 적중            | Accuracy                        | 2         |
| 5     | 정령            | Spirit                          | 2         |
| 6     | 추가 피해 증가  | Increased Extra Damage          | 2         |
| 7     | 특정 저항 무시  | Ignore Certain Resistance       | 2         |
| 8     | 올루카스        | Olucas                          | 2         |
| 9     | 아크라드        | Ah'krad                         | 2         |
| 10    | 최대 생명력     | Max HP                          | 2         |
| 11    | 저항 증가 I     | Increased Resistance I          | 2         |
| 12    | 회피력 증가     | Increased Evasion               | 2         |
| 13    | 카르메          | Carmae                          | 2         |
| 14    | 아디스          | Addis                           | 2         |
| 15    | 피해 감소 증가  | Increases Damage Reduction      | 2         |
| 16    | 살무사          | Viper                           | 2         |
| 17    | 히스트리아      | Hystria                         | 2         |
| 18    | 붉은 전장 I     | Red Battlefield I               | 2         |
| 19    | 붉은 전장 II    | Red Battlefield II              | 2         |
| 20    | 낙하 피해 감소  | Fall Damage Reduction           | 2         |
| 21    | 점프력          | Jump Height                     | 2         |
| 22    | 내구도 감소 저항 | Durability Reduction Resistance | 2         |
| 23    | 공격시 회복     | Recovery on Attack              | 2         |
| 24    | 공성 무기 회피율 | Siege Weapon Evasion Rate       | 2         |
| 25    | 잠수 시간 증가  | Submergence                     | 2         |
| 26    | 은은한 마력     | Dim Magic                       | 6         |
| 27    | 최대 기운       | Max Energy                      | 2         |
| 28    | 검붉은 용장     | Dark Red Valor                  | 2         |
| 30    | 저항 증가 II    | Increased Resistance II         | 2         |
| 31    | 생활 특수 효과  | Life Skill Special Effect       | 2         |
| 32    | 낙원            | Paradise                        | 4         |
| 33    | 극 게르비슈     | Ultimate Gervish                | 4         |
| 34    | 극 마칼로드     | Ultimate Macalod                | 4         |
| 35    | 극 훔           | Ultimate Hoom                   | 4         |
| 36    | 혹한            | Bitterness                      | 2         |
| 37    | 척살            | Decimation                      | 2         |
| 38    | 파괴            | Destruction                     | 2         |
| 39    | 에다니아        | Edania                          | 1         |
| 100   | 없음            | No Group                        | 1000      |
| 101   | 고대 정령       | Ancient Spirit                  | 1         |
| 102   | 태초            | Primordial                      | 1         |
| 103   | 새벽            | Dawn                            | 6         |

## Notes

- `max_count` is the limit the crystal inventory window checks
  (`panel_window_jewelinven_all_1.luac`): for a crystal whose
  `getJewelGroupMaxCount()` is above 0, it counts the crystals with the same
  `getJewelGroupNumber()` in all `__eJewelSlotMaxCount` slots of the selected
  preset and greys the crystal out once that count reaches `max_count`. The
  preset has 23 slots (12 normal and 11 special controls in
  `panel_window_jewelpreset_all.xml`), so `1000` sets no limit in practice.
- LOC type 121 keys each group name by `(group, max_count)`: all 42 rows find
  their name under that pair on client 3473. LOC also holds `(26, 2)` Dim
  Magic next to `(26, 6)`, and `(29, 2)` Dark Red Armor, a group with no row
  here.
- The u16 at `end-0x02` of each [`itemenchant.dbss`](itemenchant_dbss.md)
  base block (`crystal_group` there) is this group number. On client
  3473 it is `0xFFFF` except in 481 crystals, and every value they store is
  a group here: Crystal of Frozen Bitterness (`15255`, 얼어붙은 혹한의
  수정) stores 36 혹한, the 21 Dawn crystals 103 새벽, and 187 crystals 100
  (No Group), among them Magic Crystal of Infinity - Valor (`768751`).
  Groups 7, 31 and 32 have no crystal.
- Neither the 2016 PDB nor a private server's `DataSheets.bexcel` on client
  1784 has this table, and the client 1784 PAZ has no
  `jewelgroupstaticstatus.bss`. The field names come from the Lua getters
  `getJewelGroupNumber()` and `getJewelGroupMaxCount()`.
