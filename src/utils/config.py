import os
from dotenv import load_dotenv

load_dotenv()


def get_config(name):
    return os.getenv(name)


SQLITE_ADDRESS = get_config("SQLITE_ADDRESS")
