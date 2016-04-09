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

### Env Vars
```
SMTP_SERVER=(default is "smtp.gmail.com:587")
SUBJECT_LINE=(default is "Connection error for %s:%s")
SMTP_USERNAME=
SMTP_PASSWORD=
FROM_ADDR=
TO_ADDR=
CONNECTION_HOSTS=(This is a comma separated list of strings of the format "host:port")
```
