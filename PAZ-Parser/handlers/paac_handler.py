from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from _paac.registration import register_paac_handlers


register_paac_handlers()
