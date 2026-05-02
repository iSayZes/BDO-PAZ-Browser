# zodiacsign.dbss

Defines the 12 BDO horoscope (zodiac) signs. Each record stores star-position
coordinates, constellation-edge pairs, a Korean constellation name and
personality-trait text, and two texture-asset paths.

Companion files:
- `zodiacsignoffset.dbss` — ID-keyed index (same count, same order)
- `zodiacsignorder.dbss` — per-personality-type trigger/drawing-order sequences
- `zodiacsignorderoffset.dbss` — ID-keyed index for zodiacsignorder

---

## zodiacsign.dbss

### Header (4 bytes)

| Offset | Type | Field | Notes                    |
| ------ | ---- | ----- | ------------------------ |
| 0x00   | u32  | count | Number of records (= 12) |

### Record (variable length, repeated `count` times)

| Offset | Type              | Field            | Notes                                                                 |
| ------ | ----------------- | ---------------- | --------------------------------------------------------------------- |
| 0x00   | u8                | zodiac_id        | 1–12; always equal to the record's sequential index                   |
| 0x01   | u32               | float_count      | Number of constellation star positions (= **slots**); range 4–8      |
| 0x05   | f32×3 × n         | star_positions   | `float_count` triples (x, y, 1.0); third element is always 1.0       |
| —      | u32               | pairs_count      | Number of star-connection pairs; usually equals `float_count`         |
| —      | u16               | padding          | Always 0                                                              |
| —      | u16×2 × n         | star_pairs       | `pairs_count` pairs of (u16 a, u16 b); star connectivity data         |
| —      | *variable*        | text_block       | Korean text block (see below)                                         |
| —      | u32               | icon_small_len   | Char count of `icon_small` string                                     |
| —      | u32               | icon_small_pad   | Always 0                                                              |
| —      | char16 × n        | icon_small       | Path to small icon DDS, e.g. `Combine\Icon\Zodiac\Customize_Zodiac_M_Hammer.dds` |
| —      | u32               | icon_large_len   | Char count of `icon_large` string                                     |
| —      | u32               | icon_large_pad   | Always 0                                                              |
| —      | char16 × n        | icon_large       | Path to large icon DDS, e.g. `New_UI_Common_forLua\Window\Zodiac\Zodiac_Hammer.dds` |
| —      | u8                | zodiac_id_tail   | Duplicate of `zodiac_id`                                              |
| —      | u8                | zodiac_id_dup2   | Duplicate of `zodiac_id` again                                        |
| —      | u8                | pad0             | Always 0                                                              |
| —      | u16               | next_zodiac_id   | ID of the next zodiac in cycle (12 → 1)                               |
| —      | u8                | const1           | Always 1                                                              |
| —      | u8                | const0a          | Always 0                                                              |
| —      | u8                | const1b          | Always 1                                                              |
| —      | u8                | const0b          | Always 0                                                              |
| —      | u32               | reserved         | Always 0                                                              |

#### text_block layout

| Sub-offset | Type       | Field              | Notes                                                                  |
| ---------- | ---------- | ------------------ | ---------------------------------------------------------------------- |
| 0x00       | u32        | reserved_a         | Always 0                                                               |
| 0x04       | u16        | reserved_b         | Always 0                                                               |
| 0x06       | char16 × n | constellation_name | Korean name ending in 자리 (e.g. 망치자리); scan forward until `U+C790 U+B9AC` |
| —          | u64        | trait_text_len     | Char count of trait text                                               |
| —          | char16 × n | trait_text         | Korean personality traits (e.g. `용맹한, 보수적인, 의리 있는`)        |

The `constellation_name` has no explicit length prefix; locate it by scanning for
the UTF-16LE byte sequence `90 C7 AC B9` (= "자리"), which always terminates the
name. Everything from sub-offset 0x06 up to and including `AC B9` is the name.

### String encoding

Both icon path strings and the trait text use the format:
```
u32 char_count   (number of UTF-16 code units)
u32 padding = 0
char16[char_count]  (UTF-16 LE, no null terminator)
```

### Localisation

English names and trait descriptions are in `languagedata_en.loc` under `str_type=7`, keyed by `str_id1=zodiac_id`:

| str_id4 | Field              |
| ------- | ------------------ |
| 0       | Sign name          |
| 1       | Trait description  |

Example lookup for zodiac_id=1: `loc_lookup(7, 1, 0, 0, 0)` → `"Hammer"`, `loc_lookup(7, 1, 0, 0, 1)` → trait text.

---

### Zodiac ID → name mapping

| ID | English name  | Korean constellation |
| -- | ------------- | -------------------- |
|  1 | Hammer        | 망치자리              |
|  2 | Boat          | 배자리                |
|  3 | Shield        | 방패자리              |
|  4 | Giant         | 거인자리              |
|  5 | Camel         | 낙타자리              |
|  6 | Black Dragon  | 검은용자리            |
|  7 | Treant Owl    | 엔트부엉이자리        |
|  8 | Elephant      | 코끼리자리            |
|  9 | Key           | 열쇠자리              |
| 10 | Wagon         | 마차자리              |
| 11 | Sealing Stone | 봉인석자리            |
| 12 | Goblin        | 고블린자리            |

### Personality traits by zodiac

| ID | Traits (Korean)                                            |
| -- | ---------------------------------------------------------- |
|  1 | 용맹한, 보수적인, 의리 있는, 협동하는. 다혈질인.          |
|  2 | 풍류를 즐기는, 낙천적인, 자유로운. 방랑자.                |
|  3 | 이성적, 자신에게 엄격한, 계획적인.                        |
|  4 | 몽상가, 큰 뜻을 지닌, 재빠른. 관찰자.                     |
|  5 | 끈기와 인내, 온순한, 또는 재주꾼.                         |
|  6 | 재물과 명성, 고매한, 세심한, 예민한, 사교적인.            |
|  7 | 우직한, 진부한, 뛰어난 지식, 천재 또는 멍청이             |
|  8 | 명예, 믿음이 강한, 우둔한, 헌신하는, 신뢰 받는.           |
|  9 | 탁월한 집중력, 지식의 탐구, 느긋한, 결정력이 좋은.        |
| 10 | 행동하는, 재물을 타고난, 귀한, 이해타산적인               |
| 11 | 신중한, 기이한, 비밀을 가진, 단명할.                       |
| 12 | 언어 술사, 신념, 지적인, 물질적인, 뛰어난 처세술           |

---

## zodiacsignoffset.dbss

Index file, one entry per zodiac record, stored in the same order as the main file.

### Header (4 bytes)

| Offset | Type | Field | Notes                              |
| ------ | ---- | ----- | ---------------------------------- |
| 0x00   | u32  | count | Must equal `zodiacsign.dbss` count |

### Offset Record (9 bytes, repeated `count` times)

| Offset | Type | Field      | Notes                                                              |
| ------ | ---- | ---------- | ------------------------------------------------------------------ |
| 0x00   | u8   | zodiac_id  | Matches `zodiac_id` in main record                                 |
| 0x01   | u32  | data_offset| Byte offset into main file; points 1 byte past the record start (skips the u8 zodiac_id) |
| 0x05   | u32  | data_size  | Byte count of the record data (excluding the leading zodiac_id u8) |

`record_start = data_offset - 1`

---

## zodiacsignorder.dbss

Maps each personality type (variant 1 and 2 for all 12 signs = 24 records) to a
slot-trigger drawing order for the zodiac constellation animation.

### Header (4 bytes)

| Offset | Type | Field | Notes                    |
| ------ | ---- | ----- | ------------------------ |
| 0x00   | u32  | count | Number of records (= 24) |

### Record (variable, 21–27 bytes)

Records are NOT stored sequentially; use the offset file to locate them.

| Offset | Type      | Field          | Notes                                                              |
| ------ | --------- | -------------- | ------------------------------------------------------------------ |
| 0x00   | u16       | personality_type | `major × 100 + variant`; range 101–1202 (all 12 signs × 2 variants) |
| 0x02   | u16       | trigger_count  | Total number of trigger steps = `len(trigger_order)` = 1 + len(step_indices) |
| 0x04   | u32       | reserved_a     | Always 0                                                           |
| 0x08   | u32       | reserved_b     | 0 for variant 1; variant 2 may have non-zero values                |
| 0x0C   | u16 × (trigger_count − 1) | step_indices | 0-indexed slot indices for steps 1 onward |
| —      | u8        | zodiac_id      | Which zodiac sign (1–12)                                           |
| —      | u16       | personality_type_dup | Duplicate of `personality_type` at offset 0x00               |

**trigger_order** (as used in-game) = `[0] + list(step_indices)`. The first trigger
is always slot 0; the remaining `trigger_count − 1` values follow from `step_indices`.

**slots** (number of star positions) = `zodiacsign.float_count` for that zodiac_id.

### zodiacsignorderoffset.dbss

Same layout as other `*offset.dbss` companion files.

### Offset Record (10 bytes, repeated 24 times)

| Offset | Type | Field            | Notes                                                          |
| ------ | ---- | ---------------- | -------------------------------------------------------------- |
| 0x00   | u16  | personality_type | Matches personality_type in the main record                    |
| 0x02   | u32  | data_offset      | Byte offset into zodiacsignorder.dbss; points 2 bytes past the record start (skips u16 personality_type) |
| 0x06   | u16  | data_size        | Size of the record data (excluding the leading u16 personality_type) |
| 0x08   | u16  | padding          | Always 0                                                       |

`record_start = data_offset - 2`

---

## Notes

- Little-endian throughout.
- `star_positions` (x, y) pairs are 2D coordinates on the zodiac constellation
  display (range roughly ±250). The third float of each triple is always 1.0 and
  can be ignored.
- `personality_type` in npcpersonality.dbss cross-references zodiac_id via
  `major = personality_type // 100` (1–12 → zodiac IDs 1–12).
- `zodiacsignindex.bss` has a `PABR` magic header and lists the 12 zodiac IDs
  sequentially; it appears to be a simple lookup table, not needed for display.
- Variant 2 (e.g. 102, 202) `step_indices` typically differ from variant 1 —
  they represent an alternate drawing order for the same constellation. Variant 1
  is usually the canonical forward order [0,1,2,3...]; variant 2 may reverse or
  reorder steps.
- Major 9 (Key): only personality_type 901 exists in npcpersonality.dbss, but
  zodiacsignorder.dbss defines both 901 and 902.
