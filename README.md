# Python Precourse

[![Open with marimo](https://marimo.io/shield.svg)](https://molab.marimo.io/)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/drive/u/0/folders/19UCqFNGHW__DGDzOHMjPInEKhFXkhhul)

1 Python Basics [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1psEqjZHw6ETwG4rxuaBJ98PnrQOglhSB)
2 Python Essentials [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12mLPIQ29SC555kODibm_OQBqjvLOWH_P)

## Setup

### 1. Install `git` and `gh`

- [`git`](https://git-scm.com/downloads) — version control, needed to clone and work with this repo.
- [`gh`](https://cli.github.com/) — the GitHub CLI, useful for cloning, opening PRs, etc. from the terminal.

### 2. Install `uv`

[`uv`](https://docs.astral.sh/uv/) manages the Python environment (dependencies, venv, running the notebook in a sandbox).

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once `uv` is installed, set up the project's virtual environment (reads `pyproject.toml`/`uv.lock`):

```bash
uv sync
```

### 3. Install `just`

[`just`](https://just.systems/) is the task runner used to launch the project's commands (tests, notebook). Once `uv` is installed, you can run it directly without a separate install:

```bash
uvx --from rust-just just
```

If you'd rather have `just` always available on your `PATH` without going through `uvx` every time:

```bash
uv tool install rust-just
```

## `just` commands

From the repo root:

```bash
just
```
Lists all available recipes (the default command, no arguments).

```bash
just test
```
Runs the test suite in `tests/` with `pytest` (via `uv run pytest`), checking the exercises in `src/`.

```bash
just test -k second_largest
```
Passes extra arguments through to `pytest` (e.g. filter by test/function name, `-v` for verbose output, a specific path, etc.).

```bash
just marimo
```
Opens the marimo menu in your browser, locally (`127.0.0.1`), from which you can pick a notebook to create or edit (e.g. `presentations/1_Python_Basics.py`). The notebook runs in a sandbox: dependencies are read from the file's inline metadata, no manual install needed.

```bash
just marimo-tailscale
```
Same as above, but the marimo server listens on all interfaces (`0.0.0.0`), so it's reachable from any device on your Tailscale network (useful when working via SSH on a remote machine). Runs headless: it won't try to open a local browser.


## Project structure

### `presentations/`

Contains the course slides as a [marimo](https://marimo.io) notebook:

- `1_Python_Basics.py` — the notebook itself (336 cells). It's a plain Python file with dependencies declared inline (PEP 723) at the top of the file, so it's reproducible without a separate `requirements.txt`.
- `layouts/1_Python_Basics.slides.json` — the presentation configuration (which cells are `slide`, `sub-slide`, `fragment`, whether to show code, etc.), linked to the notebook via `layout_file` in `app = marimo.App(...)`.

### `src/`

One Python module per topic covered in the presentation (`variables_types.py`, `lists.py`, `functions.py`, `classes.py`, etc.). Each file contains functions/classes with a `# TODO` and `raise NotImplementedError(...)` in place of the implementation — that's where course participants write their own code.

### `tests/`

One test file per module in `src/` (same name, `test_` prefix). A test file only passes once every `NotImplementedError` in the matching `src/` module has been replaced with working code — this is how you check you've correctly solved each exercise.

### `solutions/`

A worked implementation of every exercise in `src/`, one module per topic with the same names and function signatures. Each solution has been verified against the full test suite (`just test`) before being committed. Use it to check your own approach or to unblock yourself if you're stuck; try to solve the exercise in `src/` first.

### `scripts/`

Small standalone scripts, each with a `main()` function guarded by `if __name__ == "__main__":` so the file can also be imported without running anything. Run one directly with:

```bash
uv run scripts/example.py
```

### Root files

- `pyproject.toml` — project metadata and dependencies (currently just `pytest`), plus the pytest configuration (`testpaths = ["tests"]`) so `pytest`/`uv run pytest` knows where to look.
- `.python-version` — pins the exact Python version (`3.14`) `uv` uses for this project's virtual environment, so everyone gets the same interpreter instead of whatever happens to be newest. Set with `uv python pin <version>`.
- `uv.lock` — the exact, resolved versions of every dependency, generated and updated automatically by `uv`. Commit it (don't edit it by hand) so everyone gets the same environment.
- `justfile` — the recipes behind the `just` commands described above.
- `LICENSE` — MIT license.
- `.gitignore` — excludes local/disposable artifacts (`.venv/`, `__pycache__/`, `.pytest_cache/`, etc.) from version control. It also currently excludes `solutions/`, so the worked solutions aren't published to the repo for now; remove that line once you're ready to share them.
- `README.md` — this file.
