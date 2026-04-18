"""Entry point when running `uvicorn main:app` from the repo root."""

import sys
from pathlib import Path

_api_dir = Path(__file__).resolve().parent / "SYSTEM API"
if str(_api_dir) not in sys.path:
    sys.path.insert(0, str(_api_dir))

from Main import app  # noqa: E402

__all__ = ["app"]
