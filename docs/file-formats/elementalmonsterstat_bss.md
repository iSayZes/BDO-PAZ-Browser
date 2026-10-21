# `elementalmonsterstat.bss` Format

## Purpose

The monsters of the Black Shrine (검은 사당) boss blitz in the Land of the
Morning Light: one variable-length row per character, the boss of each
group and difficulty and the monsters of its fight. A row holds the boss
group and difficulty, the aura the monster is weak to, its aura offence and
defence, the minimum AP of the higher Calamities, what unlocks the
difficulty, the reward preview of the window and the world position the
window navigates to. The Black Shrine window reads a row through
`ToClient_getElementalMonsterInfo(group, level)` and
`ToClient_getElementalMonsterInfoByCharacterKey(characterKey)`.

On client 3474 the 1,000 rows hold 108 bosses in 17 groups: groups `0` to
`9` are Black Shrine: Donghae (Solo) with ten Calamities each (seven for
groups `3` and `9`), groups `10` to `16` Black Shrine: Hwanghae (Party)
with a Normal and a Hard difficulty each.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes  | Records                    | Row bytes               |
| ------ | -------------- | ------- | -------------------------- | ------ | -------------------------- | ----------------------- |
| 3      | 3474 and later | 3474    | `elementalmonsterstat.bss` | 44,732 | 1,000 Row, 108 Reward Item | 43 to 59, 45 on average |
| 2      | 3002 to 3251   | 3251    | `elementalmonsterstat.bss` | 42,208 | 972 Row                    | 43 to 47, 43 on average |
| 1      | 2519           | 2519    | `elementalmonsterstat.bss` | 38,138 | 993 Row                    | 38 to 42, 38 on average |

| Layout | File                       | Known             | Unknown    |
| ------ | -------------------------- | ----------------- | ---------- |
| 3      | `elementalmonsterstat.bss` | 44,732 B (100.0%) | 0 B (0.0%) |
| 2      | `elementalmonsterstat.bss` | 42,208 B (100.0%) | 0 B (0.0%) |
| 1      | `elementalmonsterstat.bss` | 38,138 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. The handler names characters, items and knowledge from
`languagedata_*.loc` and the lookup indexes, and the parts, difficulties and
auras with the `stringtable.bss` keys the Black Shrine window uses (LOC
type 37), when they are loaded.

All multi-byte values are little-endian.

## Layout 3

### File Layout

Plain binary: no `PABR` magic, no offset file and no trailer.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 43 bytes + show rewards)

| Offset              | Type                            | Field                  | Notes                                                                              |
| ------------------- | ------------------------------- | ---------------------- | ---------------------------------------------------------------------------------- |
| `+0x00`             | u16                             | character_key          | Row key, the `characterstatic.dbss` character; `getCharacterKeyRaw()`              |
| `+0x02`             | u16                             | character_key_dup      | Equals `character_key` on every row                                                |
| `+0x04`             | u16                             | unlock_character_key   | Boss of the previous difficulty of the group, `0` when none; see Field Names       |
| `+0x06`             | u32                             | unlock_mental_card_key | Knowledge (LOC type 34) that unlocks the group, `0` when none; `getUnlockConditionMentalCardKeyRaw()` |
| `+0x0a`             | f32                             | offence_stat           | Aura offence; `getOffenceStat()`, see Open Questions                               |
| `+0x0e`             | f32                             | defence_stat           | Aura defence; `getDffenceStat()`, see Open Questions                               |
| `+0x12`             | u8                              | element_type           | The aura the monster is weak to, see [`elementalstat.bss` Element Types](elementalstat_bss.md#element-types); `getElementalStatType()` |
| `+0x13`             | u8                              | level                  | Difficulty, from `0`; `getLevel()`, see [Difficulties](#difficulties)              |
| `+0x14`             | u8                              | group                  | Boss group, see [Groups](#groups); `getGroup()`                                    |
| `+0x15`             | u8                              | is_boss                | `1` on the boss of the group and difficulty, `0` on the other monsters; `getIsBoss()` |
| `+0x16`             | u8                              | monster_part           | `1` Donghae (Solo), `2` Hwanghae (Party); `getMorningLandMonsterPartRaw()`         |
| `+0x17`             | u32                             | show_reward_count      | Number of `show_rewards`; `1` on the 108 bosses, `0` on the other rows (client 3474) |
| `+0x1b`             | Reward Item[show_reward_count]  | show_rewards           | The reward preview of the window; `ToClient_getElementalMonsterShowRewardItemKey` |
| `show_rewards+0x00` | f32                             | position_x             | World position the window navigates to; `getPosition()`                            |
| `show_rewards+0x04` | f32                             | position_y             | Height                                                                             |
| `show_rewards+0x08` | f32                             | position_z             |                                                                                    |
| `show_rewards+0x0c` | f32                             | min_ap                 | Minimum displayed AP to enter; `getMinAP()`, `0` when there is none               |

### Reward Item (16 bytes)

| Offset  | Type     | Field      | Notes                                                                    |
| ------- | -------- | ---------- | ------------------------------------------------------------------------ |
| `+0x00` | u32      | item_key   | Item key, `enchant_level << 24 \| item_id` (`ItemEnchantKey` in the Lua) |
| `+0x04` | bytes[4] | padding_04 | Alignment of `count`; `bf 00 00 00` on every entry (client 3474), see Notes |
| `+0x08` | i64      | count      | Number of the item; `ToClient_getElementalMonsterShowRewardItemCount`    |

## Layout 2

### Row (variable: 43 bytes + show rewards)

| Offset              | Type                    | Field                  | Notes                                 |
| ------------------- | ----------------------- | ---------------------- | ------------------------------------- |
| `+0x00`             | u16                     | character_key          |                                       |
| `+0x02`             | u16                     | character_key_dup      |                                       |
| `+0x04`             | u16                     | unlock_character_key   |                                       |
| `+0x06`             | u32                     | unlock_mental_card_key |                                       |
| `+0x0a`             | f32                     | offence_stat           |                                       |
| `+0x0e`             | f32                     | defence_stat           |                                       |
| `+0x12`             | u8                      | element_type           |                                       |
| `+0x13`             | u8                      | level                  |                                       |
| `+0x14`             | u8                      | group                  |                                       |
| `+0x15`             | u8                      | is_boss                |                                       |
| `+0x16`             | u8                      | monster_part           |                                       |
| `+0x17`             | u32                     | show_reward_count      |                                       |
| `+0x1b`             | u32[show_reward_count]  | show_rewards           | Item keys alone, no count             |
| `show_rewards+0x00` | f32                     | position_x             |                                       |
| `show_rewards+0x04` | f32                     | position_y             |                                       |
| `show_rewards+0x08` | f32                     | position_z             |                                       |
| `show_rewards+0x0c` | f32                     | min_ap                 |                                       |

## Layout 1

### Row (variable: 38 bytes + show rewards)

| Offset              | Type                    | Field                  | Notes                                 |
| ------------------- | ----------------------- | ---------------------- | ------------------------------------- |
| `+0x00`             | u16                     | character_key          |                                       |
| `+0x02`             | u16                     | character_key_dup      |                                       |
| `+0x04`             | u16                     | unlock_character_key   |                                       |
| `+0x06`             | u32                     | unlock_mental_card_key |                                       |
| `+0x0a`             | f32                     | offence_stat           |                                       |
| `+0x0e`             | f32                     | defence_stat           |                                       |
| `+0x12`             | u8                      | element_type           |                                       |
| `+0x13`             | u8                      | level                  |                                       |
| `+0x14`             | u8                      | group                  |                                       |
| `+0x15`             | u8                      | is_boss                |                                       |
| `+0x16`             | u32                     | show_reward_count      |                                       |
| `+0x1a`             | u32[show_reward_count]  | show_rewards           | Item keys alone, no count             |
| `show_rewards+0x00` | f32                     | position_x             |                                       |
| `show_rewards+0x04` | f32                     | position_y             |                                       |
| `show_rewards+0x08` | f32                     | position_z             |                                       |

Layout 1 has no `monster_part` and no `min_ap`: the client had only the
Donghae (Solo) bosses, and every difficulty was gated by its offence and
defence.

## Groups

The level `0` boss of each group on client 3474, with the aura it is weak
to. The weak auras are the ones the official event notice "[Black Shrine]
Enhanced Blessing and Unpurified Energy" lists per boss.

| Group | Part             | Boss (level 0)           | Weak aura | Levels | `unlock_mental_card_key` (levels 0 to 4) |
| ----- | ---------------- | ------------------------ | --------- | ------ | ---------------------------------------- |
| `0`   | Donghae (Solo)   | Golden Pig King          | Sun       | 0 to 9 | `11742` Tale of the Golden Pig King      |
| `1`   | Donghae (Solo)   | Oduksini                 | Sun       | 0 to 9 | `11756` Tale of the Oduksini             |
| `2`   | Donghae (Solo)   | Apex Changui             | Sun       | 0 to 9 | `11750` Tale of the Apex Changui         |
| `3`   | Donghae (Solo)   | Bari                     | Moon      | 0 to 6 | `11733` Tale of the Mudang Wraith        |
| `4`   | Donghae (Solo)   | Songakshi                | Moon      | 0 to 9 | `11739` Tale of the Songakshi            |
| `5`   | Donghae (Solo)   | Bamboo Legion Lieutenant | Moon      | 0 to 9 | `11748` Tale of the Bamboo Legion        |
| `6`   | Donghae (Solo)   | Sangoon                  | Earth     | 0 to 9 | `11753` Tale of Sangoon                  |
| `7`   | Donghae (Solo)   | Gumiho                   | Earth     | 0 to 9 | `11736` Tale of the Gumiho               |
| `8`   | Donghae (Solo)   | Duoksini                 | Earth     | 0 to 9 | `11745` Tale of Duoksini                 |
| `9`   | Donghae (Solo)   | Imoogi                   | Earth     | 0 to 6 | `11756` Tale of the Oduksini             |
| `10`  | Hwanghae (Party) | Jigwi                    | Sun       | 0 to 1 | `0`                                      |
| `11`  | Hwanghae (Party) | Blue-clad Youth          | Sun       | 0 to 1 | `0`                                      |
| `12`  | Hwanghae (Party) | Bulgasal                 | Sun       | 0 to 1 | `0`                                      |
| `13`  | Hwanghae (Party) | Uturi                    | Sun       | 0 to 1 | `0`                                      |
| `14`  | Hwanghae (Party) | Dark Bonghwang           | Sun       | 0 to 1 | `0`                                      |
| `15`  | Hwanghae (Party) | Deposed Crown Prince     | Sun       | 0 to 1 | `0`                                      |
| `16`  | Hwanghae (Party) | Bihyung                  | Sun       | 0 to 1 | `0`                                      |

Every Hwanghae (Party) row holds `element_type` `0`.

## Difficulties

The window names a Donghae (Solo) `level` with the GAME sheet key
`LUA_MORNING_ATTRBOSS_DIFFICULTY_<level>` ("Calamity 1" for `0`) and the
two Hwanghae (Party) levels with the RESOURCE sheet keys
`PANEL_MORNING2_EASY` ("Normal", `0`) and `PANEL_MORNING2_HARD` ("Hard",
`1`); its radio buttons pass `0` and `1` to `difficultySelectMorning2`.

On client 3474 the stats split by difficulty:

| Rows                         | `offence_stat`, `defence_stat` | `min_ap`              |
| ---------------------------- | ------------------------------ | --------------------- |
| Donghae (Solo), levels 0 to 6 | Set on every row              | `0`                   |
| Donghae (Solo), levels 7 to 9 | `0`                           | `305` to `385`        |
| Hwanghae (Party)             | `0`                            | `0`                   |

## Field Names

No reference source has the file. It first appears on client 2519 (absent
on client 2107), so a private server's `DataSheets.bexcel`, `.xlsm` sheets
and server dump on client 1784 have no `Elemental` sheet or column, and the
2016 client and the client 519 server tables predate it.

The names follow the getters the client Lua of client 3474 calls on a row
(`panel_window_morningland_boss_all_1.luac`,
`panel_window_morningland_detailreward_all.luac`,
`panel_widget_monsterbar_renew.luac`): `getCharacterKeyRaw`, `getGroup`,
`getLevel`, `getElementalStatType`, `getIsBoss`,
`getMorningLandMonsterPartRaw`, `getUnlockConditionMentalCardKeyRaw`,
`getPosition`, `getMinAP`, `getOffenceStat` and `getDffenceStat`. Each
field matches its getter by value:

- `character_key` is the key the window passes to
  `getCharacterStaticStatusWarpper`; the names are the bosses of the official
  wiki pages "Black Shrine: Donghae (Solo)" and "Black Shrine: Hwanghae
  (Party)".
- `group` and `level` are the two arguments of
  `ToClient_getElementalMonsterInfo(group, level)`: the window walks groups
  `0` to `_MORNINGLAND_PART1_BOSSCOUNT - 1` for Donghae and on to
  `_MORNINGLAND_PART2_BOSSCOUNT - 1` for Hwanghae, levels `0` to `9` in the
  first and `0` to `1` in the second, which are the values the rows hold.
- `element_type` is the boss weakness of the window
  (`_frmBossWeeknessUV[getElementalStatType()]`), and its values match the
  weak auras of [Groups](#groups).
- `is_boss` and `show_reward_count` are `1` on the same 108 rows, one per
  group and difficulty, and each of those rows' `show_rewards` item is the
  boss's own reward box ("Boss Blitz Reward: Golden Pig King" `761555` on
  group `0`, "Boss Slayer's Haul - Jigwi (Normal)" `761337` on group `10`
  level `0`).
- `monster_part`: the window compares `getMorningLandMonsterPartRaw()` with
  `__eMorningLandMosterPart1` and `__eMorningLandMosterPart2`, whose values
  the client Lua does not hold; `1` sits on groups `0` to `9`, `2` on
  groups `10` to `16`.
- `unlock_mental_card_key`: the window reads it from level `0` of a group
  and names the knowledge in `LUA_MORNING_ATTRBOSS_LOCK` when the group is
  locked. Each group's key is its boss's "Tale of" knowledge (LOC type 34),
  on levels `0` to `4`.
- `unlock_character_key` has no getter in the Lua. On every one of its 20
  non-zero rows (client 3474) it is the boss of the same group one level
  lower, on levels `5` and `6` (Calamity 6 and 7). The official wiki page
  "Black Shrine: Donghae (Solo)" says "Calamity 6 to 10 bosses will only
  unlock if an Adventurer successfully defeats the boss of the previous
  level". On client 2519 the field held the lower boss on levels `5` to
  `9`, before Calamity 8 to 10 moved to `min_ap`.
- `min_ap` is the "At least {value} AP" line (`PANEL_MORNINGBOSS_LIMITAPVALUE`)
  of the window, which greys out the enter button below it. The official
  "[Update History] Black Shrine (Boss Blitz)" page lists "Displayed AP"
  requirements of 330 to 380 for Calamity 8 to 10, the range of the
  levels `7` to `9` rows.
- `offence_stat` and `defence_stat`: the monster bar of a developer client
  prints `getElementalStatType()`, `getOffenceStat()` and `getDffenceStat()`
  as "속성" (aura), "공" (attack) and "방" (defence). The two f32 values at
  `+0x0a` and `+0x0e` are the only fields left for them; their order is an
  Open Question.

## Notes

- Client 3474 has 1,000 rows and every `character_key` is unique. The 892
  rows with `is_boss` `0` are the other monsters of a fight and carry the
  group, level, weak aura and stats of their boss's fight; one of them,
  `21082` Imoogi, also has a position.
- `padding_04` is the 4 bytes between the u32 `item_key` and the 8-aligned
  i64 `count`. It holds `bf 00 00 00` on every entry here and `fc 7f 00 00`
  or `f7 7f 00 00` in [`elementalmonsterreward.bss`](elementalmonsterreward_bss.md),
  the leftover bytes of the tool that wrote the file.
- The 108 boss rows hold the same position on every difficulty of a group.
- Layout 2 (clients 3002 and 3251) stored the reward preview as item keys
  alone; Layout 3 (client 3474) adds the count and the padding.
- On client 2519 (Layout 1), levels `7` to `9` held an offence and defence
  like the lower levels (`1240` and `358` on the group `0` level `7` boss),
  and `unlock_mental_card_key` was set on level `0` alone. On clients 3002
  and 3251 it was also set on levels `7` to `9` of some groups.
- The handler (`_bss/elementalmonsterstat/`) links each `character_key` to
  its `characterstatic.dbss` row, names the unlock boss with its difficulty
  ("Gumiho (Calamity 6)"), the knowledge, the weak aura, the part and the
  difficulty with the window's own text, and shows a zero `min_ap` or
  unlock key as empty.
- The rewards a boss gives by its ranking are in
  [`elementalmonsterreward.bss`](elementalmonsterreward_bss.md), keyed by the
  same `character_key`. The server blessings of a defeated boss, by its
  `element_type`, are in [`elementalserverbuff.bss`](elementalserverbuff_bss.md),
  the aura stats of the player in [`elementalstat.bss`](elementalstat_bss.md).

## Open Questions

### Order of the Offence and Defence Stats

`offence_stat` (`+0x0a`) holds the larger value on every row (`1000` and
`233` on group `1` level `5`), `defence_stat` (`+0x0e`) the smaller. The
Lua getters `getOffenceStat` and `getDffenceStat` show only their names,
not their offsets. A boss offence near the 1,000 DP of ten Light Orbs (100
DP each) and a defence near their 500 AP (50 AP each) fit this order, but
only a developer client's monster bar line, or a fight that changes with
one orb, would confirm it.
