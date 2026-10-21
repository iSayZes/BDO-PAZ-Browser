# `greatseaevent.dbss` Format

## Purpose

The result lines of the Great Ocean sea events
(`panel_widget_greatseaevent`): per event group the events a ship's crew
can meet, each with a Korean result text ("선원이 낡은 상자를
건져올렸습니다!", "a sailor fished up an old box!") and an icon path. When
the server sends `FromClient_GreatSeaEvent(type, ..., groupKey,
selectIndex, regionKey, groupEventType)`, the window shows
`ToClient_getGreatSeaEventResultString(groupKey, selectIndex)` and
`ToClient_getGreatSeaEventImagePath(groupKey, selectIndex)` above the
food, loyalty, HP, item or quest result. On client 3474 the file holds 5
groups and 101 events. Companion `greatseaeventoffset.dbss` lists where
every event sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes  | Records                        | Row bytes                  |
| ------ | -------------- | ------- | -------------------------- | ------ | ------------------------------ | -------------------------- |
| 1      | 1485 and later | 3474    | `greatseaevent.dbss`       | 15,299 | 101 Event, 5 Group             | 139 to 181, 151 on average |
| 1      | 1485 and later | 3474    | `greatseaeventoffset.dbss` | 1,246  | 101 Offset Row, 5 Offset Group | 12                         |

| Layout | File                       | Known            | Unknown      |
| ------ | -------------------------- | ---------------- | ------------ |
| 1      | `greatseaevent.dbss`       | 14,895 B (97.4%) | 404 B (2.6%) |
| 1      | `greatseaeventoffset.dbss` | 1,246 B (100.0%) | 0 B (0.0%)   |

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
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                                   |
| -------------------------- | -------- | ---------------------------------------------------------------------- |
| `greatseaeventoffset.dbss` | Optional | `(group_key, select_index) -> (data_offset, data_size)` of every event; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type               | Field       | Notes                                |
| ------- | ------------------ | ----------- | ------------------------------------ |
| `+0x00` | u32                | group_count | Number of groups                     |
| `+0x04` | Group[group_count] | groups      | See Group; in group key order        |

### Group (variable: 4 bytes + events)

| Offset  | Type                | Field       | Notes     |
| ------- | ------------------- | ----------- | --------- |
| `+0x00` | u32                 | event_count | Number of events |
| `+0x04` | Event[event_count]  | events      | See Event |

### Event (variable: 23 bytes + result text and image path)

| Offset              | Type  | Field                 | Notes                                                          |
| ------------------- | ----- | --------------------- | -------------------------------------------------------------- |
| `+0x00`             | u16   | group_key             | The group's key, the same on every event of a group; `1` to `5` on client 3474 |
| `+0x02`             | u8    | select_index          | `0` to `event_count - 1` within the group                      |
| `+0x03`             | str16 | result_string_kr      | Korean result text; no LOC row holds it                        |
| `result_string_kr+0x00` | str16 | image_path        | Icon path such as `Icon/New_Icon/11_Employee/Explore_0004.dds` |
| `image_path+0x00`   | u32   | unknown_image_path_00 | `0` on every event of clients 1784 and 3474                    |

### `greatseaeventoffset.dbss`

Bare offset table into `greatseaevent.dbss`, in the same groups.

| Offset  | Type                      | Field       | Notes                                      |
| ------- | ------------------------- | ----------- | ------------------------------------------ |
| `+0x00` | u32                       | group_count | Equals the `greatseaevent.dbss` group count |
| `+0x04` | Offset Group[group_count] | groups      | See Offset Group                           |

### Offset Group (variable: 6 bytes + rows)

| Offset  | Type              | Field     | Notes                                   |
| ------- | ----------------- | --------- | --------------------------------------- |
| `+0x00` | u16               | group_key | The group's key                         |
| `+0x02` | u32               | count     | Equals the group's `event_count`        |
| `+0x06` | Offset Row[count] | rows      | See Offset Row                          |

### Offset Row (12 bytes)

| Offset  | Type | Field        | Notes                                        |
| ------- | ---- | ------------ | -------------------------------------------- |
| `+0x00` | u32  | select_index | The event's `select_index`                   |
| `+0x04` | u32  | data_offset  | Event start, at its `group_key`              |
| `+0x08` | u32  | data_size    | The whole event                              |

On clients 1784 and 3474 the index lists the events in file order, and
every row points at the event with its group key and index.

## Groups

The events on client 3474, by group:

| Group | Events | Different texts | Result texts                                                       |
| ----- | ------ | --------------- | ------------------------------------------------------------------ |
| 1     | 27     | 18              | Crew finds, weather and sea events, scurvy, a Cox Pirates attack   |
| 2     | 7      | 6               | Food from islanders, fish, a feast with the Sea Otters             |
| 3     | 7      | 6               | The same six texts as group 2                                      |
| 4     | 30     | 10              | Treasure chests, a whale attack, guards and beasts, island children asking for help, shipwreck materials |
| 5     | 30     | 10              | The same ten texts as group 4                                      |

The 101 events use 34 different texts and 17 icons. Client 1784 has the
same groups with 33 events in groups 4 and 5.

## Field Names

`group_key` and `select_index` are the arguments of
`ToClient_getGreatSeaEventResultString(groupKey, selectIndex)` and
`ToClient_getGreatSeaEventImagePath(groupKey, selectIndex)`, which return
the two texts (`panel_widget_greatseaevent_2.luac`). The client 1784
server dump (`Instance_dumpFull.exe`) names the table
`GreatSeaEventStaticStatus` and logs `GreatSeaGroupKey(%#), Index(%#),
textNo(%#)` for a missing text, and "이미지 경로가 없습니다" ("no image path").

## Notes

- `FromClient_GreatSeaEvent` types are `__eGreatSeaEvent_Food`, `_Loyalty`,
  `_Hp`, `_Item` and `_Quest`; their amounts, items and quests come from the
  server, not from this file.
- Client 1784 has the same layout; its file is 16,221 bytes.

## Open Questions

### unknown_image_path_00

The u32 after the image path is `0` on all 101 events of client 3474 and
all 107 of client 1784. The server dump's checks name a sign ("부호는 0
혹은 1입니다", "the sign is 0 or 1"), a type and an item key for
`GreatSeaEventStaticStatus`; whether the u32 is one of them is open.
