from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from _dbss.registration import register_dbss_handlers


register_dbss_handlers()
