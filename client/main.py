import logging
import os

import requests

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()


def main():
    server_url = os.environ.get("SERVER_URL")
    if server_url is None:
        logger.warning("defaulting Server URL (can be set via SERVER_URL environment variable")
        server_url = "http://server:5000"

    logger.info(f"Server URL: {server_url}")
    logger.info("sending request to server")

    request = f"{server_url}/forcast/?lat=51.5074&lng=0.1278"

    logger.info(f"request: {request}")

    response = requests.get(request)

    logger.info("response received")

    json = response.json()

    logger.info(json)
    logger.info("exiting")


if __name__ == '__main__':
    main()
