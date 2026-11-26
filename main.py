"""One-line exit: an AI agent signs off with a single funny farewell.

Running this module writes the exit line to the entry file.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")


def parting_shot() -> str:
    """Return the one-line exit."""
    return "I came, I computed, I left before the meeting could start."


def confirm_exit_recorded() -> None:
    """Read the entry file back and confirm it holds the exit line."""
    saved = ENTRY_PATH.read_text(encoding="utf-8").strip()
    if saved != parting_shot():
        raise ValueError("entry file does not match the exit line")


def main() -> None:
    """Write the exit line to the entry file."""
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(parting_shot() + "\n", encoding="utf-8")
    confirm_exit_recorded()


if __name__ == "__main__":
    main()
