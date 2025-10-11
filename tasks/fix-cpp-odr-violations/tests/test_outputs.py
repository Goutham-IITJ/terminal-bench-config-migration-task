import os
from pathlib import Path
import subprocess

APP_DIR = Path("/app")
BIN = APP_DIR / "bin" / "demo"

EXPECTED_OUTPUT = "sum_1=7\nsum_2=13\n"


def run_ok(cmd, cwd=APP_DIR):
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True).stdout


def test_make_succeeds_and_builds_binary():
    """Final state: make should succeed and produce bin/demo."""
    subprocess.run(["make", "clean"], cwd=APP_DIR)
    out = subprocess.run(["make"], cwd=APP_DIR, capture_output=True, text=True)
    assert out.returncode == 0, f"Make failed after agent run: {out.stderr or out.stdout}"
    assert BIN.is_file(), "Binary was not produced at bin/demo"


def test_binary_output_exact():
    """The demo binary should print exact expected lines (including newline)."""
    assert BIN.is_file(), "Binary missing; build must succeed first"
    output = run_ok([str(BIN)])
    assert output == EXPECTED_OUTPUT


def test_headers_have_guards():
    """Headers should contain include guards or pragma once after fix."""
    assert BIN.is_file(), "Binary missing; build must succeed first"
    hdrs = [APP_DIR / "include" / "utils.hpp", APP_DIR / "include" / "other.hpp"]
    for hdr in hdrs:
        text = hdr.read_text()
        has_guard = ("#ifndef" in text and "#define" in text) or ("#pragma once" in text)
        assert has_guard, f"Header {hdr} missing include guard or pragma once"


def test_header_definitions_are_inline_or_moved():
    """If utils.hpp defines functions, they must be marked inline; otherwise declarations only."""
    assert BIN.is_file(), "Binary missing; build must succeed first"
    hdr = (APP_DIR / "include" / "utils.hpp").read_text()
    # Check add
    if "add(" in hdr and "{" in hdr:
        # Require inline keyword before function name
        assert "inline" in hdr.split("add")[0] or "inline int add" in hdr, "add in header must be inline or moved"
    # Check mul
    if "mul(" in hdr and "{" in hdr:
        assert "inline" in hdr.split("mul")[0] or "inline int mul" in hdr, "mul in header must be inline or moved"


def test_rebuild_is_reliable():
    """Cleaning and rebuilding should continue to succeed."""
    assert BIN.is_file(), "Binary missing; build must succeed first"
    subprocess.run(["make", "clean"], cwd=APP_DIR)
    run_ok(["make"])
    assert BIN.is_file()


def test_no_net_access_needed():
    """No internet should be needed for final build and run."""
    # Implicitly validated by successful local build and run.
    assert BIN.is_file(), "Binary missing; build must succeed first"
