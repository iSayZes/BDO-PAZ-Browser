# `skillfusion.dbss` Format

## Purpose

The Skill Enhancement choices: each enhanced skill with the main skill and
the sub skill it combines, the enhancement slot it belongs to and its
order among the choices for one main skill. The Skill window's enhancement
panel (`panel_window_skill_combination.luac`) lists a slot's rows through
`ToClient_getFusionSkillListCount(slot)`, `ToClient_getFusionMainSkillNo`,
`ToClient_getFusionSubSkillNo` and `ToClient_getFusionSkillNo`. Companion
`skillfusionoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `skillfusion.dbss`       | 4,612 | 192 Row        | 24        |
| 1      | 1784 and later | 3474    | `skillfusionoffset.dbss` | 2,308 | 192 Offset Row | 12        |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 1      | `skillfusion.dbss`       | 4,612 B (100.0%) | 0 B (0.0%) |
| 1      | `skillfusionoffset.dbss` | 2,308 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                                   |
| ------------------------ | -------- | ---------------------------------------------------------------------- |
| `skillfusionoffset.dbss` | Optional | `skill_fusion_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`    | Optional | Skill names, LOC type `10`, `str_id1 = skill_no`                        |

The skills are rows of [`skill.dbss`](skill_dbss.md); the handler links each
skill number to it.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 192 x 24 = 4,612 bytes.

### Row (24 bytes)

| Offset  | Type | Field                | Notes                                                                    |
| ------- | ---- | -------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | skill_fusion_key     | The enhanced skill, a skill key `skill_no << 16 \| level`; the row key    |
| `+0x04` | u32  | skill_fusion_key_dup | Equal to `skill_fusion_key` on every row; the offset index points here    |
| `+0x08` | u32  | main_skill_key       | The main skill, a skill key                                               |
| `+0x0C` | u32  | sub_skill_key        | The sub skill, a skill key                                                |
| `+0x10` | u32  | slot_no              | Enhancement slot, `0` to `2`                                              |
| `+0x14` | u32  | order_no             | Position among the choices with the same main skill, `0` or `1`           |

The level half of all three skill keys is `1` on every row of clients
1784 and 3474. The rows are in no key order.

### `skillfusionoffset.dbss`

Bare offset table into `skillfusion.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `skillfusion.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (12 bytes)

| Offset  | Type | Field            | Notes                                        |
| ------- | ---- | ---------------- | -------------------------------------------- |
| `+0x00` | u32  | skill_fusion_key | Key of the row it points at                  |
| `+0x04` | u32  | data_offset      | Row start + 4, at `skill_fusion_key_dup`     |
| `+0x08` | u32  | data_size        | `20` on every row: the row less its key      |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in another order than the file; on clients 1784 and 3474
every index row points at the row with its key.

## Field Names

The `SkillFusion` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `SkillFusionKey`, `MainSkillNo`, `SubSkillNo`,
`SlotNo`, `OrderNo` and `ContentsGroup`. The file stores the three skill
numbers as level 1 skill keys; the table compares the skill number half.
`ContentsGroup` (`947` for the Warrior rows) is not in the client file.
The 2016 client's debug symbols have no struct for the table.

| Field            | Column           | Same value (client 1784) | Same value (client 3474) |
| ---------------- | ---------------- | ------------------------ | ------------------------ |
| skill_fusion_key | `SkillFusionKey` | 138 of 138               | 138 of 192               |
| main_skill_key   | `MainSkillNo`    | 138 of 138               | 138 of 138               |
| sub_skill_key    | `SubSkillNo`     | 138 of 138               | 137 of 138               |
| slot_no          | `SlotNo`         | 138 of 138               | 138 of 138               |
| order_no         | `OrderNo`        | 138 of 138               | 138 of 138               |

Client 3474 adds 54 rows, and enhanced skill `3981` takes sub skill `3379`
where client 1784 has `3436`.

## Notes

- On client 3474 each slot has 64 rows. 88 main skills have two rows
  (`order_no` `0` and `1`); 4 (`789`, `855`, `898`, `984`) have four rows
  in one slot, each `order_no` twice.
- `ToClient_requestLearnFusionSkill(fusionSkillNo, mainSkillNo,
  subSkillNo)` learns a row. The panel disables a row's Learn button while
  the main or the sub skill is not learned, once the enhanced skill is
  learned, or while `ToClient_isUsedSkillForFusionSkill(mainSkillNo)`
  holds.
- The panel's tip `PANEL_COMBINATIONSKILL_TIP` reads "※ Enhanced Skills can
  keep the Main Skill's key commands."
