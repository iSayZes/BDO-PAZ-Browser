from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from _bss.registration import register_bss_handlers


register_bss_handlers()
