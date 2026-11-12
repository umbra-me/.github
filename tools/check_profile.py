"""Check the organisation profile: SVGs parse, and every asset the README links exists."""

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREFIX = "https://github.com/umbra-me/.github/raw/main/"


def main() -> int:
    errors = []
    for svg in sorted((ROOT / "profile" / "assets").glob("*.svg")):
        try:
            ET.parse(svg)
        except ET.ParseError as exc:
            errors.append(f"{svg.relative_to(ROOT)}: {exc}")
    readme = (ROOT / "profile" / "README.md").read_text(encoding="utf-8")
    for url in re.findall(r'src="([^"]+)"', readme):
        # Org profile pages do not resolve relative paths, so the README links
        # assets by absolute URL; map each one back to this checkout.
        if not url.startswith(PREFIX):
            errors.append(f"profile/README.md: unexpected image URL {url}")
        elif not (ROOT / url[len(PREFIX):]).is_file():
            errors.append(f"profile/README.md: missing asset {url[len(PREFIX):]}")
    for error in errors:
        print(error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
