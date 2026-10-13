# Map API

While the app runs, other programs can put pins on the Map view through a
small HTTP API on the app's local server. A packet capture tool can move a
`player` pin to the character's live position, for example.

## Finding the Server

The app writes `%LOCALAPPDATA%\BDO-PAZ-Browser\local_server.json` when it
starts and deletes it when it closes normally. The file is always in that
folder, also when a portable exe keeps its Data Folder next to the exe.

```json
{
  "base_url": "http://127.0.0.1:52341",
  "port": 52341,
  "token": "kY3...",
  "pid": 18132
}
```

The port changes on every start, and so does the token. Read the file again
after the app restarts.

A crash or a killed process leaves the file behind, still naming the old port.
The next start overwrites it, so the file only misleads while the app is
closed. Before a connection error, check that process `pid` runs, and treat a
file whose `pid` is gone as "the app isn't running". On Windows,
`OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, pid)` failing with anything but
access denied, or `GetExitCodeProcess` returning something other than
`STILL_ACTIVE` (259), means the process is gone. Python's `os.kill(pid, 0)` is
no check on Windows: it terminates the process.

Every request sends the token as `Authorization: Bearer <token>`. The server
listens on 127.0.0.1 only and sends no CORS headers, so a web page in a
browser cannot call it.

## Pins

A pin has a world position in centimetres, the units of the game files and of
the map (`world_map.py`): `x` and `z` on the ground plane, `y` the optional
height. North is +z. Pins live in memory and are gone when the app closes,
except a pin placed with `"save": true`, which the app keeps in
`map_pins.json` in its Data Folder and shows again on the next start.

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | Set by the app; a saved pin keeps its id after a restart |
| `type` | string | `player` or `marker` |
| `x`, `z` | number | World position in cm |
| `y` | number or null | Height in cm; not drawn |
| `label` | string | Up to 100 characters; the tooltip shows the type name when empty |
| `heading` | number or null | Degrees clockwise from north (+z), stored as 0 to 360 |
| `icon` | string or null | A game icon from [Icons](#icons); null takes the type's icon |
| `saved` | boolean | In the answer: the pin comes back after a restart. Sent as `save` |

| Type | Rule | Icon without one | `save` |
| --- | --- | --- | --- |
| `player` | At most one: placing a new one removes the old one | `player` | Refused with `400`: it follows a live position |
| `marker` | Any number | None: a dot | Allowed |

A pin with an icon is drawn as that icon, upright. A pin without one is a dot,
or with a heading an arrow pointing that way. The `player` icon turns with the
heading, and faces north when the pin has none.

The Map view's Filters panel has a Player and a Markers chip, and a chip
stays disabled while no pin of its type exists. Markers start hidden until the
chip is switched on. Player turns on by itself each time a player pin appears
while none exists, so a new live position shows at once; switching it off
hides the pin until the next time one appears. The choices are saved in
`paz_config.json`.

Clicking a pin on the map opens its name, position and a Remove button, so a
pin can be removed without the API. Removing a saved pin removes it from
`map_pins.json` too.

### Icons

The icons are the game's own world map icons, built from the loaded client's
files together with the map tiles and kept with them in the cache folder. The
sheet and rectangle of each come from the world map's UI layout,
`ui_data/window/worldmap_grand/worldmap_grand_base.xml`, so a patch that moves
a sprite moves the icon with it on the next build. A node button has a dim
sprite and a bright one with a yellow outline; the icon is the bright one,
the more opaque of the two. An icon the client lacks draws as a dot.

| Icon | Layout control |
| --- | --- |
| `node` | `Button_Node_Normal` |
| `village` | `Button_Node_Village` |
| `city` | `Button_Node_City` |
| `gate` | `Button_Node_Gate` |
| `farm` | `Button_Node_Farm` |
| `trade` | `Button_Node_Trade` |
| `collect` | `Button_Node_Collect` |
| `quarry` | `Button_Node_Quarry` |
| `logging` | `Button_Node_Logging` |
| `dangerous` | `Button_Node_Dangerous` |
| `finance` | `Button_Node_Finance` |
| `fish_trap` | `Button_Node_FishTrap` |
| `minor_finance` | `Button_Node_MinorFinance` |
| `monopoly_farm` | `Button_Node_MonopolyFarm` |
| `craft` | `Button_Node_Craft` |
| `excavation` | `Button_Node_Excavation` |
| `dead` | `Static_DeadPosition` |
| `tent` | `Static_TentPosition` |
| `horse` | `Static_VehiclePosition` |
| `camel` | `Static_CamelPosition` |
| `elephant` | `Static_ElephantPosition` |
| `dragon` | `Static_Dragon` |
| `ship` | `Static_ShipPosition` |
| `party` | `Static_PartyPosition` |
| `bandit` | `Static_BanditPosition` |
| `whale` | `Static_WhalePosition` |
| `griffon` | `Static_GriffonPosition` |
| `bookmark` | `Static_BookMarkPosition` |
| `player` | The radar's own-character pointer, cut from `ui_texture/new_ui_common_forlua/widget/rader/radar_mine00.dds` without the view cone |

### Endpoints

| Method and path | Body | Answer |
| --- | --- | --- |
| `GET /api/map/pins` | | `200 {"pins": [pin, ...]}` |
| `POST /api/map/pins` | `{"type", "x", "z", "y"?, "label"?, "heading"?, "icon"?, "save"?}` | `201 {"pin": pin}` |
| `DELETE /api/map/pins/{id}` | | `204`, or `404` when there is no such pin |
| `DELETE /api/map/pins` | | `200 {"removed": n}`, every pin |
| `DELETE /api/map/pins?type=player` | | `200 {"removed": n}`, the pins of one type |

Errors answer with `{"error": "<reason>"}`: `400` for a bad body, `401` for a
missing or wrong token.

### Example

```python
import json
import os
import urllib.request
from pathlib import Path

info_file = Path(os.environ["LOCALAPPDATA"]) / "BDO-PAZ-Browser" / "local_server.json"
info = json.loads(info_file.read_text(encoding="utf-8"))

body = json.dumps({"type": "player", "x": 13800, "z": 76996, "label": "Me"}).encode()
request = urllib.request.Request(f"{info['base_url']}/api/map/pins", data=body, method="POST")
request.add_header("Authorization", f"Bearer {info['token']}")
request.add_header("Content-Type", "application/json")
print(json.load(urllib.request.urlopen(request)))
```

```bash
curl -X POST "$BASE_URL/api/map/pins" -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" -d '{"type": "player", "x": 13800, "z": 76996}'

# A saved marker with the tent icon
curl -X POST "$BASE_URL/api/map/pins" -H "Authorization: Bearer $TOKEN"   -H "Content-Type: application/json" -d '{"type": "marker", "x": 16000, "z": 77500, "icon": "tent", "save": true}'
```
