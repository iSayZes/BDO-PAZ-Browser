# `petchangelook.dbss` Format

## Purpose

The looks a pet can change to, per look key: each record holds the looks of
one `change_look_key` of [`pet.dbss`](pet_dbss.md), each look with its
action index (the look the client asks the server for), its icons, a skill
and, from client 3474 on, a Korean skin name. Fairies use the same table (look
key `25001`) for their skins. Companion `petchangelookoffset.dbss` lists
where every record's payload sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes  | Records                           | Row bytes                 |
| ------ | -------------- | ------- | -------------------------- | ------ | --------------------------------- | ------------------------- |
| 2      | 3474 and later | 3474    | `petchangelook.dbss`       | 70,196 | 653 Look, 149 Payload, 149 Record | 99 to 211, 106 on average |
| 2      | 3474 and later | 3474    | `petchangelookoffset.dbss` | 1,494  | 149 Offset Row                    | 10                        |
| 1      | 1485 to 3251   | 3251    | `petchangelook.dbss`       | 58,131 | 619 Look, 145 Payload, 145 Record | 86 to 184, 92 on average  |
| 1      | 1485 to 3251   | 3251    | `petchangelookoffset.dbss` | 1,454  | 145 Offset Row                    | 10                        |

| Layout | File                       | Known             | Unknown        |
| ------ | -------------------------- | ----------------- | -------------- |
| 2      | `petchangelook.dbss`       | 66,931 B (95.3%)  | 3,265 B (4.7%) |
| 2      | `petchangelookoffset.dbss` | 1,494 B (100.0%)  | 0 B (0.0%)     |
| 1      | `petchangelook.dbss`       | 58,131 B (100.0%) | 0 B (0.0%)     |
| 1      | `petchangelookoffset.dbss` | 1,454 B (100.0%)  | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
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

| File                        | Required | Role                                                                          |
| --------------------------- | -------- | ----------------------------------------------------------------------------- |
| `petchangelookoffset.dbss`  | Optional | `change_look_key -> (offset, size)` of every payload; the parser walks the main file without it |
| `pet.dbss` + `petoffset.dbss` | Optional | The LOC names of the pets whose `change_look_key` is the record's key       |

The handler names a look's skill by its LOC type 10 name (`skill_no`).

All multi-byte values are little-endian.

## Layout 2

### File Layout

A record count, then the records back to back. Each record is a 2-byte key
prefix and the payload that `petchangelookoffset.dbss` addresses.

| Offset  | Type          | Field   | Notes             |
| ------- | ------------- | ------- | ----------------- |
| `+0x00` | u32           | count   | Number of records |
| `+0x04` | Record[count] | records | See Record        |

### Record (variable: 2 bytes + payload)

| Offset  | Type    | Field      | Notes                                                 |
| ------- | ------- | ---------- | ----------------------------------------------------- |
| `+0x00` | u16     | key_prefix | Equals `change_look_key`                              |
| `+0x02` | Payload | payload    | `size` bytes; the offset row points at this field     |

### Payload (variable: 6 bytes + looks, size from `petchangelookoffset.dbss`)

| Offset  | Type             | Field           | Notes                                                                 |
| ------- | ---------------- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u16              | change_look_key | The `change_look_key` of [`pet.dbss`](pet_dbss.md); equals the key prefix |
| `+0x02` | u32              | look_count      | Number of looks; 1 to 16 on client 3474                               |
| `+0x06` | Look[look_count] | looks           | See Look                                                              |

### Look (variable: 45 bytes + icon paths and skin name)

| Offset               | Type     | Field                   | Notes                                                                       |
| -------------------- | -------- | ----------------------- | --------------------------------------------------------------------------- |
| `+0x00`              | u32      | action_index            | The look's index, unique within its record                                  |
| `+0x04`              | str8     | icon_path               | Pet window icon (`New_UI_Common_forLua\Window\Stable\Pet\...`)              |
| `icon_path+0x00`     | str8     | icon_path_1             | Fairy skin slot icon; empty except on look key `25001` (fairy skins)        |
| `icon_path_1+0x00`   | str8     | icon_path_2             | Fairy window title image; empty except on look key `25001`                  |
| `icon_path_2+0x00`   | u16      | skill_level             | Level of the look's `gc::SkillKey`; `1` with a skill, else `0`              |
| `icon_path_2+0x02`   | u16      | skill_no                | Skill number of the look's skill (LOC type 10 names it); `0` for none      |
| `icon_path_2+0x04`   | u8       | unknown_icon_path_2_04  | `1` on the six looks with a skill, `0` on the rest (client 3474)           |
| `icon_path_2+0x05`   | str16    | skin_name_kr            | Korean skin name; empty except on ten looks of key `25001`                  |
| `skin_name_kr+0x00`  | u8       | unknown_skin_name_kr_00 | `0` on every look (client 3474)                                             |
| `skin_name_kr+0x01`  | bytes[3] | unknown_skin_name_kr_01 | `63 4F 37` on every look (client 3474)                                      |

### `petchangelookoffset.dbss`

Bare offset table into `petchangelook.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `petchangelook.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                        |

### Offset Row (10 bytes)

| Offset  | Type | Field           | Notes                                                                       |
| ------- | ---- | --------------- | --------------------------------------------------------------------------- |
| `+0x00` | u16  | change_look_key | Key of the record it points at                                              |
| `+0x02` | u32  | offset          | Absolute byte offset in `petchangelook.dbss` of the payload, past the key prefix |
| `+0x06` | u32  | size            | Payload size in bytes, without the key prefix                               |

The offset rows are not in file order; read in offset order they cover the
main file from `+0x04` to its end, each record's key prefix included.

## Layout 1

### Look (variable: 32 bytes + icon paths)

The look ends after the skill: no `unknown_icon_path_2_04`, skin name or
tail bytes.

| Offset             | Type | Field        | Notes                                              |
| ------------------ | ---- | ------------ | -------------------------------------------------- |
| `+0x00`            | u32  | action_index |                                                    |
| `+0x04`            | str8 | icon_path    |                                                    |
| `icon_path+0x00`   | str8 | icon_path_1  |                                                    |
| `icon_path_1+0x00` | str8 | icon_path_2  |                                                    |
| `icon_path_2+0x00` | u16  | skill_level  | `1` on the one look with a skill (client 1784)     |
| `icon_path_2+0x02` | u16  | skill_no     | `49166` on look key `25001`, action index `6`      |

## Fairy Skins

On client 3474 look key `25001` holds the fairy skins. Ten of its looks
store a skin name and both extra icons (`Combine\Etc\...`), six of them a
skill:

| `action_index` | `skin_name_kr`  | `skill_no` | Skill (LOC type 10) |
| -------------- | --------------- | ---------- | ------------------- |
| 5              | 파크 요정       | 0          |                     |
| 6              | 똑딱똑딱 요정   | 49166      | Skill EXP +10%      |
| 7              | 월향화 요정     | 49182      | Death Penalty Resistance +5% |
| 8              | 베네실 요정     | 49183      | Processing EXP +10% |
| 9              | 키벨리우스 요정 | 49182      | Death Penalty Resistance +5% |
| 10             | 흑정령 요정     | 0          |                     |
| 11             | 진혼 요정       | 0          |                     |
| 12             | 명혼 요정       | 0          |                     |
| 18             | 새싹 꼬마 요정  | 49185      | Fishing EXP +20%    |
| 19             | 새벽 꼬마 요정  | 49184      | Combat EXP +200%    |

## Field Names

The `Pet_ChangeLook_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `PetChangeLookKey`, `ActionIndex`,
`IconPath`, `IconPath1`, `IconPath2` and `SkillNo`, and its 560 rows match
the file by (`PetChangeLookKey`, `ActionIndex`) on all 560 looks and all
four value columns, on client 1784 (560 looks) and on client 3474 (653
looks). Empty cells (`<null>`) are the empty strings and the zero
`skill_no` of the file. The 2016 client's debug symbols have
`gc::PetChangeLookStaticStatus` with a u16 `_petChangeLookKey` and a map
from a u32 to `_PET_LOOK_DATA` (`_iconPath` only), the `action_index` to
`icon_path` part of the record. `skill_level` and `skill_no` are one
`gc::SkillKey`, level first, as in
[`petequipskill.bss`](petequipskill_bss.md); `skill_level` is `1` exactly
where `SkillNo` is set.

The client Lua of client 3474 reads the table through
`ToClient_getPetChangeLookCount(petStaticStatus)`,
`ToClient_getPetChangeLook_IconPath(petStaticStatus, lookIndex)` and
`ToClient_getPetChangeLook_ActionIndex(petStaticStatus, lookIndex)` in the
pet look change window (`panel_window_petlookchange_all_1.luac`), which
lists a pet only when it has more than one look and requests the change by
action index. The fairy skin window
(`panel_window_fairyskinchange_all_new_1.luac`) reads a look's
`getIconPath1()`, `getSkinName()`, `getShowSkinList()` and
`getChangeLookSkillKey()`. `skin_name_kr` is the only text field besides
the paths, so it is the skin name; which of the two u8 fields is
`getShowSkinList()` is open.

## Notes

- Layout 2 adds 13 bytes and the skin name text to every look. On client
  3474 the 653 looks are 149 records; on client 1784, 560 looks in 130
  records.
- The pet whose `change_look_key` is `23061` has no record, and nine
  records (`35001`, `49007`, `49009` to `49014`, `49017`) belong to no pet
  of `pet.dbss` (client 3474).
- `unknown_skin_name_kr_01` holds the same three bytes on every look, which
  reads as the unset upper bytes of a 4-byte member whose low byte is
  `unknown_skin_name_kr_00`, as the alignment bytes of
  [`petfusionnew.dbss`](petfusionnew_dbss.md); no source names it.
- The fairy info window (`panel_window_fairy_all_2.luac`) shows the
  current skin's `getIconPath2()` as its title image; the fairy skin window
  shows `getIconPath1()` in each skin slot.

## Open Questions

### The Two u8 Fields of Layout 2

`unknown_icon_path_2_04` is `1` on the six looks with a skill and
`unknown_skin_name_kr_00` is `0` on every look. The fairy skin window reads
`getShowSkinList()` (show a skin the player does not own yet) for each
look; one of the two bytes may be that flag, but the client data does not
tell which, and `unknown_icon_path_2_04` may as well mark the skill as
present.
