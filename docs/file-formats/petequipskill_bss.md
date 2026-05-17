# `petequipskill.bss` Format

## Purpose

Defines the equip-skill catalog for pets, keyed by `equip_skill_id` from `pet.dbss`. 116 skill entries span two sections: Section 1 (regular-pet catalog, IDs 0–42) and Section 2 (extended catalog, IDs 15–111). Each entry records the skill's type group, tier marker, and a localization ID that resolves to the in-game skill name and pet equip-skill icon number.

Example:

```text
equip_skill_id: 15  →  S2 type=4  loc=49061  "Skill EXP +1%"
equip_skill_id: 91  →  S2 type=18 loc=49162  "Barter EXP +1%"
equip_skill_id: 42  →  S1 type=20 loc=49089  "Knowledge Gain Chance Lv. 4"
```

## Graph

### Tags

- file format
- bss
- pet
- equip skill

### Connections

- [pet.dbss](pet_dbss.md) — `equip_skill_id` field keys into this file
- Localization (`loc_id`) resolved via `loc-tool.py --type 10 --id <loc_id>`
- Icon assets use the same numeric ID as `loc_id`: `ui_texture/icon/new_icon/08_servant_skill/02_pet/equipskill_{loc_id:08d}.dds`

---

## Companion Files

None — `petequipskill.bss` is a standalone catalog with no offset index.

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type   | Field | Notes                |
| ------- | ------ | ----- | -------------------- |
| `+0x00` | char×4 | magic | `PABR` (ASCII)       |

Records begin immediately at `+0x04`.

---

### Section 1 — Standard Pet Skills (43 × 12 bytes, offset `0x004`)

Covers `equip_skill_id` 0–42 (regular pets). Stride = **12 bytes**.

| Offset  | Type | Field         | Notes                                          |
| ------- | ---- | ------------- | ---------------------------------------------- |
| `+0x00` | u32  | equip_skill_id| Unique skill record key (0–42)                |
| `+0x04` | u32  | skill_type    | Skill group (1–20; see Skill Types table)      |
| `+0x08` | u8   | tier          | Always 1 in Section 1                         |
| `+0x09` | u8   | —             | Always 0; padding                             |
| `+0x0A` | u16  | loc_id        | Localization key → skill name (type 10 string)|

---

### Null Block (15 × 16 bytes, offset `0x208`)

Fifteen placeholder records for IDs 43–57 (currently unassigned). Each record = `[u32=200][u32=0][u32=0][u32=0]`. The value 200 signals a null/unused entry.

---

### Section 2 — Extended Pet Skills (variable stream, offset `0x2F8`)

Covers `equip_skill_id` 15–111 (Airiss and premium pets, plus overlap with Section 1). Base stride = **16 bytes**. Records with `equip_skill_id = 200` are null placeholders. Records with `extra_flag = 1` carry an additional u32 after the base record.

| Offset  | Type | Field         | Notes                                              |
| ------- | ---- | ------------- | -------------------------------------------------- |
| `+0x00` | u32  | equip_skill_id| Unique skill record key (15–111, or 200 = null)   |
| `+0x04` | u32  | skill_type    | Skill group (different numbering from Section 1)   |
| `+0x08` | u8   | tier          | Always 1; purpose of field unclear                |
| `+0x09` | u8   | —             | Always 0; padding                                 |
| `+0x0A` | u16  | loc_id        | Localization key → skill name (type 10 string)    |
| `+0x0C` | u32  | extra_flag    | Usually 0; 1 means an extra u32 follows           |
| `+0x10` | u32  | extra_value   | Present only when `extra_flag = 1`                |

---

## Skill Types (Section 1)

| skill_type | Skill group           | Equip skill IDs | Example names                        |
| ---------- | --------------------- | --------------- | ------------------------------------ |
| 1          | Karma Recovery        | 0–2             | +7%, +5%, +3%                        |
| 2          | Combat EXP            | 3–5             | +7%, +5%, +5%                        |
| 3          | Gathering EXP         | 6–8             | +7%, +5%, +5%                        |
| 4          | Luck                  | 9               | +1                                   |
| 5          | Fishing Speed         | 10              | +1                                   |
| 6          | Gathering Speed       | 11              | +1                                   |
| 7          | Death Penalty Resist  | 12–13           | +7%, +4%                             |
| 8          | Fishing EXP           | 14–16           | +7%, +5%, +5%                        |
| 9          | Hunting EXP           | 17–19           | +7%, +5%, +5%                        |
| 10         | Cooking EXP           | 20–22           | +7%, +5%, +5%                        |
| 11         | Alchemy EXP           | 23–25           | +7%, +5%, +5%                        |
| 12         | Processing EXP        | 26–28           | +7%, +5%, +5%                        |
| 13         | Training EXP          | 29–31           | +7%, +5%, +5%                        |
| 14         | Trading EXP           | 32–34           | +7%, +5%, +5%                        |
| 15         | Farming EXP           | 35–37           | +7%, +5%, +5%                        |
| 16         | Life EXP              | 38              | +5%                                  |
| 17         | Weight Limit          | 39              | +50 LT                               |
| 18         | Durability Resistance | 40              | +5%                                  |
| 19         | Skill EXP             | 41              | +5%                                  |
| 20         | Knowledge Gain Chance | 42              | Lv. 4                                |

---

## Selected Section 2 Skill Groups

| Equip skill IDs | Skill name (loc resolution)                      |
| --------------- | ------------------------------------------------ |
| 15–18           | Skill EXP +1%, +2%, +3%, +4%                    |
| 20–23           | Life EXP +1%, +2%, +3%, +4%                     |
| 35–38           | Durability Reduction Resistance +1%–+4%         |
| 40–43           | Normal and Higher Grade Knowledge Gain Chance   |
| 51–54           | Tingling Breath II / II+ / II++ / II+++          |
| 55–57           | Weight Limit +20/+30/+40 LT                     |
| 60–62           | Feathery Steps I / II / III                     |
| 65              | Max HP +25  *(extra_flag = 1)*                  |
| 70–74           | Combat EXP +1%, +2%, +3%, +4%, +5%              |
| 75–78           | Death Penalty Resistance +1%, +3%, +5%, +4%     |
| 79              | Item Drop Rate +1%  *(extra_flag = 1)*          |
| 83–86           | Mount EXP +1%, +2%, +3%, +4%                    |
| 87–90           | Sailing EXP +1%, +2%, +3%, +5%                  |
| 91–94           | Barter EXP +1%, +2%, +3%, +5%                   |
| 95–98           | Big Ship Inventory Weight +50/+75/+100/+150 LT  |
| 99–111          | Single-tier extras (Skill EXP, Life EXP, etc.)  |

---

## Lookup Recipe

```python
def get_equip_skill(data, equip_skill_id):
    # Section 2 preferred for IDs 15–111 (extended catalog)
    s2 = parse_section2(data)
    if equip_skill_id in s2:
        return s2[equip_skill_id]
    # Fall back to Section 1 for IDs 0–42
    s1 = parse_section1(data)
    return s1.get(equip_skill_id)
```

When an `equip_skill_id` appears in both sections, Section 2 provides the finer-grained tier (4 tiers vs Section 1's 3) and should be preferred.

---

## Notes

- No offset companion file — the file is small enough to scan linearly.
- `equip_skill_id = 200` in Section 2 records is a null placeholder; ignore these.
- Section 1 tiers use 3 entries per skill type (high/mid/mid), ordered descending by tier value.
- Section 2 tiers use 4 entries (e.g., +1%/+2%/+3%/+5%), also ordered ascending by value.
- The `extra_flag` = 1 in Section 2 identifies several records (including IDs 65–68, 79–82, 104, and 107) and adds one trailing u32 `extra_value`; the semantic is unconfirmed — possibly marks Airiss-exclusive skills.
- `skill_type` numbering is **independent** between sections — type 4 in S1 (Luck) ≠ type 4 in S2 (Skill EXP).
- Total file size: 3772 bytes = 4 (PABR) + 516 (S1) + 240 (null) + variable Section 2 stream + 4 (trailing padding).
- Localization IDs are in the range 49001–49176 for confirmed skills; use `loc-tool.py --type 10 --id <loc_id>` to resolve.
- This file defines **which skills are available** (the catalog). The per-pet slot **costs** are defined separately in `petequipskillaquire.dbss` via `acquire_type_id`. The two cross-references in `pet.dbss` are independent.

---

## Suggested UI Layout

| Column         | Type | Notes                                                       |
| -------------- | ---- | ----------------------------------------------------------- |
| Equip Skill ID | num  | `equip_skill_id` (right-aligned)                           |
| Skill Name     | text | Resolved from `loc_id` (type 10 string); fall back to raw  |
| Icon           | Icon | `equipskill_<loc_id:08d>.dds`                              |
| Skill Type     | num  | `skill_type` (group code)                                  |
| Section        | text | "S1" or "S2" (indicates which catalog entry is used)       |

---

## Open Questions

### ID overlap (15–42) across sections

Skills 15–42 appear in both Section 1 and Section 2 with different loc IDs (S1: 3-tier e.g. Fishing EXP +5%, S2: 4-tier e.g. Skill EXP +1%). The rule for which section to use for a given `equip_skill_id` is not confirmed. Hypothesis: Section 2 is for Airiss/premium pets; Section 1 for regular pets. Cross-referencing with which species use which IDs in `pet.dbss` would confirm.

### `extra_flag` in Section 2

Several Section 2 records have `extra_flag = 1` and a trailing `extra_value`. Known IDs include 65–68, 79–82, 104, and 107. The semantic is unknown. Candidates: Airiss-exclusive flag, skill incompatibility marker, alternate skill group, or unlock requirement.

### `skill_type` semantic

Within each section, skills of the same `skill_type` form a tier group (e.g., all Karma Recovery entries share type 1 in S1). The type numbering is section-local and the mapping from type ID to skill category name is derived empirically from loc IDs. No authoritative mapping table has been found.
