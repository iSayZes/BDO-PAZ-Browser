# `petaction.dbss` Format

## Purpose

Defines pet action icon records keyed by action ID. Each record stores a UTF-16 icon path for a pet command/reaction such as Like, Feed, Angry, Sleepy, Jump, Sit, Play, Bark, or Dislike. Companion `petactionoffset.dbss` provides the record count and keyed offsets.

Example:

```text
action_id: 0
icon_path: New_Icon/08_Servant_Skill/02_Pet/Action_0_Like.dds
```

## Graph

### Tags

- file format
- dbss
- pet
- action
- icon

### Connections

- [petactionoffset.dbss](petaction_dbss.md#petactionoffsetdbss) - keyed offset index for this file

---

## Companion Files

| File                    | Required | Role                                               |
| ----------------------- | -------- | -------------------------------------------------- |
| `petactionoffset.dbss`  | Required | `action_id -> (record_offset, record_size)` lookup |

All multi-byte values are little-endian.

---

## File Layout

`petaction.dbss` has no standalone header or record count. Records start at byte `0x0000`; use `petactionoffset.dbss` to enumerate them.

| Offset  | Type | Field   | Notes                                           |
| ------- | ---- | ------- | ----------------------------------------------- |
| `+0x00` | row  | records | Variable-size record stream; observed 10 rows   |

---

## Record Structure

Records are variable size because `icon_path_len` differs. Most records are 146-154 bytes.

### Standard Record

Offsets are relative to `record_offset` from `petactionoffset.dbss`.

| Offset  | Type       | Field           | Notes                                                          |
| ------- | ---------- | --------------- | -------------------------------------------------------------- |
| `+0x00` | u32        | action_id       | Primary key; matches offset-table key                          |
| `+0x04` | u32        | reserved_04     | Always 0                                                       |
| `+0x08` | u32        | reserved_08     | Always 0                                                       |
| `+0x0C` | u32        | magic           | Always `0xDEBA1DCD`                                            |
| `+0x10` | u32        | action_group    | Usually 2; observed 4 only for action ID 7 (`Action_7_Play2`)  |
| `+0x14` | u32        | reserved_14     | Always 0                                                       |
| `+0x18` | u32        | icon_hash       | Hash-like value associated with the icon/action                |
| `+0x1C` | u32        | icon_path_len   | UTF-16 code-unit count for `icon_path`; no null terminator     |
| `+0x20` | u32        | reserved_20     | Always 0                                                       |
| `+0x24` | utf16le[]  | icon_path       | `icon_path_len * 2` bytes                                      |
| varies  | u8 x 12    | trailing_zeroes | Always 12 zero bytes after the icon path                       |

### Extended Hash Record

Action ID 7 (`Action_7_Play2.dds`) has `action_group = 4` and inserts a second hash before `icon_path_len`.

| Offset  | Type       | Field           | Notes                                                      |
| ------- | ---------- | --------------- | ---------------------------------------------------------- |
| `+0x00` | u32        | action_id       | 7                                                          |
| `+0x04` | u32        | reserved_04     | Always 0                                                   |
| `+0x08` | u32        | reserved_08     | Always 0                                                   |
| `+0x0C` | u32        | magic           | `0xDEBA1DCD`                                               |
| `+0x10` | u32        | action_group    | 4                                                          |
| `+0x14` | u32        | reserved_14     | Always 0                                                   |
| `+0x18` | u32        | icon_hash_a     | `0xD06CC6C5` observed                                      |
| `+0x1C` | u32        | icon_hash_b     | `0xAE30B9AC` observed                                      |
| `+0x20` | u32        | icon_path_len   | 51 UTF-16 code units                                       |
| `+0x24` | u32        | reserved_24     | Always 0                                                   |
| `+0x28` | utf16le[]  | icon_path       | `New_Icon/08_Servant_Skill/02_Pet/Action_7_Play2.dds`     |
| varies  | u8 x 12    | trailing_zeroes | Always 12 zero bytes after the icon path                   |

---

## Observed Records

| Action ID | Action Name | Group | Hash Values                 | Icon Path                                                    |
| --------- | ----------- | ----- | --------------------------- | ------------------------------------------------------------ |
| 0         | Like        | 2     | `0xC068AE30`                | `New_Icon/08_Servant_Skill/02_Pet/Action_0_Like.dds`        |
| 1         | Feed        | 2     | `0xC774BA39`                | `New_Icon/08_Servant_Skill/02_Pet/Action_9_Feed.dds`        |
| 2         | Angry       | 2     | `0xB0A8D654`                | `New_Icon/08_Servant_Skill/02_Pet/Action_2_Angry.dds`       |
| 3         | Sleepy      | 2     | `0xB9BCC878`                | `New_Icon/08_Servant_Skill/02_Pet/Action_3_Sleepy.dds`      |
| 4         | Jump        | 2     | `0xD504C810`                | `New_Icon/08_Servant_Skill/02_Pet/Action_4_Jump.dds`        |
| 5         | Sit         | 2     | `0xAE30C549`                | `New_Icon/08_Servant_Skill/02_Pet/Action_5_Sit.dds`         |
| 6         | Play1       | 2     | `0xB09CC7A5`                | `New_Icon/08_Servant_Skill/02_Pet/Action_6_Play1.dds`       |
| 7         | Play2       | 4     | `0xD06CC6C5`, `0xAE30B9AC` | `New_Icon/08_Servant_Skill/02_Pet/Action_7_Play2.dds`       |
| 8         | Bark        | 2     | `0xC74CC6B8`                | `New_Icon/08_Servant_Skill/02_Pet/Action_8_Bark.dds`        |
| 9         | Dislike     | 2     | `0xC9D0C090`                | `New_Icon/08_Servant_Skill/02_Pet/Action_1_Dislike.dds`     |

> Action ID 1 points to `Action_9_Feed.dds`, and action ID 9 points to `Action_1_Dislike.dds`. The record key order and filename number are not the same for those two actions.

---

## petactionoffset.dbss

Provides keyed lookup into `petaction.dbss` and supplies the record count.

### Header (4 bytes)

| Offset  | Type | Field | Notes                              |
| ------- | ---- | ----- | ---------------------------------- |
| `+0x00` | u32  | count | Number of action records (10)      |

### Offset Record (12 bytes, repeated `count` times)

| Offset  | Type | Field         | Notes                                         |
| ------- | ---- | ------------- | --------------------------------------------- |
| `+0x00` | u32  | action_id     | Key for the action/icon record                |
| `+0x04` | u32  | record_offset | Absolute byte offset in `petaction.dbss`      |
| `+0x08` | u32  | record_size   | Size of the record in bytes                   |

---

## Suggested UI Layout

| Column      | Type | Notes                                      |
| ----------- | ---- | ------------------------------------------ |
| Action ID   | num  | Primary key; right-aligned                 |
| Action Name | text | Derived from icon filename suffix          |
| Group       | num  | `action_group`                             |
| Icon        | icon | DDS preview from `icon_path`, when loaded  |
| Icon Path   | text | Full UTF-16 source path                    |

---

## Notes

- `petaction.dbss` itself starts with action ID 0, not a count. Always use `petactionoffset.dbss` to enumerate records.
- Icon paths are UTF-16-LE and are not null-terminated. A fixed 12-byte zero trailer follows each path.
- The `magic` value `0xDEBA1DCD` appears in every record.

---

## Open Questions

### Hash Field Semantics

The `icon_hash` values look like hashes or resource identifiers, but the hashing scheme and lookup target are unconfirmed. Action ID 7 carries two hash values instead of one, likely because `action_group = 4`, but the reason for the extra hash is still unknown.

### Action ID Consumers

No confirmed cross-reference was found in currently documented pet formats. The consuming pet UI or behavior table should join by `action_id`, but the exact source file is not confirmed.
