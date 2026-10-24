# `pad00000.meta` Format

## Purpose

`pad00000.meta` sits in the `Paz` folder next to the `PAD*.PAZ` archives. It
lists every archive and every file inside them, with the archive, offset and
sizes of each file and its full path. `read_bdo_meta` in
`PAZ-Parser/paz/bdo_meta_reader.py` reads the header and the archive table;
`read_meta_entries` reads the file table and both name blocks, so a client's
whole file list is known from the `.meta` alone, without its archives.

The layout is the same on every client checked, 435 (2017-05) to 3482
(2026-10).

## Layout

All integers are little-endian.

| Offset | Size                   | Type        | Field               | Notes |
| ------ | ---------------------- | ----------- | ------------------- | ----- |
| 0x0    | 4                      | u32         | `version`           | The client number (`fixtures: up to date with client NNNN` in pytest) |
| 0x4    | 4                      | u32         | `archive_count`     | Rows in the archive table |
| 0x8    | 12 x `archive_count`   | Archive Row | `archives`          | |
|        | 4                      | u32         | `file_count`        | Rows in the file table |
|        | 28 x `file_count`      | File Row    | `files`             | |
|        | 4                      | u32         | `folder_block_size` | A multiple of 8 |
|        | `folder_block_size`    | bytes       | `folder_block`      | ICE-encrypted Folder Records |
|        | 4                      | u32         | `name_block_size`   | A multiple of 8 |
|        | `name_block_size`      | bytes       | `name_block`        | ICE-encrypted file names; the file ends here |

### Archive Row

| Offset | Size | Type | Field         | Notes |
| ------ | ---- | ---- | ------------- | ----- |
| 0x0    | 4    | u32  | `archive`     | Archive number: `PAD00001.PAZ` is 1 |
| 0x4    | 4    | u32  | `checksum`    | Checksum of the archive file from byte 4 on; the archive's own header starts with the same value |
| 0x8    | 4    | u32  | `size`        | Size of the archive file in bytes |

### File Row

| Offset | Size | Type | Field             | Notes |
| ------ | ---- | ---- | ----------------- | ----- |
| 0x0    | 4    | u32  | `path_hash`       | Checksum of the file's path (folder path and name, bytes as stored); the archive header row starts with the same value |
| 0x4    | 4    | u32  | `folder_index`    | Index of the Folder Record that holds the file's folder path |
| 0x8    | 4    | u32  | `name_index`      | Index of the file's name in the name block |
| 0xC    | 4    | u32  | `archive`         | Archive number of the archive that stores the file |
| 0x10   | 4    | u32  | `offset`          | Offset of the payload in that archive |
| 0x14   | 4    | u32  | `compressed_size` | Stored size of the payload |
| 0x18   | 4    | u32  | `original_size`   | Size after decompression |

The file's path is the folder path followed by the name:
`gamecommondata/binary/` + `stringtable.bss`.

### Folder Record

| Offset | Size     | Type    | Field              | Notes |
| ------ | -------- | ------- | ------------------ | ----- |
| 0x0    | 4        | u32     | `first_name_index` | Index of the folder's first file name in the name block |
| 0x4    | 4        | u32     | `name_count`       | Number of file names in the folder |
| 0x8    | variable | cstring | `path`             | Folder path ending in `/`, then a zero byte |

Records follow each other without gaps. Each record's `first_name_index`
is the previous record's `first_name_index + name_count`, and every file
row's `name_index` lies in its folder's range (every row on clients 435 and
3482). Zero bytes after the last record pad the block to 8 bytes.

### Name Block

File names, each ending in a zero byte, in `name_index` order. Zero bytes
after the last name pad the block to 8 bytes; the padding is not a name.

## Checksum

`checksum` and `path_hash` use one function: Bob Jenkins' lookup3
`hashlittle` with its own start value and final mix. All arithmetic is on
u32 values.

1. `a`, `b` and `c` start at `length - 0x2145E233` (the input length in
   bytes; `0xDEADBEEF + length + 0xC5EDE` in lookup3 terms). An empty input
   gives 0.
2. While more than 12 bytes remain, add the next three little-endian u32 to
   `a`, `b` and `c` and run lookup3's `mix`.
3. Add the last 1 to 12 bytes, zero-padded to 12, to `a`, `b` and `c` the
   same way.
4. Final mix, where `rol` and `ror` rotate left and right:

| Step | Value |
| ---- | ----- |
| 1    | `p = (b ^ c) - rol(b, 14)` |
| 2    | `q = (a ^ p) - rol(p, 11)` |
| 3    | `r = (q ^ b) - ror(q, 7)` |
| 4    | `s = (r ^ p) - rol(r, 16)` |
| 5    | `t = (q ^ s) - rol(s, 4)` |
| 6    | `u = (t ^ r) - rol(t, 14)` |
| 7    | result `(u ^ s) - ror(u, 8)` |

On clients 435, 1784 and 3482, `path_hash` matches every file row
(471,162, 568,977 and 872,965 rows) and `checksum` matches every archive on
disk (30, 32 and 30). `pa_checksum` in `PAZ-Parser/paz/bdo_checksum.py` computes it, and
`PAZ-Parser/tests/test_checksum.py` checks it on the smallest archive of the
installed client. The function is `PaChecksum` in
MrIkso/CrimsonDesertTools (`Utils/PaChecksum.cs`, written for Crimson
Desert); `calculatePackCRC` in kukdh1/PAZ-Unpacker starts from the same
`length - 0x2145E233`.

## Notes

Both blocks are encrypted with ICE and the same key as the path block of a
`PAD*.PAZ` header (`BDO_ICE_KEY` in `PAZ-Parser/paz/bdo_ice.py`). ICE has no
chaining between 8-byte blocks, so each block decrypts in one call.

`read_meta_entries` decodes paths as UTF-8 with invalid bytes replaced, as
`parse_paz_files` does for the archive headers, so the two give the same
paths. A few names are CP949 (Korean) bytes and come out as replacement
characters in both; decoded as CP949 they read `gamecommondata/dialogscene/스폰.zip`
and `character/ai 스크립트_메뉴얼.xml`.

On clients 435, 508, 1058, 2313 and 3482, the entries `read_meta_entries`
gives for every archive on disk equal the entries `parse_paz_files` reads
from those archives' headers. `PAZ-Parser/tests/test_meta_reader.py` checks
this on the first 20 archives of the installed client.
