# `zodiacsign.dbss` Format

## Purpose

Defines the 12 BDO horoscope (zodiac) signs. Each record stores star-position coordinates, constellation-edge pairs, a Korean constellation name and personality-trait text, and two texture-asset paths.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records       | Row bytes                  |
| ------ | -------------- | ------- | ----------------------- | ----- | ------------- | -------------------------- |
| 1      | 3473 and later | 3473    | `zodiacsign.dbss`       | 4,810 | 12 Record     | 360 to 434, 400 on average |
| 1      | 3473 and later | 3473    | `zodiacsignoffset.dbss` | 112   | 12 Offset Row | 9                          |

| Layout | File                    | Known           | Unknown      |
| ------ | ----------------------- | --------------- | ------------ |
| 1      | `zodiacsign.dbss`       | 4,702 B (97.8%) | 108 B (2.2%) |
| 1      | `zodiacsignoffset.dbss` | 112 B (100.0%)  | 0 B (0.0%)   |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                       |
| ----------------------- | -------- | ------------------------------------------ |
| `zodiacsignoffset.dbss` | Required | ID-keyed index (same count, same order)    |
| `languagedata_en.loc`   | Optional | English names and trait text (str_type=7)  |

[`zodiacsignorder.dbss`](zodiacsignorder_dbss.md) holds the order the stars
light up per personality type, and
[`zodiacsignindex.bss`](zodiacsignindex_bss.md) the display order of the 12
signs.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                    |
| ------- | ------------- | ------- | ------------------------ |
| `+0x00` | u32           | count   | Number of records (= 12) |
| `+0x04` | Record[count] | records | See Record               |

### Record (variable: 54 bytes + stars and text)

All four strings are `str16`: a u64 count of UTF-16 code units (a u32 count
and a u32 `0`), then UTF-16LE text with no terminator.

| Offset                  | Type                     | Field              | Notes                                                          |
| ----------------------- | ------------------------ | ------------------ | -------------------------------------------------------------- |
| `+0x00`                 | u8                       | zodiac_id          | 1–12; always equal to the record's sequential index            |
| `+0x01`                 | u32                      | float_count        | Number of constellation star positions (slots); range 4–8      |
| `+0x05`                 | f32[float_count][3]      | star_positions     | `float_count` triples (x, y, 1.0); third element is always 1.0 |
| `star_positions+0x00`   | u32                      | pairs_count        | Number of star-connection pairs; usually equals `float_count`  |
| `star_positions+0x04`   | u16[pairs_count][2]      | star_pairs         | `pairs_count` pairs of (u16 a, u16 b); star connectivity data. Both are zero-based indices into `star_positions`; the first pair is `(0, 1)` on every sign |
| `star_pairs+0x00`       | str16                    | name_kr            | Korean constellation name ending in 자리, e.g. `망치자리`      |
| `name_kr+0x00` | str16                  | trait_text         | Korean personality traits                                      |
| `trait_text+0x00`       | str16                    | icon_small         | Path to small icon DDS                                         |
| `icon_small+0x00`       | str16                    | icon_large         | Path to large icon DDS                                         |
| `icon_large+0x00`       | u8                       | zodiac_id_dup      | Duplicate of `zodiac_id`                                       |
| `icon_large+0x01`       | u8                       | zodiac_id_dup2     | Duplicate of `zodiac_id` again                                 |
| `icon_large+0x02`       | u8                       | unknown_tail_02    | Always 0                                                       |
| `icon_large+0x03`       | u16                      | next_zodiac_id     | ID of the next zodiac in cycle (12 → 1)                        |
| `icon_large+0x05`       | u8                       | unknown_tail_05    | Always 1                                                       |
| `icon_large+0x06`       | u8                       | unknown_tail_06    | Always 0                                                       |
| `icon_large+0x07`       | u8                       | unknown_tail_07    | Always 1                                                       |
| `icon_large+0x08`       | u8                       | unknown_tail_08    | Always 0                                                       |
| `icon_large+0x09`       | u32                      | unknown_end        | Always 0                                                       |

The `unknown_tail_<hex>` offsets count from `zodiac_id_dup`.

Earlier versions of this doc called `zodiac_id_dup` `zodiac_id_tail`, and
read a u16 `unknown_after_pairs_count` after `pairs_count`, a `text_block` opening with a u32 `unknown_00` and a u16
`unknown_04`, and a `constellation_name` (now `name_kr`) with no length that
a reader found by scanning for the UTF-16LE bytes `90 C7 AC B9` ("자리").
Those 8 bytes are the first star index of `star_pairs` (always `0`) and the
top 6 bytes of the name's u64 count; the old reading shifted `star_pairs` by
2 bytes, so its last pair ended in the low half of that count. `star_pairs`
starts right after `pairs_count`, and the name is a `str16` like the other
three strings. Read this way the 12 records end exactly at end of file.

### `zodiacsignoffset.dbss`

Index file, one entry per zodiac record, stored in the same order as the main file.

| Offset  | Type              | Field   | Notes                              |
| ------- | ----------------- | ------- | ---------------------------------- |
| `+0x00` | u32               | count   | Must equal `zodiacsign.dbss` count |
| `+0x04` | Offset Row[count] | rows    | See Offset Row                     |

### Offset Row (9 bytes)

| Offset  | Type | Field       | Notes                                                            |
| ------- | ---- | ----------- | ---------------------------------------------------------------- |
| `+0x00` | u8   | zodiac_id   | Matches `zodiac_id` in main record                               |
| `+0x01` | u32  | data_offset | Byte offset into main file; 1 byte past the record start         |
| `+0x05` | u32  | data_size   | Byte count of record data (excluding the leading `zodiac_id` u8) |

`record_start = data_offset - 1`

## Reference Tables

### Zodiac ID → Name

| ID  | English Name  | Korean Constellation |
| --- | ------------- | -------------------- |
| 1   | Hammer        | 망치자리             |
| 2   | Boat          | 배자리               |
| 3   | Shield        | 방패자리             |
| 4   | Giant         | 거인자리             |
| 5   | Camel         | 낙타자리             |
| 6   | Black Dragon  | 검은용자리           |
| 7   | Treant Owl    | 엔트부엉이자리       |
| 8   | Elephant      | 코끼리자리           |
| 9   | Key           | 열쇠자리             |
| 10  | Wagon         | 마차자리             |
| 11  | Sealing Stone | 봉인석자리           |
| 12  | Goblin        | 고블린자리           |

### Personality Traits by Zodiac

| ID  | Traits (Korean)                                    |
| --- | -------------------------------------------------- |
| 1   | 용맹한, 보수적인, 의리 있는, 협동하는. 다혈질인.   |
| 2   | 풍류를 즐기는, 낙천적인, 자유로운. 방랑자.         |
| 3   | 이성적, 자신에게 엄격한, 계획적인.                 |
| 4   | 몽상가, 큰 뜻을 지닌, 재빠른. 관찰자.              |
| 5   | 끈기와 인내, 온순한, 또는 재주꾼.                  |
| 6   | 재물과 명성, 고매한, 세심한, 예민한, 사교적인.     |
| 7   | 우직한, 진부한, 뛰어난 지식, 천재 또는 멍청이      |
| 8   | 명예, 믿음이 강한, 우둔한, 헌신하는, 신뢰 받는.    |
| 9   | 탁월한 집중력, 지식의 탐구, 느긋한, 결정력이 좋은. |
| 10  | 행동하는, 재물을 타고난, 귀한, 이해타산적인        |
| 11  | 신중한, 기이한, 비밀을 가진, 단명할.               |
| 12  | 언어 술사, 신념, 지적인, 물질적인, 뛰어난 처세술   |

### Localisation

Names and trait descriptions in the user's language are in the LOC file under `str_type=7`, keyed by `str_id1=zodiac_id`:

| str_id4 | Field             |
| ------- | ----------------- |
| 0       | Sign name         |
| 1       | Trait description |

## Notes

- `star_positions` (x, y) pairs are 2D coordinates on the zodiac constellation display (range roughly ±250). The third float of each triple is always 1.0 and can be ignored.
- `personality_type` in `npcpersonality.dbss` cross-references `zodiac_id` via `major = personality_type // 100`.
