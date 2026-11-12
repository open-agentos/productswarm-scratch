"""Print a greeting."""

import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.parse_args(argv)
    line = "Hello, world"
    print(line)
    return line


if __name__ == "__main__":
    main()
