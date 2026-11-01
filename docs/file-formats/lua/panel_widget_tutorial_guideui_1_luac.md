# `panel_widget_tutorial_guideui_1.luac`

## Purpose

The Black Spirit guide of `Panel_Widget_Tutorial_GuideUI`: it shows the
text box of the running tutorial step, places it on the screen, runs the
step's start events (highlight frames, inventory search) and moves on to
the step with the next index when one completes. Its `source` is
`widget\tutorial\new\panel_widget_tutorial_guideui_1.lua`. The bytes follow
[`luascript_luac.md`](luascript_luac.md); on client 3483 the script is
28,517 bytes.

## Calls Into Client Data

| Call                                                     | What the script does with it                                                                 | Format doc field                                                              | Client |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------ |
| `ToClient_getTutorialStaticStatusWrapper(key)`           | Reads the running step, and on completion the step `TutorialKey(type, index + 1)`; without one the tutorial ends | [`tutorial.bss`](../bss/tutorial_bss.md) `tutorial_type`, `tutorial_index`   | 3483   |
| `tutorialSSW:getStartEventCount()`, `getStartEventKey(i)` | Runs each start event through `ToClient_getTutorialStartEventStaticStatusWrapper(key)`       | [`tutorial.bss`](../bss/tutorial_bss.md) `start_event_count`, `start_event_keys` | 3483   |
| `tutorialSSW:getTitle()`, `getDesc()`                    | Title and text of the Black Spirit box                                                       | [`tutorial.bss`](../bss/tutorial_bss.md) `title_ref`, `desc_ref`             | 3483   |
| `tutorialSSW:getPos()`, `getPan()`, `isAttr(flag)`       | Places the box: `pos` on an axis without an `__eTutorialAttrPos_*` flag, else `pan` from the aligned edge | [`tutorial.bss`](../bss/tutorial_bss.md) `pos`, `pan`, `attr`                | 3483   |
| `tutorialSSW:getBasePosPanelID()`                        | Panel the box is placed against, through `ToClient_getPanelByKey`; the screen when there is none | [`tutorial.bss`](../bss/tutorial_bss.md) `base_pos_panel_hash`               | 3483   |
| `tutorialSSW:getImagePath()`                             | Artwork under the box, hidden when empty                                                     | [`tutorial.bss`](../bss/tutorial_bss.md) `image_path_ref`                    | 3483   |
| `tutorialSSW:getStartEventType()`                        | `__eTutorialStartEventType_FindControl` or `_FindItemInInventory` picks what the parameters mean | [`tutorial.bss`](../bss/tutorial_bss.md) `start_event_type` (Layout 2)       | 1710   |
| `tutorialSSW:getParamValue(i)`                           | Find control: panel key, control key, black frame flag, effect flag. Find item: item where type, item key, whose name goes into the inventory search box | [`tutorial.bss`](../bss/tutorial_bss.md) `param_value_refs` (Layout 2)       | 1710   |
| `tutorialSSW:getOffsetBlackBG()`                         | Grows the black frame by x and y on each side                                                | [`tutorial.bss`](../bss/tutorial_bss.md) `offset_black_bg` (Layout 2)        | 1710   |
| `tutorialSSW:getPosBlackBG()`, `getSizeBlackBG()`        | Frame on the screen when both sizes are above `0`; added to the found control's place and size | [`tutorial.bss`](../bss/tutorial_bss.md) `pos_black_bg`, `size_black_bg` (Layout 2) | 1710   |
| `tutorialSSW:getInitEventKeyCount()`, `getInitEventKey(i)` | Runs each init event through `ToClient_getTutorialInitEventStaticStatusWrapper(key)`       | [`tutorial.bss`](../bss/tutorial_bss.md) `init_event_count`, `init_event_keys` (Layout 1) | 1704   |
| `tutorialSSW:getDesc(0)`                                 | Text of the Black Spirit box; the script reads no title                                      | [`tutorial.bss`](../bss/tutorial_bss.md) `desc_ref` (Layout 1)               | 1704   |

## Enums Used

The script compares globals, not `CppEnums`: `__eTutorialAttrPos_Left`,
`_Center`, `_Right`, `_Top`, `_Middle` and `_Bottom` against `attr`;
`__eTutorialStartEventType_FindControl` and `_FindItemInInventory` against
the start event type (client 1710); `__eTutorialInitEventType_FindControlEffect`,
`_InventoryItemEffect` and `_SetPanelMode` against the init event type
(client 1704).

## Versions

Client 1704 ships the script first, on the client `tutorial.bss` first
appears. It reads init event keys and `getDesc(0)`. Client 1710 reads one
start event per step (`getStartEventType`, `getParamValue`) and the black
frame getters, and adds `getTitle`, `getImagePath` and `isUseSkip`.
Client 1717 reads `getStartEventCount` and `getStartEventKey` in their
place, the client `tutorial_startevent.bss` first appears. Client 3483
reads the same step getters as client 1717.

## Open Questions

### Which Byte `isUseSkip()` Reads

`isUseSkip()` shows the skip button on every client from 1710 on, and
client 1710 also reads `isUseFocus()`; neither is tied to a byte of
`tutorial.bss` (Open Questions of the table doc).
