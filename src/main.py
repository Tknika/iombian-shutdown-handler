#!/usr/bin/env python3

import logging
import os
import signal

from sub_client import SubClient

logging.basicConfig(format='%(asctime)s %(levelname)-8s - %(name)-16s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

CLIENT_PORT = 5556
TOPIC_FILTER = "system_button_event"
SHUTDOWN_EVENT = "long_click"


def button_event_callback(event):
    payload = event.replace(TOPIC_FILTER, '').strip()
    logger.debug(f"'{payload}' event received")
    if payload == SHUTDOWN_EVENT:
        os.system("poweroff")


def signal_handler(sig, frame):
    logger.info("Stopping IoMBian Shutdown Handler")
    client.stop()


if __name__ == "__main__":
    logger.info("Starting IoMBian Shutdown Handler")

    client = SubClient(topic_filter=TOPIC_FILTER, on_message_callback=button_event_callback, port=CLIENT_PORT)
    client.start()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()