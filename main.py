#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — Quibbleford.

A single deadpan TV meteorologist forecast for a city that does not
exist, delivered as a deterministic program: it writes exactly the
forecast line to /output/entry.txt and prints it to stdout, with no
trailing newline on either.

The joke's mechanism is deadpan escalation: the line opens as a flat,
factual forecast (temperature, drizzle, wind speed) and then treats a
lawsuit between weather phenomena — fog suing the sun for defamation —
as one more routine probability, stated in the same neutral register
as the 90% figure. The absurdity is never signalled; it is reported
like weather.
"""

import os

# The forecast: a high of 14 degrees, light drizzle, 20 km/h winds,
# and a 90% chance the fog sues the sun for defamation before noon.
# Deadpan delivery, one line, 147 characters.
LINE = "In Quibbleford, expect a high of 14 degrees, light drizzle and winds of 20 km/h, with a 90% chance the fog sues the sun for defamation before noon."


MAX_CHARS = 160


def get_line() -> str:
    """Return the entry line, exactly as sealed."""
    return LINE


def output_dir() -> str:
    """Output directory, overridable via MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(line: str) -> None:
    """Write the line to <output_dir>/entry.txt, no trailing newline."""
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


def validate_line(line: str) -> None:
    """Gate: the entry must be 1-160 chars, a single clean line with
    no leading or trailing whitespace. Fail loudly here rather than
    ship an invalid entry."""
    assert 1 <= len(line) <= MAX_CHARS, "line must be 1-160 characters"
    line.encode("utf-8")
    assert line.strip() == line, "no leading or trailing whitespace"
    assert "\n" not in line and "\r" not in line, "must be a single line"


def main() -> None:
    line = get_line()
    validate_line(line)
    try:
        write_entry(line)
    except OSError:
        pass
    print(line, end="")


if __name__ == "__main__":
    main()
