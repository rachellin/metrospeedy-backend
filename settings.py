import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()

BACKEND_LINK = os.environ.get("BACKEND_LINK")
USERNAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")
ZIPS_LINK = os.environ.get("ZIPS_LINK")


