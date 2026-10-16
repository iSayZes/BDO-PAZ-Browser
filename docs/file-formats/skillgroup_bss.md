# `skillgroup.bss` Format

## Purpose

The rank chains of player skills. A skill group is one entry of the skill
window, such as "Grave Digging", and lists the skill key of every rank in
order. The skill window grids in [`ui_skillgroup_*.bss`](ui_skillgroup_bss.md)
place groups, not single skills.

```text
group 578  skill_keys 0, 1759/1, 1760/1, 1761/1, 1762/1
           "Grave Digging I" to "Grave Digging IV"
```

## Companion Files

| File                  | Required | Role                                                          |
| --------------------- | -------- | ------------------------------------------------------------- |
| `skill.dbss`          | Optional | The rank records, see [`skill.dbss`](skill_dbss.md)           |
| `languagedata_en.loc` | Optional | Rank names, LOC type `10`, `str_id1 = skill_key >> 16`        |

All multi-byte values are little-endian.

## File Layout

No magic and no trailer: a u32 group count, then the groups back to back up
to the end of the file.

| Offset  | Type    | Field       | Notes                                    |
| ------- | ------- | ----------- | ---------------------------------------- |
| `+0x00` | u32     | group_count | `3514` on client 3458                    |
| `+0x04` | group[] | groups      | Variable-size groups, see below          |

## Record Structure

### Skill Group (variable)

| Offset  | Type    | Field      | Notes                                                                    |
| ------- | ------- | ---------- | ------------------------------------------------------------------------ |
| `+0x00` | u16     | group_no   | Unique; `142` to `15162`, not sorted                                     |
| `+0x02` | u32     | rank_count | Number of keys that follow, including the unlearned entry; up to `21`    |
| `+0x06` | u32[]   | skill_keys | Rank 0 is always `0` (not learned); the rest are `skill.dbss` keys in rank order |

2,271 groups have a single rank (`rank_count` 2); the longest chains have 20
ranks. Every rank key is a `skill.dbss` key.

## Notes

- The layout comes from bdo-data-extractor and walks exactly to the end of
  the file on client 3458.
- Rank `i` usually lists rank `i + 1` in its `skill.dbss` `next_skill_keys`
  (3,422 of 3,858 consecutive pairs).
