# list available recipes
default:
    @just --list

# run the exercises test suite
test *args:
    uv run pytest {{args}}

# open the marimo menu to pick a notebook, reachable only on this machine
marimo:
    uvx marimo@latest edit --no-token --sandbox

# open the marimo menu to pick a notebook, reachable from any device on the Tailscale network
marimo-tailscale:
    uvx marimo@latest edit --no-token --sandbox --host 0.0.0.0 --headless
