import os
import json
import random
import string
import re
import requests
import webbrowser

API_URL = 'https://www.kaggle.com/api/v1'

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


def creds_exist():
    """Check if credentials file exits"""
    return os.path.exists(CREDS_PATH)


def read_creds():
    """Read the credentials file"""
    with open(CREDS_PATH, 'r') as f:
        return json.load(f)


def log_creds_missing():
    print(CREDS_MISSING_MSG)


def gen_hash(len=5):
    return ''.join([random.choice(string.ascii_lowercase + string.digits) for _ in xrange(len)])


def slugify(title):
    return re.sub(r'\W+', '-', title.lower()).replace('_', '-')


def create_kernel(path, public=False, no_browser=False, new=False, prefix='kr/'):
    """Instantly create and run a Kaggle kernel using a local Jupyter notebook file

    Arguments:
        path (string): Path to the Jupyter notebook to be uploaded.
        public (bool, optional): If true, creates a public kernel. A private kernel
            is created by default.
        no_browser (bool, optional): If true, does not attempt to automatically open 
            a browser tab to edit the created Kernel
        new (bool, optional): If true, creates a new Kernel by adding a random 
            5-letter string at the end of the title. 
        prefix (bool, optional): A prefix added to the Kernel title, to indicate that
            the Kernel was created using kernel-run.

    """
    # Read credentials
    if creds_exist():
        creds = read_creds()
        username = creds['username']
        key = creds['key']
    else:
        log_creds_missing()
        return

    # Detect file & filename
    if os.path.exists(path):
        fname = os.path.basename(path)
        if not fname.endswith(".ipynb"):
            print("""ERROR: Invalid file '""" + fname +
                  """'. Please provide a Jupyter notebook with '.ipynb' extension.""")
            return
        else:
            with open(path) as f:
                text = f.read()
    else:
        print("""ERROR: No such file or directory: '""" + path + "'")
        return

    # Create title and slug
    title = prefix + fname[:-6]
    if new:
        # Add a random hash at the end of the kernel
        title += "-" + gen_hash()
    slug = username + "/" + slugify(title)

    # Create the request payload
    body = {
        'newTitle': title,
        'enableGpu': 'true',
        'language': 'python',
        'competitionDataSources': [],
        'text': text,
        'kernelDataSources': [],
        'categoryIds': [],
        'enableInternet': 'true',
        'kernelType': 'notebook',
        'isPrivate': 'false' if public else 'true',
        'datasetDataSources': [],
        'slug': slug
    }

    # Execute the API request
    res = requests.post(API_URL + '/kernels/push',
                        auth=(username, key),
                        json=body,
                        headers={'Content-Type': 'application/json'})

    # Parse and verify result
    res_json = res.json()
    if res.status_code == 200:
        kernel_url = res_json['url'] + "/edit"
        print('Kernel created successfully: ' + kernel_url)
        if not no_browser:
            # Launch browser window to edit created kernel
            webbrowser.open_new_tab(kernel_url)
    else:
        print(res_json)

    return res.status_code, res_json
