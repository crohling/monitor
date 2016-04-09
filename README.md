# Monitor
A simple TCP service monitor

# Setup
## Install Docker
https://docs.docker.com/engine/installation/

# Usage

## Building
`docker build -t monitor .`

## Running
`docker run --rm --env-file=<A_FILE_WITH_ENV_VARS> monitor:latest`

You can put this line in a crontab, and it should execute based on that schedule
