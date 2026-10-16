# `petaction.dbss` Format

## Purpose

Defines pet action records keyed by action ID. Each record stores the Korean action name and a UTF-16 icon path for a pet command/reaction such as Like, Feed, Angry, Sleepy, Jump, Sit, Play, Bark, or Dislike. Companion `petactionoffset.dbss` provides the record count and keyed offsets.

Example:

```text
action_id: 0
name_kr:   기쁨 (LOC type 19: Joy)
icon_path: New_Icon/08_Servant_Skill/02_Pet/Action_0_Like.dds
```

## Companion Files

| File                   | Required | Role                                               |
| ---------------------- | -------- | -------------------------------------------------- |
| `petactionoffset.dbss` | Required | `action_id -> (record_offset, record_size)` lookup |
| `languagedata_en.loc`  | Optional | English action names via LOC type 19               |

All multi-byte values are little-endian.

## File Layout

`petaction.dbss` has no standalone header or record count. Records start at byte `0x0000`; use `petactionoffset.dbss` to enumerate them.

| Offset  | Type | Field   | Notes                                         |
| ------- | ---- | ------- | --------------------------------------------- |
| `+0x00` | row  | records | Variable-size record stream; observed 10 rows |

## Record Structure

Records are variable size because both strings are. Observed records are 146-154 bytes. Offsets are relative to `record_offset` from `petactionoffset.dbss`.

| Offset  | Type             | Field           | Notes                                                               |
| ------- | ---------------- | --------------- | ------------------------------------------------------------------- |
| `+0x00` | u32              | action_id       | Primary key; matches offset-table key                               |
| `+0x04` | u32              | reserved_04     | Always 0                                                            |
| `+0x08` | u32              | reserved_08     | Always 0                                                            |
| `+0x0C` | u32              | magic           | Always `0xDEBA1DCD`                                                 |
| `+0x10` | u64 + utf16le[n] | name_kr         | Korean action name; the u64 counts UTF-16 code units                |
| varies  | u64 + utf16le[n] | icon_path       | Icon path; no null terminator                                       |
| varies  | u8 x 12          | trailing_zeroes | Always 12 zero bytes; the record ends exactly after them            |

Both strings use the u64 length prefix read by `read_prefixed_at` in `_common/prefixed_string.py`.

Earlier versions of this doc read the `name_kr` length as a u32 `action_group` (2, or 4 for action 7) and the name's UTF-16 code units as one or two `icon_hash` values (`0xC068AE30` is `기쁨` read as a u32). That is why action 7, whose name `웅크리기` has four characters, looked like an "extended hash record".

## Observed Records

| Action ID | LOC Name | Korean Name | Icon Name | Icon Path                                               |
| --------- | -------- | ----------- | --------- | ------------------------------------------------------- |
| 0         | Joy      | 기쁨        | Like      | `New_Icon/08_Servant_Skill/02_Pet/Action_0_Like.dds`    |
| 1         | Feed     | 먹이        | Feed      | `New_Icon/08_Servant_Skill/02_Pet/Action_9_Feed.dds`    |
| 2         | Angry    | 화남        | Angry     | `New_Icon/08_Servant_Skill/02_Pet/Action_2_Angry.dds`   |
| 3         | Sleepy   | 졸림        | Sleepy    | `New_Icon/08_Servant_Skill/02_Pet/Action_3_Sleepy.dds`  |
| 4         | Jump     | 점프        | Jump      | `New_Icon/08_Servant_Skill/02_Pet/Action_4_Jump.dds`    |
| 5         | Sit      | 앉기        | Sit       | `New_Icon/08_Servant_Skill/02_Pet/Action_5_Sit.dds`     |
| 6         | Play     | 장난        | Play1     | `New_Icon/08_Servant_Skill/02_Pet/Action_6_Play1.dds`   |
| 7         | Crouch   | 웅크리기    | Play2     | `New_Icon/08_Servant_Skill/02_Pet/Action_7_Play2.dds`   |
| 8         | Weep     | 울음        | Bark      | `New_Icon/08_Servant_Skill/02_Pet/Action_8_Bark.dds`    |
| 9         | Sulky    | 삐짐        | Dislike   | `New_Icon/08_Servant_Skill/02_Pet/Action_1_Dislike.dds` |

> Action ID 1 points to `Action_9_Feed.dds`, and action ID 9 points to `Action_1_Dislike.dds`. The record key order and filename number are not the same for those two actions.

The file is byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.

## petactionoffset.dbss

Provides keyed lookup into `petaction.dbss` and supplies the record count.

### Header (4 bytes)

| Offset  | Type | Field | Notes                         |
| ------- | ---- | ----- | ----------------------------- |
| `+0x00` | u32  | count | Number of action records (10) |

### Offset Record (12 bytes, repeated `count` times)

| Offset  | Type | Field         | Notes                                    |
| ------- | ---- | ------------- | ---------------------------------------- |
| `+0x00` | u32  | action_id     | Key for the action/icon record           |
| `+0x04` | u32  | record_offset | Absolute byte offset in `petaction.dbss` |
| `+0x08` | u32  | record_size   | Size of the record in bytes              |

## Notes

- `petaction.dbss` itself starts with action ID 0, not a count. Always use `petactionoffset.dbss` to enumerate records.
- Both strings are UTF-16-LE and are not null-terminated. A fixed 12-byte zero trailer follows the icon path.
- The `magic` value `0xDEBA1DCD` appears in every record.
- Action names resolve through `languagedata_en.loc` with `str_type=19` and `str_id1=action_id`. The icon filename suffix is an asset name and does not always match the UI label.

## Open Questions

### Action ID Consumers

The action IDs are confirmed in-game to match LOC type 19 labels. The consuming pet UI or behavior table should join by `action_id`, but the exact source file is not confirmed.
