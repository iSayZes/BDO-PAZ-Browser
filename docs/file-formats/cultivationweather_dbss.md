# `cultivationweather.dbss` Format

## Purpose

How weather changes the growth speed of a farming crop. Each record is one
crop, keyed by its exchange key (the `itemexchangesource.bss` key that
`characterobject.dbss` stores as the crop's `product_recipe_key`), and holds
the five weather kinds of the 2016 `gc::WeatherKind` (water, temperature,
humidity, pruning, birds). Per kind a list of ranges gives the growth speed
change while the weather value lies in that range. The farm info window
reads it through `getCultivationWeatherStaticStatusWrapper()` and shows the
change next to the temperature, humidity and groundwater bars. Companion
`cultivationweatheroffset.dbss` lists where every record's payload sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes  | Records                                             | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ------ | --------------------------------------------------- | --------- |
| 2      | 3002 and later | 3474    | `cultivationweather.dbss`       | 77,916 | 5,247 Range, 2,020 Weather, 404 Payload, 404 Record | 12        |
| 2      | 3002 and later | 3474    | `cultivationweatheroffset.dbss` | 4,852  | 404 Offset Row                                      | 12        |
| 1      | 1485 to 2519   | 2519    | `cultivationweather.dbss`       | 64,771 | 4,454 Range, 1,715 Weather, 343 Payload, 343 Record | 12        |
| 1      | 1485 to 2519   | 2519    | `cultivationweatheroffset.dbss` | 3,434  | 343 Offset Row                                      | 10        |

| Layout | File                            | Known             | Unknown    |
| ------ | ------------------------------- | ----------------- | ---------- |
| 2      | `cultivationweather.dbss`       | 77,916 B (100.0%) | 0 B (0.0%) |
| 2      | `cultivationweatheroffset.dbss` | 4,852 B (100.0%)  | 0 B (0.0%) |
| 1      | `cultivationweather.dbss`       | 64,771 B (100.0%) | 0 B (0.0%) |
| 1      | `cultivationweatheroffset.dbss` | 3,434 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                                                     |
| ------------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `cultivationweatheroffset.dbss` | Optional | `exchange_key -> (data_offset, data_size)` of every payload; the parser walks the main file without it |

The handler links each exchange key to its `itemexchangesource.bss` row
through the `EXCHANGE_NAME_KR` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A record count, then the records back
to back; the file ends after the last record.

| Offset  | Type          | Field | Notes             |
| ------- | ------------- | ----- | ----------------- |
| `+0x00` | u32           | count | Number of records |
| `+0x04` | Record[count] | records | See Record      |

### Record (variable: 4 bytes + payload)

| Offset  | Type    | Field      | Notes                                             |
| ------- | ------- | ---------- | ------------------------------------------------- |
| `+0x00` | u32     | key_prefix | Equals `exchange_key`                             |
| `+0x04` | Payload | payload    | The offset row points at this field               |

### Payload (variable: 8 bytes + weathers)

| Offset  | Type                    | Field         | Notes                                                                 |
| ------- | ----------------------- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u32                     | exchange_key  | Crop exchange key; `57001` to `58000` on client 3474                  |
| `+0x04` | u32                     | weather_count | `5` on every record of clients 1784 and 3474                          |
| `+0x08` | Weather[weather_count]  | weathers      | See Weather                                                           |

### Weather (variable: 5 bytes + ranges)

| Offset  | Type               | Field        | Notes                                                       |
| ------- | ------------------ | ------------ | ----------------------------------------------------------- |
| `+0x00` | u8                 | weather_kind | See Weather Kinds; `1` to `5` in that order on every record |
| `+0x01` | u32                | range_count  | `1` to `3`                                                  |
| `+0x05` | Range[range_count] | ranges       | See Range                                                   |

### Range (12 bytes)

| Offset  | Type | Field              | Notes                                                                        |
| ------- | ---- | ------------------ | ---------------------------------------------------------------------------- |
| `+0x00` | f32  | weather_start_rate | Lower bound of the weather value, in percent; `-100.0` on temperature        |
| `+0x04` | f32  | weather_end_rate   | Upper bound                                                                  |
| `+0x08` | i32  | product_speed_rate | Growth speed change on the 1,000,000 = 100% scale; `-16668` to `1000000` on client 3474 |

The ranges of a kind follow in ascending order. On water, temperature and
humidity each range starts where the one before ends; the pruning ranges
leave gaps (`0` to `4`, `5` to `7`, `8` to `10`).

### `cultivationweatheroffset.dbss`

Bare offset table into `cultivationweather.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `cultivationweather.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field        | Notes                                                                       |
| ------- | ---- | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32  | exchange_key | Key of the record it points at                                              |
| `+0x04` | u32  | data_offset  | Absolute offset in `cultivationweather.dbss` of the payload, past the key prefix |
| `+0x08` | u32  | data_size    | Payload size in bytes, without the key prefix; `177` to `189` on client 3474 |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
offset rows are not in file order; on clients 1784 and 3474 every one points
at the payload of the record with its key.

## Layout 1

The keys are u16; the rest is as in Layout 2.

### Record (variable: 2 bytes + payload)

| Offset  | Type    | Field      | Notes |
| ------- | ------- | ---------- | ----- |
| `+0x00` | u16     | key_prefix |       |
| `+0x02` | Payload | payload    |       |

### Payload (variable: 6 bytes + weathers)

| Offset  | Type                   | Field         | Notes                              |
| ------- | ---------------------- | ------------- | ---------------------------------- |
| `+0x00` | u16                    | exchange_key  | `57001` to `58000` on client 1784  |
| `+0x02` | u32                    | weather_count |                                    |
| `+0x06` | Weather[weather_count] | weathers      |                                    |

### `cultivationweatheroffset.dbss`

| Offset  | Type              | Field | Notes |
| ------- | ----------------- | ----- | ----- |
| `+0x00` | u32               | count |       |
| `+0x04` | Offset Row[count] | rows  |       |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                       |
| ------- | ---- | ------------ | ----------------------------------------------------------- |
| `+0x00` | u16  | exchange_key |                                                             |
| `+0x02` | u32  | data_offset  |                                                             |
| `+0x06` | u32  | data_size    | `175` to `187` on client 1784                               |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`.

## Weather Kinds

`weather_kind` is the 2016 `gc::WeatherKind` (an unsigned char). The farm
info window (`panel_housing_farminfo_all_1.luac`) asks for kinds `Water`,
`Temperature` and `Humidity` by these names through `CppEnums.WeatherKind`.

| Value | `gc::WeatherKind`         | Bounds (client 3474) | Ranges per record (client 3474) |
| ----- | ------------------------- | -------------------- | ------------------------------- |
| 1     | `WeatherKind_Water`       | `0` to `100`         | 3                               |
| 2     | `WeatherKind_Temperature` | `-100` to `100`      | 3                               |
| 3     | `WeatherKind_Humidity`    | `0` to `100`         | 2                               |
| 4     | `WeatherKind_NeedLop`     | `0` to `10`          | 3                               |
| 5     | `WeatherKind_BirdsAttack` | `0` to `100`         | 2, or 1 on 5 records            |

## Field Names

The `CultivationWeather_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `ExchangeKey`,
`WeatherKind`, `WeatherStartRate`, `WeatherEndRate` and `ProductSpeedRate`,
one sheet row per range. Grouped by key and kind, its 3,870 rows match the
298 records of client 1784 on every range and value, 298 of 298. The sheet
lives in `datasheet_collectdatatable.xlsm`, whose `#Nodename` note column
names key `57001` `재배용 후추` (pepper for farming); `characterobject.dbss`
documents character `1201` Pepper Crop with `product_recipe_key` `57001`.

The 2016 client has no table of this name. Its debug symbols have
`gc::PlantZoneStaticStatus::WeatherRate` as `_maxRate` (f32) and
`_productRate` (f32), and an `unordered_map` from `gc::WeatherKind` to a
`pa_map<float, WeatherRate>`: the same range-to-rate shape.

## Notes

- The farm info window prints `getRateByWeather(kind, value) * 1.0E-4` as a
  percent, so `product_speed_rate` `10000` shows as `1.00%`. For water it
  shows the value with its sign flipped.
- It marks the best temperature with `getTopValue(Temperature)` and the best
  humidity with `getBottomValue(Humidity)`.
- Client 3474 holds 404 records, client 1784 298. 290 keys are in both,
  every one with changed values; `57238` to `57242`, `57442`, `57622` and
  `57722` are only in client 1784.
