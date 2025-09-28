# Use a standard Ubuntu base image
FROM ubuntu:22.04

# Install base dependencies required by the harness
RUN apt-get update && apt-get install -y --no-install-recommends tmux asciinema && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Create the directory structure for the task
RUN mkdir -p service1 service2 logs

# Create the sample configuration and log files
RUN echo 'hostname=db-old.prod.local' > service1/settings.conf
RUN echo 'host = db-old.prod.local' > service2/database.ini
RUN echo 'server=cache-server.local' > service2/cache.conf
RUN echo '[INFO] Connection made to db-old.prod.local' > logs/access.log