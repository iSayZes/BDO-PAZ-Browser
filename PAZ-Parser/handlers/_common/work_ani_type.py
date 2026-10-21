"""Names of the work animation types (`work_ani_type`), in value order from `0`.

The 2016 `gc::EWorkAniType` enum (the current client Lua has no copy), with
the member prefix dropped. `itemexchangesource.bss`, `plantzone.dbss` and
`buildingsource.bss` store the value.
"""

from __future__ import annotations

WORK_ANI_TYPE_NAMES: tuple[str, ...] = (
    "Mining",
    "Gather",
    "Cultivation",
    "Logging",
    "Making",
    "Architecture",
    "Hide",
    "HouseParty",
    "Breeding",
)

# `eWorkAniType_Count`: the value of a row without a work animation.
NO_WORK_ANI_TYPE = len(WORK_ANI_TYPE_NAMES)
