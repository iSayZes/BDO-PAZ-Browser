# `pet.dbss` Format

## Purpose

Defines one record per pet type/tier combination, covering icon path, species, tier, equip-skill slots, and several numeric parameters. Each record represents a specific pet at a specific tier (e.g. "Dog variant #40 at Tier 4"). Companion `petoffset.dbss` enables O(1) lookup by pet ID.

Example:

```text
pet_id: 0xFC05  →  species: 105 (GoldStar)  tier: 4
equip_skill_slots: 4   dds_variant: 4
icon: New_UI_Common_forLua\Window\Stable\Pet\GoldStar_Pet_0004.dds
```

## Graph

### Tags

- file format
- dbss
- pet
- companion

### Connections

- [petoffset.dbss](petoffset_dbss.md) — keyed offset index for this file
- [petgrade.dbss](petgrade_dbss.md) — join on `(species, variant)` to get grade per pet type
- [petequipskillaquire.dbss](petequipskillaquire_dbss.md) — `acquire_type_id` keys into this table
- [petequipskill.bss](petequipskill_bss.md) — `equip_skill_id` keys into this file for skill name and type
- [petexp.dbss](petexp_dbss.md) — pet EXP tables; `max_level` values match this file's level counts

---

## Companion Files

| File             | Required | Role                                                     |
| ---------------- | -------- | -------------------------------------------------------- |
| `petoffset.dbss` | Required | `pet_id → (data_offset, data_size)` for variable records |
| `petgrade.dbss`  | Optional | `(species, variant) → grade` per pet type                |

All multi-byte values are little-endian.

---

## File Layout

### Header (6 bytes)

| Offset  | Type | Field            | Notes                                                                        |
| ------- | ---- | ---------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u32  | count            | Number of pet records (observed: 1782)                                       |
| `+0x04` | u16  | first_record_key | `pet_id` of the first record — part of record 0, not a separate header field |

> `+0x04` is the key prefix of the first record, not a standalone header field. Records begin immediately at `+0x04`.

### Record (variable size, typically 181–194 bytes)

Each record is stored as `[u16 key_prefix][data_bytes]`. The `key_prefix` (2 bytes) equals `pet_id` and is also the first 2 bytes of `data_bytes`.

#### Fixed Header (32 bytes)

| Offset  | Type | Field             | Notes                                                                                   |
| ------- | ---- | ----------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id            | Unique record key; equal to the preceding 2-byte file prefix                            |
| `+0x02` | u8   | variant           | Sub-variant within the species (1–54 observed)                                          |
| `+0x03` | u8   | species           | Pet family/model code                                                                   |
| `+0x04` | u8   | —                 | Always 0; reserved                                                                      |
| `+0x05` | u8   | tier              | Tier (0 = lowest, 4 = highest for regular pets)                                         |
| `+0x06` | u8   | —                 | Always 1; reserved                                                                      |
| `+0x07` | u8   | max_level         | Usually 10; Airiss variants have 20, 30, or 50                                          |
| `+0x08` | u32  | —                 | Always `0x90000000`; purpose unknown                                                    |
| `+0x0C` | u8   | —                 | Always 1; reserved                                                                      |
| `+0x0D` | u16  | —                 | Always 0; reserved                                                                      |
| `+0x0F` | u8   | equip_skill_slots | Number of equip skill slots; = `tier + 1` for regular pets (max 4); Airiss have up to 9 |
| `+0x10` | u16  | —                 | Always 0; reserved                                                                      |
| `+0x12` | u8   | —                 | Purpose unknown; not reliably equal to the icon filename number                         |
| `+0x13` | u8   | —                 | Always 0; reserved                                                                      |
| `+0x14` | u32  | type_param        | Pet-type specific value (0 for many species; non-zero for some)                         |
| `+0x18` | u32  | icon_path_len     | Byte length of the icon path string (no null terminator)                                |
| `+0x1C` | u32  | —                 | Always 0; reserved                                                                      |

#### Icon Path (variable, `icon_path_len` bytes)

Stored immediately after the fixed header. **Not null-terminated.** Length is given by `icon_path_len`.

```text
New_UI_Common_forLua\Window\Stable\Pet\GoldStar_Pet_0004.dds
```

The icon path is ASCII-encoded with no null terminator; its byte length is given by `icon_path_len`.

#### Fixed Footer (94 bytes, immediately after the icon path)

| Offset  | Type     | Field           | Notes                                                         |
| ------- | -------- | --------------- | ------------------------------------------------------------- |
| `+0x00` | u32      | const_30000_a   | Always 30000 across all 1782 records                          |
| `+0x04` | u32      | —               | Always 0                                                      |
| `+0x08` | u32      | const_15000     | Always 15000 (= const_30000_a / 2)                            |
| `+0x0C` | u32      | —               | Always 0                                                      |
| `+0x10` | u32      | const_30000_b   | Always 30000                                                  |
| `+0x14` | u32      | —               | Always 0                                                      |
| `+0x18` | u32      | const_500000    | Always 500000                                                 |
| `+0x1C` | u32      | const_1000000   | Always 1000000                                                |
| `+0x20` | u32      | const_2         | Always 2                                                      |
| `+0x24` | u16      | acquire_type_id | Key into `petequipskillaquire.dbss`; 0 = none; varies by tier |
| `+0x26` | u16      | equip_skill_id  | Pet equip-skill identifier; varies by pet type and tier       |
| `+0x28` | u16      | —               | Always 0; padding                                             |
| `+0x2A` | u32 × 10 | upgrade_table   | 10 values, all 1000000; purpose unknown                       |
| `+0x52` | u8       | —               | Always 0                                                      |
| `+0x53` | u8       | tier_score      | 17 for tier ≥ 3; 16 for tier 2; 11 for tier ≤ 1               |
| `+0x54` | u8       | —               | Always 0                                                      |
| `+0x55` | u8       | —               | Always 26; purpose unknown                                    |
| `+0x56` | u8       | —               | Always 0                                                      |
| `+0x57` | u8       | —               | Always 1; purpose unknown                                     |
| `+0x58` | u8       | —               | Always 1; purpose unknown                                     |
| `+0x59` | u8 × 5   | —               | Always 0; padding                                             |

> Footer offsets are relative to the byte immediately following the icon path.

---

## petoffset.dbss

Provides O(1) lookup of any pet record by `pet_id`. Records are **not** stored in file order — use the offset to locate any record.

### Header (4 bytes)

| Offset  | Type | Field | Notes                       |
| ------- | ---- | ----- | --------------------------- |
| `+0x00` | u32  | count | Must equal `pet.dbss` count |

### Offset Record (10 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                                           |
| ------- | ---- | ----------- | ------------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id      | Matches `pet_id` in the main record                                             |
| `+0x02` | u32  | data_offset | Absolute byte offset in `pet.dbss` to the **data** (past the 2-byte key prefix) |
| `+0x06` | u16  | data_size   | Size of data in bytes (excluding the 2-byte key prefix)                         |
| `+0x08` | u16  | —           | Always 0; padding                                                               |

`record_start = data_offset - 2` gives the position of the 2-byte key prefix in the file.  
`total_record_size = data_size + 2`.

---

## Suggested UI Layout

| Column         | Type | Notes                                                                                                  |
| -------------- | ---- | ------------------------------------------------------------------------------------------------------ |
| Pet ID         | num  | `pet_id` as decimal only                                                                               |
| Icon           | Icon | Rendered from `icon_path`; shown immediately after Pet ID                                              |
| Name           | text | LOC type 6 lookup with `str_id1 = pet_id`; fallback to raw species ID                                  |
| Species ID     | num  | Raw `species` code                                                                                     |
| Tier           | num  | `tier` (0–4)                                                                                           |
| Skill Slots    | num  | `equip_skill_slots`                                                                                    |
| Max Level      | num  | `skill_capacity` (10 for normal, 20/30/50 for Airiss)                                                  |
| Acquire Type   | num  | `acquire_type_id` → `petequipskillaquire.dbss`                                                         |
| Equip Skill ID | num  | `equip_skill_id`                                                                                       |
| Grade          | text | Optional `petgrade.dbss` join on `(species, variant)`: 1 Classic, 2 Rare, 3 Premium, 4 Rare, 5 Special |

Rows are sorted by `pet_id` ascending for stable browsing.

---

## Notes

- Total file size = 6 + Σ(2 + `data_size`) for all 1782 records = 332420 bytes.
- Record size varies because `icon_path_len` differs per pet (observed: 55–68 bytes). The 32-byte header and 94-byte footer are fixed; only the path varies.
- `pet_id` appears three times per record: as the 2-byte key prefix in the file, as field `+0x00` in the data header, and as the `pet_id` field in the `petoffset.dbss` index.
- English pet display names resolve from `languagedata_en.loc` with `str_type = 6` and `str_id1 = pet_id`.
- `equip_skill_slots` = `tier + 1` for all regular pets (values 1–4). Airiss pets break this rule, reaching values of 7, 8, or 9.
- `skill_capacity` is 10 for all regular pets. Airiss variants: tier 1 = 20, tier 2 = 30, tier 3 = 50.
- Byte `+0x12` value is unknown; it does NOT reliably match the icon filename's 4-digit number (e.g. Cat_0991 → byte=0, Cat_0000 → byte=45).
- The three constant groups in the footer (30000, 15000, 30000, 500000, 1000000, 2) are identical in every record.
- `acquire_type_id` values 301–304 appear for regular pets and correspond to tiers 0–4 (tier 0 → 301, tier 4 → 304); lower values (1, 2, 3, 4) and mid-range values (101–104, 201–204) appear for specific sub-groups.
- The `upgrade_table` (10 × 1,000,000) is uniform across every record; the meaning of the 10 slots is unknown.

---

## Open Questions

### Byte `+0x12` purpose

This byte was initially labeled `dds_variant` under the assumption that it matched the 4-digit icon filename number, but that is incorrect. Cats 0991–0993 all return 0; Cat_0000 returns 45; Dogs show values like 79, 68, 51 that don't match path numbers or tier. The field's actual meaning is unknown.

### Footer constant fields

The six constant u32 values in the footer (30000, 15000, 30000, 500000, 1000000, 2) are identical for all 1782 records. They may be global pet system parameters duplicated per record, or references to shared game tables. Their in-game meaning (satiety, exchange cost, breeding cost?) is unconfirmed.

### `upgrade_table` (footer `+0x2A`)

Ten u32 values, all 1,000,000, in every record. Possible candidates: experience thresholds, or maximum capacity values. The uniform value makes interpretation difficult without a game reference.

### `acquire_type_id` semantics

`acquire_type_id` keys into `petequipskillaquire.dbss`, which defines per-slot acquisition costs (3 cost fields per slot, 14 sub-entries per record). The semantic meaning of the three cost fields (silver / item / removal cost?) and which sub-entry index maps to which slot is not confirmed.

### `type_param` (`+0x14`)

Varies by pet type (0 for many; non-zero values like 0x00BF7A00 for others). Consistent within a species group. Purpose unknown — could be a bitfield of capabilities, a hash, or a sub-type attribute.

### `tier_score` (`+0x53`)

Values: 11 (tier ≤ 1), 16 (tier 2), 17 (tier ≥ 3). Monotonically related to tier but not a simple 1:1 mapping. Possibly a UI display tier, a difficulty tier, or a capacity index.
