# `petupgrade.bss` Format

## Purpose

The item cost of Tier 5 Pet Training, per pet tier. On client 3474 the file
holds one entry: a Tier 4 pet (stored tier `3`) trains into Tier 5 with one
Royal Plume (item `59376`). The file has no PABR magic and no trailer. The
alpha bonus of a Tier 5 pet is in [`petleaderbuff.bss`](petleaderbuff_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------- | --------- |
| 1      | 2107 and later | 3474    | `petupgrade.bss` | 26    | 1 Entry | 22        |

| Layout | File             | Known        | Unknown     |
| ------ | ---------------- | ------------ | ----------- |
| 1      | `petupgrade.bss` | 22 B (84.6%) | 4 B (15.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler names the item with its LOC type 0 name from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field   | Notes                                 |
| ------- | ------------ | ------- | ------------------------------------- |
| `+0x00` | u32          | count   | Number of entries; `1` on client 3474 |
| `+0x04` | Entry[count] | entries | See Entry                             |

### Entry (22 bytes)

| Offset  | Type | Field        | Notes                                                                 |
| ------- | ---- | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u8   | pet_tier     | Map key: the tier the pet trains from, as `tier` of [`pet.dbss`](pet_dbss.md) stores it, from 0; `3` is Tier 4 |
| `+0x01` | u32  | item_id      | Training item; `59376` Royal Plume on client 3474                     |
| `+0x05` | u64  | item_count   | Items one training uses; `1` on client 3474                           |
| `+0x0d` | u32  | success_rate | Training success rate; `1000000` (100%) on the only entry            |
| `+0x11` | u32  | unknown_11   | `1000000` on the only entry, see Open Questions                       |
| `+0x15` | u8   | pet_tier_dup | Equals `pet_tier` on the only entry                                   |

## Field Names

No reference source has the table: the file is in the client 2107 archive
but not in the client 1784 one, and a private server's `DataSheets.bexcel`
on client 1784 has no sheet with `Pet` and `Upgrade` in its name. The names
come from the client Lua of client 3474 (`panel_dialog_petleader_all_1.luac`
and `_2.luac`, the Tier 5 Pet Training window):

- `pet_tier` and `item_id`: the window asks for the training item with
  `ToClient_getPetUpgradeItem(petStaticStatus:getPetTier())` for the pet in
  the slot, and with `ToClient_getPetUpgradeItem(3)` for the empty slot. It
  turns the training button on only when the inventory holds that item. A
  pet below Tier 4 (`getPetTier() + 1 < 4`) gets
  `LUA_PETCOMPOSE_CANTBETOGETHER_TEXT`, so the key is the stored tier of the
  Tier 4 pet. Its item `59376` is Royal Plume, whose LOC text says "Usage:
  Tier 5 Pet Training".
- `item_count`: the window trains with
  `ToClient_requestPetUpgradeByItem(name, petNo, eInventory, itemSlotNo, 1)`,
  one item. Garmoth's "BDO Basics - Pets" guide (section "5. Tier 5 Pet
  Enhancement") says the training is done at a Pet Trainer NPC and consumes
  a Royal Plume. The official Black Desert wiki page "Tier 5 Pet
  Training/Alpha Appointment" says "To train a Tier 5 pet, you will need a
  "Royal Plume"" and that the menu trains "Tier 4 pets to Tier 5", which is
  `pet_tier` `3` and item `59376`.

## Notes

- Raw bytes on client 3474: `01 00 00 00 03 F0 E7 00 00 01 00 00 00 00 00
  00 00 40 42 0F 00 40 42 0F 00 03`. Clients 2107, 2519, 3002 and 3251 ship
  the same 26 bytes.
- `global_define_cpp_enum.luac` lists `Contents_PetUpgrade`, and the window
  calls `ToClient_UpdateOpenUICondition(__eCheckOpenUIType_5TierPetUpgrade)`
  when it opens.
- The window shows the trained pet from
  `ToClient_getPetUpgradeSimulationResult(characterKey)`, and the alpha
  bonus of the new tier from `ToClient_getPetLeaderBuff`
  ([`petleaderbuff.bss`](petleaderbuff_bss.md)). Which pet a pet trains
  into, and its talent as the alpha, is in
  [`petupgraderesult.bss`](petupgraderesult_bss.md).
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`, with the item's icon and name next to its ID.

## Open Questions

### Second Rate Value

`success_rate` and `unknown_11` are both `1000000`, 100% on the client's
1,000,000 = 100% rate scale. A private server's `Fairy_Upgrade` sheet on
client 1784 has the columns `Tier`, `NeedItem`, `ItemCount` and `Rate`, the
order of the first four fields here, with `Rate` `1000000` on every row,
and in game my Tier 5 Pet Training always succeeds; so the field after the
count is the success rate. No Lua reads a rate from the training window,
and the official Black Desert wiki page "Tier 5 Pet Training/Alpha
Appointment" names no success rate. What `unknown_11` holds is unknown.
