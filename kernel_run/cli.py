import argparse
from argparse import RawTextHelpFormatter
from kernel_run import create_kernel
from kernel_run.utils.misc import DEFAULT_PREFIX

CLI_DESC = """Instantly create and run a Kaggle kernel from a Jupyter notebook (local file or URL). Examples:
$ kernel-run path/to/jupyter_notebook.py
$ kernel-run https://raw.githubusercontent.com/aakashns/deep-learning-workbook/master/examples/00_mnist_basic.ipynb
"""

PUBLIC_MSG = "Create a public kernel"
NEW_MSG = "Create a new kernel, if a kernel with the same name exists"
BROWSER_MSG = "Don't open a browser window automatically"
PREFIX_MSG = "Prefix added to kernel title to easy identification (defaults to 'kr/')"
OUTPUT_MSG = "Clear output cells before uploading notebook"


def main():
    parser = argparse.ArgumentParser(
        description=CLI_DESC, formatter_class=RawTextHelpFormatter)
    parser.add_argument('notebook_path_or_url',
                        help="Path/URL of the Jupyter notebook")
    parser.add_argument('--public', help=PUBLIC_MSG, action="store_true")
    parser.add_argument('--new', help=NEW_MSG, action='store_true')
    parser.add_argument('--no-browser', help=BROWSER_MSG, action="store_true")
    parser.add_argument('--strip-output', help=OUTPUT_MSG, action="store_true")
    parser.add_argument('--prefix', help=PREFIX_MSG, default=DEFAULT_PREFIX)
    args = parser.parse_args()
    create_kernel(path_or_url=args.notebook_path_or_url,
                  public=args.public,
                  no_browser=args.no_browser,
                  new=args.new,
                  strip_output=args.strip_output,
                  prefix=args.prefix)


if __name__ == '__main__':
    main()
