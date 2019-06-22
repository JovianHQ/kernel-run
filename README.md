# `kernel-run` 🔥🚀

Instantly create and run a Kaggle kernel from any Jupyter notebook (local file or URL).

![kaggle-run-demo](https://i.imgur.com/KsrIYH3.gif)

```
$ pip install kernel-run --upgrade

$ kernel-run path/to/notebook.ipynb
Kernel created successfully: https://www.kaggle.com/aakashns/kr-notebook/edit

$ kernel-run http://cs231n.stanford.edu/notebooks/pytorch_tutorial.ipynb
Kernel created successfully: https://www.kaggle.com/aakashns/kr-pytorch-tutorial/edit
```

`kernel-run` uploads the Jupyter notebook to a private kernel in your Kaggle account, and launches a browser window so you can start editing/executing the code immediately.

## Installation

```
pip install kernel-run --upgrade
```

The above command install a command-line tool called `kernel-run` which can be invoked from the terminal/command prompt.

Note: To allow `kaggle-run` to upload the notebook to your Kaggle account, you need to download the [Kaggle API credentials file `kaggle.json`](https://github.com/Kaggle/kaggle-api#api-credentials). To download the `kaggle.json` file:

1. Go to https://kaggle.com
2. Log in and go to your account page
3. Click the "Create New API Token" button in the "API" section
4. Move the downloaded `kaggle.json` file to the folder `~/.kaggle/`

## CLI Usage & Options

Run the `kernel-run` command on your terminal/command prompt with a Jupyter notebook's path (or URL) as the argument:

```
$ kernel-run path/to/notebook.ipynb
Kernel created successfully: https://www.kaggle.com/aakashns/kr-notebook/edit

$ kernel-run http://cs231n.stanford.edu/notebooks/pytorch_tutorial.ipynb
Kernel created successfully: https://www.kaggle.com/aakashns/kr-pytorch-tutorial/edit
```

There are various options you can configure. Run `kernel-run -h` to see the options:

```
usage: kernel-run notebook_path_or_url [-h] [--public] [--new] [--no-browser] [--strip-output] [--prefix PREFIX]

positional arguments:
  notebook_path_or_url  Path/URL of the Jupyter notebook

optional arguments:
  -h, --help            show this help message and exit
  --public              Create a public kernel
  --new                 Create a new kernel, if a kernel with the same name exists
  --no-browser          Don't open a browser window automatically
  --strip-output        Clear output cells before uploading notebook (useful for large files)
  --prefix PREFIX       Prefix added to kernel title to easy identification (defaults to 'kr/')
```

## Python API

You can also use the library form a Python script or Jupyter notebook. It can be imported as `kernel_run`.

```python
from kernel_run import create_kernel

create_kernel('path/to/notebook.ipynb', public=True, no_browser=True)
# Kernel created successfully: https://www.kaggle.com/aakashns/kr-notebook/edit
```

The arguments to `create_kernel` are identical to the CLI options:

```python
def create_kernel(path_or_url, public=False, no_browser=False, new=False,
                  strip_output=False, prefix='kr/', creds_path=None):
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
```

## Credits

Developed with love by the Jovian team ( https://www.jvn.io )! Contributions welcome.
