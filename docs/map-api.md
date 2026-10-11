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
height. North is +z. Pins live in memory and are gone when the app closes.

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | Set by the app |
| `type` | string | `player` or `marker` |
| `x`, `z` | number | World position in cm |
| `y` | number or null | Height in cm; not drawn |
| `label` | string | Up to 100 characters; the tooltip shows the type name when empty |
| `heading` | number or null | Degrees clockwise from north (+z), stored as 0 to 360; the pin is drawn as an arrow pointing that way, a dot when null |

| Type | Rule |
| --- | --- |
| `player` | At most one: placing a new one removes the old one |
| `marker` | Any number |

### Endpoints

| Method and path | Body | Answer |
| --- | --- | --- |
| `GET /api/map/pins` | | `200 {"pins": [pin, ...]}` |
| `POST /api/map/pins` | `{"type", "x", "z", "y"?, "label"?, "heading"?}` | `201 {"pin": pin}` |
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
```
