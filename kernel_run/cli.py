import argparse
from kernel_run import create_kernel

PUBLIC_MSG = "Create a public kernel"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_or_url', help="Path/URL of the Jupyter notebook")
    parser.add_argument(
        '--public', help=PUBLIC_MSG, action="store_true")
    parser.add_argument(
        '--new', help="Create a new kernel, if a kernel with the same name exists", action='store_true')
    parser.add_argument(
        '--no-browser', help="Don't open a browser window automatically", action="store_true")
    parser.add_argument(
        '--prefix', help="Prefix added to kernel title to easy identification (defaults to 'kr/')")
    args = parser.parse_args()
    create_kernel(args.path_or_url)


if __name__ == '__main__':
    main()
