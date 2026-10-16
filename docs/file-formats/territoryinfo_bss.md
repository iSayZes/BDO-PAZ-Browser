# `territoryinfo.bss` Format

## Purpose

The world's territories (Balenos, Serendia, Calpheon, ...) in game order: one
row per territory with its Korean territory and nation names, world map mark
icons, conquest crown and armor items and up to three world positions. The row
key is the LOC type 12 ID, so the English territory and nation names come from
that type.

Example:

```text
territory 0  발레노스 자치령 -> "Balenos"   nation 칼페온 공화국 -> "Republic of Calpheon"
  autonomous, icon territorymark_valenos_small.dds
  crown 23381 Silver Mane Horse Crown, armor 23386 Silver Mane's Armor
```

## Companion Files

| File                  | Required | Role                                                                                     |
| --------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | LOC type 12, `str_id1` = `territory_key`, `str_id4` 0 / 1 = nation or realm / territory name |
| `languagedata_en.loc` | Optional | LOC type 0 names of the crown and armor items                                            |

All multi-byte values are little-endian.

## File Layout

The shared PABR string table layout (`_common/pabr_strings.py`).

| Offset        | Type    | Field        | Notes                                                            |
| ------------- | ------- | ------------ | ---------------------------------------------------------------- |
| `+0x00`       | char[4] | magic        | ASCII `PABR`                                                     |
| `+0x04`       | u32     | count        | Number of rows; 14 on client 3458                                |
| `+0x08`       | row[]   | rows         | Variable rows repeated `count` times, byte-packed                |
| `table_start` | table   | string_table | u32 count, then `count` x (u8 is_wide, u32 byte length, payload) |
| EOF - 8       | u32     | table_start  | Offset of the string table, where the rows end                   |
| EOF - 4       | u32     | zero         | Always 0                                                         |

A row is `88 + 4 * list_count` bytes. The rows tile `[0x08, table_start)`
exactly (12 rows of 88 bytes and 2 of 92 on client 3458), so a parser walks
them in order and fails when they do not end at `table_start`.

## Record Structure

### Territory Row (88 + 4 x `list_count` bytes)

| Offset             | Type        | Field          | Notes                                                                                 |
| ------------------ | ----------- | -------------- | ------------------------------------------------------------------------------------- |
| `+0x00`            | u16         | territory_key  | 0 to 13, equal to the row index; LOC type 12 `str_id1`                                |
| `+0x02`            | u8          | unknown_2      | `1` on Calpheon to Outer Edania, `0` on Balenos, Serendia and Inner Edania            |
| `+0x03`            | u8          | is_autonomous  | `1` on Balenos and Serendia only, the two names ending in 자치령 (autonomous territory) |
| `+0x04`            | f32[3] x 3  | positions      | Three world `x, y, z` positions; all zero when unused                                 |
| `+0x28`            | u32         | nation_hash    | Same value on every territory of one nation, different between nations                |
| `+0x2C`            | u32         | nation_ref     | String table index of the Korean nation or realm name                                 |
| `+0x30`            | u32         | name_ref       | String table index of the Korean territory name                                       |
| `+0x34`            | u32         | icon_large_ref | String table index of the large world map mark, relative to `ui_texture/`             |
| `+0x38`            | u32         | icon_small_ref | String table index of the small world map mark, relative to `ui_texture/`             |
| `+0x3C`            | u32         | unknown_3c     | `2` on every row                                                                      |
| `+0x40`            | u32         | unknown_40     | `0` on every row                                                                      |
| `+0x44`            | u32         | crown_item_id  | Conquest crown item (LOC type 0)                                                      |
| `+0x48`            | u32         | armor_item_id  | Conquest armor item (LOC type 0)                                                      |
| `+0x4C`            | u32         | list_count     | Entries in `unknown_54`; `1` on Serendia and Mediah, `0` elsewhere                    |
| `+0x50`            | u32         | unknown_50     | `0` on every row                                                                      |
| `+0x54`            | u32[]       | unknown_54     | `list_count` values: `114` on Serendia, `312` on Mediah                               |
| `+0x54 + 4n`       | u32         | unknown_tail   | `0` on every row                                                                      |

Positions on client 3458: Calpheon, Mediah and Valencia fill all three,
Kamasylvia and O'dyllita only the first, the rest none. The first and third
positions lie within about 20,000 units of a castle node in
`mapdata_realexplore2.bwp`: `calpheon_castle` (702), `mediacastle` (1152),
`valencia_castle` (1342) and `othilita_castle` (1692). Valencia's second
position sits next to `ruins of castle valencia` (1374).

Crowns and armor: Balenos to Mediah each have their own pair (Silver Mane,
Blue Lion, Golden Eagle, Asula); Valencia and every later territory store
the Crown of Aal (23385) and Armor of Aal (23390).

### String Table

46 strings on client 3458, all referenced. The territories of one nation
share its nation entry (Republic of Calpheon, Alyaelli), and where nation and
territory names match (The Great Ocean, Kamasylvia and the other single
territory realms) both refs point at one entry. The Great Ocean (territory 5) stores Valencia's marks under
`New_UI_Common_forLua/Widget/WorldMap/territory/`; every other icon is under
`Renewal/ETC/WordMap/`. Paths keep mixed case, so the handler lowercases them.

## Notes

- iDevelopThings' [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  documents the same layout (FORMATS.md, section 10), with `unknown_2` as a
  primary-territory flag and the positions as world map marks; neither
  meaning is confirmed here, so `unknown_2` keeps its offset name.
- bdo-data-extractor reads a territory index in each `regioninfo.bss` region
  that joins this file and LOC type 12.
- The `territory_key` of `dropuimaincategoryinfo.bss` (see
  [dropuihuntinggroundinfo](dropuihuntinggroundinfo_bss.md)) is the same LOC
  type 12 key.

## Open Questions

### What `unknown_54` Holds

Serendia stores `114` and Mediah `312`. LOC type 17 names region 114 Faust
Forest and 312 Calpheon Holy College Trade Zone, neither of which fits its
territory, so these are not region keys. The list position is also only
inferred: with one entry the zero `unknown_50` and `unknown_tail` around it
could sit on either side, since every other row has them at zero.

### What `unknown_2` Means

It is `1` on every territory from Calpheon to Outer Edania and `0` on the two
autonomous territories and Inner Edania. bdo-data-extractor calls it the
nation's primary territory, but Kamasylvia, Drieghan and the other single
territory realms also carry `1`, and Outer Edania does while Inner Edania
does not.

### What the Three Positions Mark

The first and third positions lie near each territory's castle node and the
second, on Valencia, near the castle ruins, which points at siege use, but
Calpheon's and Mediah's second positions match no named node and
Kamasylvia's first position is near no castle node. bdo-data-extractor calls
them world map marks.
