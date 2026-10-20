# `lightstoneset.bss` Format

## Purpose

The Lightstone sets: each row names three or four Lightstones that, slotted
into Artifacts together, apply a set effect. A row holds the set ID, the
passive skill that carries the effect, the member Lightstone item IDs and the
Korean name and effect text. A table after the rows lists which Lightstone
items count as which member, so an Amplified Lightstone completes a set like
its base Lightstone.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes  | Records                         | Row bytes               |
| ------ | -------------- | ------- | ------------------- | ------ | ------------------------------- | ----------------------- |
| 1      | 3473 and later | 3474    | `lightstoneset.bss` | 30,209 | 165 Set Row, 105 Substitute Row | 26 to 30, 29 on average |

| Layout | File                | Known             | Unknown    |
| ------ | ------------------- | ----------------- | ---------- |
| 1      | `lightstoneset.bss` | 30,209 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

The file is self-contained. The handler reads these through shared lookups:

| File                  | Required | Role                                                                    |
| --------------------- | -------- | ----------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Set name and effect (LOC type 113, `str_id1` = set ID), item names (type 0) |
| `skill.dbss`          | Optional | The buffs of the set skill at level 1 (`SKILL_BUFFS` lookup index)      |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The PABR string table layout of `buffsimply.bss` (`_common/pabr_strings.py`),
with variable-size rows and a second table between the rows and the strings.

| Offset              | Type                 | Field        | Notes                                                       |
| ------------------- | -------------------- | ------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                                |
| `+0x04`             | u32                  | count        | Number of sets; 165 on client 3464                          |
| `+0x08`             | Set Row[count]       | sets         | See Set Row                                                 |
| `sets+0x00`         | Substitute Table     | substitutes  | See Substitute Table                                        |
| `substitutes+0x00`  | String Table         | string_table | See String Table                                            |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where the substitute table ends |
| `string_table+0x04` | u32                  | zero         | Always 0                                                    |

On client 3464 the walk over 165 sets and 105 substitute rows ends at
`0x162A`, the stored `table_start`.

### Set Row (variable: 14 bytes + member IDs)

Fields are unaligned.

| Offset            | Type              | Field        | Notes                                                                  |
| ----------------- | ----------------- | ------------ | ---------------------------------------------------------------------- |
| `+0x00`           | u32               | set_id       | Unique; LOC type 113 `str_id1`, and the number in the skill name       |
| `+0x04`           | u16               | skill_no     | Passive skill of the set effect; unique                                |
| `+0x06`           | u32               | member_count | `3` or `4` on client 3464                                              |
| `+0x0A`           | u32[member_count] | member_ids   | Lightstone item IDs, ascending; a stone may repeat                     |
| `member_ids+0x00` | u32               | text_ref     | String table index of the Korean name and effect; equals the row index |

The skill confirms the set ID: LOC type 10 names skill `55078` "Set 2 -
[Well-prepared]" and skill `47521` "Set 182 - [The Wild: Edania]", and
`skill.dbss` gives skill `55078` level 1 the three buffs whose LOC type 5
first lines are the three effect lines of set 2. On client 3464 the level 1
rank of every set skill has one buff per effect line.

The text is the Korean source of the LOC type 113 row:
`<PAColor0xffd2ffad>[준비된 자]<PAOldColor>\n전투 경험치 획득량 +50%\n...`.
The first line is the name in brackets and colour, each further line one
effect. Line breaks are stored as the two characters `\` and `n`
(`_common/inline_text.py`).

### Substitute Table (variable: 4 bytes + rows)

| Offset  | Type                  | Field | Notes                         |
| ------- | --------------------- | ----- | ----------------------------- |
| `+0x00` | u32                   | count | Number of substitute rows     |
| `+0x04` | Substitute Row[count] | rows  | See Substitute Row            |

### Substitute Row (8 bytes)

| Offset  | Type | Field     | Notes                                                       |
| ------- | ---- | --------- | ----------------------------------------------------------- |
| `+0x00` | u32  | item_id   | A Lightstone item ID; unique                                |
| `+0x04` | u32  | member_id | The member item ID it counts as in `member_ids`             |

On client 3464 there are 105 rows: 53 map every member item to itself, and
52 map an Amplified Lightstone (`member_id + 200`, such as `758203`
Amplified Lightstone of Fire: Predation) to its base Lightstone. The rows are
in no sorted order. Garmoth's Lightstone sets page lists each member as "Any
of" the base and the Amplified Lightstone, which matches these rows.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Notes

- The sets with four members come first, then the sets with three, each
  group in ascending `set_id`.
- Set IDs run from 1 to 182 with 17 gaps (30, 51 to 55, 64, 66, 70, 72, 73,
  77 to 80, 164, 173). LOC type 113 still has a row for each gap
  (`[Blacksmith's Blessing]`, `[Brown Bear]`), so these are sets the client
  no longer has.
- The 21 substitute rows from `764201` to `764221` (Lightstone of Flora
  `+200`) name items with no LOC type 0 name and no item icon on client 3464;
  In-Game Checks has a test for whether they exist.
- Iridescent Lightstone (`766101`) is a member of 50 sets, always as the
  last stone.
- The `LIGHTSTONE_SETS` lookup index (`build_lightstone_set_index()` in
  `parser.py`) maps each member and substitute item ID to the sets it counts
  toward, so the [itemenchant.dbss](itemenchant_dbss.md) Lightstone Sets
  column lists them without opening this file.
- The LOC type 113 name of set 96 repeats itself: `[Drills: Blight-Fallen]
  [Drills: Blight-Fallen]`, while the skill name is `Set 96 - [Drills:
  Blight-Fallen]`.
- Cross-check against Garmoth's Lightstone sets page (combat sets only): all
  83 sets it lists have the same members, and the first effect tier values
  equal the LOC type 113 values. Its two further columns, "Including
  Lightstone Effects" and "Including Amplified Lightstone Effects", hold
  values this file does not have.
- The Artifact window and tooltip Lua (`panel_window_artifacts_all`,
  `panel_equiment_artifactstooltip`) get the active set through
  `ToClient_getLightStoneSet`, `ToClient_getLightStoneSetByInvenSlotNo` and
  `ToClient_getLightStoneSetByFromLifeEquipSlotNo` and write it to the set
  option text.

## In-Game Checks

### Amplified Lightstones of Flora

Needs item (all):

- [Lightstone of Flora: Wildlife](https://bdocodex.com/us/item/764001/), or any other Lightstone of Flora (`764001` to `764021`)
- [Crystallized Energy of Endtimes](https://bdocodex.com/us/item/821252/) x30
- [Magical Shard](https://bdocodex.com/us/item/4918/) x50
- [Magical Lightstone Crystal](https://bdocodex.com/us/item/766108/) x100

The LOC description of Crystallized Energy of Endtimes gives the Amplified
Lightstone recipe: Heating "Lightstone (any type) x1" with the three
materials above. Heat a Lightstone of Flora with them. If it gives an
Amplified Lightstone of Flora (item `764001` + 200 = `764201` for Wildlife),
the 21 substitute rows from `764201` to `764221` are live items whose name
and icon the client lacks. If Heating rejects a Flora Lightstone, they are
rows for items the game does not hand out.
