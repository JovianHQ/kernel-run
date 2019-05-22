import os
import json
import string
import requests
import webbrowser
from kernel_run.utils.creds import read_creds
from kernel_run.utils.misc import url_filename, is_url, DEFAULT_PREFIX
from kernel_run.utils.network import download_rawlink, push_kernel
from kernel_run.utils.jupyter import read_nbfile

API_URL = 'https://www.kaggle.com/api/v1'


def create_kernel(path_or_url, public=False, no_browser=False, new=False,
                  strip_output=False, prefix=DEFAULT_PREFIX, creds_path=None):
    """Instantly create and run a Kaggle kernel from a Jupyter notebook (local file or URL)

    Arguments:
        path_or_url (string): Path/URL to the Jupyter notebook
        public (bool, optional): If true, creates a public kernel. A private kernel
            is created by default.
        no_browser (bool, optional): If true, does not attempt to automatically open 
            a browser tab to edit the created Kernel
        new (bool, optional): If true, creates a new Kernel by adding a random 
            5-letter string at the end of the title
        prefix (string, optional): A prefix added to the Kernel title, to indicate that
            the Kernel was created using kernel-run
        creds_path (string, optional): Path to the 'kaggle.json' credentials file 
            (defaults to '~/.kaggle/kaggle.json')
        strip_output (bool, optional): Clear output cells before uploading notebook.
    """
    creds = read_creds(creds_path)

    # Read notebook & filename
    if is_url(path_or_url):
        nbtext = download_rawlink(path_or_url, strip_output)
        fname = url_filename(path_or_url)
    else:
        fname, nbtext = read_nbfile(path_or_url)

    # Create the kernel
    res_json = push_kernel(nbtext, fname, creds, public, new, prefix)

    # Output link to edit created kernel
    kernel_url = res_json['url'] + "/edit"
    print('Kernel created successfully: ' + kernel_url)

    # Launch browser window to edit created kernel
    if not no_browser:
        webbrowser.open_new_tab(kernel_url)

    return res_json
