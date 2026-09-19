# `fairyequipskill.bss` Format

## Purpose

Defines the fairy skill catalog, the 35 skills a fairy can hold, grouped into 8 skill types with tier progressions (e.g. `Tingling Breath I`–`V`). Each record stores its skill type group, a tier marker, and a localization ID that resolves to both the skill name and its effect description, and that doubles as the icon filename number.

The remainder of the file is a 200-slot reserved block of null placeholders, so the catalog can grow without changing the layout.

Example:

```text
equip_skill_id: 0   →  type=1  loc=49096  "Tingling Breath I"  / "Underwater Breathing +5 sec"
equip_skill_id: 20  →  type=6  loc=49121  "Miraculous Cheer 10 Seconds" / "Auto-use HP/Resource potions. Cooldown: 10 sec"
equip_skill_id: 34  →  type=8  loc=49181  "Continuous Care V"  / "Auto-use from 30 selected items."
```

## Graph

### Tags

- file format
- bss
- fairy
- equip skill

### Connections

- [fairyequipskillaquire.dbss](fairyequipskillaquire_dbss.md), fairy equip-skill acquisition cost tables; no confirmed key relationship to this catalog
- [petequipskill.bss](petequipskill_bss.md), structurally the same PABR catalog format for pets
- Localization (`loc_id`) resolved via `loc-tool.py --type 10 --id <loc_id>`
- Icon assets use the `loc_id`: `ui_texture/icon/new_icon/08_servant_skill/02_pet/equipskill_fairy_{loc_id:08d}.dds`

---

## Companion Files

None, `fairyequipskill.bss` is a standalone catalog with no offset index.

| File                  | Required | Role                                             |
| --------------------- | -------- | ------------------------------------------------ |
| `languagedata_en.loc` | Optional | Skill names (`id4=0`) and descriptions (`id4=1`) |

All multi-byte values are little-endian.

---

## File Layout

Total file size: 3636 bytes = 4 (magic) + 420 (catalog) + 3200 (reserved block) + 12 (trailer).

| Offset   | Size | Section        | Notes                           |
| -------- | ---- | -------------- | ------------------------------- |
| `+0x000` | 4    | magic          | `PABR` (ASCII)                  |
| `+0x004` | 420  | catalog        | 35 × 12-byte skill records      |
| `+0x1A8` | 3200 | reserved block | 200 × 16-byte null placeholders |
| `+0xE28` | 12   | trailer        | `[u32 0][u32 0x0E28][u32 0]`    |

### Header (4 bytes)

| Offset  | Type   | Field | Notes          |
| ------- | ------ | ----- | -------------- |
| `+0x00` | char×4 | magic | `PABR` (ASCII) |

Records begin immediately at `+0x04`. There is **no record count field**, the catalog is terminated by the first record whose `equip_skill_id` is `200`.

### Skill Record (12 bytes, ×35, offset `0x004`)

| Offset  | Type | Field          | Notes                                                  |
| ------- | ---- | -------------- | ------------------------------------------------------ |
| `+0x00` | u32  | equip_skill_id | Sequential record key, `0`–`34`; `200` marks the end   |
| `+0x04` | u32  | skill_type     | Skill group, `1`–`8` (see Skill Types)                 |
| `+0x08` | u8   | tier           | Always `1` in all 35 observed records                  |
| `+0x09` | u8   | —              | Always `0`; padding                                    |
| `+0x0A` | u16  | loc_id         | Localization key → skill name/description, icon number |

### Reserved Block (16 bytes, ×200, offset `0x1A8`)

Two hundred unused catalog slots. Every record is `[u32 200][u32 0][u32 0][u32 0]`, where `200` is the null-entry sentinel. Skip these when parsing.

Note the stride here is **16 bytes**, not the 12 used by live records, matching the wider Section 2 record shape in `petequipskill.bss`, whose extended catalog is fully populated. In `fairyequipskill.bss` that extended section is entirely null.

### Trailer (12 bytes, offset `0xE28`)

| Offset  | Type | Field    | Notes                              |
| ------- | ---- | -------- | ---------------------------------- |
| `+0x00` | u32  | —        | Always `0`                         |
| `+0x04` | u32  | data_end | `0x0E28` (3624) = `file_size - 12` |
| `+0x08` | u32  | —        | Always `0`                         |

`petequipskill.bss` carries the identical trailer (`data_end = 0x0EB0 = file_size - 12`), so this is a shared PABR convention rather than a fairy-specific field.

---

## Skill Types

| skill_type | Skill group        | equip_skill_id | loc_id range | Effect                                              |
| ---------- | ------------------ | -------------- | ------------ | --------------------------------------------------- |
| 1          | Tingling Breath    | 0–4            | 49096–49100  | Underwater Breathing +5/+10/+15/+20/+30 sec         |
| 2          | Feathery Steps     | 5–9            | 49106–49110  | Weight Penalty Reduction up to 105%–125%            |
| 3          | Fairy's Tear       | 10–13          | 49114–49111  | Instant Resurrection, 0 EXP loss; 12/6/3/1 hr CD    |
| 4          | Inexhaustible Well | 14–18          | 49115–49119  | Auto-use Purified Water/Star Anise Tea; 20→3 min CD |
| 5          | Morning Star       | 19             | 49120        | Summoned fairy lights up the surroundings           |
| 6          | Miraculous Cheer   | 20–28          | 49121–49129  | Auto-use HP/Resource potions; 10 sec → 2 sec CD     |
| 7          | Gift               | 29             | 49130        | Luck +1                                             |
| 8          | Continuous Care    | 30–34          | 49177–49181  | Auto-use from 7/10/15/20/30 selected items          |

### Full Record Table

| equip_skill_id | skill_type | loc_id | Skill name                  | Description                                                                            |
| -------------- | ---------- | ------ | --------------------------- | -------------------------------------------------------------------------------------- |
| 0              | 1          | 49096  | Tingling Breath I           | Underwater Breathing +5 sec                                                            |
| 1              | 1          | 49097  | Tingling Breath II          | Underwater Breathing +10 sec                                                           |
| 2              | 1          | 49098  | Tingling Breath III         | Underwater Breathing +15 sec                                                           |
| 3              | 1          | 49099  | Tingling Breath IV          | Underwater Breathing +20 sec                                                           |
| 4              | 1          | 49100  | Tingling Breath V           | Underwater Breathing +30 sec                                                           |
| 5              | 2          | 49106  | Feathery Steps I            | Weight Penalty Reduction (Up to 105%)                                                  |
| 6              | 2          | 49107  | Feathery Steps II           | Weight Penalty Reduction (Up to 110%)                                                  |
| 7              | 2          | 49108  | Feathery Steps III          | Weight Penalty Reduction (Up to 115%)                                                  |
| 8              | 2          | 49109  | Feathery Steps IV           | Weight Penalty Reduction (Up to 120%)                                                  |
| 9              | 2          | 49110  | Feathery Steps V            | Weight Penalty Reduction (Up to 125%)                                                  |
| 10             | 3          | 49114  | Fairy's Tear I              | Instant Resurrection, 0 EXP loss. Cooldown: 12 hr                                      |
| 11             | 3          | 49113  | Fairy's Tear II             | Instant Resurrection, 0 EXP loss. Cooldown: 6 hr                                       |
| 12             | 3          | 49112  | Fairy's Tear III            | Instant Resurrection, 0 EXP loss. Cooldown: 3 hr                                       |
| 13             | 3          | 49111  | Fairy's Tear IV             | Instant Resurrection, 0 EXP loss. Cooldown: 1 hr                                       |
| 14             | 4          | 49115  | Inexhaustible Well I        | Auto-use Purified Water/Star Anise Tea during Heatstroke/Hypothermia. Cooldown: 20 min |
| 15             | 4          | 49116  | Inexhaustible Well II       | Auto-use Purified Water/Star Anise Tea during Heatstroke/Hypothermia. Cooldown: 15 min |
| 16             | 4          | 49117  | Inexhaustible Well III      | Auto-use Purified Water/Star Anise Tea during Heatstroke/Hypothermia. Cooldown: 10 min |
| 17             | 4          | 49118  | Inexhaustible Well IV       | Auto-use Purified Water/Star Anise Tea during Heatstroke/Hypothermia. Cooldown: 5 min  |
| 18             | 4          | 49119  | Inexhaustible Well V        | Auto-use Purified Water/Star Anise Tea during Heatstroke/Hypothermia. Cooldown: 3 min  |
| 19             | 5          | 49120  | Morning Star                | The summoned fairy will shine and light up the surroundings.                           |
| 20             | 6          | 49121  | Miraculous Cheer 10 Seconds | Auto-use HP/Resource potions. Cooldown: 10 sec                                         |
| 21             | 6          | 49122  | Miraculous Cheer 9 Seconds  | Auto-use HP/Resource potions. Cooldown: 9 sec                                          |
| 22             | 6          | 49123  | Miraculous Cheer 8 Seconds  | Auto-use HP/Resource potions. Cooldown: 8 sec                                          |
| 23             | 6          | 49124  | Miraculous Cheer 7 Seconds  | Auto-use HP/Resource potions. Cooldown: 7 sec                                          |
| 24             | 6          | 49125  | Miraculous Cheer I          | Auto-use HP/Resource potions. Cooldown: 6 sec                                          |
| 25             | 6          | 49126  | Miraculous Cheer II         | Auto-use HP/Resource potions. Cooldown: 5 sec                                          |
| 26             | 6          | 49127  | Miraculous Cheer III        | Auto-use HP/Resource potions. Cooldown: 4 sec                                          |
| 27             | 6          | 49128  | Miraculous Cheer IV         | Auto-use HP/Resource potions. Cooldown: 3 sec                                          |
| 28             | 6          | 49129  | Miraculous Cheer V          | Auto-use HP/Resource potions. Cooldown: 2 sec                                          |
| 29             | 7          | 49130  | Gift                        | Luck +1                                                                                |
| 30             | 8          | 49177  | Continuous Care I           | Auto-use from 7 selected items.                                                        |
| 31             | 8          | 49178  | Continuous Care II          | Auto-use from 10 selected items.                                                       |
| 32             | 8          | 49179  | Continuous Care III         | Auto-use from 15 selected items.                                                       |
| 33             | 8          | 49180  | Continuous Care IV          | Auto-use from 20 selected items.                                                       |
| 34             | 8          | 49181  | Continuous Care V           | Auto-use from 30 selected items.                                                       |

---

## Lookup Recipe

```python
def parse_fairy_equip_skills(data):
    assert data[:4] == b"PABR"
    offset = 4
    while True:
        equip_skill_id, skill_type = struct.unpack_from("<II", data, offset)
        if equip_skill_id == NULL_ENTRY_ID:  # 200 -> reserved block reached
            break
        tier, loc_id = struct.unpack_from("<HH", data, offset + 8)
        yield equip_skill_id, skill_type, tier, loc_id
        offset += 12
```

Resolve display text with `loc-tool.py --type 10 --id <loc_id>`: `id4=0` is the skill name, `id4=1` is the effect description.

---

## Suggested UI Layout

| Column         | Type | Notes                                                        |
| -------------- | ---- | ------------------------------------------------------------ |
| Equip Skill ID | num  | `equip_skill_id` (right-aligned)                             |
| Icon           | Icon | `equipskill_fairy_<loc_id:08d>.dds`                          |
| Skill Name     | text | LOC type 10, `id4=0`; falls back to `loc_id` when unresolved |
| Description    | text | LOC type 10, `id4=1`; the skill's effect text                |
| Skill Type     | num  | `skill_type` group code (`1`–`8`)                            |
| Loc ID         | num  | `loc_id` (right-aligned)                                     |

The `tier` and padding fields are internal-only and omitted from the table.

---

## Notes

- No offset companion file, the file is small enough to scan linearly.
- The catalog has no count field; parsing stops at the first `equip_skill_id == 200`, the same null sentinel `petequipskill.bss` uses.
- `skill_type` numbering is fairy-local and does **not** match `petequipskill.bss` type numbering.
- The `I`–`V` suffix in a skill's name is the **rolled skill level**, assigned randomly when a fairy learns the skill. Each full group is therefore a five-rung ladder of the same effect; Fairy's Tear stops at `IV`, and Morning Star and Gift carry no suffix at all. This is separate from the record's `tier` field, which is always `1`.
- Gift (`equip_skill_id 29`, Luck +1) is the skill every fairy starts with, which is consistent with it being the one type-7 entry and the only record whose icon is missing.
- Skill type 3 (Fairy's Tear) is the one group whose `loc_id`s run **descending** as `equip_skill_id` ascends (49114 → 49111), because tier I has the longest cooldown. Do not assume `loc_id` order tracks record order.
- Skill type 6 (Miraculous Cheer) holds 9 entries: four legacy "`N` Seconds" names (49121–49124) followed by the current `I`–`V` naming (49125–49129). Both sets are live records, not placeholders.
- Icons live in the **pet** icon folder (`02_pet`) despite being fairy assets, prefixed `equipskill_fairy_`.
- 34 of the 35 `loc_id`s have a matching icon; `49130` (`Gift`, type 7) has no `equipskill_fairy_00049130.dds` in the archive, so the UI must tolerate a missing icon.
- `tier` is `1` in every record, so it carries no information in the current data; it is kept in the spec because `petequipskill.bss` uses the same field position.
- The file in `files/` was verified byte-identical to a fresh extraction from the PAZ archive, so this spec reflects current game data.

---

## Open Questions

### Reserved block size

The reserved block holds exactly 200 slots and the null sentinel value is also `200`. This is most likely a coincidence of a round reserve capacity rather than a self-describing field, but nothing confirms whether the client reads the block length from anywhere or simply scans to the trailer.

### Link to `fairyequipskillaquire.dbss`

The acquisition cost tables are keyed by `acquire_type_id` `501`–`504`, which do not appear anywhere in this catalog, and this catalog's IDs `0`–`34` do not appear in the acquire file. The join between a fairy skill and its acquisition cost is therefore still unresolved; a fairy definition file (not yet located) likely carries both keys.

### Which skills a fairy of a given grade can roll

Resolved. A fairy learns one random skill from this catalog every 10 levels, and each learned skill rolls a random rank of `1`–`5`, the `I`–`V` ladders below. The per-grade odds live in [fairyequipskillaquire.dbss](fairyequipskillaquire_dbss.md), whose four records are the four fairy grades and whose weights are indexed by this file's `equip_skill_id`. Only Radiant carries non-zero weights for rank IV and V.

That table also explains two oddities here: `equip_skill_id 29` (Gift) has weight `0` in every grade because every fairy starts with it, and the four legacy `Miraculous Cheer` "`N` Seconds" entries (`20`–`23`) are likewise `0` everywhere, confirming they are dead records.

### `tier` field purpose

`tier` is always `1`, matching `petequipskill.bss` where it is also invariably `1`. Whether it distinguishes fairy grades, marks records as active, or is vestigial cannot be determined from the data alone.
