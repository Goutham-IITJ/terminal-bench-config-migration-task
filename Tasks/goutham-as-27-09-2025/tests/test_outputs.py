import os
from pathlib import Path

# --- Configuration ---
# Define paths and expected values for clarity and easy maintenance.
APP_DIR = Path("/app")
REPORT_FILE = APP_DIR / "migration_report.txt"
OLD_HOSTNAME = "db-old.prod.local"
NEW_HOSTNAME = "db-new.prod.local"

# Define the files that should have been modified.
MODIFIED_FILES = [
    APP_DIR / "service1/settings.conf",
    APP_DIR / "service2/database.ini",
]

# Define files that should NOT have been touched.
UNTOUCHED_FILES = [
    APP_DIR / "service2/cache.conf",
    APP_DIR / "logs/access.log",
]

# --- Test Cases ---

def test_report_file_exists():
    """Checks if the migration report was created."""
    assert REPORT_FILE.is_file(), f"Report file not found at {REPORT_FILE}"

def test_report_content():
    """Checks if the report contains the correct absolute paths of modified files."""
    assert REPORT_FILE.is_file(), f"Cannot check report content: file not found at {REPORT_FILE}"

    with open(REPORT_FILE, "r") as f:
        # Read paths and convert to a set to ignore order.
        reported_paths = set(line.strip() for line in f if line.strip())

    expected_paths = {str(p.resolve()) for p in MODIFIED_FILES}
    assert reported_paths == expected_paths, f"Report content mismatch. Expected {expected_paths}, but got {reported_paths}"

def test_files_were_modified():
    """Checks that the target files were correctly updated with the new hostname."""
    for file_path in MODIFIED_FILES:
        assert file_path.is_file(), f"Expected modified file not found: {file_path}"
        content = file_path.read_text()
        assert NEW_HOSTNAME in content, f"File {file_path} does not contain the new hostname."
        assert OLD_HOSTNAME not in content, f"File {file_path} still contains the old hostname."

def test_backups_were_created():
    """Checks that a .bak file was created for each modified file."""
    for file_path in MODIFIED_FILES:
        backup_path = file_path.with_suffix(file_path.suffix + ".bak")
        assert backup_path.is_file(), f"Backup file not found for {file_path}"
        # Verify the backup contains the original content.
        backup_content = backup_path.read_text()
        assert OLD_HOSTNAME in backup_content, f"Backup file {backup_path} has incorrect content."

def test_files_were_not_modified():
    """Checks that unrelated files were left untouched."""
    for file_path in UNTOUCHED_FILES:
        assert file_path.is_file(), f"An expected original file is missing: {file_path}"
        content = file_path.read_text()
        # Ensure the new hostname wasn't accidentally added.
        assert NEW_HOSTNAME not in content, f"File {file_path} was modified but shouldn't have been."
        # Check for backup files that shouldn't exist.
        backup_path = file_path.with_suffix(file_path.suffix + ".bak")
        assert not backup_path.exists(), f"A backup was incorrectly created for {file_path}"