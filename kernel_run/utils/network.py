import requests
from kernel_run.utils.jupyter import sanitize_nb
from kernel_run.utils.misc import gen_hash, slugify

API_URL = 'https://www.kaggle.com/api/v1'


class ApiError(Exception):
    """Error class for web API related Exceptions"""
    pass


def _pretty(res):
    """Make a human readable output from an HTML response"""
    return '(HTTP ' + str(res.status_code) + ') ' + res.content


def download_rawlink(link, strip_output=False):
    """Download a Jupyter notebook from a raw file link"""
    res = requests.get(link)
    if res.status_code == 200:
        return sanitize_nb(res.text, strip_output)
    else:
        raise ApiError(_pretty(res))


def push_kernel(text, fname, creds, public, new, prefix):
    """Push notebook text to Kaggle using the kernels API"""
    # Extract username & API key
    username, key = creds['username'], creds['key']

    # Create title and slug
    title = prefix + fname.replace('.ipynb', '')
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

    # Verify and return result
    if res.status_code != 200:
        raise ApiError(_pretty(res))
    return res.json()
