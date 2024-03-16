#!/usr/bin/env python3

import logging
import os
import signal

from sub_client import SubClient
from communication_module import CommunicationModule


SHUTDOWN_EVENT = os.environ.get("SHUTDOWN_EVENT", "long_click")
LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)
BUTTON_EVENTS_PORT = int(os.environ.get("BUTTON_EVENTS_PORT", 5556))
BUTTON_EVENTS_HOST = os.environ.get("BUTTON_EVENTS_HOST", "127.0.0.1")
SHUTDOWN_SERVICE_HOST = os.environ.get("SHUTDOWN_HOST", "127.0.0.1")
SHUTDOWN_SERVICE_PORT = int(os.environ.get("SHUTDOWN_PORT", 5558))

SHUTDOWN_COMMAND = "shutdown"

logging.basicConfig(format="%(asctime)s %(levelname)-8s - %(name)-16s - %(message)s", level=LOG_LEVEL)
logger = logging.getLogger(__name__)


def button_event_callback(event):
    logger.debug(f"'{event}' event received")
    if event == SHUTDOWN_EVENT:
        logger.debug(f"Sending {SHUTDOWN_COMMAND} command to {SHUTDOWN_SERVICE_HOST}:{SHUTDOWN_SERVICE_PORT}")
        comm_module.execute_command(SHUTDOWN_COMMAND)


def signal_handler(sig, frame):
    logger.info("Stopping IoMBian Shutdown Handler")
    client.stop()
    comm_module.stop()


if __name__ == "__main__":
    logger.info("Starting IoMBian Shutdown Handler")

    client = SubClient(on_message_callback=button_event_callback, host=BUTTON_EVENTS_HOST, port=BUTTON_EVENTS_PORT)
    client.start()

    comm_module = CommunicationModule(host=SHUTDOWN_SERVICE_HOST, port=SHUTDOWN_SERVICE_PORT)
    comm_module.start()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()
