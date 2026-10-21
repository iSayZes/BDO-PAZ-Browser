# `personalmonster.dbss` Format

## Purpose

The Dark Rift bosses (`어둠의 틈`, `panel_window_personalmonster_all`):
per boss character a Korean description, a difficulty, a world map image
and the items it drops. On client 3474 the file has 6 rows, Red Nose,
Dastard Bheg, Ahib Griffon, Muskan, Dim Tree Spirit and Ferrid, all with
the same 13 drop items. The spawn points are in
[`personalmonsterposition.dbss`](personalmonsterposition_dbss.md) and the
world map icon settings in
[`personalmonsteretc.bss`](personalmonsteretc_bss.md). Companion
`personalmonsteroffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records      | Row bytes                  |
| ------ | -------------- | ------- | ---------------------------- | ----- | ------------ | -------------------------- |
| 1      | 1485 and later | 3474    | `personalmonster.dbss`       | 1,120 | 6 Row        | 179 to 197, 186 on average |
| 1      | 1485 and later | 3474    | `personalmonsteroffset.dbss` | 64    | 6 Offset Row | 10                         |

| Layout | File                         | Known           | Unknown     |
| ------ | ---------------------------- | --------------- | ----------- |
| 1      | `personalmonster.dbss`       | 1,096 B (97.9%) | 24 B (2.1%) |
| 1      | `personalmonsteroffset.dbss` | 64 B (100.0%)   | 0 B (0.0%)  |

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
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                     |
| ---------------------------- | -------- | ------------------------------------------------------------------------ |
| `personalmonsteroffset.dbss` | Optional | `character_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `characterstaticoffset.dbss` | Optional | Which character keys have a `characterstatic.dbss` row, for the key link |
| `languagedata_en.loc`        | Optional | Boss names (type `6`), descriptions (type `61`), item names (type `0`) and the difficulty labels (type `37`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 30 bytes + description, image path and drop items)

| Offset                | Type                    | Field                     | Notes                                                                      |
| --------------------- | ----------------------- | ------------------------- | -------------------------------------------------------------------------- |
| `+0x00`               | u16                     | character_key             | The boss, a `characterstatic.dbss` key                                     |
| `+0x02`               | str16                   | description_kr            | Korean description; LOC type `61` holds it under `character_key`           |
| `description_kr+0x00` | u32                     | difficulty                | `1` to `3`; see Difficulty                                                 |
| `description_kr+0x04` | str8                    | monster_image             | Image path under `ui_texture/` (`UI_Artwork/IC_04013.dds`), or empty       |
| `monster_image+0x00`  | u32                     | drop_item_count           | Number of `drop_item_keys`                                                 |
| `monster_image+0x04`  | u32[drop_item_count]    | drop_item_keys            | Item enchant keys (`enchant_level << 24 \| item_id`); every level is `0` on clients 1784 and 3474 |
| `drop_item_keys+0x00` | u32                     | unknown_drop_item_keys_00 | `0` on every row of clients 1784 and 3474                                  |

The rows are not sorted by key.

### `personalmonsteroffset.dbss`

Bare offset table into `personalmonster.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `personalmonster.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                         |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | character_key | Key of the row it points at                                  |
| `+0x02` | u32  | data_offset   | Absolute offset of the row in `personalmonster.dbss`, at its `character_key` |
| `+0x06` | u32  | data_size     | The whole row                                                |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3474 every
index row points at the row with its key, and the rows fill the file.

## Difficulty

`panel_window_personalmonster_all_1.luac` shows `difficulty` through the
`_difficultyText` table of `panel_window_personalmonster_all.luac`, which
reads the GAME sheet keys `LUA_PERSONALMONSTER_DIFFICULTY_1` to `_3`;
difficulty `3` also turns on the special background of the list row.

| Value | GAME key                           | LOC English    | Rows (client 3474) |
| ----- | ---------------------------------- | -------------- | ------------------ |
| 1     | `LUA_PERSONALMONSTER_DIFFICULTY_1` | Normal         | 2                  |
| 2     | `LUA_PERSONALMONSTER_DIFFICULTY_2` | Difficult      | 2                  |
| 3     | `LUA_PERSONALMONSTER_DIFFICULTY_3` | Very Difficult | 2                  |

## Field Names

The `PersonalMonster_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `CharacterKey`, `Difficulty`,
`Description`, `MonsterImage` and `DropItemList`, and the server-only
(`%`) columns `FirstSpawnTime`, `FirstVariableTime`, `SpawnCoolTime`,
`SpawnVariableTime`, `PositionIndex` and `AcceptCondition`, which the file
does not hold. The client 1784 file has 12 rows, and the sheet matches it on
all 12 keys for `Difficulty`, `Description`, `MonsterImage` (empty where
the sheet has none) and `DropItemList` in order. On client 3474 the 6 rows
still match on `Difficulty`, `Description` and `MonsterImage`; every drop
list changed. The sheet's developer notes call the columns the monster key,
the difficulty (`1` easy, `2` normal, `3` hard), the description and image
shown on world map mouse-over, and the item keys the monster drops.

The client Lua of client 3474 reads the row through
`ToClient_GetPersonalMonsterWrapper(characterKey)`: `getDescription()`,
`getDifficult()`, `getDropItemCount()` and `getDropItemKey(index)`, which
it passes to `getItemEnchantStaticStatus(ItemEnchantKey(itemKey))`. The
boss name comes from `ToClient_GetCharacterStaticStatusWrapper`. The 2016
client's debug symbols have no personal monster type.

## Notes

- The sheet on client 1784 has 30 rows; the client file holds the 12 whose
  `ContentsGroupKey` list contains `585` (`585`, `234, 585` or
  `585, 722`), and none of the 18 without it.
- On client 3474 all 6 rows drop the same 13 items, Dawn Black Stone
  (`820984`) to Gold Bar 1,000G (`5`) and Gold Bar 100G (`4`). Every one
  has a LOC type `0` name.
- LOC type `61` has an English description for each of the 6 keys of
  client 3474; it is the text `getDescription()` shows in the loaded
  language.
- The 6 keys of client 3474 all have a `characterstatic.dbss` row and a
  LOC type `6` name.
- `drop_item_count` is a u32 and `difficulty` a u32 by the byte count of
  the row; no value on clients 1784 and 3474 needs more than one byte.

## Open Questions

### unknown_drop_item_keys_00

The last u32 of every row is `0` on clients 1784 and 3474. The sheet's
last client column is `ContentsGroupKey` (`585` on every row the file
holds), so the field is not that list unless the build leaves it out; it
could be the count of a list that is always empty. No Lua getter reads a
fifth value.
