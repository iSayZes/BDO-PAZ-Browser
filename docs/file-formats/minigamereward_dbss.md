# `minigamereward.dbss` Format

## Purpose

The energy and item drop of three minigames, one row each: the energy of a
success and of a failure, the `itemmaingroup.bss` drop group a success
gives, and the vehicle type the player must be on. On client 3474 the rows
are minigame `1` on a Cow (vehicle type `26`, group 65021: Milk), `2` on a
herbal machine (`24`, group 65023: Sunrise Herb, Silver Azalea and the other
herbs) and `3` on an extractor (`25`, group 65022: Black Stone Powder, Rough
Stone).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | ------------ | --------- |
| 2      | 3002 and later | 3474    | `minigamereward.dbss`       | 43    | 3 Row        | 13        |
| 2      | 3002 and later | 3474    | `minigamerewardoffset.dbss` | 34    | 3 Offset Row | 10        |
| 1      | 1485 to 2519   | 2519    | `minigamereward.dbss`       | 37    | 3 Row        | 11        |
| 1      | 1485 to 2519   | 2519    | `minigamerewardoffset.dbss` | 34    | 3 Offset Row | 10        |

| Layout | File                        | Known         | Unknown    |
| ------ | --------------------------- | ------------- | ---------- |
| 2      | `minigamereward.dbss`       | 43 B (100.0%) | 0 B (0.0%) |
| 2      | `minigamerewardoffset.dbss` | 34 B (100.0%) | 0 B (0.0%) |
| 1      | `minigamereward.dbss`       | 37 B (100.0%) | 0 B (0.0%) |
| 1      | `minigamerewardoffset.dbss` | 34 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                              |
| ----------------------------- | -------- | ----------------------------------------------------------------- |
| `minigamerewardoffset.dbss`   | Optional | `minigame_key -> (data_offset, data_size)` index; the rows are fixed size and can be walked without it |
| [`itemmaingroup.bss`](itemmaingroup_bss.md) | Optional | The drop group a `drop_group` names; the handler links each group to its row |
| `itemsubgroup.dbss`, `itemsubgroupoffset.dbss` | Optional | The items of the drop group's subgroups |

Item names come from LOC type 0.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `3` on client 3474           |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (13 bytes)

| Offset  | Type | Field              | Notes                                                                    |
| ------- | ---- | ------------------ | ------------------------------------------------------------------------ |
| `+0x00` | u16  | minigame_key       | Minigame; unique per row, the index key                                  |
| `+0x02` | u16  | minigame_key_dup   | Equal to `minigame_key` in every row; the index's `data_offset` points here |
| `+0x04` | i16  | success_wp         | Energy (WP) on a success; see Open Questions                            |
| `+0x06` | i16  | fail_wp            | Energy (WP) on a failure                                                 |
| `+0x08` | u32  | drop_group         | `itemmaingroup.bss` group a success gives                                |
| `+0x0C` | u8   | check_vehicle_type | `CppEnums.VehicleType` the player must be on: `24`, `25` or `26` (client 3474) |

The rows are stored in key order `3`, `2`, `1` on clients 1784 and 3474.

### `minigamerewardoffset.dbss`

| Offset  | Type              | Field | Notes                                     |
| ------- | ----------------- | ----- | ----------------------------------------- |
| `+0x00` | u32               | count | Equals the `minigamereward.dbss` count    |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row      |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                   |
| ------- | ---- | ------------ | --------------------------------------- |
| `+0x00` | u16  | minigame_key | Row key                                 |
| `+0x02` | u32  | data_offset  | Row start + 2, at `minigame_key_dup`    |
| `+0x06` | u32  | data_size    | Row size - 2: `11` on client 3474       |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order; on clients 1784 and 3474 every index row points at
the row with its key.

## Layout 1

### Row (11 bytes)

| Offset  | Type | Field              | Notes                                                |
| ------- | ---- | ------------------ | ---------------------------------------------------- |
| `+0x00` | u16  | minigame_key       | Minigame                                             |
| `+0x02` | u16  | minigame_key_dup   | Equal to `minigame_key` in every row                 |
| `+0x04` | i16  | success_wp         | Energy (WP) on a success                             |
| `+0x06` | i16  | fail_wp            | Energy (WP) on a failure                             |
| `+0x08` | u16  | drop_group         | `itemmaingroup.bss` group a success gives            |
| `+0x0A` | u8   | check_vehicle_type | `CppEnums.VehicleType` the player must be on         |

`drop_group` is u16 here and u32 in Layout 2; the index's `data_size` is
`9`.

## Field Names

The row is the 2016 `gc::MiniGameRewardStaticStatus` in member order:
`_key` (u16), `_successWp` (short), `_failWp` (short), `_dropKey` (u16, with
a pointer to its `gc::ItemMainGroupStaticStatus` that the file does not
store) and `_checkVehicleType` (`gc::VehicleType`). The 2016 drop key is
u16, as in Layout 1.

The values match the `MiniGameReward` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `MiniGameKey`, 3 of 3 keys on clients
1784 and 3474 in every column:

| Field                | Column         | Same value (client 1784) | Same value (client 3474) |
| -------------------- | -------------- | ------------------------ | ------------------------ |
| `minigame_key`       | `MiniGameKey`  | 3 of 3                   | 3 of 3                   |
| `success_wp`         | `SuccessWp`    | 3 of 3                   | 3 of 3                   |
| `fail_wp`            | `FailWp`       | 3 of 3                   | 3 of 3                   |
| `drop_group`         | `DropGroup`    | 3 of 3                   | 3 of 3                   |
| `check_vehicle_type` | `CheckVehicle` | 3 of 3                   | 3 of 3                   |

The sheet's developer comment on `MiniGameKey` (`DataSheet_MiniGameReward.xlsm`)
names the keys: `1` 소 (cow), `2` 약탕기 (herbal machine), `3` 추출장
(extractor). They match the vehicle types the rows check: `26` Cow, `24`
QuestObjectHerbalMachines and `25` QuestObjectExtractor in
`CppEnums.VehicleType` (`_common/vehicle_type.py`).

WP is the client's name for energy: `panel_characterinfo_basic_all_3.luac`
writes `getWp()` / `getMaxWp()` into the character window's
`StaticText_Energy` control.

## Notes

- The drop groups on client 3474: 65021 holds subgroups 65021, 49477 and
  49478, which give Milk (9065) and Gathering EXP (350); 65022 gives Black
  Stone Powder (4901) or Rough Stone (4006); 65023 gives one of 11 herbs
  (5401 to 5406, 5421 to 5425).
- On client 3474, minigame `1` has `success_wp` 10 and `fail_wp` 4, the
  other two 5 and 2. The `MiniGameReward` table of a private server on
  client 519 has 5 and 2 for all three keys, with the same drop groups and
  vehicle types.
- The client 794 and 1230 builds do not ship the file.

## Open Questions

### Energy Taken or Given

The sheet calls the columns `SuccessWp` and `FailWp` and both are positive
on every row. The BdoEmu server code on client 519
(`CMMiniGameResult.java`) subtracts `SuccessWp` from the player's energy on
a success, then gives the drop group's items, and subtracts `FailWp` on a
failure. That code is a reconstruction, not Pearl Abyss's server; the client
Lua (`luacscript/x64/widget/minigame/`) only sends the result through
`SetMiniGameResult` and shows no energy change.
