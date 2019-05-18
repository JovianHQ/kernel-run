# kernel-run

Create Kaggle kernels instantly from any Jupyter notebook.

Installation:

```
pip install kernel-run
```

The above command install a command-line tool called `kernel-run` which can be invoked from the terminal.

Usage:

Run the `kernel-run` command on your terminal/command prompt with a Jupyter notebook's path as the argument:

```
kernel-run path/to/jupyter/noteobook.ipynb
```

This will upload the notebook to your Kaggle account, create a private kernel, and launch the Kaggle web page where you can edit/run the kernel.

Note: To allow `kaggle-run` to upload the notebook to your Kaggle account, you need to download the Kaggle API credentials file `kaggle.json`. To download the 'kaggle.json' file:

1. Go to https://kaggle.com
2. Log in and go to your account page
3. Click the "Create New API Token" button in the "API" section
4. Move the downloaded `kaggle.json` file to the folder `~/.kaggle/`
