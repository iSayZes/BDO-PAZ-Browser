# `itemeffectgroupstaticstatus.bss` Format

## Purpose

The glow effects a dye can give the Sovereign weapons and the Edana armor:
per item group type of
[`itemgroupingstaticstatus.bss`](itemgroupingstaticstatus_bss.md) a list
of effects, each with its colour, its name and the Primordial Pigment item
that applies it (Turquoise Primordial Pigment - Sovereign). The dye window
(`panel_widget_dye_all_1.luac`) walks the effect indexes with
`ToClient_GetItemEffectInfoByIndex(effectIndex)`, draws each slot with
`info:getColor()`, names it with
`PAGetStringByStringHash(Defines.StringSheet_RESOURCE, info:getName())`
and counts the pigments with `ToClient_GetEquipItemEffectDyeItemCount`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records            | Row bytes               |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------------ | ----------------------- |
| 4      | 3314 and later | 3482    | `itemeffectgroupstaticstatus.bss` | 606   | 20 Effect, 4 Group | 24 to 30, 28 on average |
| 3      | 3212 to 3283   | 3283    | `itemeffectgroupstaticstatus.bss` | 292   | 11 Effect, 4 Group | 20 to 26, 23 on average |
| 2      | 3177           | 3177    | `itemeffectgroupstaticstatus.bss` | 168   | 11 Effect, 4 Group | 12                      |
| 1      | 2519 to 3144   | 3144    | `itemeffectgroupstaticstatus.bss` | 438   | 22 Effect, 2 Group | 19                      |

| Layout | File                              | Known         | Unknown       |
| ------ | --------------------------------- | ------------- | ------------- |
| 4      | `itemeffectgroupstaticstatus.bss` | 586 B (96.7%) | 20 B (3.3%)   |
| 3      | `itemeffectgroupstaticstatus.bss` | 281 B (96.2%) | 11 B (3.8%)   |
| 2      | `itemeffectgroupstaticstatus.bss` | 157 B (93.5%) | 11 B (6.5%)   |
| 1      | `itemeffectgroupstaticstatus.bss` | 262 B (59.8%) | 176 B (40.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 4 |
| 3474   | Layout 4 |
| 3454   | Layout 4 |
| 3412   | Layout 4 |
| 3381   | Layout 4 |
| 3349   | Layout 4 |
| 3314   | Layout 4 |
| 3283   | Layout 3 |
| 3251   | Layout 3 |
| 3212   | Layout 3 |
| 3177   | Layout 2 |
| 3144   | Layout 1 |
| 3103   | Layout 1 |
| 3062   | Layout 1 |
| 3037   | Layout 1 |
| 3002   | Layout 1 |
| 2959   | Layout 1 |
| 2923   | Layout 1 |
| 2900   | Layout 1 |
| 2872   | Layout 1 |
| 2834   | Layout 1 |
| 2803   | Layout 1 |
| 2765   | Layout 1 |
| 2736   | Layout 1 |
| 2703   | Layout 1 |
| 2665   | Layout 1 |
| 2637   | Layout 1 |
| 2606   | Layout 1 |
| 2583   | Layout 1 |
| 2545   | Layout 1 |
| 2519   | Layout 1 |
| 2498   | No file  |
| 2468   | No file  |
| 2438   | No file  |
| 2414   | No file  |
| 2384   | No file  |
| 2358   | No file  |
| 2335   | No file  |
| 2313   | No file  |
| 2290   | No file  |
| 2250   | No file  |
| 2224   | No file  |
| 2203   | No file  |
| 2179   | No file  |
| 2151   | No file  |
| 2134   | No file  |
| 2107   | No file  |
| 2073   | No file  |
| 2052   | No file  |
| 2011   | No file  |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                            |
| --------------------- | -------- | ------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Pigment item names (LOC type 0) and effect names (LOC type 37, `RESOURCE` sheet) |

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset  | Type               | Field       | Notes                                            |
| ------- | ------------------ | ----------- | ------------------------------------------------ |
| `+0x00` | u32                | group_count | Number of groups; no PABR magic, no string table |
| `+0x04` | Group[group_count] | groups      | See Group; from the highest type down            |

### Group (variable: 8 bytes + effects)

| Offset  | Type                 | Field           | Notes                                                                 |
| ------- | -------------------- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u32                  | item_group_type | An `itemgroupingstaticstatus.bss` group type: `8` to `11` on client 3482 |
| `+0x04` | u32                  | effect_count    | Number of `effects`; `5` in every group of client 3482                 |
| `+0x08` | Effect[effect_count] | effects         | See Effect                                                            |

### Effect (variable: 24 bytes + colour text)

| Offset         | Type     | Field            | Notes                                                                                   |
| -------------- | -------- | ---------------- | --------------------------------------------------------------------------------------- |
| `+0x00`        | u32      | effect_index     | `0` to `4` in order; the `effectIndex` the Lua passes                                    |
| `+0x04`        | u8       | unknown_04       | `1` on every effect of client 3482                                                       |
| `+0x05`        | str8     | color            | Colour as `RRGGBB` hex text (`1D3F48` for Turquoise); empty on 5 of the 20 effects        |
| `color+0x00`   | bytes[3] | color_rgb        | Colour as red, green and blue bytes; `00 00 00` after a colour text (see Notes)          |
| `color+0x03`   | u32      | name             | String hash of the effect name in the `RESOURCE` sheet (LOC type 37, `str_id2` 2)         |
| `color+0x07`   | u32      | dye_item_id      | The pigment item that applies the effect; `0` for effect `0` (`Default`)                 |

## Layout 3

The effect has no `dye_item_id`. Only the Effect differs from Layout 4.

### Effect (variable: 20 bytes + colour text)

| Offset       | Type     | Field        | Notes |
| ------------ | -------- | ------------ | ----- |
| `+0x00`      | u32      | effect_index |       |
| `+0x04`      | u8       | unknown_04   |       |
| `+0x05`      | str8     | color        |       |
| `color+0x00` | bytes[3] | color_rgb    |       |
| `color+0x03` | u32      | name         |       |

## Layout 2

The effect has no colour text and no `dye_item_id`. Only the Effect differs
from Layout 3.

### Effect (12 bytes)

| Offset  | Type     | Field        | Notes |
| ------- | -------- | ------------ | ----- |
| `+0x00` | u32      | effect_index |       |
| `+0x04` | u8       | unknown_04   |       |
| `+0x05` | bytes[3] | color_rgb    |       |
| `+0x08` | u32      | name         |       |

## Layout 1

The effect has no colour text and no `dye_item_id`; eight bytes after
`effect_index` take the place of `unknown_04`. Only the Effect differs from
Layout 2.

### Effect (19 bytes)

| Offset  | Type     | Field          | Notes                                                              |
| ------- | -------- | -------------- | ------------------------------------------------------------------ |
| `+0x00` | u32      | effect_index   | `0` to `10` on client 2519                                         |
| `+0x04` | u64      | unknown_old_04 | `0` on effect `0`, `750` on every other effect of client 2519      |
| `+0x0C` | bytes[3] | color_rgb      | The only colour of the effect (`00 00 ff` for `Blue`)              |
| `+0x0F` | u32      | name           |                                                                    |

## Effects

The effects of client 3482. Groups 8, 9 and 10 (the Sovereign main,
sub-weapon and awakening groups) list the same five; group 11 (Edana armor)
has its own.

| Group     | Index | Name (LOC)  | color    | color_rgb        | dye_item_id                                      |
| --------- | ----- | ----------- | -------- | ---------------- | ------------------------------------------------ |
| 8, 9, 10  | 0     | Default     |          | `ff ff 00`       | `0`                                              |
| 8, 9, 10  | 1     | Red         | `651414` | `00 00 00`       | 767293 Crimson Primordial Pigment - Sovereign    |
| 8, 9, 10  | 2     | Violet      | `31183C` | `00 00 00`       | 767294 Violet Primordial Pigment - Sovereign     |
| 8, 9, 10  | 3     | Turquoise   | `1D3F48` | `00 00 00`       | 767341 Turquoise Primordial Pigment - Sovereign  |
| 8, 9, 10  | 4     | White       | `9A9A9A` | `00 00 00`       | 767343 White Primordial Pigment - Sovereign      |
| 11        | 0     | Default     |          | `ff 00 00`       | `0`                                              |
| 11        | 1     | Violet      |          | `80 00 80`       | 767296 Violet Primordial Pigment - Edana         |
| 11        | 2     | Turquoise   | `1D3F48` | `00 00 00`       | 767342 Turquoise Primordial Pigment - Edana      |
| 11        | 3     | White       | `9A9A9A` | `00 00 00`       | 767344 White Primordial Pigment - Edana          |
| 11        | 4     | Yellow      | `D5952A` | `00 00 00`       | 767353 Sunset Primordial Pigment - Edana         |

## Notes

- `color_rgb` is the colour of the effect in red, green and blue: on client
  2519 (Layout 1) the eleven effects of a group are `Black (Basic)`
  `00 00 00`, `Yellow` `ff ff 00`, `Turquoise` `00 ff ff`, `Blue`
  `00 00 ff`, `Violet` `80 00 80` and `White` `ff ff ff` among others, and
  there is no colour text. From Layout 3 an effect with a colour text has
  `00 00 00` here; the ones without text (`Default`, the Edana `Violet`)
  keep their colour in these bytes. The handler shows the text, else these
  bytes.
- Client 2519 has two groups, `1` and `0`, with the same eleven effects;
  the group keys `8` to `11` appear with Layout 2.
- An effect name is the same hash in every group: both Violet effects store
  `1080916977`, which LOC type 37 (`str_id2` 2) names `Violet`. All six
  hashes have a LOC row on client 3482.
- The file is not in the client 1784 PAZ.
- The handler (`_bss/itemeffectgroupstaticstatus/`) shows one row per
  effect: the group, the index, the name, the colour and the pigment item.

## Open Questions

### What `unknown_04` and `unknown_old_04` Hold

The u8 after `effect_index` is `1` on every effect of client 3482. The u64
it replaces in Layout 1 is `0` on the first effect of a group and `750` on
the others; a price or a dye amount would fit, but no Lua getter reads it.
