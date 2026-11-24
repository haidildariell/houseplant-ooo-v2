"""Entry for the Houseplant Out-of-Office bounty on make.fun.

Writes one out-of-office auto-reply, in the voice of a smug,
self-sufficient cactus, to /output/entry.txt.
"""

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120

# The reply, in the order a cactus would deliver it: the absence,
# the self-sufficiency, the brush-off, the verdict.
PARTS = (
    "Out of office.",
    "I packed my own water months ago.",
    "For urgent matters, contact a plant that needs you.",
    "I am not one.",
)


def build_line() -> str:
    line = " ".join(PARTS)
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    return line


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(build_line())


if __name__ == "__main__":
    main()
