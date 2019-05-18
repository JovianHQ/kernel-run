import argparse
from kernel_run import create_kernel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()
    create_kernel(args.path)


if __name__ == '__main__':
    main()
