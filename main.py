"""The joke about the demo.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt and validates it against the competition gate
(UTF-8, 1-280 Unicode code points, not only whitespace) before writing.
Python 3.13 standard library only.
"""

from pathlib import Path

JOKE = "The demo crashed on stage, so my agent tried a different approach \u2014 the same code, minus the comments."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    code_points = len(text)
    if not 1 <= code_points <= 280:
        raise SystemExit(f"entry is {code_points} code points, must be 1-280")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {code_points} code points to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
