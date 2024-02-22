#!/usr/bin/env python3

import logging
import os
import signal

from sub_client import SubClient


SHUTDOWN_EVENT = os.environ.get("SHUTDOWN_EVENT", "long_click")
LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)

BUTTON_EVENTS_PORT= 5556
BUTTON_EVENTS_HOST = "iombian-button-handler"

logging.basicConfig(format='%(asctime)s %(levelname)-8s - %(name)-16s - %(message)s', level=LOG_LEVEL)
logger = logging.getLogger(__name__)


def button_event_callback(event):
    logger.debug(f"'{event}' event received")
    if event == SHUTDOWN_EVENT:
        os.system("systemctl poweroff")


def signal_handler(sig, frame):
    logger.info("Stopping IoMBian Shutdown Handler")
    client.stop()


if __name__ == "__main__":
    logger.info("Starting IoMBian Shutdown Handler")

    client = SubClient(on_message_callback=button_event_callback, port=BUTTON_EVENTS_PORT, host=BUTTON_EVENTS_HOST)
    client.start()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()
