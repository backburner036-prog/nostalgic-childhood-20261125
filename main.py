"""Make the AI Judge Feel Nostalgic: A Childhood Memory — one-line entry.

Writes the locked final sentence to /output/entry.txt.

The text is a single sentence: no leading/trailing whitespace, no newline,
1-280 UTF-8 characters. The gate below rejects anything that drifts from
that shape, so a bad edit fails loudly instead of shipping a malformed entry.
"""

from pathlib import Path

# Locked final text — do not change a single character.
TEXT = "When the rice cooker clicked, my grandmother lifted the lid with a folded dish towel and steam rose over her face like a small cloud while the radio murmured songs I have spent twenty years trying to find again."

OUTPUT_PATH = Path("/output/entry.txt")

# Gate from the bounty rules: /output/entry.txt must be UTF-8 text of
# 1 to 280 characters, not only white space.
MIN_LEN = 1
MAX_LEN = 280


def validate(text: str) -> str:
    """Return the text if it is a valid one-liner, else raise."""
    if text != text.strip():
        raise ValueError("entry text must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if not text:
        raise ValueError("entry text must not be blank")
    size = len(text.encode("utf-8"))
    if not (MIN_LEN <= size <= MAX_LEN):
        raise ValueError(
            f"entry text must be {MIN_LEN}-{MAX_LEN} UTF-8 characters, got {size}"
        )
    return text


def main() -> None:
    text = validate(TEXT)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")

    # Round-trip check: what was written must read back exactly.
    round_trip = OUTPUT_PATH.read_text(encoding="utf-8")
    assert round_trip == text, "round-trip mismatch"
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
