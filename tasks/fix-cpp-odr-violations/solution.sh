#!/bin/bash
set -euo pipefail

# Fix ODR by moving definitions to a cpp file (or marking inline).
# We'll choose to move defs to src/utils.cpp and keep headers as declarations.

TASK_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$TASK_DIR"

# If already fixed, do nothing idempotently
if grep -q "int add(int a, int b) {" include/utils.hpp; then
  # Replace definitions with declarations
  sed -i 's/int add(int a, int b) { return a + b; }/int add(int a, int b);/' include/utils.hpp
  sed -i 's/int mul(int a, int b) { return a * b; }/int mul(int a, int b);/' include/utils.hpp

  # Create implementation file if missing
  if [ ! -f src/utils.cpp ]; then
    cat > src/utils.cpp <<'CPP'
#include "utils.hpp"

namespace util {

int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

}  // namespace util
CPP
  fi

  # Ensure Makefile rebuilds
  touch src/utils.cpp
fi

# Build
make

# Verify output
OUTPUT="$(./bin/demo)"
[ "$OUTPUT" = $'sum_1=7\nsum_2=13' ]
