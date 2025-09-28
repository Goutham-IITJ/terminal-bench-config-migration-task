# Terminal-Bench Task: Configuration File Migration

This repository contains a custom task developed for the Terminal-Bench assessment framework. The task simulates a real-world DevOps scenario where a script is needed to update database hostnames across multiple configuration files.

---

## 📝 Task Overview

The goal is to create a bash script that performs the following actions:

1.  **Searches** the `/app/` directory for `.conf` and `.ini` files.
2.  **Finds** all occurrences of the old hostname `db-old.prod.local`.
3.  **Replaces** it with the new hostname `db-new.prod.local`.
4.  **Backs up** every modified file with a `.bak` extension.
5.  **Generates** a report at `/app/migration_report.txt` listing the absolute paths of all modified files.

---

## ✅ Prerequisites

To run this task, you will need the following installed:

- Docker
- Python 3.12
- `uv` (the Python package manager from Astral)
- The `terminal-bench` framework itself.

---

## 🚀 How to Run

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Goutham-IITJ/terminal-bench-config-migration-task.git
    cd [terminal-bench-config-migration-task]
    ```

2.  **Install Dependencies (if not already installed):**
    _Ensure you are inside the `terminal-bench` project directory where its `pyproject.toml` is located._

    ```bash
    uv sync
    ```

3.  **Run the Tests:**
    The task can be validated using the `terminal-bench` harness.

    - **Test against the reference solution (should pass):**

      ```bash
      uv run tb run --agent oracle --task-id goutham-a-s-27-09-2025
      ```

    - **Test against a null agent (should fail, confirming tests work):**
      ```bash
      uv run tb run --agent nop --task-id goutham-a-s-27-09-2025
      ```
