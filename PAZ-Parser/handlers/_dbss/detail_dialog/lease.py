"""Lease options: dialog actions that hand out an item for contribution points.

A lease option's action is `buyItemByPoint(item, 0, 1, 5, cost)`: the item key,
two fixed values, a fixed `5` and the contribution point cost. Full notes in
docs/file-formats/dbss/detail_dialog_dbss.md. `Lease` and its text live in
`_common/lease.py`.
"""

from __future__ import annotations

import re

from _common.lease import Lease

_LEASE_ACTION = re.compile(r"buyItemByPoint\((\d+),\s*\d+,\s*\d+,\s*\d+,\s*(\d+)\)", re.IGNORECASE)


def parse_lease(action: str) -> Lease | None:
    """The leased item and its cost, or None when the action leases nothing."""
    match = _LEASE_ACTION.search(action)
    if match is None:
        return None
    return Lease(item_id=int(match.group(1)), cost=int(match.group(2)))
