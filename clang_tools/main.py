import sys
import argparse
from clang_tools.install import install_clang_tools


def parse_args(args):
    parser = argparse.ArgumentParser(prog='clang-tools')

    parser.add_argument(
        "-i",
        "--install",
        default="12",
        help="Install clang-tools with specific version. default is 12.",
    )

    parser.add_argument(
        "-d",
        "--directory",
        default="",
        help="The directory where is the clang-tools install.",
    )
    return parser.parse_args()


def main():
    args = parse_args(sys.argv[1:])

    version = args.install
    directory = args.directory
    install_clang_tools(version, directory)


if __name__ == '__main__':
    main()
