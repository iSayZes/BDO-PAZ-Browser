# `petpcroom.dbss` Format

## Purpose

The equip skills of the PC room pets: each row is a pet key from
[`pet.dbss`](pet_dbss.md) and three `equip_skill_id`s from Section 1 of
[`petequipskill.bss`](petequipskill_bss.md). Companion
`petpcroomoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------------- | --------- |
| 1      | 1485 and later | 3474    | `petpcroom.dbss`       | 144   | 10 Row        | 14        |
| 1      | 1485 and later | 3474    | `petpcroomoffset.dbss` | 104   | 10 Offset Row | 10        |

| Layout | File                   | Known          | Unknown    |
| ------ | ---------------------- | -------------- | ---------- |
| 1      | `petpcroom.dbss`       | 144 B (100.0%) | 0 B (0.0%) |
| 1      | `petpcroomoffset.dbss` | 104 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                                     |
| ---------------------- | -------- | ------------------------------------------------------------------------ |
| `petpcroomoffset.dbss` | Optional | `pet_id -> (offset, size)` of every row; the parser walks the main file without it |
| `petequipskill.bss`    | Optional | `equip_skill_id -> skill_no`, for the skill names (LOC type 10)          |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

The rows fill the file exactly: 4 + 10 x 14 = 144 bytes on client 3474.

### Row (14 bytes)

| Offset  | Type | Field            | Notes                                                                        |
| ------- | ---- | ---------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id           | Row key; the `pet_id` of a [`pet.dbss`](pet_dbss.md) record                  |
| `+0x02` | u32  | equip_skill_id_0 | Section 1 `equip_skill_id` of [`petequipskill.bss`](petequipskill_bss.md)    |
| `+0x06` | u32  | equip_skill_id_1 | Section 1 `equip_skill_id` of `petequipskill.bss`                            |
| `+0x0A` | u32  | equip_skill_id_2 | Section 1 `equip_skill_id` of `petequipskill.bss`                            |

The rows have no padding: the client 1784 server loader fills a 24-byte
entry with the key at `+0x00` and the three skill ids at `+0x04`, `+0x08`
and `+0x0C`, and the file packs those members back to back.

### `petpcroomoffset.dbss`

Bare offset table into `petpcroom.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `petpcroom.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (10 bytes)

| Offset  | Type | Field  | Notes                                                                 |
| ------- | ---- | ------ | --------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id | Key of the row it points at                                           |
| `+0x02` | u32  | offset | Absolute byte offset of the row in `petpcroom.dbss`, at its `pet_id`  |
| `+0x06` | u32  | size   | The whole row: always `14`                                            |

Both files list the keys in the same order: 55663 first, then 55672 down
to 55664. The offset points at the row's own key, as in
[`petdetectposition.dbss`](petdetectposition_dbss.md).

## PC Room Pets

On client 3474 the ten rows key the pets `55663` to `55672`, one each of
ten species (Puppy, Red Panda, Panda, Polar Bear, Desert Fox, Young
Griffon, Newborn Crimson Dragon, Hawk, Hedgehog, Cat), all `tier` `3` and
all with `pc_room_type` `1` in `pet.dbss`. `pet.dbss` sets `pc_room_type`
on ten more pets, `56572` to `56581` (`tier` `4`, the same ten species),
which have no row here; they are not in the client 1784 `Pet_Table` sheet.

Every row has `equip_skill_id_0` `4` (Combat EXP +5%). `equip_skill_id_1`
is `41` (Skill EXP +5%), `38` (Life EXP +5%), `39` (Weight Limit +50 LT)
or `13` (Death Penalty Resistance +4%), and `equip_skill_id_2` one of
`9`, `10`, `11`, `13`, `40`, `41`, `42`. The names are the LOC type 10
names of the catalog's `skill_no` (client 3474).

## Field Names

The `Pet_PcRoom_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `CharacterKey`, `Skillindex_0`, `Skillindex_1`
and `Skillindex_2`, and its 10 rows match the file on all 10 keys and all
three skill columns (clients 1784 and 3474). The developer workbook
(`datasheet_petdatatable.xlsm`) adds note columns: `#CharName` names each
pet with a `_PC방` (PC room) suffix (`반려동물_황백 악동개_T4_PC방` for
`55663`), and `#SkillName_0` to `#SkillName_2` name each skill index with
the skill Section 1 of `petequipskill.bss` holds at that `equip_skill_id`
(`전투 경험치 +5%`, combat EXP +5%, for `4`; `행운 1단계`, luck level 1,
for `9`). `CharacterKey` is the `pet.dbss` key, named `pet_id` there.

The client 1784 server dump names the type `gc::PetPcRoomStaticStatus`,
held in a `BinaryUnorderedMap` keyed by `KeyType<unsigned short>`, with the
manager `PetPcRoomStaticStatusManager`. Its sheet loader (VA `0x14086f440`)
reads `CharacterKey` with `ReadCellInt` and keeps the low u16 at `+0x00`,
then formats `Skillindex_%#` for indexes 0 to 2 and reads each with
`ReadCellInt` into a 4-byte slot at `+0x04`, `+0x08` and `+0x0C`. Each slot
starts at `43` (`0x2B`) before the read, one past the last Section 1
`equip_skill_id`. The 2016 client's debug symbols and the client 519
server tables have no PC room pet type.

## Notes

- Clients 1485, 1784, 2107, 2519, 3002, 3251 and 3474 have the same
  144-byte file and 104-byte offset file, byte for byte. Clients 794 and
  1230 have neither file. The private server's own compiled
  `petpcroom.dbss` and `petpcroomoffset.dbss` (client 1784) are the same
  bytes as the client files.
- `pet.dbss` gives all 20 PC room pets `acquire_type_id` `0`, the same
  roll group as 344 other pets (client 3474), so the roll tables in
  [`petequipskillaquire.dbss`](petequipskillaquire_dbss.md) do not single
  them out.
- The client Lua of the pet list (`panel_window_petlist_all`) shows the
  PC room parts only in a premium PC room with the content group
  `_ContentsGroup_PcRoomPet`: it adds `ToClient_getPetUseMaxCountPcRoom()`
  to the summon limit, filters pets by `getPetStaticStatus():isOnlyPcRoom()`
  and registers the pets with `ToClient_requestPetForPcRoomRegister()`. No
  client Lua reads the skill indexes.
- The NA/EU LOC (client 3474) has no PC room pet text; the pet names in the
  PC Room Pets section are the LOC type 6 names of the pet keys.

## Open Questions

### How the Server Applies the Three Skills

The rows give each PC room pet three fixed equip skills, while other pets
roll theirs from `petequipskillaquire.dbss`. Whether the server gives the
three skills in place of a roll or on top of it, and why the second set of
PC room pets (`56572` to `56581`) has no row, cannot be read from the
client data.
