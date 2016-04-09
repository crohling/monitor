#!/usr/bin/env python
import socket
import smtplib
import logging
from os import getenv

logging.basicConfig(level=logging.INFO)

ENV_VARS = [
    "SMTP_USERNAME",
    "SMTP_PASSWORD",
    "FROM_ADDR",
    "TO_ADDR",
    "CONNECTION_HOSTS",
    "SMTP_SERVER",
    "SUBJECT_LINE",
]

config = {}

def setup_config():
    for env_var in ENV_VARS:
        value = getenv(env_var)
        if not value:
            raise Exception("%s must be set as an environment variable" % env_var)
        config[env_var] = value
    indiv_connects = config["CONNECTION_HOSTS"].split(',')
    config["CONNECTION_HOSTS"] = [tuple(i.split(":")) for i in indiv_connects]

def connect_to_socket(host, port):
    try:
        s = socket.create_connection((host, port), 5)
        s.close()
        logging.info("Successfully connected to %s on port %s" % (host, port))
    except Exception as e:
        msg = "Was unable to connect to %s:%s because of error: %s" % (host, port, e)
        logging.error(msg)
        msg = "Subject: %s\n\n%s" % (config.get("SUBJECT_LINE") % (host, port), msg)
        send_mail(msg)

# The actual mail send
def send_mail(msg):
    server = smtplib.SMTP(config.get("SMTP_SERVER"))
    server.starttls()
    server.login(config.get("SMTP_USERNAME"), config.get("SMTP_PASSWORD"))
    server.sendmail(config.get("FROM_ADDR"), config.get("TO_ADDR"), msg)
    server.quit()

if __name__ == "__main__":
    setup_config()
    for host, port in config.get("CONNECTION_HOSTS"):
        logging.info("Connection to host %s:%s", host, port)
        connect_to_socket(host, port)
