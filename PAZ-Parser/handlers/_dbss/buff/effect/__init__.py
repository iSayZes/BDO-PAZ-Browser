"""Effect text and Param column labels of a buff, read from its parameters.

The parameters are the applied value; the name and the description can both
be stale (see docs/file-formats/buff_dbss.md). Only the effect types whose
parameters are confirmed, against the English LOC type 5 text, item names or
bdocodex tooltips, get a text, in the game's own wording (`Life EXP +15%`);
every other type yields ''. Some types name what their parameters point at
from LOC (`Summon Rock Golem`), and types 1 and 4 also read the buff's tick
interval and condition.

- `formats.py`: what each type's parameters mean, one entry per type.
- `named.py`: the types whose parameters name something in LOC.
- `render.py`: the Effect text and the Param labels from those entries.
- `units.py`: how amounts are scaled and written.
- `type_names.py`: the 2016 client's names of the effect types.

Kept out of `handler.py` so the tests can import it (see "Unit Tests" in
docs/handler.md).
"""

from .render import EffectInput, effect_text, param_labels
from .type_names import EFFECT_TYPE_NAMES, effect_type_text

__all__ = ["EFFECT_TYPE_NAMES", "EffectInput", "effect_text", "effect_type_text", "param_labels"]
