import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "PAZ-Parser"))

from bdo_app import main  # noqa: E402

if __name__ == "__main__":
    main()
