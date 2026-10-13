# `explorepointexperiencenew.bss` Format

## Purpose

Contribution EXP table: the contribution EXP a character needs for one more
contribution point, stepped by the contribution points it already holds. The
client shows this EXP as the bar next to the contribution points (`remained /
acquired`) on the main status and EXP gauge widgets.

Example (client 3464):

```text
0 points    95 EXP per point
300 points  5,057 EXP per point
600 points  3,745,996 EXP per point
```

The file is self-contained. All multi-byte values are little-endian.

## File Layout

No `PABR` magic and no trailer: a row count, then the rows, which fill the
file exactly (4 + 24 x 10 = 244 bytes on client 3464).

| Offset  | Type  | Field     | Notes                                       |
| ------- | ----- | --------- | ------------------------------------------- |
| `+0x00` | u32   | row_count | Number of rows; 24 on client 3464           |
| `+0x04` | row[] | rows      | `row_count` rows of 10 bytes, ascending `contribution_points` |

## Record Structure

### Row (10 bytes)

| Offset  | Type | Field               | Notes                                                        |
| ------- | ---- | ------------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | contribution_points | Acquired contribution points the row starts at               |
| `+0x02` | u64  | exp                 | Contribution EXP for each next point from `contribution_points` up to the next row's key (Notes) |

On client 3464 the keys are 0, then 50 to 600 in steps of 25, and the high
four bytes of `exp` are 0 in every row.

## Suggested UI Layout

| Column                         | Type | Notes                          |
| ------------------------------ | ---- | ------------------------------ |
| Contribution Points            | num  | `contribution_points`          |
| Contribution EXP to Next Point | num  | `exp`, with thousands separators |

## Notes

- Field names follow the client Lua (decompiled with unluac).
  `MainStatus:updateContribute()` in `panel_mainstatus_remaster.luac` and
  `contributePoint_UpdateFunc()` in `panel_selfplayerexpgage.luac` read
  `ToClient_getExplorePoint()` and show `getRemainedPoint() .. " / " ..
  getAquiredPoint()`, with the EXP bar at `explorePoint:getExperience_s64() /
  getRequireExplorationExperience_s64()`. The row key matches the range of
  `getAquiredPoint()` (total contribution points) and `exp` is the
  `getRequireExplorationExperience_s64()` value; the `_s64` getter is why
  `exp` is read as a u64 over the eight bytes after the key.
- The EXP restarts at 0 on every point: the bar divides the current EXP by
  the requirement for the next point, as the skill point tables do
  ([skillexperience](skillexperience_dbss.md)).
- Contribution EXP comes from quest rewards of type `__eRewardExploreExp`
  (`baseReward:getExploreExperience()` in `panel_window_questinfo_all_1.luac`).
- Curve on client 3464, as each row's `exp` over the row before it: 1.3x from
  50 to 175 points, 1.4x at 200 and 225, 1.5x at 250 and 275, 2.5x and 1.8x
  in turn from 300 to 425, 1.5x at 450 and 475, 1.378x at 500 and 1.6x from
  525 to 600.
- Each row is a step: its `exp` applies to every point from its key up to
  the next row's key, and the last row (600) to every point above it. The
  official [patch notes for the 11 September 2025 maintenance](https://www.naeu.playblackdesert.com/en-us/Adventure/History?_groupMasterNo=9108)
  list the
  required EXP per CP range above 500 as one value per 25-CP band (500 to
  525, 525 to 550, 550 to 575, 575 to 600), each about 1.6 times the band
  before, and call 600+ the "practical maximum limit". The rows at 525 to
  600 are 1.6x the row before on client 3464. The same notes say the 500 to
  525 band costs the same total EXP as the old single step from 500 to 501.
- Client 3464 has no `explorepointexperience.bss` without `new`; this is the
  only contribution EXP table in the PAZ index, so a file of the old name is
  not read by the current client.
