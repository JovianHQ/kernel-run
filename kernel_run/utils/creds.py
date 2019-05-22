import os
import json

HOME = os.path.expanduser('~')
KAGGLE_DIR = HOME + '/.kaggle'
CREDS_FNAME = 'kaggle.json'
CREDS_PATH = KAGGLE_DIR + '/' + CREDS_FNAME

CREDS_MISSING_MSG = """ERROR: Could not find 'kaggle.json'! Make sure it's located in '""" + CREDS_PATH + """'.

To download the 'kaggle.json' file:
1. Go to https://kaggle.com     
2. Log in and go to your account page
3. Click the "Create New API Token" button in the "API" section
4. Move the downloaded 'kaggle.json' file to '""" + KAGGLE_DIR + """'
"""


class CredentialError(Exception):
    """Error class for credential related Exceptions"""
    pass


def creds_exist(path=CREDS_PATH):
    """Check if credentials file exits"""
    return os.path.exists(path)


def read_creds(path=CREDS_PATH):
    """Read the credentials file"""
    if path is None:
        path = CREDS_PATH
    if not creds_exist(path):
        raise CredentialError(CREDS_MISSING_MSG)
    with open(path, 'r') as f:
        return json.load(f)
