"""Minimal example of a script with a main() entry point.

Run it directly:
    uv run scripts/example.py
"""


def main() -> None:
    """Print a greeting."""
    print("hello world")
    return None


# __name__ is "__main__" only when this file is run directly (e.g. `uv run
# scripts/example.py`), not when it's imported by another module. This
# guard keeps main() from running as a side effect of that import.
if __name__ == "__main__":
    main()
