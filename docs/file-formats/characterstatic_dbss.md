# `characterstatic.dbss` Format

## Purpose

Variable-length character/NPC static data table: render and interaction metadata for every character template (player classes, NPCs, monsters, mounts, objects), not combat stats. Each record is keyed by a character ID and stores two inline scripts, the character's kind, a model path, a large numeric attribute block and, for player characters, the gameplay class type. Many NPC records have a `getknowledge(<id>);` script, which links the character to the knowledge entry the player gains by talking to it.

Example:

```text
character_id: 47759 -> "Yamarko"
script: getknowledge(15546);   -> knowledge 15546 "Yamarko"
npc_kind: 2 (NPC)
model_path: npc/...

character_id: 2 -> "Ranger"
class_type: 4                  -> LOC type 21 "Ranger"
```

Field names `npcKind` and `classType` follow the notes of [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor); this doc writes them as `npc_kind` and `class_type`.

## Companion Files

| File                    | Required | Role                                                   |
| ----------------------- | -------- | ------------------------------------------------------ |
| `characterstaticoffset.dbss` | Required | Maps `character_id` to byte offset and payload size |
| `languagedata_en.loc`   | Optional | Resolves display names for `character_id` and `class_type` |

Related but not required:

| File                                                   | Role |
| ------------------------------------------------------ | ---- |
| `playercharacterstatic.bss`                            | `PABR` list of player-like character IDs; see [below](#playercharacterstaticbss) |
| `hardcorerandomspawncharacterstaticstatusmanager.bss`  | Small `PABR` data file that references character IDs, including `62223` ("Wandering Merchant"); layout not yet decoded |
| `fuelinsertcharacterstaticstatus.bss`                  | Small related BSS entry; layout not yet decoded |

All multi-byte integer values observed in the DBSS payload are little-endian.

## File Layout

| Offset  | Type | Field         | Notes                                      |
| ------- | ---- | ------------- | ------------------------------------------ |
| `+0x00` | u32  | record_count  | Number of records; observed `24418` (older fixture: `24017`; 2026-09-27 client: `24551`) |
| `+0x04` | ...  | record_stream | Repeated inline ID + variable-length payload chunks |

The stream is not fixed-width. Use `characterstaticoffset.dbss` to slice records.

## Record Structure

### Stream Entry

Each logical record occupies `2 + payload_size` bytes in the main stream.

| Offset  | Type | Field        | Notes |
| ------- | ---- | ------------ | ----- |
| `+0x00` | u16  | character_id | Matches the offset-table `character_id`; unique across observed records |
| `+0x02` | ...  | payload      | Starts at the offset listed in `characterstaticoffset.dbss`; byte count is `payload_size` |

Offset-table `data_offset` values point to the payload, not to the inline `character_id`. In observed data, the two bytes immediately before every `data_offset` equal the row's `character_id`.

### Payload Head

Offsets are relative to `data_offset`. The two scripts are length-prefixed, so everything after them moves with their length. `p` is the first byte after `condition_script`.

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u8[8] | header          | Unknown; 8 byte patterns cover most rows, the most common being `00 00 00 00 00 01 01 00` (7,947 rows) |
| `+0x08` | u8   | tag              | `0x15` on all 24,418 rows |
| `+0x09` | i64  | action_len       | Length of `action_script` in UTF-16 code units |
| `+0x11` | u16[] | action_script   | UTF-16LE, not null-terminated; empty on 18,733 rows, `getknowledge(<id>);` on 5,684 |
| varies  | i64  | condition_len    | Length of `condition_script` in UTF-16 code units |
| varies  | u16[] | condition_script | UTF-16LE; non-empty on 403 rows, see [Script Values](#script-values) |
| `p`     | u8   | unknown_p        | `0` on 24,072 rows, `1` on 346 |
| `p+1`   | u16  | character_id     | Equals the offset-table key on all 24,418 rows |
| `p+3`   | u16  | unknown_p3       | `0` on 21,965 rows; non-zero on 2,453, all but one with `npc_kind` low byte `1` (e.g. `29929` Garmoth `95`, `29916` Mole `184`) |
| `p+5`   | u32  | npc_kind         | Low byte is the character kind (see below); higher bits look like flags |
| `p+9`   | u32  | unknown_p9       | Usually `0`; `65535` on 2,921 rows |
| `p+13`  | u32  | unknown_p13      | Usually `0`; high-bit values such as `0x80000000` on some rows |
| `p+17` onward | ... | attributes  | Mixed u32/f32-like fields; many common constants and zero regions. Client 3464 inserted 8 bytes, at `p+196` on most rows |

Reading `p+1` as a u32 (as bdo-data-extractor does) only works when `unknown_p3` is `0`; on 2,453 rows the high half is non-zero, so the ID is a u16.

### `npc_kind` Low Byte

Observed correlation between the low byte and the first folder of `model_path`:

| Value | Rows | Model folders |
| ----- | ---- | ------------- |
| `0`   | 61    | `pc` only; exactly the player-character IDs `1`-`47` and `201`-`214` |
| `1`   | 9,112 | Mostly `monster`, also `infinitydefence`, `pc_summon`, `object` |
| `2`   | 6,201 | Mostly `npc`, also `object`, `monster` |
| `3`   | 3,293 | `creature`, `riding`, `cash` (pets and mounts) |
| `4`   | 564   | `object` only |
| `7`   | 940   | Mostly `monster` |
| `8`   | 3,964 | `monster` |
| `9`   | 220   | `summon` |

Values `5`, `6`, `12`, `15` and `17` occur on 1 to 50 rows each. The value names are not confirmed.

### Model Path

Every record holds at least one model path, stored as an i64 byte length followed by ASCII text with no terminator, e.g. `[i64 25] npc/pedu2/npc_pedu2_named`. Its position after `p` varies (most often `p+299` on client 3464, `p+291` before), so find it by scanning for the length-prefixed string. 315 records hold a second path-like string; the longer one is the model. Top-level folders: `monster` (13,655), `npc` (5,078), `creature` (2,109), `object` (1,359), `riding` (793), `cash` (473).

The same length-prefixed ASCII form holds one or two other strings per record,
behaviour names rather than paths: `9999` (8,212 rows in the 24,017-record
fixture), `9999_Bow`, `Monsters_Main_Manager`, `Pet_Dog`, `HiredWorker`. None
contains a `/`, so the parser takes the longest string with a `/` in it as
`model_path`. In that fixture every record has exactly one such string.

### Payload Tail

Offsets are relative to the end of the payload (`data_offset + payload_size`).

| Offset | Type | Field      | Notes |
| ------ | ---- | ---------- | ----- |
| `-24`  | u8   | class_type | Gameplay class enum; `101` on every non-player row, `0`-`46` on the 106 `playercharacterstatic.bss` members |
| `-23`  | u8   | unknown_t23 | `0`, or `3` on 65 rows (siege structures such as `12821` "Field HQ" and the node forts) |
| `-22`  | u8[2] | zero      | Always `0` |
| `-5`   | f32  | unknown_tail_f32 | `5000.0` on 23,969 rows, `15000.0` on 339, `3000.0` on 157, `1000.0` on 70 |
| `-1`   | u8   | unknown_t1 | New in client 3464; `1` on 2,418 rows, 2,388 of them with `npc_kind` low byte `1`; else `0` |

Before client 3464 the payload ended at the f32, so each offset above sat one
byte closer to the end (`class_type` at `-23`). The parser reads only the
current layout.

`class_type` is a different ID from `character_id`: Warrior is character `1` / class `0`, Ranger `2` / `4`, Sorceress `3` / `8`, Berserker `4` / `12`, Tamer `5` / `16`, Musa `21` / `20`, Valkyrie `25` / `24`. The class number resolves through LOC `str_type=21` (class names) and is the value the client's `getClassType()` returns. bdo-data-extractor reads it as a u32; that fails on the 65 rows where `unknown_t23` is `3`, so it is read here as a u8. Kunoichi and Ninja are separate classes (`25` and `26` in LOC type 21): character `26` Kunoichi has `25` and character `27` Ninja has `26`, but character `209`, also named Kunoichi with the same female model (`pc/13_pnw/ninjawomenaction_noweaponmain_w`), stores `26`. Whether that is a data slip or means something is not known; it cannot be seen in game.

Observed `payload_size` ranges from `465` to `1042` bytes on client 3464 (earlier clients: `456` to `1033`; older fixture: `478` to `1055`).

## Script Values

`action_script` holds the interaction action:

| Pattern                 | Rows     | Notes |
| ----------------------- | -------- | ----- |
| empty                   | `18733`  | Most records |
| `getknowledge(<id>);`   | `5684`   | Knowledge gained on interaction; one row (`50613`) spells it `getKnowledge(933);` |

The app groups these links into the `KNOWLEDGE_CHARACTERS` lookup index (`build_knowledge_character_index`), which the `mentalcard.dbss` Learned From column reads together with the `knowledgelearning.dbss` links. The `getknowledge` argument is a knowledge `entry_id`: 5,680 of the 5,684 arguments exist in `mentalcard.dbss` and 5,683 have a LOC `str_type=34` name, which matches the NPC name (e.g. `47791` "Ehren" -> `15936` "Ehren").

`condition_script` is empty on 24,015 rows. The other 403 hold semicolon-separated condition expressions, 98 of them alongside a `getknowledge` action. Most common calls: `progressQuest` (239, plus `ProgressQuest`/`progressquest` spellings), `CheckRideCharacter` (188), `getOceanTendency` (38), `getIntimacy` (28), `getLifelevel` (27), `clearQuest` (17). Example: `!CheckRideCharacter(29820);...;getIntimacy(47098)>-2500;`.

## `characterstaticoffset.dbss`

Provides lookup rows for `characterstatic.dbss`.

### Header (8 bytes)

| Offset  | Type  | Field | Notes |
| ------- | ----- | ----- | ----- |
| `+0x00` | u8[4] | magic | ASCII `PABR` |
| `+0x04` | u32   | count | Number of rows; observed `24418`, matching `characterstatic.dbss` |

### Index Row (10 bytes, repeated `count` times)

| Offset  | Type | Field        | Notes |
| ------- | ---- | ------------ | ----- |
| `+0x00` | u16  | character_id | Matches the two inline ID bytes immediately before `data_offset` |
| `+0x02` | u32  | data_offset  | Absolute byte offset into `characterstatic.dbss` payload data |
| `+0x06` | u32  | payload_size | Payload byte count, excluding the two inline ID bytes |

### Trailer (12 bytes)

| Offset  | Type | Value | Notes |
| ------- | ---- | ----- | ----- |
| `+0x00` | u32  | `0`   | Consistent with an empty string-table count, as in `playercharacterstatic.bss` |
| `+0x04` | u32  | varies | Observed `244188`; equals the end offset of the offset-table rows |
| `+0x08` | u32  | `0`   | Sentinel-like value |

Rows sorted by `data_offset` cover the whole main file from `+0x04` through EOF when the two inline ID bytes before each payload are included.

## `playercharacterstatic.bss`

`PABR` membership list of player-like character IDs: the live classes plus reserved, test, mercenary and alternate-mode characters. It is not an active-class list by itself.

| Offset  | Type    | Field         | Notes |
| ------- | ------- | ------------- | ----- |
| `+0x00` | u8[4]   | magic         | ASCII `PABR` |
| `+0x04` | u32     | count         | Observed `106` (bdo-data-extractor saw `96` on an older client, which matches the 96 non-`101` `class_type` rows in the older fixture) |
| `+0x08` | u16[]   | character_ids | `count` character IDs |
| varies  | u32     | string_count  | `0` |
| varies  | u32     | rows_end      | `220` = `8 + count * 2` |
| varies  | u32     | zero          | `0` |

Every member has a `characterstatic.dbss` record with `class_type` other than `101`, and no other record does. The members are `1`-`47`, `201`-`214`, the mercenaries `521`, `523`-`528` and `536`, and the unnamed `39831`-`39867`, whose `class_type` values run `0`-`36`.

## Suggested UI Layout

| Column       | Type | Notes |
| ------------ | ---- | ----- |
| Character ID | num  | `character_id`; right-aligned |
| Icon         | text | Resolved from the character ID through the character icon index; covers about 20% of characters |
| Name         | text | LOC lookup `str_type=6`, `str_id1=character_id`; shown only when LOC is loaded |
| Action Script | text | `action_script` |
| Condition    | text | `condition_script` |
| Knowledge ID | num  | Extract from `getknowledge(<id>);` (case-insensitive) when present; dash otherwise, stored as `None` so it sorts last |
| NPC Kind     | num  | `npc_kind` low byte (`npc_kind_low` in the handler, which also keeps the full u32 for search and CSV) |
| Class Type   | num  | `class_type`; dash when `101` (not a player character), stored as `None` so it sorts last |
| Model        | text | `model_path` |
| Payload Size | num  | Useful for debugging variable layouts |

## Notes

- Observed files contain `24418` records (older fixture: `24017`; 2026-09-27 client and client 3464: `24551`).
- Offset rows are sorted by descending character ID in early data but should be treated as an index, not as a sorted table guarantee.
- `character_id` values are unique u16s; the highest observed is `65302`.
- LOC lookup confirms sample IDs: `47759` is "Yamarko", `16640` is "Dev Plant210", and `62223` is "Wandering Merchant".
- A character ID can be reused for a different character: in the older fixture `47759` was "Edania Merchant" (`getknowledge(14469);`, model `npc/pedu/npc_pedu_named`), and it heads the offset table there; in the 2026-09-27 client `47791` "Ehren" heads it.
- `characterstaticoffset.dbss` uses the same `PABR` 10-byte row pattern as `characterspawntypeoffset.dbss`, but its `data_offset` points after an inline u16 ID.
- An earlier version of this doc read the script as a null-terminated UTF-16BE string at `+0x10` followed by 8 zero bytes. That misread is one byte off the real `action_len` + UTF-16LE layout; it decodes ASCII scripts correctly only while `condition_script` is empty, and it is the source of the "306 control-like strings" the old doc listed.
- `tag`, the inline `character_id` at `p+1` and `class_type` validate on both the current client and the older test fixture (96 players there).

## Open Questions

### Numeric Attribute Semantics

The block after `npc_kind` contains many stable fields and constants, but its sub-structure is not confirmed. Additional cross-references, a client symbol name list, or in-game examples are needed before naming fields beyond raw offsets.

### What do the `npc_kind` values and high bits mean?

The low byte tracks the model folder (`0` player, `1`/`7`/`8` monster, `2` NPC, `3` pet or mount, `4` object, `9` summon), but the names of the values are not confirmed, and the high bits (e.g. `0xFE0C0003` on 2,788 rows) are unmapped. bdo-data-extractor calls it a semantic entity-kind bitfield with partly unmapped combat flags.

### What are `unknown_p3`, `unknown_p`, `unknown_t23` and `unknown_t1`?

`unknown_p3` is non-zero on 2,453 rows, all but one of kind `1` (monster), with values such as `95` and `184`. `unknown_p` is `1` on 346 rows, `unknown_t23` is `3` only on siege structures, and `unknown_t1` (added in client 3464) is `1` on 2,418 rows, nearly all monsters. None has been tied to another table.

### What is the 8-byte payload header?

Its bytes form a handful of patterns (`00 00 00 00 00 01 01 00`, `01 00 00 00 00 01 00 00`, ...), which look like independent boolean flags, but no flag has been named.

### Related BSS Files

`hardcorerandomspawncharacterstaticstatusmanager.bss` and `fuelinsertcharacterstaticstatus.bss` are related by name, but they are not required to parse `characterstatic.dbss`. Their layouts should be documented separately if needed.
