# `possiblefusionpet.bss` Format

## Purpose

The pets a pet exchange can give, grouped by fusion key: each row is one
fusion key (variant, species and tier, the four bytes `pet.dbss` stores at
payload `+0x02`) and one [`pet.dbss`](pet_dbss.md) `pet_id` with that key.
The rows are sorted by the fusion key read as a u32, so the pets of one key
sit together. The file has no PABR magic and no trailer.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records   | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | --------- | --------- |
| 1      | 1230 and later | 3474    | `possiblefusionpet.bss` | 7,726 | 1,287 Row | 6         |

| Layout | File                    | Known           | Unknown         |
| ------ | ----------------------- | --------------- | --------------- |
| 1      | `possiblefusionpet.bss` | 6,439 B (83.3%) | 1,287 B (16.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | Layout 1 |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler names each pet with its LOC type 6 name when LOC is
loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 1,287 x 6 = 7,726 bytes.

### Row (6 bytes)

| Offset  | Type | Field      | Notes                                                                              |
| ------- | ---- | ---------- | ---------------------------------------------------------------------------------- |
| `+0x00` | u8   | variant    | Fusion key byte 0: `variant` (sheet `Kind`) of the pet in `pet.dbss`               |
| `+0x01` | u8   | species    | Fusion key byte 1: `species` (sheet `Race`)                                        |
| `+0x02` | u8   | unknown_02 | Fusion key byte 2: `0` on every row, as `unknown_04` of `pet.dbss`                  |
| `+0x03` | u8   | tier       | Fusion key byte 3: `tier`, from 0 (Tier 1); `0` to `3` on client 3474              |
| `+0x04` | u16  | pet_id     | A [`pet.dbss`](pet_dbss.md) `pet_id` whose four key bytes equal this row's          |

## Pets per Key

On client 3474 the 1,287 rows hold 903 fusion keys and 1,287 different
pets. 805 keys have one pet. The largest groups are the four keys of
species `23`, variant `1` (one per tier), with 53 pets each of different
LOC names (Boar, Worm, Saurus, Lizard, Iguana); five keys of species `1`
(Cat) hold 6 to 9 pets each.

Which pets have a row (client 3474, against the 2,009 `pet.dbss` records):

| `pet.dbss` records                      | Rows  |
| --------------------------------------- | ----- |
| `tier` `0` to `3`, `acquire_type_id` not `0` | 1,287 of 1,287 |
| `tier` `0` to `3`, `acquire_type_id` `0`     | 0 of 278       |
| `tier` `4` (Tier 5)                          | 0 of 444       |

The 278 pets with `acquire_type_id` `0` are 151 named Dog, 117 named Cat,
nine other PC room pets and one Wizard Gosphy; all ten PC room pets below
Tier 5 (`pc_room_type` `1`) are among them. 273 of the 278 share their fusion key
with a pet that has a row.

## Field Names

The fusion key is the 2016 `gc::PetStaticStatus` member `_fusionKey`, a u32
the pet doc splits into `variant`, `species`, a zero byte and `tier`, and
the 2016 client keys `gc::PetFusionStaticStatus` with a `gc::PetFusionKey`
of one u32 `_value`. The four bytes of every row equal the four bytes of
its pet in `pet.dbss` (1,287 of 1,287 rows, client 3474), so the fields
take the `pet.dbss` names; the zero byte keeps an `unknown_` name there
too. The `Pet_Fusion_Table` of a private server on client 519 (4 rows:
`Tier`, `SelectRate_0`, `SelectTier_0`, `SelectRate_1`, `SelectTier_1`) is
the source of
[`petfusionnew.dbss`](petfusionnew_dbss.md), not of this file. A private
server's `DataSheets.bexcel` on client 1784 has no sheet with `Possible` in
its name, and its server dump has no `PossibleFusion` text.

## Notes

- Clients 1485, 1784, 2107, 2519, 3002 and 3251 ship the file with the
  same row layout; client 1784 has 986 rows.
- No client Lua reads the file. The exchange window
  (`panel_window_petfusion_all_1.luac`) sends the pets with
  `ToClient_pushFusionPetList(petNo, index)` and lets the player pick the
  look of one of them (`openSelectLook`); the new pet's tier comes from
  [`petfusionnew.dbss`](petfusionnew_dbss.md).
- The installed `BlackDesert64.exe` (client 3474) holds no
  `possiblefusionpet` or `PossibleFusion` text as ASCII or UTF-16.

## Open Questions

### How the Exchange Uses the Groups

A fusion key with several pets (the 53 of species `23`) would need a rule
to pick one of them as the exchange result: the first row, a random row,
or a match on another field. The client Lua sends only the pet numbers and
the chosen look, so the pick happens on the server.

### Rows Only for `acquire_type_id` Other Than 0

The split by `acquire_type_id` in Pets per Key holds on all 1,565 pets
below Tier 5 on client 3474. Whether the compiler leaves those pets out on
purpose (the exchange then cannot give them) or the split follows from
another column is not in the client data.
