# Empty DBSS Tables Format

## Purpose

DBSS tables the client ships with no records. Each file below is a u32 count
of `0` and nothing else, on every client checked (1784 and 3473):

| Main file               | Offset companion              |
| ----------------------- | ----------------------------- |
| `alchemystatus.dbss`    | `alchemystatusoffset.dbss`    |
| `buffcondition.dbss`    | `buffconditionoffset.dbss`    |
| `cashforui.dbss`        | `cashforuioffset.dbss`        |
| `chinaspawnoption.dbss` | `chinaspawnoptionoffset.dbss` |
| `grenadedata.dbss`      | `grenadedataoffset.dbss`      |
| `installation.dbss`     | `installationoffset.dbss`     |
| `petmarketsetting.dbss` | `petmarketsettingoffset.dbss` |
| `petset.dbss`           | `petsetoffset.dbss`           |
| `servantcategory.dbss`  | `servantcategoryoffset.dbss`  |
| `worldquest.dbss`       | none in the archive           |

`itemcouponreward.dbss` also declares zero records but has 12 bytes after the
count; see [itemcouponreward](itemcouponreward_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3473    | `alchemystatus.dbss`          | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `alchemystatusoffset.dbss`    | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `buffcondition.dbss`          | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `buffconditionoffset.dbss`    | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `cashforui.dbss`              | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `cashforuioffset.dbss`        | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `chinaspawnoption.dbss`       | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `chinaspawnoptionoffset.dbss` | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `grenadedata.dbss`            | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `grenadedataoffset.dbss`      | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `installation.dbss`           | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `installationoffset.dbss`     | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `petmarketsetting.dbss`       | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `petmarketsettingoffset.dbss` | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `petset.dbss`                 | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `petsetoffset.dbss`           | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `servantcategory.dbss`        | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `servantcategoryoffset.dbss`  | 4     | -       | -         |
| 1      | 1784 and later | 3473    | `worldquest.dbss`             | 4     | -       | -         |

| Layout | File                          | Known        | Unknown    |
| ------ | ----------------------------- | ------------ | ---------- |
| 1      | `alchemystatus.dbss`          | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `alchemystatusoffset.dbss`    | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `buffcondition.dbss`          | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `buffconditionoffset.dbss`    | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `cashforui.dbss`              | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `cashforuioffset.dbss`        | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `chinaspawnoption.dbss`       | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `chinaspawnoptionoffset.dbss` | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `grenadedata.dbss`            | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `grenadedataoffset.dbss`      | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `installation.dbss`           | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `installationoffset.dbss`     | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `petmarketsetting.dbss`       | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `petmarketsettingoffset.dbss` | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `petset.dbss`                 | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `petsetoffset.dbss`           | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `servantcategory.dbss`        | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `servantcategoryoffset.dbss`  | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `worldquest.dbss`             | 4 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. Each offset companion in the table above is a file of its own with
the same layout as its main file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

Main files and offset companions share one layout. No record structure can
be inferred because the files hold no records.

| Offset  | Type | Field | Notes                                  |
| ------- | ---- | ----- | -------------------------------------- |
| `+0x00` | u32  | count | Number of records; `0` in every file   |

## Notes

- Raw bytes of every file: `00 00 00 00`.
- The list comes from a scan of every file under `gamecommondata/binary/` for
  files of at most 8 bytes that are all zero.
- One handler class (`EmptyTableHandler`, `_common/empty_table.py`) previews
  every file in `_dbss/empty_tables/tables.py`. A file whose count is not `0`
  raises an error, so a client that fills one of these tables shows up as a
  parse error and in the tests.
- `worldquest.dbss` had the same 4 bytes before the 2026-09-27 client update.
- `growthpasspointshop.dbss`, `instancedungeonskillstatic.dbss` and
  `itemtradegroupfromnpc.dbss` are a count of `0` on client 3473 but hold
  records on client 1784, so each has a doc and a handler of its own:
  [growthpasspointshop](growthpasspointshop_dbss.md),
  [instancedungeonskillstatic](instancedungeonskillstatic_dbss.md) and
  [itemtradegroupfromnpc](itemtradegroupfromnpc_dbss.md).

## Open Questions

### Non-Empty Layout

No file has a record on client 1784 or client 3473, so every record layout
is unknown. When a client ships `count > 0` for one of these tables, it
moves to its own doc and handler, with records starting at `+0x04`.
