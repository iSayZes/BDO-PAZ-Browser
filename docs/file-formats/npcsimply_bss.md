# `npcsimply.bss` Format

## Purpose

Stores a compact identity table for service and story NPCs. Each row maps a character ID to its primary NPC service role, inline Korean display strings and, for most rows, a `getknowledge(<id>);` action script that links the NPC to a knowledge ID. Names and roles in the user's language come from LOC type `6`, keyed by the same character ID: `str_id4` 0 is the name and 1 the role.

Example:

```text
character_id: 47727 -> "Jackson"  -> kind: 3 (ShopMerchant) -> name: 잭슨  -> role: <과일상인>
character_id: 47647 -> "Neoksam"  -> kind: 25 (ItemMarket)  -> role: <거래소장> -> script: getknowledge(2387);
```

## File Layout

Top-level PABR block with a fixed-width record table followed by an inline string pool.

| Offset  | Type     | Field       | Notes                                      |
| ------- | -------- | ----------- | ------------------------------------------ |
| `+0x00` | char[4]  | magic       | ASCII `PABR`                               |
| `+0x04` | u32      | count       | Number of NPC records (observed: 2,169 in an older extraction, 2,237 in the pre-2026-09-27 fixture, 2,238 in the 2026-09-27 client) |
| `+0x08` | record[] | records     | 33-byte records repeated `count` times     |
| varies  | pool     | string_pool | Counted string table referenced by records |
| EOF - 8 | trailer  | trailer     | Offset of the string pool, see below       |

All multi-byte values are little-endian unless noted otherwise.

## Record Structure

### NPC Record (33 bytes, repeated `count` times)

| Offset  | Type | Field             | Notes                                                                 |
| ------- | ---- | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_id      | Character-template key; all 2237 exist in `characterstatic.dbss`; all 2238 have a LOC type `6` name in client 3458, see Notes |
| `+0x02` | u8   | unknown_02        | `1` on 2074 rows; runs of sequential values on related NPCs, see Open Questions |
| `+0x03` | u8   | zero              | Always 0                                                              |
| `+0x04` | u32  | kind              | Primary `SpawnType` role; 23 observed values in the range 1-40         |
| `+0x08` | u32  | script_ref        | String-pool index of the action script; `getknowledge(...)` on 2161 rows (one spelled `getKnowledge`), the empty string on 76 |
| `+0x0C` | u32  | lease_item_id     | Usually 0; on 58 rows the item key (LOC type `0`) of the `[CP]` item the NPC leases, see Notes |
| `+0x10` | u16  | lease_cost        | Usually 0; the lease cost in contribution points on the same 58 rows as `lease_item_id` |
| `+0x12` | u16  | unknown_12        | Usually `0xFFFF`; 0 on the same 58 rows as `lease_item_id`             |
| `+0x14` | u8   | has_lease_condition | `1` when the NPC's lease dialog option has a condition script (32 of the 58 lease rows), see Notes |
| `+0x15` | u32  | name_ref          | String-pool index for the Korean display name                          |
| `+0x19` | u32  | role_ref          | String-pool index for Korean role/title text; points at the empty string when absent |
| `+0x1D` | u32  | padding           | Always 0                                                              |

An earlier version of this doc read `+0x00` as a u32 `npc_id`. The high half is `unknown_02`: as a u32 only 20 of 2237 values resolve through LOC, as a u16 all of them do. Earlier versions of this doc also called `lease_item_id` `unknown_id` and then `unknown_0c`, `lease_cost` `unknown_value` and then `unknown_10`, `unknown_12` `sentinel` and `has_lease_condition` `unknown_flag` and then `unknown_14`.

`script_ref`, `name_ref`, and `role_ref` are unaligned u32 values inside the 33-byte row. bdo-data-extractor ([iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)) reads the same references as aligned u32s at `+0x14` and `+0x18` shifted right by 8 (`packedNameRef`, `packedTitleRef`); both readings give the same index on every row, because the byte after each unaligned reference is always 0. `name_ref` is usually `script_ref + 1` (2045 rows).

The `script_ref` string equals the `characterstatic.dbss` action script of the same character on all 2237 rows.

### `kind` Values

`kind` is a `CppEnums.SpawnType` value, the same enum as the 46 role flags in `characterspawntype.dbss`. For all 2237 rows, the `characterspawntype.dbss` flag at index `kind` is set for the same character, so `kind` picks one primary role from that character's flags. Most common values:

| Value | Rows | SpawnType | Typical role text |
| ----- | ---- | --------- | ----------------- |
| 4     | 1197 | `ImportantNpc` | `<탐험 거점 관리>`, `<물물교환원>`, empty |
| 3     | 226  | `ShopMerchant` | `<창고지기>`, `<약초상인>` |
| 5     | 121  | `TradeMerchant` | `<무역 관리>` |
| 2     | 105  | `ItemRepairer` | `<대장장이>`, `<무기상인>` |
| 16    | 97   | `Potion` | `<잡화상인>` |
| 7     | 87   | `Stable` | `<마구간지기>` |
| 20    | 55   | `Collect` | `<재료상인>` |
| 1     | 46   | `SkillTrainer` | `<기술교관>` |
| 8     | 38   | `Wharf` | `<나루터지기>` |
| 25    | 22   | `ItemMarket` | `<거래소장>` |

### String Pool

The string pool begins immediately after the fixed record table:

```text
string_pool_offset = 0x08 + count * 33
```

Observed `string_pool_offset` is `0x12065` (older extraction: `0x117A1`).

| Offset  | Type        | Field        | Notes                                      |
| ------- | ----------- | ------------ | ------------------------------------------ |
| `+0x00` | u32         | string_count | Observed: 4746                             |
| `+0x04` | string[]    | strings      | Counted entries, indexed from 0            |

### String Entry

Every entry has a one-byte encoding flag and a u32 byte length. There is no
terminator: the next entry starts right after the payload, and the last one ends
exactly at the trailer.

| Offset  | Type  | Field       | Notes                                   |
| ------- | ----- | ----------- | --------------------------------------- |
| `+0x00` | u8    | is_wide     | `1` for UTF-16LE, `0` for UTF-8         |
| `+0x01` | u32   | byte_length | Payload length in bytes                 |
| `+0x05` | bytes | payload     | UTF-16LE when `is_wide=1`, else UTF-8   |

An earlier version of this doc read the flag as an optional marker and the
next entry's `0` flag as a terminator; both readings split the pool the same
way. `exploration.bss` uses the same entry layout, and the parser shares one
reader for both (`handlers/_common/pabr_strings.py`).

Observed pool contents: 2636 UTF-8 strings and 2110 UTF-16LE strings. The pool is not purely 8-bit: every script entry is UTF-16LE. One entry is the empty string (index 34 in the current file, index 0 in the older extraction); absent scripts and roles point at it.

### Trailer (8 bytes)

| Offset  | Type | Field              | Notes                                      |
| ------- | ---- | ------------------ | ------------------------------------------ |
| `+0x00` | u32  | string_pool_offset | Equals `0x08 + count * 33` (`0x12065`)     |
| `+0x04` | u32  | zero               | Always 0                                   |

This is the same `[string table][u32 rows_end][u32 0]` tail that `playercharacterstatic.bss` and `characterstaticoffset.dbss` carry after their rows.

## Suggested UI Layout

| Column       | Type | Notes                                                     |
| ------------ | ---- | --------------------------------------------------------- |
| Character ID | num  | `character_id`                                            |
| Name         | text | LOC `str_type=6`, `str_id1=character_id`, `str_id4=0`; the Korean `name_ref` without LOC |
| Kind         | text | `kind` shown as its role's display name, the same as the `characterspawntype.dbss` role headers (`role_labels.py`); the `SpawnType` name and value are in the tooltip |
| Role         | text | LOC `str_type=6`, `str_id1=character_id`, `str_id4=1` (`<Fruit Vendor>`); the Korean `role_ref` without LOC; blank when LOC holds `<null>` |
| Knowledge ID | num  | Parsed from `getknowledge(<id>);` in `script_ref`         |
| Leases       | list | Every lease of the character: the `CHARACTER_LEASES` index (all lease options in `detail_dialog.dbss`), as LOC `str_type=0` item name (in its grade colour) and cost, e.g. `[CP] Container (10 CP)`; the lease stored here keeps its own cost, and is the only one without the index; sorts by count |
| Script       | text | Raw script string for debugging/export                    |

## Notes

- The record table size is exactly `count * 33` bytes; fixed records end at `0x12065` (`0x12086` in the 2026-09-27 client), and the string pool parses exactly up to the 8-byte trailer.
- `script_ref` points to a `getknowledge(<id>);` UTF-16LE string for 2161 of 2237 records.
- `name_ref` and `role_ref` point to Korean UTF-8 strings in the same pool. Role strings are often bracketed labels such as `<과일상인>` or `<거점관리인>`. LOC type `6` `str_id4=1` holds the same role in the user's language on all 1998 rows with a role (`<과일상인>` is `<Fruit Vendor>`), and `<null>` on the 240 rows whose `role_ref` is empty (client 3458).
- Every row's character has `npc_kind` `2` (NPC) in `characterstatic.dbss`.
- `lease_item_id` is the `[CP]` item the NPC leases for contribution points. In client 3458 every one of the 58 values resolves through LOC type `0` to a `[CP]` item: `3001` [CP] Container on the Storage Keepers (and Basquean Ljurik, Bank of Hope), `58008` to `58012` the [CP] fences on Material Vendors, node managers and Old Moon Managers, `16142` [CP] Practice Matchlock, `16143` [CP] Flute, and single items such as `23004` [CP] Kaia Longsword on Kanobas, `693901` [CP] Leight's Hoe on Norma Leight and `45601` / `45602` the Licensed / Acknowledged Adventurer's Seal. `lease_cost` is the same for every NPC with the same item: Container `10`, Strong Fence `10`, Plain Fence `6`, Small Fence `3`, Practice Matchlock `2`, Flute `1`, the Kaia and Nesser gear and Leight's Hoe `50`, Licensed Seal `20`, Acknowledged Seal `60`. Checked in game (2026-09-28): Delorence (`47008`, `3001` / `10`) is a Storage Keeper who leases a [CP] Container for 10 CP.
- The lease itself is an NPC dialog option in `detail_dialog.dbss` (records keyed `1 << 16 | character_id`). Each option stores a condition script, a title such as `[대여] 작은 울타리` ("[Lease] Small Fence"), the dialog text and the action `buyItemByPoint(item, 0, 1, 5, cost)`. `lease_item_id` and `lease_cost` repeat the item and cost of the NPC's first lease option: the item matches on all 58 rows and the cost on 57. Merio (`43501`) is the exception, `2` here and `1` in his dialog; in game his Matchlock lease costs 2 (checked 2026-09-28), the same as the other Matchlock NPCs, so the charged cost follows `lease_cost` and the dialog's `1` is stale. NPCs with several lease options keep only the first here (Kanobas `23004` of his 25 Kaia weapons, Basquean Ljurik the Container and not the Excellent Adventurer's Seal `45603` at 100 CP), and Wale (`40605`) has a Small Fence lease in his dialog but no lease item here.
- `has_lease_condition` is `1` exactly when that option has a condition script, on all 58 lease rows (client 3458). The Containers, Flutes and Matchlocks check that you do not own one yet (`!getitemcount(3001,0)>0;`), the Kaia and Nesser gear add a level, quest and class check, and the fences of Martina Finto (`40024`) and Mercianne Moretti (`41085`) are quest-gated: Martina's reads `!iscontentsgroupopen(0,4017);<or>iscontentsgroupopen(0,4017);!clearquest(21125,64);<or>iscontentsgroupopen(0,4017);clearquest(21125,64);clearquest(21125,74);`, which item databases show as "Not finished quest: Tracking Giath, or finished Tracking Giath and Sands of Time". The fence NPCs with `0` (Zaaira `40002` and the others) have an empty condition.
- Every character has a LOC type `6` name in client 3458. Older clients missed 39 (`47623`, `47753`, `47772` to `47807` and `61267`); the handler shows the Korean `name_ref` for such a row.

## Open Questions

### What does `unknown_02` encode?

It is `1` on 2074 rows (every NPC of the older towns, Velia, Heidel and Calpheon included), `0` on 20 (mostly The Magnus entrances) and `2` on 18 (lore NPCs such as the Kalis Councilors and the Nesser family). In client 3458 the remaining 126 rows form numbered runs on the newer groups, roughly in character ID order:

- the Edania town NPCs `47742` to `47770` hold `5` to `33` (Alustin `5`, Bakora `6`, ... Resh `27`, Zario `29`, ... Clorince `33`), and the node managers `47773` to `47795` continue with `35` to `57`
- the node managers `47675` to `47704` hold `34` to `63`, and the five Thrones `47705` to `47709` `64` to `68`
- the Olvia Academy staff `62480` to `62502` hold `10` to `27`, and its bulletin board `62521` holds `99`. Here the ID order breaks once: Cliff (`62484`) holds `13` and Eileen (`62483`) `14`
- smaller runs: the Vestiges `47801` to `47807` (`100` to `108`) and the stable and wharf managers `50981` to `50989` (`144` to `151`)

The ranges overlap between groups (`35` is Abene in one run and Erhan in another), so it looks like an order within a group. It is not the knowledge order: in all four runs it follows neither the NPCs' card IDs nor their card order in the `mentaltheme.dbss` entry lists, which is the Knowledge window order (in game the Olvia Academy category lists Eileen before Cliff) (the Edania town NPCs are split over themes `355` and `356` while the values run through both). Two readings remain. It may be a sort key for an NPC list: `0` sits only on things never picked from a list (The Magnus entrance wells, the Referees, a Swing), `1` is the default of the older towns, and explicit numbers exist only in newer content. Or it is the authoring order with no visible effect, which would explain how closely it tracks the character IDs. Olvia Academy separates the two: an NPC list (not the Knowledge window) that shows Cliff before Eileen sorts by this value. The world map search for "Cliff" lists the Olvia Academy Cliff (`62484`, value `13`) before the Western Guard Camp Captain Cliff (`40029`, value `1`) (2026-09-28). The search for "Emma Bartali" lists the Olvia Academy Head Administrator (`62481`, value `11`), then the Food Vendor at the farm (`47763`, value `26`), then Node Management at the outpost (`40025`, value `1`). Both searches follow character ID from high to low, and neither follows this value. It is not a code per title (Wharf Manager holds `16`, `25` and `146` to `149`, Stable Keeper `14`, `144` and `145`), but inside a group it reads as a job ranking: Olvia Academy runs Headmaster `10`, Head Administrator `11`, Deputy Headmaster `12`, the professors from Combat `13` and Alchemy `14` on, then the staff; the Edania town runs Secret Guard, Blacksmith, Skill Instructor, Storage Keeper, Central Market, Trade Manager and Work Supervisor (`5` to `11`), then the priest, stable and wharf, the guild and imperial delivery NPCs, and the vendors last (`23` to `33`). The Knowledge window and the map search are both ruled out, and the NPC search only finds one NPC at a time, so no list I can check in game shows the order (2026-09-28). It is most likely the authoring order and stays `unknown_02`.

### What is `unknown_12`?

It is `0` on the 58 rows with a lease item and `0xFFFF` on every other row, never anything else. It is probably the index of the lease option in the NPC's dialog (`0` the first, which is the one `lease_item_id` repeats; `0xFFFF` none) and has no visible effect.

### How does the client choose `kind` among several role flags?

`kind` is always one of the character's `characterspawntype.dbss` flags, but characters often have several (for example `Stable` and `Mating`). Whether `kind` drives the map icon, the NPC list filter or something else is not confirmed.
