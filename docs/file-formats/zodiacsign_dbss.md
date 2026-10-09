# `zodiacsign.dbss` Format

## Purpose

Defines the 12 BDO horoscope (zodiac) signs. Each record stores star-position coordinates, constellation-edge pairs, a Korean constellation name and personality-trait text, and two texture-asset paths.

Example:

```text
zodiac_id: 1  →  Hammer / 망치자리
Traits: Brave, Conservative, Hot-Blooded.
Stars: 5 positions, icon: Customize_Zodiac_M_Hammer.dds
```

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

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                    |
| ------- | ---- | ----- | ------------------------ |
| `+0x00` | u32  | count | Number of records (= 12) |

### Record (variable length, repeated `count` times)

| Offset  | Type       | Field          | Notes                                                          |
| ------- | ---------- | -------------- | -------------------------------------------------------------- |
| `+0x00` | u8         | zodiac_id      | 1–12; always equal to the record's sequential index            |
| `+0x01` | u32        | float_count    | Number of constellation star positions (slots); range 4–8      |
| `+0x05` | f32×3 × n  | star_positions | `float_count` triples (x, y, 1.0); third element is always 1.0 |
| -       | u32        | pairs_count    | Number of star-connection pairs; usually equals `float_count`  |
| -       | u16        | padding        | Always 0                                                       |
| -       | u16×2 × n  | star_pairs     | `pairs_count` pairs of (u16 a, u16 b); star connectivity data  |
| -       | _variable_ | text_block     | Korean text block (see below)                                  |
| -       | u32        | icon_small_len | Char count of `icon_small` string                              |
| -       | u32        | icon_small_pad | Always 0                                                       |
| -       | char16 × n | icon_small     | Path to small icon DDS                                         |
| -       | u32        | icon_large_len | Char count of `icon_large` string                              |
| -       | u32        | icon_large_pad | Always 0                                                       |
| -       | char16 × n | icon_large     | Path to large icon DDS                                         |
| -       | u8         | zodiac_id_tail | Duplicate of `zodiac_id`                                       |
| -       | u8         | zodiac_id_dup2 | Duplicate of `zodiac_id` again                                 |
| -       | u8         | pad0           | Always 0                                                       |
| -       | u16        | next_zodiac_id | ID of the next zodiac in cycle (12 → 1)                        |
| -       | u8         | const1         | Always 1                                                       |
| -       | u8         | const0a        | Always 0                                                       |
| -       | u8         | const1b        | Always 1                                                       |
| -       | u8         | const0b        | Always 0                                                       |
| -       | u32        | reserved       | Always 0                                                       |

#### text_block Layout

| Sub-offset | Type       | Field              | Notes                                                           |
| ---------- | ---------- | ------------------ | --------------------------------------------------------------- |
| `+0x00`    | u32        | reserved_a         | Always 0                                                        |
| `+0x04`    | u16        | reserved_b         | Always 0                                                        |
| `+0x06`    | char16 × n | constellation_name | Korean name ending in 자리; scan for `U+C790 U+B9AC` (= "자리") |
| -          | u64        | trait_text_len     | Char count of trait text                                        |
| -          | char16 × n | trait_text         | Korean personality traits                                       |

`constellation_name` has no explicit length prefix; locate by scanning for the UTF-16LE byte sequence `90 C7 AC B9` (= "자리"). Everything from sub-offset `+0x06` up to and including those bytes is the name.

#### String Encoding

Icon path strings and trait text both use:

```text
u32 char_count   (number of UTF-16 code units)
u32 padding = 0
char16[char_count]  (UTF-16 LE, no null terminator)
```

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

## zodiacsignoffset.dbss

Index file, one entry per zodiac record, stored in the same order as the main file.

### Header (4 bytes)

| Offset  | Type | Field | Notes                              |
| ------- | ---- | ----- | ---------------------------------- |
| `+0x00` | u32  | count | Must equal `zodiacsign.dbss` count |

### Offset Record (9 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                            |
| ------- | ---- | ----------- | ---------------------------------------------------------------- |
| `+0x00` | u8   | zodiac_id   | Matches `zodiac_id` in main record                               |
| `+0x01` | u32  | data_offset | Byte offset into main file; 1 byte past the record start         |
| `+0x05` | u32  | data_size   | Byte count of record data (excluding the leading `zodiac_id` u8) |

`record_start = data_offset - 1`

## Suggested UI Layout

| Column        | Type | Notes                                             |
| ------------- | ---- | ------------------------------------------------- |
| ID            | num  | `zodiac_id`                                       |
| Name          | text | LOC `str_type=7`, `str_id1=zodiac_id`, `str_id4=0`; the inline Korean `constellation_name` without LOC |
| Stars         | num  | Number of stars in the constellation              |
| Pairs         | num  | Number of connecting line pairs                   |
| Traits        | text | LOC `str_id4=1` trait text; the inline Korean `trait_text` without LOC |

## Notes

- `star_positions` (x, y) pairs are 2D coordinates on the zodiac constellation display (range roughly ±250). The third float of each triple is always 1.0 and can be ignored.
- `personality_type` in `npcpersonality.dbss` cross-references `zodiac_id` via `major = personality_type // 100`.
