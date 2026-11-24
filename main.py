#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters — one loading-screen tip.

Writes exactly one single-line tip (1-200 chars, UTF-8) to
/output/entry.txt.

The tip: the agent has read the same error three times, and the
tired developer watching the loading screen should not interrupt —
the agent is not stuck, it is stalling while it works out how to
tell the human it has no idea. The joke is about both of them at
once: the human waiting, and the agent looping on one error.
"""

import os

# --- beats ---------------------------------------------------------------
SETUP = "Tip: your agent has read the same error three times now."
ADVICE = "Do not interrupt —"
PUNCH = "it is not stuck, it is stalling while it works out how to tell you it has no idea."

MAX_CHARS = 200


def entry_text():
    """Build the single-line tip from its beats."""
    return "{} {} {}".format(SETUP, ADVICE, PUNCH)


def validate(text):
    """The sealed scorer's gate: 1-200 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "same error" not in text:
        raise ValueError("entry must keep its subject")
    text.encode("utf-8")
    return True


def run_checks():
    """Self-test the entry the way the sealed scorer gates it."""
    text = entry_text()
    validate(text)
    assert len(text) == 158, "expected 158 chars, got %d" % len(text)
    assert text == ("Tip: your agent has read the same error three times now. "
                    "Do not interrupt — it is not stuck, it is stalling while "
                    "it works out how to tell you it has no idea."), "the line drifted: %r" % text
    assert text.count(".") == 2, "expected 2 sentences, got %d" % text.count(".")
    assert text.startswith("Tip: "), "the line must read as a loading-screen tip"
    return True


def main():
    text = entry_text()
    validate(text)
    run_checks()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
