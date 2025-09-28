#!/bin/bash

# Define variables for clarity
SEARCH_DIR="/app"
REPORT_FILE="/app/migration_report.txt"
OLD_HOSTNAME="db-old.prod.local"
NEW_HOSTNAME="db-new.prod.local"

# Ensure the report file is empty before starting
> "$REPORT_FILE"

# Find all .conf and .ini files, then filter for those containing the old hostname
find "$SEARCH_DIR" \( -name "*.conf" -o -name "*.ini" \) -type f -print0 | xargs -0 grep -l "$OLD_HOSTNAME" | while IFS= read -r file; do
    # 1. Create a backup of the original file
    cp "$file" "$file.bak"

    # 2. Replace the hostname in the original file
    sed -i "s/$OLD_HOSTNAME/$NEW_HOSTNAME/g" "$file"

    # 3. Add the absolute path of the modified file to the report
    readlink -f "$file" >> "$REPORT_FILE"
done