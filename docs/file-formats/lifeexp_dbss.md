# `lifeexp.dbss` Format

## Purpose

EXP tables of the life skills (Gathering, Fishing, Hunting, Cooking, Alchemy, Processing, Training, Trading, Farming, Sailing, Barter and four spare slots). Each row gives the EXP one life skill needs to go from one level to the next, from level 0 to the max level. Companion `lifeexpoffset.dbss` lists where every row sits, and [lifeexpmaxlevel](lifeexpmaxlevel_bss.md) holds the max level per life skill. The client shows a level as a rank and a number (`Guru 12` is level 92), see Rank Groups.

Example:

```text
Gathering  Lv 1    Beginner 1    EXP 400
Fishing    Lv 1    Beginner 1    EXP 200
Gathering  Lv 81   Guru 1        EXP 41,166,000
Gathering  Lv 180  Guru 100      EXP 1,165,424,299,500
```

## Companion Files

| File                  | Required | Role                                                                    |
| --------------------- | -------- | ----------------------------------------------------------------------- |
| `lifeexpoffset.dbss`  | Required | `(life skill, level) -> (offset, size)` of every row                    |
| `lifeexpmaxlevel.bss` | Optional | Max level per life skill, see [lifeexpmaxlevel](lifeexpmaxlevel_bss.md) |
| `stringtable.bss`     | Optional | Hashes of the `GAME` sheet keys that name the life skills and ranks     |

All multi-byte values are little-endian.

## File Layout

| Offset  | Type    | Field       | Notes                                                    |
| ------- | ------- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32     | skill_count | Number of life skill blocks; 15 on client 3464, the client's `Type_Count` |
| `+0x04` | block[] | blocks      | `skill_count` blocks, one per life skill in ID order     |

### Block (repeated `skill_count` times)

| Offset  | Type  | Field       | Notes                                                        |
| ------- | ----- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u32   | level_count | Rows in this block; 181 (levels 0 to 180) on client 3464     |
| `+0x04` | row[] | rows        | `level_count` rows of 13 bytes                               |

The blocks fill the file exactly: 4 + 15 x (4 + 181 x 13) = 35,359 bytes on client 3464.

## Record Structure

### Level Row (13 bytes)

| Offset  | Type | Field      | Notes                                                       |
| ------- | ---- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u8   | life_skill | Life skill ID, see Life Skills; equals the block index      |
| `+0x01` | u32  | level      | `0` to the max level, ascending inside a block               |
| `+0x05` | u64  | exp        | EXP to go from `level` to `level + 1`, the demand the client's EXP bar divides by (Notes) |

## Enum Values

### Life Skills

The IDs and names come from `global_define_cpp_enum.luac`: `CppEnums.LifeExperienceType` numbers the life skills and `CppEnums.LifeExperienceString` names each one with a `GAME` sheet key. The English column is the LOC type 37 text of that key. The order matches the life skill parameter of buff effect types 80 and 149 in [buff](buff_dbss.md).

| ID  | Enum          | Name key                            | English    |
| --- | ------------- | ----------------------------------- | ---------- |
| 0   | `gather`      | `LUA_SELFCHARACTERINFO_GATHER`      | Gathering  |
| 1   | `fishing`     | `LUA_SELFCHARACTERINFO_FISH`        | Fishing    |
| 2   | `hunting`     | `LUA_SELFCHARACTERINFO_HUNT`        | Hunting    |
| 3   | `cooking`     | `LUA_SELFCHARACTERINFO_COOK`        | Cooking    |
| 4   | `alchemy`     | `LUA_SELFCHARACTERINFO_ALCHEMY`     | Alchemy    |
| 5   | `manufacture` | `LUA_SELFCHARACTERINFO_MANUFACTURE` | Processing |
| 6   | `training`    | `LUA_SELFCHARACTERINFO_OBEDIENCE`   | Training   |
| 7   | `trade`       | `LUA_SELFCHARACTERINFO_TRADE`       | Trading    |
| 8   | `growth`      | `LUA_SELFCHARACTERINFO_GROWTH`      | Farming    |
| 9   | `sail`        | `LUA_SELFCHARACTERINFO_SAIL`        | Sailing    |
| 10  | `temp1`       | none, Korean `예비1` ("spare 1")    |            |
| 11  | `barter`      | `LUA_SELFCHARACTERINFO_BARTER`      | Barter     |
| 12  | `temp2`       | none, Korean `예비2`                |            |
| 13  | `temp3`       | none, Korean `예비3`                |            |
| 14  | `temp4`       | none, Korean `예비4`                |            |

The handlers show the spare slots by their enum name.

### Rank Groups

`PaGlobalFunc_Util_CraftLevelReplace` in `global_util.luac` turns a level into the rank text: the group key's LOC text, then the level minus the levels of the groups below it. `panel_transferlifeexperience_all.luac` shows life skill levels with the same keys.

| Levels    | Key                                    | English      | Shown as                    |
| --------- | -------------------------------------- | ------------ | --------------------------- |
| 1 to 10   | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_1` | Beginner     | Beginner 1 to Beginner 10   |
| 11 to 20  | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_2` | Apprentice   | Apprentice 1 to 10          |
| 21 to 30  | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_3` | Skilled      | Skilled 1 to 10             |
| 31 to 40  | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_4` | Professional | Professional 1 to 10        |
| 41 to 50  | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_5` | Artisan      | Artisan 1 to 10             |
| 51 to 80  | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_6` | Master       | Master 1 to 30              |
| 81 to 180 | `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_7` | Guru         | Guru 1 to 100               |

Level 0 has no rank; the Lua function falls through and returns the bare level.

## lifeexpoffset.dbss

Index into `lifeexp.dbss`, with the same block shape as the main file, including the leading skill count.

| Offset  | Type    | Field       | Notes                                          |
| ------- | ------- | ----------- | ---------------------------------------------- |
| `+0x00` | u32     | skill_count | Equals the `lifeexp.dbss` skill count           |
| `+0x04` | block[] | blocks      | `skill_count` blocks                           |

### Block (repeated `skill_count` times)

| Offset  | Type  | Field       | Notes                              |
| ------- | ----- | ----------- | ---------------------------------- |
| `+0x00` | u32   | level_count | Rows in this block (181 on client 3464) |
| `+0x04` | row[] | rows        | `level_count` rows of 12 bytes     |

The block index is the life skill; the file stores no life skill field. 4 + 15 x (4 + 181 x 12) = 32,644 bytes on client 3464.

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                           |
| ------- | ---- | ----------- | --------------------------------------------------------------- |
| `+0x00` | u32  | level       | Level of the row it points at                                   |
| `+0x04` | u32  | data_offset | Absolute byte offset of the 13-byte row in `lifeexp.dbss`       |
| `+0x08` | u32  | data_size   | Always 13                                                       |

The first Gathering row sits at `0x08`, after the skill count and Gathering's level count; each later block starts 4 bytes past the previous block's last row. The parser reads the main file through these rows and checks that each row's `life_skill` and `level` match the offset row's block and key.

## Suggested UI Layout

### lifeexp.dbss

| Column        | Type | Notes                                                      |
| ------------- | ---- | ---------------------------------------------------------- |
| Life Skill ID | num  | `life_skill`                                               |
| Life Skill    | text | Name from the Life Skills table, the enum name for spares  |
| Level         | num  | `level`                                                    |
| Rank          | text | `Guru 12`, from Rank Groups; a dash on level 0; not sortable, Level sorts the same way |
| EXP to Next Level | num | `exp`                                                    |

### lifeexpoffset.dbss

| Column        | Type | Notes                          |
| ------------- | ---- | ------------------------------ |
| Life Skill ID | num  | Block index (`life_skill`)     |
| Level         | num  | `level`                        |
| Data Offset   | num  | `data_offset`, as hex          |
| Data Size     | num  | `data_size`                    |

## Notes

- Observed on client 3464: twelve of the fifteen blocks hold the same EXP on every level (IDs 0, 2 to 6, 8 to 10 and 12 to 14). Fishing (1) needs less on levels 1 to 128 (level 1: 200 against 400) and matches them from level 129 up. Barter (11) has its own curve on every level but 0.
- Trading (7) holds finite EXP up to level 60 (212,980,644 to go from Master 10 to Master 11), then `999,999,999,999` on levels 61 to 130 and `9,999,999,999,999` on levels 131 to 180, so Trading stops at Master 11 (level 61), while [lifeexpmaxlevel](lifeexpmaxlevel_bss.md) still gives it 180.
- The shared curve and Barter both change pace at level 131: Barter rises by about 8,150 EXP per level on levels 125 to 130, then 13% per level from 131 (4,104,606 on 130, 4,638,200 on 131). Trading's second sentinel starts on the same level.
- Every block starts with level 0 at `100` EXP, `20` for Trading.
- The client reads a life skill's level and EXP through `getLifeExperienceLevel`, `getCurrLifeExperiencePoint` and `getDemandLifeExperiencePoint` (`panel_transferlifeexperience_all.luac`) and draws the bar as current / demand, so EXP restarts at 0 on every level.
- The level-up notice (`nakmessage_life.luac`) names the rank groups `__eLifeGrade_Master` and `__eLifeGrade_GURU` in its constants.
- `fitnesslevel.dbss` uses the same block shape with 29-byte rows and is read with the same row direction; see [fitnesslevel](fitnesslevel_dbss.md).
- Row direction, checked 2026-10-09 with a packet capture while gathering at Gathering Master 8 (level 58): the server sends the current EXP in message `0x1C91` (u64 current EXP, u8 life skill, u32 level). It went from 6,601,966 to 6,608,284 while the in-game bar went from 44.41% to 44.45%, which is current EXP divided by the level 58 row (14,865,500: 44.41% to 44.45%), not the level 59 row (15,935,300: 41.43%). So the row of level N is the EXP to go from N to N + 1.
