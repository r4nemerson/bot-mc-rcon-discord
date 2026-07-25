"""
Config file
"""

import os

import loguru
from dotenv import load_dotenv


class Setup:
    """
    Setup application
    """

    def __init__(self):
        load_dotenv()

        self.configs = os.environ.items()

        try:
            self.rcon_host = os.environ["RCON_HOST"]
            self.rcon_port = int(os.environ["RCON_PORT"])
            self.rcon_password = os.environ["RCON_PASSWORD"]
            self.bot_token = os.environ["BOT_TOKEN"]

        except KeyError as e:
            loguru.logger.error(f"Missing environment variable: {e}")
            raise

        except ValueError as e:
            loguru.logger.error(f"Invalid value for environment variable: {e}")
            raise


setup = Setup()
