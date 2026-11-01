"""The client version the loaded files are read as, for handlers that need it.

Most handlers tell a file's layout from the file itself (the first layout that
reads it to its end). A few cannot: the same bytes mean different things on
different clients, such as the quest type values of `totalquestcounttype.bss`.
Those ask `effective_client()`.

The core sets the value on folder load (`bdo_preview.set_handler_client`): the
`.meta` version of the folder. Reading it notes the `CLIENT` dependency, so the
parsed records disk cache re-parses only the tables whose build asked for it
when the client changes (`data_deps.py`).
"""

from __future__ import annotations

import bdo_preview

from _common.data_deps import CLIENT, note_read


def effective_client() -> int | None:
    """The client version handlers read the loaded folder as.

    None means no folder is loaded, or the exe predates `set_handler_client`;
    read the file as the live client then.
    """
    note_read(CLIENT)
    return unrecorded_client()


def unrecorded_client() -> int | None:
    """`effective_client()` without noting the `CLIENT` dependency.

    Only for code that notes a narrower dependency itself, such as the layout
    order of `client_versions.py`.
    """
    # A handler pack can run on an older exe whose core lacks the getter.
    getter = getattr(bdo_preview, "handler_client", None)
    return getter() if getter is not None else None
