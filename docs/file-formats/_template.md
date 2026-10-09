# `<filename.ext>` Format

## Purpose

Describe what this file stores and what part of the game/tool it affects.

Example:

```text
Short example of the in-game meaning, UI display, or decoded output.
```

## Companion Files

List every file that must be read alongside this one. Omit this section if the
format is fully self-contained.

| File                  | Required | Role                                        |
| --------------------- | -------- | ------------------------------------------- |
| `companion.dbss`      | Required | Provides `id → (offset, size)` block lookup |
| `languagedata_en.loc` | Optional | English display strings                     |

All multi-byte values are little-endian unless noted otherwise.

## File Layout

Top-level structure of the file (compression, magic bytes, header).

| Offset  | Type | Field | Notes             |
| ------- | ---- | ----- | ----------------- |
| `+0x00` | u32  | count | Number of records |
| `+0x04` | ...  | data  | Record stream     |

## Record Structure

Repeat this sub-section once per logical record type. Use H3 headings.

### Header (N bytes)

| Offset  | Type | Field | Notes |
| ------- | ---- | ----- | ----- |
| `+0x00` | u32  | id    |       |

### Row / Entry (N bytes, repeated `count` times)

| Offset  | Type | Field   | Notes |
| ------- | ---- | ------- | ----- |
| `+0x00` | u32  | field_a |       |
| `+0x04` | u32  | field_b |       |

Include observed value ranges or invariants inline as Notes cells.

## Enum Values

Document enumerations inline here or inside the section where they first appear.

| ID  | Name |
| --- | ---- |
| 0   | Name |
| 1   | Name |

## Suggested UI Layout

| Column | Type | Notes                            |
| ------ | ---- | -------------------------------- |
| ID     | num  | Primary key                      |
| Name   | text | LOC lookup fallback to raw value |

## Notes

- Bullet-point facts that don't fit neatly into a table.
- Cross-references to other confirmed behaviors.
- Disproven hypotheses worth recording so they aren't re-investigated.

## Open Questions

### Question Title

What is still unknown and why it matters. Include disproven candidates if any.

## In-Game Checks

A check is an open question with a testable guess that needs a character
with a given item, quest, NPC, class or zone. Check client Lua, UI XML and
the data first. A question lives in one place: it moves here from Open
Questions once it has a testable guess, and an answered check goes into
Notes. Omit this section when there are no checks.

Each check opens with what it needs, one line (paragraph) per kind:
`Needs item:`, `Needs quest:`, `Needs NPC:`, `Needs class:`, `Needs zone:`,
and `Needs worker:` or `Needs skill:` when a check needs one.
The name links to its page, usually bdocodex under `/us/` (`/us/item/<id>/`,
`/us/quest/<chain>/<quest>/`, `/us/npc/<id>/`, worker skills
`/us/sskill/<id>/`), else Garmoth or another
source; a name with no page stays plain text. Several entries of one kind
get `(all)` or `(any one)` and a bullet list. When different values need
different things, each list says what it checks first. Then say what to
look at and what each result means.

### One Thing Needed

Needs item: [Item Name](https://bdocodex.com/us/item/<id>/)

Needs zone: Zone Name

Use the item in that zone and read the buff tooltip. A duration line means
`unknown_10` is the duration in seconds; no line means it is something else.

### Several of One Kind

Needs NPC (any one):

- [NPC One](https://bdocodex.com/us/npc/<id>/)
- [NPC Two](https://bdocodex.com/us/npc/<id>/)

Open the NPC's shop. A Repair button means `unknown_04` value `3` is the
repair slot.

### Different Values Need Different Things

To check value 1 in `unknown_10`, needs item (all):

- [Item One](https://bdocodex.com/us/item/<id>/)
- [Item Two](https://bdocodex.com/us/item/<id>/)

To check value 2 in `unknown_10`, needs item (all):

- [Item Three](https://bdocodex.com/us/item/<id>/)
- [Item Four](https://bdocodex.com/us/item/<id>/)

Equip each set and read the set bonus line. If value 1 sets show a bonus
and value 2 sets do not, `unknown_10` is the set bonus flag.
