# `vehicleskillcount.dbss` Format

## Purpose

One byte: the highest mount and ship skill key in
[vehicleskill.dbss](vehicleskill_dbss.md) plus one. On client 3474 it is
`107` (`0x6B`), and `vehicleskill.dbss` holds the 106 skills with keys 1
to 106. The client Lua reads the value through
`vehicleSkillStaticStatus_skillCount()` and walks the skill keys from 1 to
one below it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------- | --------- |
| 1      | 1485 and later | 3474    | `vehicleskillcount.dbss` | 1     | -       | -         |

| Layout | File                     | Known        | Unknown    |
| ------ | ------------------------ | ------------ | ---------- |
| 1      | `vehicleskillcount.dbss` | 1 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. The file has no offset index.

## Layout 1

### File Layout

| Offset  | Type | Field | Notes                                                     |
| ------- | ---- | ----- | --------------------------------------------------------- |
| `+0x00` | u8   | count | Highest `vehicleskill.dbss` `key` + 1; `107` on client 3474 |

## Values per Client

The byte against `vehicleskill.dbss` on every test client that has the
file. The keys run from 1 to the record count with no gap on all of them,
so the byte is also the record count plus one.

| Client | `count` | `vehicleskill.dbss` records | Highest key |
| ------ | ------- | --------------------------- | ----------- |
| 1485   | 72      | 71                          | 71          |
| 1784   | 77      | 76                          | 76          |
| 2107   | 88      | 87                          | 87          |
| 2519   | 95      | 94                          | 94          |
| 3002   | 106     | 105                         | 105         |
| 3251   | 107     | 106                         | 106         |
| 3474   | 107     | 106                         | 106         |

Clients 794 and 1230 have neither file; their skills are in
`vehicleskill.bss`.

## Field Names

The 2016 `gc::VehicleSkillStaticStatusManager` starts with
`unsigned char _count`, followed by `_list`, a fixed array of
`gc::VehicleSkillStaticStatus` indexed by the u8 skill key (31 slots in
2016). Its `insert_StaticStatus` stores each skill at `_list[key]` and then
sets `_count` to `key + 1` when `_count` is not above `key`, so `_count` is
the highest key plus one; a gap in the keys would put it more than one
above the number of skills. The field takes that name. The client Lua on client 3474 agrees:
`panel_worldmap_stablelist`, `panel_dialog_servantmarket_all` and
`panel_dialog_servantmarket_rental_mating_all` count a servant's learned
skills with `for skillIdx = 1, vehicleSkillStaticStatus_skillCount() - 1`,
and `panel_window_vehicleinfo_all` loops up to the value itself.

## Notes

- The first byte of `vehicleskill.dbss` (`unknown_00` there) holds the
  same value on every client in the table above.
- `count` is a u8 because the skill key is one; it cannot pass 255.
