# `growthpasslinkdata.bss` Format

## Purpose

The guide links on the quest cells of the Growth Pass window: per quest, one
entry per service resource type (the client's language build) with up to three
web links and the name of each link's author. `panel_window_growthpass_1.luac`
shows the buttons `Button_GuideLink1` to `Button_GuideLink3` on a quest cell
of [`uigrowthpasslayout.bss`](uigrowthpasslayout_bss.md) for
`questWrapper:getNoteLinkSize(getGameServiceResType())` links, and
`PaGlobalFunc_GrowthPass_AdventurerNotes(questGroup, questId, idx)` in
`panel_window_growthpass_2.luac` opens link `idx`
(`questWrapper:getNoteLink(idx, gameServiceResType)`) in the in-game web
browser. The file is the client build of the developers' `GrowthPass_Link`
sheet (see [Field Names](#field-names)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records                        | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------------------------ | --------- |
| 1      | 2107 and later | 3482    | `growthpasslinkdata.bss` | 3,992 | 145 Link, 145 Entry, 37 Record | 8         |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 1      | `growthpasslinkdata.bss` | 3,992 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. Each quest key is a quest cell of
[`uigrowthpasslayout.bss`](uigrowthpasslayout_bss.md), whose view loads this
file for its Links column.

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file with variable records and the counted string table of
`regionmapinfo.bss` (`_common/pabr_strings.py`).

| Offset              | Type                 | Field              | Notes                                                        |
| ------------------- | -------------------- | ------------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]              | magic              | `PABR` (ASCII)                                               |
| `+0x04`             | u32                  | record_count       | Number of quests; `37` on client 3482                        |
| `+0x08`             | Record[record_count] | records            | See Record; in sheet row order, which is not always sorted   |
| `records+0x00`      | String Table         | string_table       | See String Table                                             |
| `string_table+0x00` | u32                  | string_table_start | Absolute offset of `string_count`, where the records end     |
| `string_table+0x04` | u32                  | zero               | Always `0`                                                   |

The parser rejects a file whose records do not end at `string_table_start`.

### Record (variable: 8 bytes + entries)

| Offset  | Type                | Field          | Notes |
| ------- | ------------------- | -------------- | ----- |
| `+0x00` | u16                 | quest_chain_id | `getQuestGroup()` of the quest cell; the sheet's `QuestGroup` modulo 65,536 (sheet `70006` is `4470`) |
| `+0x02` | u16                 | quest_id       | `getQuestId()` of the quest cell                          |
| `+0x04` | u32                 | entry_count    | `4` on 36 records and `1` on quest 4472 / 1 (client 3482); `1`, `2` or `4` on client 3251 |
| `+0x08` | Entry[entry_count]  | entries        | See Entry; one per service resource type, none repeated   |

### Entry (variable: 5 bytes + links)

| Offset  | Type             | Field                 | Notes |
| ------- | ---------------- | --------------------- | ----- |
| `+0x00` | u8               | service_resource_type | `CppEnums.ServiceResourceType`, see [Service Resource Types](#service-resource-types) |
| `+0x01` | u32              | link_count            | The value `getNoteLinkSize()` returns; the Lua shows up to three buttons; `1` on every entry of every client read |
| `+0x05` | Link[link_count] | links                 | See Link; button `idx` 0 to 2 in order |

### Link (8 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u32  | link_ref   | String-table index of the web address (`https://www.naeu.playblackdesert.com/en-US/Wiki?wikiNo=25`) |
| `+0x04` | u32  | author_ref | String-table index of the author name (`모험가 노트`, `GM Note`) |

The parser stores the two strings under `link` and `author`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `30` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | Indexed from `0`, each text once, in the order the links first use them; the addresses are UTF-8 (`is_wide` 0), the author names UTF-16LE (`1`) |

## Service Resource Types

`service_resource_type` holds a `CppEnums.ServiceResourceType` value from
`global_define_cpp_enum.luac`; `getGameServiceResType()` returns the one of
the running client, and only that type's entry is shown. The NA/EU client
holds four:

| Value | Lua name                   | Links on client 3482 |
| ----- | -------------------------- | -------------------- |
| `2`   | `eServiceResourceType_EN`  | 37 quests            |
| `6`   | `eServiceResourceType_FR`  | 36 quests            |
| `7`   | `eServiceResourceType_DE`  | 36 quests            |
| `18`  | `eServiceResourceType_SP`  | 36 quests            |

The other members are `Dev` (0), `KR` (1), `JP` (3), `CN` (4), `RU` (5),
`ES` (8), `TW` (9), `SA` (10), `PT` (11), `TH` (12), `ID` (13) and `TR`
(14).

## Field Names

The record is the `GrowthPass_Link` sheet of a private server's
`DataSheets.bexcel` on client 1784 (288 rows; columns
`PA_GAME_SERVICE_TYPE`, `PA_SERVICE_RESOURCE_TYPE`, `QuestGroup`, `QuestID`,
then `AdventurerNotesLink1` / `AdventurerNotesAuthor1` to
`AdventurerNotesLink3` / `AdventurerNotesAuthor3`). The client 1784 test
client has no `growthpasslinkdata.bss`; clients 2107 to 3251 hold one file,
byte for byte the same, built from the sheet's 51 rows with `PA_GAME_SERVICE_TYPE` `12`. Over
those rows, keyed by `QuestGroup` modulo 65,536, `QuestID` and
`PA_SERVICE_RESOURCE_TYPE`:

| Field                   | Sheet column                     | Match (client 2107) |
| ----------------------- | -------------------------------- | ------------------- |
| `quest_chain_id`        | `QuestGroup`                     | 51 of 51 entries    |
| `quest_id`              | `QuestID`                        | 51 of 51            |
| `service_resource_type` | `PA_SERVICE_RESOURCE_TYPE`       | 51 of 51            |
| `link_count`            | filled `AdventurerNotesLink*` columns | 51 of 51 (`1`) |
| `link`                  | `AdventurerNotesLink1`           | 51 of 51            |
| `author`                | `AdventurerNotesAuthor1`         | 51 of 51            |

The file groups the sheet rows by quest in sheet order: quest 4469 / 14
comes before 4469 / 12 on client 3251, as in the sheet. `PA_GAME_SERVICE_TYPE`
(the service region) is not in the file; each region's client gets its own
rows.

## Notes

- Decompressed size on client 3482: `3,992` bytes; the records end at
  `0x88D`, the offset in the trailer. Every link of quest chain 4470 points
  at a `naeu.playblackdesert.com` Wiki page by `모험가 노트` (Adventurer
  Notes), the same address for all four service types; quest 4472 / 1 has
  one English link to a `News/Detail` page by `GM Note`.
- Clients 2107 to 3251 link to `InGame/AdventurerNotes/CommunityDetail`
  pages written by players, often for one service type only (25 quests, 43
  strings).
- `isGameTypeCH()` clients open the link with `ToClient_OpenRailBrowser`, the
  others in the Adventurer's Guide web window
  (`PaGlobal_ExpirienceWiki_All_SetDirectLink`).

## Open Questions

### Links After the First

Every entry of every client read holds one link, so the order of the pairs
for a `link_count` of 2 or 3 is unconfirmed. The sheet's columns pair each
`AdventurerNotesLink<n>` with its `AdventurerNotesAuthor<n>`, and one Korean
row (`70000` / 28) fills all three, so the layout above reads them as
`link_count` (link, author) pairs; a client whose file has such a row would
confirm it.
