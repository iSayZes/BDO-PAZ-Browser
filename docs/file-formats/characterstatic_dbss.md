# `characterstatic.dbss` Format

## Purpose

Variable-length character/NPC static data table: render and interaction metadata for every character template (player classes, NPCs, monsters, mounts, objects), not combat stats. Each record is keyed by a character ID and stores two inline scripts, the character's kind and grade, the karma change when it dies, its vehicle type, the name of its AI script, a model path, its Korean name and title, a large numeric attribute block, the item that places or summons it and, for player characters, the gameplay class type. Many NPC records have a `getknowledge(<id>);` script, which links the character to the knowledge entry the player gains by talking to it.

Example:

```text
character_id: 47759 -> "Yamarko"
script: getknowledge(15546);   -> knowledge 15546 "Yamarko"
npc_kind: 2 (NPC)
model_path: npc/...

character_id: 2 -> "Ranger"
class_type: 4                  -> LOC type 21 "Ranger"

character_id: 9001 -> "Beginner's Brown Horse"
vehicle_type: 0                -> CppEnums.VehicleType Type_Horse
tendency_on_dead: -500         -> killing it costs 500 karma

character_id: 2053 -> "[Event] Fence"
source_item_id: 58011          -> item "[Event] Fence"
```

Field names `npcKind` and `classType` follow the notes of [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor); this doc writes them as `npc_kind` and `class_type`.

## Companion Files

| File                    | Required | Role                                                   |
| ----------------------- | -------- | ------------------------------------------------------ |
| `characterstaticoffset.dbss` | Required | Maps `character_id` to byte offset and payload size |
| `languagedata_en.loc`   | Optional | Resolves display names for `character_id`, `class_type` and `source_item_id` |

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
| `p+3`   | u16  | unknown_p3       | `0` on 21,965 rows; non-zero on 2,453, all but one with `npc_kind` `1` (e.g. `29929` Garmoth `95`, `29916` Mole `184`) |
| `p+5`   | u8   | npc_kind         | `gc::CharacterKind` of the 2016 client; see [`npc_kind` Values](#npc_kind-values) |
| `p+6`   | u8   | grade            | `CppEnums.CharacterGradeType`; see [Grade](#grade) |
| `p+7`   | i32  | tendency_on_dead | Karma change when the character dies; see [Karma](#karma) |
| `p+11`  | i32  | ocean_tendency   | Naval fame value on sea monsters and ships; see [Ocean Tendency](#ocean-tendency) |
| `p+15` to `p+165` | ... | attributes | Mixed u32/f32-like fields; many common constants and zero regions |
| `p+166` | u8   | vehicle_type     | `CppEnums.VehicleType`; `65` when the character is not a vehicle. See [Vehicle Type](#vehicle-type) |
| `p+167` onward | ... | attributes | Client 3464 inserted 8 bytes, at `p+196` on most rows |

Reading `p+1` as a u32 (as bdo-data-extractor does) only works when `unknown_p3` is `0`; on 2,453 rows the high half is non-zero, so the ID is a u16.

An earlier version of this doc read `p+5` as a u32 `npc_kind` with flag bits above the kind, and `p+9` and `p+13` as two more u32 fields. The "flags" are `grade` and the low half of `tendency_on_dead`: the common `0xFE0C0003` is kind `3`, grade `0` and karma `-500` (`0xFE0C`), and the old `p+9` value `65535` is the sign extension of a negative `tendency_on_dead`.

### `npc_kind` Values

The 2016 client (build of 2016-01-11) ships with debug symbols. Its
`gc::CharacterKind::Type` names `0` to `9`, and the characters that store each
value still fit the name:

| Value | `gc::CharacterKind` | Rows (client 3464) | Model folders | Examples |
| ----- | ------------------- | ----- | ------------- | -------- |
| `0`   | Player              | 61    | `pc` only; exactly the player-character IDs `1`-`47` and `201`-`214` | `1` Warrior |
| `1`   | Monster             | 9,212 | Mostly `monster`, also `infinitydefence`, `pc_summon`, `object` | `29929` Garmoth |
| `2`   | Npc                 | 6,225 | Mostly `npc`, also `object`, `monster` | `47791` Ehren |
| `3`   | Vehicle             | 3,296 | `creature`, `riding`, `cash` (pets and mounts) | `9001` Beginner's Brown Horse, `35423` Crank, carried quest objects |
| `4`   | Collect             | 564   | `object` only | `11982` Rhyolite, trees |
| `5`   | SiegeGate           | 10    |               | `529` Outer Gate |
| `6`   | SiegeSymbol         | 1     |               | `517` Siege Guardian Stone |
| `7`   | Household           | 940   | Mostly `monster` | Field HQ, Command Post, Indomitable Flag |
| `8`   | Installation        | 3,970 | `monster` | `16110` Beautiful Opal Vase, `16640` Dev Plant210 |
| `9`   | InstanceObject      | 220   | `summon` | `12842` Flimsy Wooden Fence, barricades |

`12`, `15` and `17` (1, 1 and 50 rows) came after 2016 and have no name. The
Lua's `CppEnums.ActorType` (`4` Gate, `5` Alterego, `6` Collect, `9` Deadbody)
is a different numbering and fits only `0` to `3`.

### Grade

`grade` is a `CppEnums.CharacterGradeType` value. The enum in `global_define_cpp_enum.luac` names `0` Normal, `1` Elite, `2` Hero, `3` Legend, `4` Boss and `5` Assistant, and the target bar script (`panel_widget_enemygauge_new.luac`) draws the boss HP bar when `getCharacterGradeType()` returns `4`. World bosses store `4`: `29929` Garmoth, `8609` Kzarka, `8608` Nouver.

| Value | Rows (client 3464) | Examples |
| ----- | ------------------ | -------- |
| `0`   | 21,576 | Most characters; Naive workers (`8011` Naive Fadus Worker) |
| `1`   | 552    | Plain workers (`8040` Human Worker), quest characters (`62083` Al Rhundi) |
| `2`   | 554    | Skilled workers (`8041`) |
| `3`   | 171    | Professional workers (`8042`) |
| `4`   | 1,650  | Bosses; Artisan workers (`8043`) |
| `5`   | 3      | `28468` Centaurus Axeman and two other Infinity Tower monsters |
| `6`   | 37     | Traps and towers (`60109` Flame Trap, `62415` Defense Tower) |
| `7`   | 8      | Sacraments and relics (`27134` Forest Sacrament, `26399` Blood Relic) |

Workers store their worker grade here, Naive `0` to Artisan `4`, so the enum names do not fit them. `6` and `7` are not in the enum.

### Karma

`tendency_on_dead` is the karma change for killing the character. The client calls karma "tendency": the target bar scripts (`panel_widget_enemygauge_new.luac`, `panel_widget_monsterbar_renew.luac`) read `getTendencyOnDead()` from the character static status and warn that attacking the target lowers your karma when the value is below `0`. The stored values follow that sign, on client 3464:

| `npc_kind` | Positive | Zero | Negative |
| ---------- | -------- | ---- | -------- |
| `0` (player) | 0 | 2 | 59 (`-200000` on 47, `-5000` on 12) |
| `1` (monster) | 4,869 | 4,323 | 20 |
| `2` (NPC) | 126 | 6,097 | 2 |
| `3` (pet, mount) | 0 | 363 | 2,933 (`-500` on 2,791) |

Every other kind stores `0`. Values range from `-200000` to `500`. The positive NPC rows are quest objects such as `37062` Old Book from Cron Castle.

### Ocean Tendency

`ocean_tendency` is non-zero on 104 rows (client 3464), all of kind `1` or `3`: positive on 62 monsters, nearly all sea monsters and pirate ships (`21418` Hekaru, `21484` Goldmont Large Battleship, `28682` Lyngbakr; up to `10000`), `-200000` on 40 player ships (`9032` Rowboat, `31045` Epheria Carrack) and `-30000` on the two Monsterbane Cannons (`31046`, `31052`). The client's word for naval fame is ocean tendency (`getOceanTendency()` in this table's condition scripts, `FromClient_OceanTendencyChanged` in the Lua). That this is the naval fame change on death, like `tendency_on_dead` for karma, is read from the sign pattern; no client getter for the static value was found.

### Vehicle Type

`vehicle_type` is a `CppEnums.VehicleType` value (`global_define_cpp_enum.luac`). The enum is sparse (`0` to `63` with gaps), and the names fit the characters that store them on client 3464: `0` Horse on 319 rows (`9001` Beginner's Brown Horse), `30` Cat on 778 and `31` Dog on 1,682 (pets), `18` Boat (`9032` Rowboat), `34` SailingBoat (`9090` Galley), `47` CampingTent (`9999` Camp), `58` BossMonster (`31629` Skyrend), `60` Carrack (`31045` Epheria Carrack), `63` GuildDragon (`31125` Doomcaller).

Every record of `npc_kind` `3` stores a vehicle type; every other record stores `65`, except two kind `2` Shrine Relics (`30122`, `30167`) with `5` Bomb. `65` is not an enum member and reads as "not a vehicle". The data also holds values the Lua enum does not name: `6` (cranks, `35423`), `8` (Heuklang, `60076`), `20` (`59720` Fwuzzy), `21` and `23` (Catapults `9038`, `9039`) and `27` (`9046` Log). The 2016 client's `gc::VehicleType` names all six, and the names fit: `6` GateCrank, `8` Haetae, `20` QuestDonkey, `21` Catapult, `23` Catapult2, `27` LumberVerticalSaw. The browser uses those names for them (`_common/vehicle_type.py`). Where both enums name a value, the Lua wins (`26` Cow, 2016 MilkCow; `35` Train, 2016 Tank).

### Model Path

Every record holds at least one model path, stored as an i64 byte length followed by ASCII text with no terminator, e.g. `[i64 25] npc/pedu2/npc_pedu2_named`. Its position after `p` varies (most often `p+299` on client 3464, `p+291` before), so find it by scanning for the length-prefixed string. 315 records hold a second path-like string; the longer one is the model. Top-level folders: `monster` (13,655), `npc` (5,078), `creature` (2,109), `object` (1,359), `riding` (793), `cash` (473).

The same length-prefixed ASCII form holds one or two other strings per record.
None contains a `/`, so the parser takes the longest string with a `/` in it as
`model_path`. On client 3464 (24,551 records) the strings come in this order:

| Strings | Rows | Example |
| ------- | ---- | ------- |
| AI script, model path | 14,400 | `47791`: `9999`, `npc/pedu2/npc_pedu2_named` |
| AI script, model path, voice | 10,103 | `47343`: `NPC_Social_MorningLand`, `npc/npc_named_morningland_stand`, `NPC_VCE_47343` |
| model path, voice | 44 | `47`: `pc/36_pyfw/pyfwaction_noweapon`, `PC_VCE_28PMYF` |
| model path | 4 | `37`: `pc/19_prum/rutumaction_noweapon` |

### AI Script

The string right before the model path is `ai_script`, the stem of the
character's [`.ai` script](aiscript_ai.md) without its folder or extension:
`9999` for `character/aiscript/9999.ai`, `Party_Leader_Dragon_Boss` for `29929`
Garmoth. On client 3464, 24,503 records name one. Of the 48 that store the
model path first and name none, 47 are player characters with a `pc/` model;
the other 59 player-like records name one, such as `Maid_PC_Common` on `39855`.

The names compare with the file stems without case. Of the 5,895 distinct
names, 5,621 match one of the 7,037 distinct stems of the 7,070 `.ai` files;
327 records name one of 274 scripts the client does not ship
(`Hadum_M0519_Demonland_Gimmick`). The most common names are `9999` (8,280
records) and `9999_Bow` (1,893).

The app groups these names into the `CHARACTER_AI_SCRIPT` lookup index
(`build_character_ai_script_index`), which the `.ai` view reads for its Used by
box.

The ASCII string after the Korean strings, on 10,147 rows, holds `VCE`
(`NPC_VCE_47343`, `PC_VCE_28PMYF`, `Creature_Fairy_E_Common_VCE`). The parser
does not read it.

### Korean Strings

Three UTF-16 strings follow the model path on all 24,551 records (client
3464), each an i64 code-unit count plus UTF-16LE text like the scripts:

| Field      | Notes |
| ---------- | ----- |
| name_kr    | Korean name, never empty: `29929` `가모스` (Garmoth), `1` `워리어` (Warrior) |
| label_kr   | Longer Korean label with region and role: `47791` `에다니아2_아우리스 해안_거점관리인_idx53`, `29929` `Dri_드리간 월드 레이드 보스 소환용`; never empty |
| title_kr   | Korean title: `47791` `<거점 관리인>` (Node Manager). Non-empty on 6,242 rows, 6,168 of them in angle brackets |

The LOC type 6 `str_id4=1` title is the translation of `title_kr`
(`<Node Manager>` for `<거점 관리인>`): 6,178 records have both, 64 have only
the Korean one and 3 only the LOC one. The parser reads all three: the Name
column shows `name_kr` when LOC has no name for the character, the Title
column `title_kr` when LOC has no title (`47481` `<여관 관리인>`, an unnamed
inn keeper), and the Internal Label column `label_kr` as stored.

### Payload Tail

Offsets are relative to the end of the payload (`data_offset + payload_size`).

| Offset | Type | Field      | Notes |
| ------ | ---- | ---------- | ----- |
| `-24`  | u8   | class_type | Gameplay class enum; `101` on every non-player row, `0`-`46` on the 106 `playercharacterstatic.bss` members |
| `-23`  | u8   | unknown_t23 | `0`, or `3` on 65 rows (siege structures such as `12821` "Field HQ" and the node forts) |
| `-22`  | u8[7] | zero      | Always `0` |
| `-15`  | u32  | source_item_id | Item that places or summons the character; `0` on most rows. See [Source Item](#source-item) |
| `-11`  | u8[4] | zero      | Always `0` |
| `-7`   | u8   | unknown_t7 | `1` on 759 rows (client 3464): 551 of `npc_kind` `3`, 195 of `9`, 13 of `7` (`35129` Horse, `62414` Wooden Fence); else `0` |
| `-6`   | u8   | zero      | Always `0` |
| `-5`   | f32  | unknown_tail_f32 | `5000.0` on 23,969 rows, `15000.0` on 339, `3000.0` on 157, `1000.0` on 70 |
| `-1`   | u8   | unknown_t1 | New in client 3464; `1` on 2,418 rows, 2,388 of them with `npc_kind` low byte `1`; else `0` |

Before client 3464 the payload ended at the f32, so each offset above sat one
byte closer to the end (`class_type` at `-23`). The parser reads only the
current layout.

`class_type` is a different ID from `character_id`: Warrior is character `1` / class `0`, Ranger `2` / `4`, Sorceress `3` / `8`, Berserker `4` / `12`, Tamer `5` / `16`, Musa `21` / `20`, Valkyrie `25` / `24`. The class number resolves through LOC `str_type=21` (class names) and is the value the client's `getClassType()` returns. bdo-data-extractor reads it as a u32; that fails on the 65 rows where `unknown_t23` is `3`, so it is read here as a u8. Kunoichi and Ninja are separate classes (`25` and `26` in LOC type 21): character `26` Kunoichi has `25` and character `27` Ninja has `26`, but character `209`, also named Kunoichi with the same female model (`pc/13_pnw/ninjawomenaction_noweaponmain_w`), stores `26`. Whether that is a data slip or means something is not known; it cannot be seen in game.

### Source Item

`source_item_id` is the reverse of the `itemenchant.dbss` `+0xAA` `character_id` link
(the `CHARACTER_ITEM` lookup index). On client 3464, 4,874 records store a
non-zero item, and on every one it is the item whose level-0 `itemenchant.dbss`
record names the character: `2053` [Event] Fence -> `58011` [Event] Fence,
`64527` Olvia Academy Pass - Fishing -> `619701`. `CHARACTER_ITEM` holds 5,108
links; the other 234 are mounts, wagons and ships (178 under `riding/horse`)
that store `0` here while a registration item names them: Horse Emblems (165),
Ship Licenses (23), Donkey Emblems (12), Wagon Registrations (11), e.g. `9967`
Horse from `50094` Horse Emblem: Tier 7-4 (Male).

So `CHARACTER_ITEM` gains nothing from `source_item_id` on client 3464: every
character that stores one already has that item in the index. The 4
characters the index leaves out because several items name them are horses
that store `0` here: `31533`, `31544`, `31590` and `31591`, named by 2 to 6
Horse Emblems each. The index stays on `itemenchant.dbss` alone, and
`test_source_item_matches_the_itemenchant_link` checks that the two agree.

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

The block after `ocean_tendency` contains many stable fields and constants, but its sub-structure is not confirmed. Additional cross-references, a client symbol name list, or in-game examples are needed before naming fields beyond raw offsets.

One piece is known from other files: on client 3464, 15,064 records carry the 200-byte stat body of [experience.bss](experience_bss.md) (found by its four `1.0` floats), with `5, 5, 5` and `10, 10, 10` triads as in [servantexperience.dbss](servantexperience_dbss.md). Where the body starts relative to `p` is not mapped.

### What are `unknown_p3`, `unknown_p`, `unknown_t23`, `unknown_t7` and `unknown_t1`?

`unknown_p3` is non-zero on 2,453 rows, all but one of kind `1` (monster), with values such as `95` and `184`. It groups monsters by content: `157` Infinity Tower monsters (199 rows), `96` Savage Rift (89), `95` world and raid bosses (`29929` Garmoth, `28732` Vell), `84` sea monsters, `121` node bosses. Third-party notes read it as a tribe type, but its 258 distinct non-zero values do not fit `CppEnums.TribeType` (`0` to `6`) or the `__eNewTribeType` values that [dropuihuntinggroundinfo.bss](dropuihuntinggroundinfo_bss.md) stores (`0` to `4`). `unknown_p` is `1` on 346 rows, `unknown_t23` is `3` only on siege structures, `unknown_t7` is `1` on 759 vehicles and installations, and `unknown_t1` (added in client 3464) is `1` on 2,418 rows, nearly all monsters. None has been tied to another table.

### Is `p+195` the character level?

The byte at `p+195` (client 3464) holds `1` on 9,628 rows (players, workers, `16640` Dev Plant210), `99` on 5,529 (mostly NPCs, `47791` Ehren) and monster-like levels elsewhere (`29929` Garmoth `60`, `8609` Kzarka `55`). Third-party notes call it the level. No client file confirms it yet; a monster's level shown in game would settle it.

### Is `p+181` a talk flag?

The byte at `p+181` is `0` on 18,828 rows and `1` on 5,723 (client 3464); `47791` Ehren has `1`. Third-party notes call it talkable, but it only partly follows the NPCs that have dialog. Not confirmed.

### What is the 8-byte payload header?

Its bytes form a handful of patterns (`00 00 00 00 00 01 01 00`, `01 00 00 00 00 01 00 00`, ...), which look like independent boolean flags, but no flag has been named.

### Related BSS Files

`hardcorerandomspawncharacterstaticstatusmanager.bss` and `fuelinsertcharacterstaticstatus.bss` are related by name, but they are not required to parse `characterstatic.dbss`. Their layouts should be documented separately if needed.
