# `midiinstrument.bss` Format

## Purpose

The instruments of the music composer and the instrument play: per
instrument its Wwise bank and event, the in-game name key, the
articulations it can play, the start, end and loop actions of the playing
character, the composer tab it sits on and whether every player owns it.
The composer Lua (`panel_window_selectinstruments_all_1.luac`,
`panel_window_myinstruments_all_1.luac`) reads it through
`Toclient_MidiInstrumentTrackCount()`, `Toclient_getInstrumentByIndex()`,
`ToClient_getAdvancedTypeByIndex()` and
`ToClient_getInstrumentIsOpenedByIndex()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | ----------------------- |
| 4      | 1866 and later | 3482    | `midiinstrument.bss` | 5,242 | 38 Row  | 56 to 69, 63 on average |
| 3      | 1565 to 3482   | 3482    | `midiinstrument.bss` | 5,242 | 38 Row  | 56 to 69, 63 on average |
| 2      | 1509 to 3482   | 3482    | `midiinstrument.bss` | 5,242 | 38 Row  | 56 to 69, 63 on average |
| 1      | 1409 to 1838   | 1838    | `midiinstrument.bss` | 1,833 | 15 Row  | 53 to 61, 55 on average |

| Layout | File                 | Known            | Unknown      |
| ------ | -------------------- | ---------------- | ------------ |
| 4      | `midiinstrument.bss` | 5,128 B (97.8%)  | 114 B (2.2%) |
| 3      | `midiinstrument.bss` | 5,128 B (97.8%)  | 114 B (2.2%) |
| 2      | `midiinstrument.bss` | 5,128 B (97.8%)  | 114 B (2.2%) |
| 1      | `midiinstrument.bss` | 1,833 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 4             |
| 3474   | Layout 4             |
| 3454   | Layout 4             |
| 3412   | Layout 4             |
| 3381   | Layout 4             |
| 3349   | Layout 4             |
| 3314   | Layout 4             |
| 3283   | Layout 4             |
| 3251   | Layout 4             |
| 3212   | Layout 4             |
| 3177   | Layout 4             |
| 3144   | Layout 4             |
| 3103   | Layout 4             |
| 3062   | Layout 4             |
| 3037   | Layout 4             |
| 3002   | Layout 4             |
| 2959   | Layout 4             |
| 2923   | Layout 4             |
| 2900   | Layout 4             |
| 2872   | Layout 4             |
| 2834   | Layout 4             |
| 2803   | Layout 4             |
| 2765   | Layout 4             |
| 2736   | Layout 4             |
| 2703   | Layout 4             |
| 2665   | Layout 4             |
| 2637   | Layout 4             |
| 2606   | Layout 4             |
| 2583   | Layout 4             |
| 2545   | Layout 4             |
| 2519   | Layout 4             |
| 2498   | Layout 4             |
| 2468   | Layout 4             |
| 2438   | Layout 4             |
| 2414   | Layout 4             |
| 2384   | Layout 4             |
| 2358   | Layout 4             |
| 2335   | Layout 4             |
| 2313   | Layout 4             |
| 2290   | Layout 4             |
| 2250   | Layout 4             |
| 2224   | Layout 4             |
| 2203   | Layout 4             |
| 2179   | Layout 4             |
| 2151   | Layout 4             |
| 2134   | Layout 4             |
| 2107   | Layout 4             |
| 2073   | Layout 4             |
| 2052   | Layout 4             |
| 2011   | Layout 4             |
| 1996   | Layout 4             |
| 1969   | Layout 4             |
| 1937   | Layout 4             |
| 1914   | Layout 4             |
| 1886   | Layout 4             |
| 1866   | Layout 4             |
| 1838   | Layout 3             |
| 1818   | Layout 3             |
| 1794   | Layout 3             |
| 1784   | Layout 3             |
| 1749   | Layout 3             |
| 1717   | Layout 3             |
| 1698   | Layout 3             |
| 1674   | Layout 3             |
| 1636   | Layout 3             |
| 1608   | Layout 3             |
| 1587   | Layout 3             |
| 1565   | Layout 3             |
| 1537   | Layout 2             |
| 1509   | Layout 2             |
| 1485   | Layout 1             |
| 1466   | Layout 1             |
| 1445   | Layout 1             |
| 1426   | Layout 1             |
| 1409   | Layout 1             |
| 1390   | No documented layout |
| 1372   | No documented layout |
| 1360   | No documented layout |
| 1348   | No documented layout |
| 1338   | No documented layout |
| 1324   | No documented layout |
| 1316   | No documented layout |
| 1309   | No documented layout |
| 1286   | No documented layout |
| 1256   | No documented layout |
| 1230   | No file              |
| 1211   | No file              |
| 1194   | No file              |
| 1177   | No file              |
| 1156   | No file              |
| 1127   | No file              |
| 1109   | No file              |
| 1076   | No file              |
| 1058   | No file              |
| 1016   | No file              |
| 990    | No file              |
| 955    | No file              |
| 911    | No file              |
| 885    | No file              |
| 855    | No file              |
| 822    | No file              |
| 794    | No file              |
| 748    | No file              |
| 711    | No file              |
| 683    | No file              |
| 656    | No file              |
| 630    | No file              |
| 606    | No file              |
| 577    | No file              |
| 542    | No file              |
| 526    | No file              |
| 508    | No file              |
| 485    | No file              |
| 457    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset                       | Type                     | Field              | Notes                                         |
| ---------------------------- | ------------------------ | ------------------ | --------------------------------------------- |
| `+0x00`                      | char[4]                  | magic              | ASCII `PABR`                                  |
| `+0x04`                      | u32                      | row_count          | Number of instruments                         |
| `+0x08`                      | Row[row_count]           | rows               | See Row                                       |
| `rows+0x00`                  | u32                      | action_hash_count  | Number of `action_hashes`                     |
| `rows+0x04`                  | u32[action_hash_count]   | action_hashes      | Every distinct start and loop action hash of the rows, each once; see Notes |
| `action_hashes+0x00`         | String Table             | string_table       | See String Table                              |
| `string_table+0x00`          | u32                      | string_table_start | Offset of the string table, where `action_hashes` ends |
| `string_table+0x04`          | u32                      | zero               | `0`                                           |

### Row (variable: 43 bytes + articulations and loop actions)

| Offset                     | Type                     | Field                        | Notes                                                                                       |
| -------------------------- | ------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------- |
| `+0x00`                    | u8                       | index                        | Row key, `0` to `40` with gaps on client 3482; the number in `bank_name` for `0` to `19`    |
| `+0x01`                    | u32                      | bank_name                    | Index into `strings`: the Wwise bank (`MIDI_Instrument_00_AcousticGuitar`)                  |
| `+0x05`                    | u32                      | event_name                   | Index into `strings`: the Wwise event; the same string as `bank_name` on every row          |
| `+0x09`                    | u32                      | ingame_name                  | Index into `strings`: the name key (`AcousticGuitar`, `Advanced_Piano`)                     |
| `+0x0D`                    | u64                      | articulation_count           | Number of `articulations`                                                                   |
| `+0x15`                    | u8[articulation_count]   | articulations                | Articulation numbers; `99` alone for an instrument with one way to play                     |
| `articulations+0x00`       | u32                      | start_action_hash            | `ascii_key_hash` of the start action name (`SHY_MusicStart_Guitar` on client 1784)          |
| `articulations+0x04`       | u32                      | end_action_hash              | `ascii_key_hash` of the end action name                                                     |
| `articulations+0x08`       | u8                       | advanced_type                | Composer tab; see Advanced Type                                                             |
| `articulations+0x09`       | u32                      | instrument_name_type         | Index into `strings`: the tab name key (`AUDIO_MIDI_TAB_NOVICE`), UTF-16LE                  |
| `articulations+0x0D`       | u8                       | is_opened                    | `1` on every row                                                                            |
| `articulations+0x0E`       | u32                      | ing_action_count             | Number of `ing_action_hashes`; `3` on every row                                             |
| `articulations+0x12`       | u32[ing_action_count]    | ing_action_hashes            | `ascii_key_hash` of the loop action names (`SHY_MusicIng_Guitar` to `SHY_MusicIng3_Guitar`) |
| `ing_action_hashes+0x00`   | u8                       | is_provided                  | `1` for the instruments every character owns (Acoustic Guitar, Flute, Hand Drum on client 1784) |
| `ing_action_hashes+0x01`   | u8                       | unknown_ing_action_hashes_01 | `0` to `3`; see Open Questions                                                              |
| `ing_action_hashes+0x02`   | u8                       | unknown_ing_action_hashes_02 | The bank number in `bank_name` (`24` for `MIDI_Instrument_24_ProGuitarElectricClean`); `20` to `23` for the sine, triangle, square and saw synths |
| `ing_action_hashes+0x03`   | u8                       | unknown_ing_action_hashes_03 | `0` to `3` for the synth variants Basic, Stereo, Super and SuperOct; `0` on every other row |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                  |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                      |
| `+0x04` | pstr[string_count] | strings      | Bank, name and tab keys; a string several rows use is stored once; the tab keys are UTF-16LE (`is_wide` `1`), the rest UTF-8 |

## Layout 3

The row ends with `is_provided`: the three bytes after it do not exist yet.
Only the Row differs from Layout 4.

### Row (variable: 40 bytes + articulations and loop actions)

| Offset                     | Type                     | Field                | Notes                                                    |
| -------------------------- | ------------------------ | -------------------- | -------------------------------------------------------- |
| `+0x00`                    | u8                       | index                | Row key, `0` to `19` with gaps on client 1784            |
| `+0x01`                    | u32                      | bank_name            | Index into `strings`                                     |
| `+0x05`                    | u32                      | event_name           | Index into `strings`                                     |
| `+0x09`                    | u32                      | ingame_name          | Index into `strings`                                     |
| `+0x0D`                    | u64                      | articulation_count   | Number of `articulations`                                |
| `+0x15`                    | u8[articulation_count]   | articulations        | Articulation numbers                                     |
| `articulations+0x00`       | u32                      | start_action_hash    | `ascii_key_hash` of the start action name                |
| `articulations+0x04`       | u32                      | end_action_hash      | `ascii_key_hash` of the end action name                  |
| `articulations+0x08`       | u8                       | advanced_type        | Composer tab; see Advanced Type                          |
| `articulations+0x09`       | u32                      | instrument_name_type | Index into `strings`                                     |
| `articulations+0x0D`       | u8                       | is_opened            | `1` on every row                                         |
| `articulations+0x0E`       | u32                      | ing_action_count     | Number of `ing_action_hashes`                            |
| `articulations+0x12`       | u32[ing_action_count]    | ing_action_hashes    | `ascii_key_hash` of the loop action names                |
| `ing_action_hashes+0x00`   | u8                       | is_provided          | `1` for the instruments every character owns             |

## Layout 2

No `is_opened` byte after `instrument_name_type`, and the row ends with
`is_provided` as in Layout 3. Only the Row differs from Layout 3.

### Row (variable: 39 bytes + articulations and loop actions)

| Offset                     | Type                     | Field                | Notes                                                    |
| -------------------------- | ------------------------ | -------------------- | -------------------------------------------------------- |
| `+0x00`                    | u8                       | index                | Row key, `0` to `8` with gaps on client 1537             |
| `+0x01`                    | u32                      | bank_name            | Index into `strings`                                     |
| `+0x05`                    | u32                      | event_name           | Index into `strings`                                     |
| `+0x09`                    | u32                      | ingame_name          | Index into `strings`                                     |
| `+0x0D`                    | u64                      | articulation_count   | Number of `articulations`                                |
| `+0x15`                    | u8[articulation_count]   | articulations        | Articulation numbers                                     |
| `articulations+0x00`       | u32                      | start_action_hash    | `ascii_key_hash` of the start action name                |
| `articulations+0x04`       | u32                      | end_action_hash      | `ascii_key_hash` of the end action name                  |
| `articulations+0x08`       | u8                       | advanced_type        | Composer tab; see Advanced Type                          |
| `articulations+0x09`       | u32                      | instrument_name_type | Index into `strings`                                     |
| `articulations+0x0D`       | u32                      | ing_action_count     | Number of `ing_action_hashes`                            |
| `articulations+0x11`       | u32[ing_action_count]    | ing_action_hashes    | `ascii_key_hash` of the loop action names                |
| `ing_action_hashes+0x00`   | u8                       | is_provided          | `1` for the instruments every character owns             |

## Layout 1

No composer tab: the row has no `advanced_type`, `instrument_name_type` or
`is_opened`, and the loop actions follow the end action. Only the Row
differs from Layout 2.

### Row (variable: 34 bytes + articulations and loop actions)

| Offset                     | Type                     | Field              | Notes                                                    |
| -------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                    | u8                       | index              | Row key, `0` to `8` with gaps on client 1485             |
| `+0x01`                    | u32                      | bank_name          | Index into `strings`                                     |
| `+0x05`                    | u32                      | event_name         | Index into `strings`                                     |
| `+0x09`                    | u32                      | ingame_name        | Index into `strings`                                     |
| `+0x0D`                    | u64                      | articulation_count | Number of `articulations`                                |
| `+0x15`                    | u8[articulation_count]   | articulations      | Articulation numbers                                     |
| `articulations+0x00`       | u32                      | start_action_hash  | `ascii_key_hash` of the start action name                |
| `articulations+0x04`       | u32                      | end_action_hash    | `ascii_key_hash` of the end action name                  |
| `articulations+0x08`       | u32                      | ing_action_count   | Number of `ing_action_hashes`                            |
| `articulations+0x0C`       | u32[ing_action_count]    | ing_action_hashes  | `ascii_key_hash` of the loop action names                |
| `ing_action_hashes+0x00`   | u8                       | is_provided        | `1` for the instruments every character owns             |

## Advanced Type

| Value | Tab key (`instrument_name_type`)        | Instruments on client 3482                                  |
| ----- | --------------------------------------- | ----------------------------------------------------------- |
| 0     | `AUDIO_MIDI_TAB_NOVICE`                 | Acoustic Guitar to Violin, the beginner instruments          |
| 1     | `AUDIO_MIDI_TAB_ADVANCED`               | The Marnian instruments (`Advanced_*`) without the electric ones |
| 2     | `AUDIO_MIDI_TAB_ADVANCED_ELECTRONIC`    | Electric bass and guitars, the 16 synths                     |

The composer Lua names `__eInstrumentAdvancedType_Novice`,
`__eInstrumentAdvancedType_Advanced`, `__eeInstrumentAdvancedType_Synth`
(sic) and `__eInstrumentAdvancedType_Count`.

## Field Names

The `MidiInstrument_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Index`, `BankName`, `EventName`,
`ArticulationList`, `IngameName`, `IsOpened`, `ContentsGroupKey`,
`StartAction`, `EndAction`, `IsProvided`, `IngAction`, `SoundEffector`,
`AdvancedType`, `InstrumentNameType` and `InstrumentName`, 20 rows. The
client file holds the 15 rows with `IsOpened` `1`; the five with `0` are
not compiled. On those 15 rows every named field matches its column (15 of
15, client 1784); the action hashes are `ascii_key_hash` of the
`StartAction`, `EndAction` and `IngAction` names. `SoundEffector` holds the
same values as `AdvancedType` on all 20 rows; the field is named after
`AdvancedType`, which sits before `InstrumentNameType` in the sheet as the
field does in the row, and the electronic tab rows of client 3482 hold `2`
there. `ContentsGroupKey` and `InstrumentName`
(`AUDIO_MIDI_INSTRUMENT_0`) are not in the client file.

## Notes

- On client 3482 the start, end and loop action hashes match none of the
  client 1784 action names: the actions were renamed. Rows that share an
  instrument model (Acoustic Guitar and Marnian Acoustic Guitar, the four
  variants of one synth) share their hashes.
- `action_hashes` lists every distinct `start_action_hash` and
  `ing_action_hash` of the rows, each once and in no sorted order; no
  `end_action_hash` is in it (clients 1784 and 3482).

## Open Questions

### Instrument Family Byte

`unknown_ing_action_hashes_01` groups the instruments on client 3482: `0`
piano and the synths, `1` flute, recorder, clarinet and horn, `2` the
string instruments (guitars, harp, violin, basses), `3` the drums, cymbals
and hand pan. No sheet column of client 1784 holds it; the composer may
pick the play animation or the score clef with it.

### Rows Before Client 1409

Clients 1256 to 1390 hold another row (client 1256: two instruments in
144 bytes) that breaks every layout at `articulation_count`. No layout
reads these files yet.
