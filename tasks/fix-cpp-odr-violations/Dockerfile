FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    tmux \
    asciinema \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only build sources; DO NOT copy tests/ or solution.sh into the image
COPY include/ /app/include/
COPY src/ /app/src/
COPY Makefile /app/Makefile

# Build once to surface the ODR issue in default state
RUN make || true
