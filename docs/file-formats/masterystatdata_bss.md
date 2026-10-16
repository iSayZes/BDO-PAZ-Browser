# `{alchemy,collecting,cooking,fishing,hunting,sail,training}statdata.bss` and `manufacturingstat.bss` Format

## Purpose

The life skill mastery tables: for each mastery step, the bonuses that the
Life Skill tab tooltips show. Eight files share the layout and differ only
in the fields after the mastery value and in the number of row groups:

| File                     | Life skill | Row groups      | Row size | Fields after mastery |
| ------------------------ | ---------- | --------------- | -------- | -------------------- |
| `fishingstatdata.bss`    | Fishing    | 1               | 8        | 1                    |
| `cookingstatdata.bss`    | Cooking    | 1               | 24       | 5                    |
| `huntingstatdata.bss`    | Hunting    | 1               | 36       | 8                    |
| `alchemystatdata.bss`    | Alchemy    | 1               | 40       | 9                    |
| `sailstatdata.bss`       | Sailing    | 1               | 44       | 10                   |
| `trainingstatdata.bss`   | Training   | 1               | 16       | 3                    |
| `collectingstatdata.bss` | Gathering  | one per type    | 36       | 8                    |
| `manufacturingstat.bss`  | Processing | one per type    | 16       | 3                    |

The six single-group files step by 50 mastery from 3000 down to 0. The
gathering table does the same once per gathering type; the processing table
runs up from 1 to 2999 once per processing type.

```text
cookingstatdata.bss, mastery 3000:
  mass cooking 100.00%, max dishes 76.45%, higher grade dish 24.20%,
  max higher grade dishes 76.45%, Imperial Delivery extra profit 181.25%
```

The Gathering and Processing mastery that life levels give is in
[`commonlifestatdata.bss`](commonlifestatdata_bss.md), which has its own
layout.

The files are self-contained. All multi-byte values are little-endian.

## File Layout

The PABR layout of [`blizzardregioninfo.bss`](blizzardregioninfo_bss.md):
fixed rows, an empty string table and the 8-byte trailer. The rows come in
groups, each with its own row count; a single-group file is the plain PABR
table.

| Offset   | Type    | Field        | Notes                                           |
| -------- | ------- | ------------ | ----------------------------------------------- |
| `+0x00`  | char[4] | magic        | ASCII `PABR`                                    |
| `+0x04`  | group[] | groups       | Groups back to back until `table_start`         |
| after    | u32     | string_count | Always `0`                                      |
| EOF - 8  | u32     | table_start  | Offset of `string_count`, where the groups end  |
| EOF - 4  | u32     | zero         | Always `0`                                      |

### Group

| Offset  | Type  | Field | Notes                         |
| ------- | ----- | ----- | ----------------------------- |
| `+0x00` | u32   | count | Number of rows in the group   |
| `+0x04` | row[] | rows  | `count` rows                  |

The group index, counted from 0, is the type `subType` that the Lua passes to
the table's getter (see [Gathering Row](#gathering-row-36-bytes) and
[Processing Row](#processing-row-16-bytes)). Group counts on client 3464:

| File                     | Groups | Group counts                           |
| ------------------------ | ------ | -------------------------------------- |
| six single-group files   | 1      | `61`                                   |
| `collectingstatdata.bss` | 19     | `0`, then `61` for groups 1 to 7, then `0` for groups 8 to 18 |
| `manufacturingstat.bss`  | 7      | `0`, then `76` for groups 1 to 6       |

The seven gathering groups are byte-identical on client 3464, and so are
the six processing groups.

## Record Structure

Every row opens with the mastery threshold:

| Offset  | Type | Field   | Notes                                                     |
| ------- | ---- | ------- | --------------------------------------------------------- |
| `+0x00` | f32  | mastery | `3000.0` down to `0.0` in steps of 50 on client 3464; `1.0` up to `2999.0` in `manufacturingstat.bss` |

The fields after it are u32 rates unless noted, with `1,000,000` = 100%.
`PaGlobalFunc_GlobalUtil_RoundRateToSecondPoint` in `global_util_ui.luac`
turns a rate into the tooltip percent: floor((rate + 50) / 100) / 100, two
decimals.

The field names are the members the Life Skill tab script reads,
`HandleEventOnOut_CharInfoLife_All_LifeType_Tooltip` in
`panel_characterinfo_life_all_2.luac` (decompiled with unluac), from the
`ToClient_get*StatStaticStatus()` wrapper of each skill. The tooltip text
is the LOC type 37 row of the `LUA_CHARACTERINFO_LIFE_*_DESC*` key in
`stringtable.bss`.

### Fishing Row (8 bytes)

| Offset  | Type | Field | Notes                                                    |
| ------- | ---- | ----- | -------------------------------------------------------- |
| `+0x04` | u32  | rate  | `_rate`, "Prize Catch Fish Rate" (`LUA_CHARACTERINFO_LIFE_FISHINGSTAT_DESC`) |

### Cooking Row (24 bytes)

| Offset  | Type | Field                      | Notes                                         |
| ------- | ---- | -------------------------- | --------------------------------------------- |
| `+0x04` | u32  | speed_cook_rate            | `_speedCookRate`, "Chance of mass cooking activating" |
| `+0x08` | u32  | basic_max_drop_rate        | `_basicMaxDropRate`, "Chance of max dishes"   |
| `+0x0C` | u32  | add_critical_drop_rate     | `_addCriticalDropRate`, "Chance of cooking higher grade dish" |
| `+0x10` | u32  | add_critical_max_drop_rate | `_addCriticalMaxDropRate`, "Chance of cooking max higher grade dishes" |
| `+0x14` | u32  | add_royal_trade_bonus      | `_addRoyalTradeBonus`, Imperial Delivery "Extra Profit" |

The tooltip reads the five members in this order and fills `rate1` to `rate4`
of `LUA_CHARACTERINFO_LIFE_COOK_DESC_1` and `rate1` of `_DESC_2` with them.
Two facts from the data fit the order: `+0x08` and `+0x10`, the two "max"
fields, hold the same value in every row on client 3464, and `+0x14` equals
the Alchemy `add_royal_trade_bonus` in every row. The in-game tooltip at
Cooking Mastery 595 shows 21.16%, 6.76%, 2.25%, 6.76% and 24.60%, the
mastery 550 row in this order (client 3464).

### Hunting Row (36 bytes)

| Offset  | Type   | Field        | Notes                                              |
| ------- | ------ | ------------ | -------------------------------------------------- |
| `+0x04` | u32    | unknown_04   | Always `0` on client 3464                          |
| `+0x08` | u32    | hunting_rate | "Chance of butchering more items"                  |
| `+0x0C` | u32[6] | unknown_0c ... unknown_20 | Always `0` on client 3464             |

The hunting tooltip shows one mastery value, `ToClient_getHuntingRate()`, in
`LUA_CHARACTERINFO_LIFE_HUNTING_DESC`; there is no hunting static status
wrapper in the Lua. `+0x08` is the only field that is not always 0, so it
takes the getter's name. The in-game tooltip at Hunting Mastery 405 shows
"Chance of butchering more items: +43.91%", the mastery 400 row's `439,091`
(client 3464).

### Alchemy Row (40 bytes)

| Offset  | Type | Field                 | Notes                                                    |
| ------- | ---- | --------------------- | -------------------------------------------------------- |
| `+0x04` | u32  | basic_max_drop_rate   | `_basicMaxDropRate`, "Chance of max products"            |
| `+0x08` | u32  | add_royal_trade_bonus | `_addRoyalTradeBonus`, Imperial Delivery "Extra Profit"  |
| `+0x0C` | u32  | unknown_0c            | `15690` in every row on client 3464                      |
| `+0x10` | u32  | event_drop_rate_0     | `getEventDropRateForTooltip(0)`; `1,000,000` in every row on client 3464 |
| `+0x14` | u32  | unknown_14            | `15691` in every row on client 3464                      |
| `+0x18` | u32  | event_drop_rate_1     | `getEventDropRateForTooltip(1)`, special item share      |
| `+0x1C` | u32  | unknown_1c            | `15692` in every row on client 3464                      |
| `+0x20` | u32  | event_drop_rate_2     | `getEventDropRateForTooltip(2)`, rare item share         |
| `+0x24` | u32  | event_drop_rate       | `_eventDropRate`, chance of an extra item                |

The tooltip splits `event_drop_rate` into the three "Chance of extra ...
items" lines of `LUA_CHARACTERINFO_LIFE_ALCHEMY_DESC_1`:

```text
basic   = event_drop_rate * (1 - share_2) * (1 - share_1)
special = event_drop_rate * (1 - share_2) * share_1
rare    = event_drop_rate * share_2
```

and rounds them with `PaGlobalFunc_GlobalUtil_RoundRateToThridPoint`
(floor((rate + 5) / 10) / 1000, three decimals). Share 0 is read but not
used. The handler stores the three results as `extra_basic_item_rate`,
`extra_special_item_rate` and `extra_rare_item_rate`.

The tooltip reads `_basicMaxDropRate` first and `_addRoyalTradeBonus` last,
so the read order does not match the file here. `+0x08` is the royal trade
bonus because it equals the Cooking `add_royal_trade_bonus` in every row; the
Lua describes both as the Imperial Delivery "Extra Profit". Of `+0x04` and
`+0x24`, `+0x04` is 0 at mastery 0 and has the shape and size of the Cooking
`basic_max_drop_rate` (`500,000` against `611,524` at mastery 2000), while
`+0x24` is `3,000` at mastery 0 like the event shares, which are not 0 there
either (`150,000` and `20,000`).

### Sailing Row (44 bytes)

| Offset  | Type   | Field            | Notes                                                    |
| ------- | ------ | ---------------- | -------------------------------------------------------- |
| `+0x04` | f32    | unknown_04       | Mastery / 50 on client 3464 (`60.0` at 3000)              |
| `+0x08` | u32    | unknown_08       | Always `8`, the number of `CppEnums.ServantStatType` entries |
| `+0x0C` | u32    | acceleration     | `getVariedStatByIndex(0)`, "Accel."                      |
| `+0x10` | u32    | max_move_speed   | `getVariedStatByIndex(1)`, "Speed"                       |
| `+0x14` | u32    | cornering_speed  | `getVariedStatByIndex(2)`, "Turn"                        |
| `+0x18` | u32    | brake_speed      | `getVariedStatByIndex(3)`, "Brake"                       |
| `+0x1C` | u32    | cannon_cool_time | Mastery / 50 on client 3464; not a rate                  |
| `+0x20` | u32    | cannon_accuracy  | Same values as `cannon_cool_time`                        |
| `+0x24` | u32    | max_length       | Same values as `cannon_cool_time`                        |
| `+0x28` | u32    | max_angle        | Same values as `cannon_cool_time`                        |

The eight values from `+0x0C` follow `CppEnums.ServantStatType` in
`global_define_cpp_enum.luac`: `Type_Acceleration` 0, `Type_MaxMoveSpeed` 1,
`Type_CorneringSpeed` 2, `Type_BrakeSpeed` 3, `Type_CannonCoolTime` 4,
`Type_CannonAccuracy` 5, `Type_MaxLength` 6, `Type_MaxAngle` 7. The Life
Skill tab and `panel_window_shipinfo_all_1.luac` /
`panel_window_shipinfo_renewal_all_1.luac` read index 0 as acceleration and
1 as speed, the enum order. `PaGlobal_SailStatToolTip` in
`panel_window_servantinfo_workership.luac` reads index 0 for speed and 1 for
acceleration. All four are equal in every row on client 3464, so the shown
values do not depend on it. No Lua reads indices 4 to 7.

The four rates match `LUA_CHARACTERINFO_LIFE_SAILSTAT_DESC_1`: +0.5% per 50
mastery up to 2000 and +0.25% per 50 above, `250,000` (25%) at 3000.

### Training Row (16 bytes)

| Offset  | Type | Field                        | Notes                                                       |
| ------- | ---- | ---------------------------- | ----------------------------------------------------------- |
| `+0x04` | u32  | add_horse_capture_rate       | `_addHorseCaptureRate`, "Horse Capture Rate"; `437,500` at 3000 (client 3464) |
| `+0x08` | u32  | add_mating_rate              | `_addMatingRate`, "Chance of getting a higher tier horse from breeding or exchange"; rises by `10,000` every 200 mastery |
| `+0x0C` | u32  | add_vehicle_experience_rate  | `_addVehicleExperienceRate`, "Mount EXP"; `937,500` at 3000 |

The tooltip (`LUA_CHARACTERINFO_LIFE_TRAINING_DESC_1`) fills `rate1` to
`rate3` with capture rate, mount EXP and higher tier chance. The in-game
tooltip at Training Mastery 385 shows 3.84%, 5.62% and 2.00%: the mastery 350
row's `+0x04`, `+0x0C` and `+0x08` (client 3464).

### Gathering Row (36 bytes)

| Offset  | Type | Field                 | Notes                                                 |
| ------- | ---- | --------------------- | ----------------------------------------------------- |
| `+0x04` | u32  | add_drop_rate_0       | `getCollectingStatAddDropRate(0)`, Basic Resources "Drop rate" |
| `+0x08` | u32  | add_drop_count_rate_0 | `getCollectingStatAddDropCountRate(0)`, Basic Resources "Quantity" |
| `+0x0C` | u32  | add_drop_rate_1       | Same getters with index 1, Special Resources          |
| `+0x10` | u32  | add_drop_count_rate_1 |                                                       |
| `+0x14` | u32  | add_drop_rate_2       | Same getters with index 2, Rare Resources             |
| `+0x18` | u32  | add_drop_count_rate_2 |                                                       |
| `+0x1C` | u32  | unknown_1c            | `500,000` in every row on client 3464                 |
| `+0x20` | u32  | unknown_20            | `0` in every row on client 3464                       |

The gathering tooltip in `panel_characterinfo_life_all_2.luac` calls
`ToClient_LoadCollectingStatData(subType)` for the hovered gathering type,
then reads `ToClient_getCollectingStatAddDropRate(ii)` and
`ToClient_getCollectingStatAddDropCountRate(ii)` for `ii` = 0 to count - 2
into `LUA_COLLECTING_POWER_DESC_1` to `_3` ("Basic Resources", "Special
Resources", "Rare Resources", each with "Drop rate +{rate1}%" and "Quantity
+{rate2}%"). Three tiers read up to count - 2 leave a fourth entry, and the
32 bytes after the mastery hold four (drop rate, quantity) pairs.

The pairs read in row order, not as four drop rates followed by four
quantities. With pairs, all six tooltip values are 0 at mastery 0 and rise
with mastery, as `LUA_COLLECTING_POWER_DESC_MAIN` says ("Higher Gathering
Mastery increases the gathered drop rate and quantity of basic, special, and
rare resources"). Read as two arrays, the rare quantity would be `+0x1C`,
`500,000` (+50%) at every mastery including 0 (client 3464). The fourth pair
(`+0x1C`, `+0x20`) is constant and nothing reads it. The in-game tooltips of
Lumbering, Fluid Collecting and Butchering at Gathering Mastery 440 show
Basic +80.00% / +50.49%, Special +25.25% / +12.62% and Rare +31.56% /
+10.52%, the mastery 400 row read as pairs (client 3464).

On client 3464 the basic drop rate is 0 at mastery 0 and 50 and `800,000`
(+80%) from 100 up; the other five values rise to 500%, 250%, 125%, 312.31%
and 105.80% at 3000.

The group index is the `subType`: the Life Skill tab names group `n` with
`_SUBLIFE_COLLECT_STRING[n]` in `panel_characterinfo_life_all.luac`, keys of
the `RESOURCE` sheet:

| Group | Key                                                  | Name (English LOC) |
| ----- | ---------------------------------------------------- | ------------------ |
| 1     | `PANEL_CHARACTERINFO_RENEW_WATERING_TITLE`            | Water Scooping     |
| 2     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_FELLING`      | Lumbering          |
| 3     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_SAP`          | Fluid Collecting   |
| 4     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_HOMMY`        | Hoe Gathering      |
| 5     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_SLAUGHTER`    | Butchering         |
| 6     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_TANNING`      | Tanning            |
| 7     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_MINING`       | Mining             |

The buff detail panel (`panel_characterinfo_buffdetail_all.luac`) passes
`__eCollectToolType_Axe` and the other tool types to the same
`ToClient_LoadCollectingStatData`, so the group index is also the
`CollectToolType`: `CppEnums.CollectToolTypeName` lists BareHands,
EmptyBottle, Axe, Syringe, Hoe, ButcheryKnife, SkinKnife and Pickax first,
and group 0 (bare hands) is empty. `LUA_COLLECTING_POWER_DESC_SUB_1` to `_7`
list the resources of each type ("Basic Resources: Timber, Plank, Log" for
group 2).

### Processing Row (16 bytes)

| Offset  | Type | Field      | Notes                                                        |
| ------- | ---- | ---------- | ------------------------------------------------------------ |
| `+0x04` | u32  | unknown_04 | 1,000,000 x (1 - 10 / `count_rate`) in every row on client 3464 |
| `+0x08` | u32  | count_rate | `ToClient_getManufacturingStatCountRate(subType)`, mass processing batches |
| `+0x0C` | u32  | unknown_0c | `0` in every row on client 3464                              |

The processing tooltip fills `data2` of `LUA_MANUFACTURING_POWER_TOOLTIP_DESC`
("You can mass process {data2} batches of materials at once") with
`tostring(ToClient_getManufacturingStatCountRate(subType))`, and the
processing window (`panel_window_manufacture_all_2.luac`) puts the same
value in `LUA_MANUFACTURING_POWER_DESC` ("(Mass Process {count} times)").
`+0x08` is the only whole-number count in the row: `10` at mastery 1 up to
`315` at 2999 on client 3464. `+0x04` follows from it (`90,909` for 11
batches, `968,253` for 315), and no Lua reads a second processing value.

The rows run up: mastery `1.0`, then `19.0` to `779.0` in steps of 20, and
larger steps up to `2999.0` (client 3464). At Processing Mastery 480 every
type shows "(Mass Process 34 times)", the `479.0` row; the `499.0` row would
give 35, so the client takes the row at or below the mastery here too. The group index is the `subType`,
named by `_SUBLIFE_MANUFACTURE[n]`; the processing window passes its tab
index + 1:

| Group | Key                                                  | Name (English LOC) |
| ----- | ---------------------------------------------------- | ------------------ |
| 1     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_SHAKING`      | Shaking            |
| 2     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_GRIDING`      | Grinding           |
| 3     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_FIREWOOD`     | Chopping           |
| 4     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_DRYING`       | Drying             |
| 5     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_THINOUT`      | Filtering          |
| 6     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_HEATING`      | Heating            |

## Notes

- The handler is one class, `_bss/masterystatdata/handler.py`; the fields and
  columns of each file are a `MasteryTable` in `spec.py`. The type names
  resolve through the `stringtable.bss` key hashes stored in `sub_types.py`.
- The client takes the row at or below the player's mastery and does not
  interpolate: the in-game tooltips at Cooking 595, Hunting 405,
  Training 385, Gathering 440 and Processing 480 match the 550, 400, 350,
  400 and 479 rows exactly (client 3464); the 600 cooking row would give
  mass cooking 22.37% instead of 21.16%.
- Most curves change slope at mastery 2000: below it many values are perfect
  squares (Cooking `+0x0C` at 1200 is `78,400` = 280²), above it they rise by
  a fixed step per 50 mastery.
- `15690`, `15691` and `15692` in the Alchemy rows are not the extra items:
  item 15690 is "Glorious Crystal of Gallantry - Ah'krad", 15691 the Olucas
  crystal and 15692 "Resplendent Medal of Honor". They are not
  `itemsubgroup.dbss` keys, and `itemmaingroup.bss` holds none of them as a
  u32 or u16 at any byte offset, nor as ASCII digits (client 3464).
- bdo-data-extractor (`FORMATS.md`, "Life-skill mastery and level-effect
  tables") lists the eight shapes and the `1,000,000` = 100% scale, and calls
  the gathering pairs dropRate / quantityRate and the processing fields
  procRate / batchSize. The names here come from the client Lua instead.

## Open Questions

### The Alchemy Keys

`unknown_0c`, `unknown_14` and `unknown_1c` pair a constant (`15690` to
`15692`) with each event share. They read like keys of the basic, special
and rare extra item groups, but no decoded table holds them.

### The Sailing Cannon Fields And `unknown_04`

The enum names the four values from `+0x1C`, but they hold mastery / 50 like
`unknown_04`, not a rate, and no UI reads them. Whether sailing mastery
changes cannon stats is not shown anywhere in the client.

### The Processing Rate `unknown_04`

`unknown_04` in `manufacturingstat.bss` is 1 - 10 / batches, scaled to
1,000,000. It could be the share of processing time a mass process saves
over ten single runs, but no Lua or tooltip reads it.

### The Gathering Groups 8 To 18 And The Fourth Pair

`collectingstatdata.bss` ends with eleven empty groups after Mining. The
tool types after Pickax in `CppEnums.CollectToolTypeName` (Tweezers, Pray,
MagnifyingLens, MassStone, FishingChair, Whip, Oar, Reserve) are eight, not
eleven. The constant fourth pair (`unknown_1c`, `unknown_20`) has no reader.
