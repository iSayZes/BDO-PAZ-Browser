# `socialaction.dbss` Format

## Purpose

The social actions (emotes) of the Social Actions window: one row per action
with its Korean name, the condition script that unlocks it, the chat
command and keywords that play it, the action chart name, the icon, the
Korean condition message and its contents groups. The window
(`panel_socialaction.luac`) reads the rows through
`ToClient_getSocialActionInfoList()`, `ToClient_getSocialActionInfoByIndex()`
and `ToClient_getSocialActionStaticStatusByKey()` and their getters
`getName()`, `getCommand()`, `getKeywordBuffer()`, `getIconPath()` and
`getConditionMessage()`. Companion `socialactionoffset.dbss` lists where
every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records       | Row bytes                    |
| ------ | -------------- | ------- | ------------------------- | ------ | ------------- | ---------------------------- |
| 2      | 3251 and later | 3482    | `socialaction.dbss`       | 82,933 | 86 Row        | 199 to 3,888, 964 on average |
| 2      | 3251 and later | 3482    | `socialactionoffset.dbss` | 864    | 86 Offset Row | 10                           |
| 1      | 1348 to 3002   | 3002    | `socialaction.dbss`       | 49,041 | 73 Row        | 198 to 3,771, 672 on average |
| 1      | 1348 to 3002   | 3002    | `socialactionoffset.dbss` | 734    | 73 Offset Row | 10                           |

| Layout | File                      | Known            | Unknown      |
| ------ | ------------------------- | ---------------- | ------------ |
| 2      | `socialaction.dbss`       | 82,503 B (99.5%) | 430 B (0.5%) |
| 2      | `socialactionoffset.dbss` | 864 B (100.0%)   | 0 B (0.0%)   |
| 1      | `socialaction.dbss`       | 48,749 B (99.4%) | 292 B (0.6%) |
| 1      | `socialactionoffset.dbss` | 734 B (100.0%)   | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                                       |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------ |
| `socialactionoffset.dbss` | Optional | `social_action_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`     | Optional | LOC type 15, `str_id1` = `social_action_key`: `str_id4` `0` name, `1` chat command, `2` keywords, `3` condition message |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 77 bytes + texts and contents groups)

| Offset                       | Type                        | Field                           | Notes                                                                                           |
| ---------------------------- | --------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------- |
| `+0x00`                      | u16                         | social_action_key               | Row key; the rows are in no key order (client 3482 opens with 96, 79, 78)                       |
| `+0x02`                      | u16                         | social_action_key_dup           | Equals `social_action_key` on every row; the index points here                                 |
| `+0x04`                      | str16                       | name_kr                         | Korean name (`손 흔들기`, Wave)                                                                  |
| `name_kr+0x00`               | str16                       | condition                       | Unlock script (`checksocialaction(96);checkclass(0);<or>...`, `getLevel()>9`); empty on 15 rows of client 3482 |
| `condition+0x00`             | str16                       | chatting_command_kr             | Korean chat command (`손`)                                                                       |
| `chatting_command_kr+0x00`   | u32                         | chatting_command_hash           | `key_hash()` of the lower-cased command; 86 of 86 rows on client 3482                           |
| `chatting_command_kr+0x04`   | str16                       | chatting_keywords_kr            | Korean chat keywords, `;`-separated (`하이;ㅎㅇ`)                                                |
| `chatting_keywords_kr+0x00`  | str8                        | action_name                     | Action chart name (`SOCIAL_Bye`)                                                                |
| `action_name+0x00`           | u32                         | action_hash                     | `ascii_key_hash()` of `action_name`; 86 of 86 rows on client 3482                               |
| `action_name+0x04`           | str16                       | icon_path                       | Icon under `ui_texture/icon/` (`New_Icon/10_SocialAction/SocialAction0006.dds`)                 |
| `icon_path+0x00`             | str16                       | condition_message_kr            | Korean text the window shows for a locked action; empty on 28 rows of client 3482               |
| `condition_message_kr+0x00`  | u32                         | contents_group_count            | Number of `contents_group_hashes`, `1` to `3` on client 3482                                    |
| `condition_message_kr+0x04`  | u32[contents_group_count]   | contents_group_hashes           | Contents groups as `key_hash()` of their decimal key; group `0` is `0x6016CFF7`                 |
| `contents_group_hashes+0x00` | u32                         | unknown_contents_group_hashes_00 | `0` on every row of clients 1784 and 3482                                                      |
| `contents_group_hashes+0x04` | u8                          | unknown_contents_group_hashes_04 | `0`, `1` or `2`; see Open Questions                                                            |

The hash functions are in `_common/string_hash.py`; the contents group keys
behind the hashes come from `_common/contents_group.py`, and all 100 hashes
of client 3482 resolve.

### `socialactionoffset.dbss`

Bare offset table into `socialaction.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                |
| ------- | ----------------- | ----- | ------------------------------------ |
| `+0x00` | u32               | count | Equals the `socialaction.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                       |

### Offset Row (10 bytes)

| Offset  | Type | Field             | Notes                                                                               |
| ------- | ---- | ----------------- | ----------------------------------------------------------------------------------- |
| `+0x00` | u16  | social_action_key | Key of the row it points at                                                         |
| `+0x02` | u32  | data_offset       | Absolute offset in `socialaction.dbss` of the row's `social_action_key_dup`, 2 bytes past the row start |
| `+0x06` | u32  | data_size         | The row without its leading `social_action_key`                                     |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order; on client 3482 every index row points at the row
with its key.

## Layout 1

No `unknown_contents_group_hashes_04` byte at the end of the row. Only the
Row differs from Layout 2.

### Row (variable: 76 bytes + texts and contents groups)

| Offset                       | Type                        | Field                            | Notes                       |
| ---------------------------- | --------------------------- | -------------------------------- | --------------------------- |
| `+0x00`                      | u16                         | social_action_key                |                             |
| `+0x02`                      | u16                         | social_action_key_dup            |                             |
| `+0x04`                      | str16                       | name_kr                          |                             |
| `name_kr+0x00`               | str16                       | condition                        |                             |
| `condition+0x00`             | str16                       | chatting_command_kr              |                             |
| `chatting_command_kr+0x00`   | u32                         | chatting_command_hash            |                             |
| `chatting_command_kr+0x04`   | str16                       | chatting_keywords_kr             |                             |
| `chatting_keywords_kr+0x00`  | str8                        | action_name                      |                             |
| `action_name+0x00`           | u32                         | action_hash                      |                             |
| `action_name+0x04`           | str16                       | icon_path                        |                             |
| `icon_path+0x00`             | str16                       | condition_message_kr             |                             |
| `condition_message_kr+0x00`  | u32                         | contents_group_count             |                             |
| `condition_message_kr+0x04`  | u32[contents_group_count]   | contents_group_hashes            |                             |
| `contents_group_hashes+0x00` | u32                         | unknown_contents_group_hashes_00 | `0` on every row (client 1784) |

## Field Names

The 2016 `gc::SocialActionStaticStatus` holds `_key`, `_name`,
`_conditionString`, `_conditions` (parsed, not stored), `_chattingCommand`,
`_chattingCommandHash`, `_chattingKeywordBuffer`, `_actionName`,
`_actionHashKey`, `_iconPath` and `_conditionMessage` in the file's order.
The `SocialAction_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Index`, `SocialActionName`, `UseCondition`,
`ChattingCommand`, `ChattingKeyword`, `ActionName`, `ActionName_Mount`,
`IconImage`, `ConditionMessage` and `ContentsGroupKey` (a comma list), 64
rows; client 3482 shares 56 keys with it.

| Field                 | Column             | Same value (client 3482) |
| --------------------- | ------------------ | ------------------------ |
| social_action_key     | `Index`            | 56 of 56                 |
| name_kr               | `SocialActionName` | 56 of 56                 |
| condition             | `UseCondition`     | 16 of 56                 |
| chatting_command_kr   | `ChattingCommand`  | 56 of 56                 |
| chatting_keywords_kr  | `ChattingKeyword`  | 56 of 56                 |
| action_name           | `ActionName`       | 56 of 56                 |
| icon_path             | `IconImage`        | 56 of 56                 |
| condition_message_kr  | `ConditionMessage` | 52 of 56                 |
| contents_group_hashes | `ContentsGroupKey` | 39 of 56                 |

The `condition` misses are level and quest checks client 3482 has where the
sheet column is empty (`getLevel()>9` on key `15`); the struct member
`_conditionString` names the field. The contents group misses drop a group
the sheet lists (`3,27,111` against `3,27` on key `30`). `ActionName_Mount`
is empty on every sheet row and has no field.

## Notes

- LOC type 15 holds the English text by `social_action_key`: `str_id4` `0`
  name (`Wave`), `1` chat command (`Hand`), `2` keywords (`What's up;Yo`),
  `3` condition message.
- Keys `61` and `62` have the commands `O` and `X`; their hashes are of `o`
  and `x`, so the client lower-cases a command before hashing it.

## Open Questions

### What the Last Byte Selects

`unknown_contents_group_hashes_04` is `2` on 20 rows of client 3482 (keys
`73` to `90`, `94` and `96`; most of their condition messages name the
Pearl Shop or an event), `0` on keys `54`, `60` and `92` (sweeping while
moving, the graduation cap throw and the snowboard) and `1` on the other
63. Client 1784 has no such byte. No Lua getter reads it.

### What the Zero After the Contents Groups Holds

`unknown_contents_group_hashes_00` is `0` on every row of clients 1784 and
3482. It may be the count of a second, always empty list, or the hash of
the empty `ActionName_Mount` column.
