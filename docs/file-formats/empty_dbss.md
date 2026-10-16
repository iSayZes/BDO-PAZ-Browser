# Empty DBSS Tables Format

## Purpose

DBSS tables the client ships with no records. Each file below is a u32 count
of `0` and nothing else, on client 3464:

| Main file                         | Offset companion                        |
| --------------------------------- | --------------------------------------- |
| `alchemystatus.dbss`              | `alchemystatusoffset.dbss`              |
| `buffcondition.dbss`              | `buffconditionoffset.dbss`              |
| `cashforui.dbss`                  | `cashforuioffset.dbss`                  |
| `chinaspawnoption.dbss`           | `chinaspawnoptionoffset.dbss`           |
| `grenadedata.dbss`                | `grenadedataoffset.dbss`                |
| `growthpasspointshop.dbss`        | `growthpasspointshopoffset.dbss`        |
| `installation.dbss`               | `installationoffset.dbss`               |
| `instancedungeonskillstatic.dbss` | `instancedungeonskillstaticoffset.dbss` |
| `itemtradegroupfromnpc.dbss`      | `itemtradegroupfromnpcoffset.dbss`      |
| `petmarketsetting.dbss`           | `petmarketsettingoffset.dbss`           |
| `petset.dbss`                     | `petsetoffset.dbss`                     |
| `servantcategory.dbss`            | `servantcategoryoffset.dbss`            |
| `worldquest.dbss`                 | none in the archive                     |

`itemcouponreward.dbss` also declares zero records but has 12 bytes after the
count; see [itemcouponreward](itemcouponreward_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

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

## Open Questions

### Non-Empty Layout

No file has a record, so every record layout is unknown. When a client ships
`count > 0` for one of these tables, it moves to its own doc and handler, with
records starting at `+0x04`.
