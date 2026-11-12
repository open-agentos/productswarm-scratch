"""Print a greeting."""

import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("--shout", action="store_true", help="print the greeting in capitals")
    args = parser.parse_args(argv)
    line = "Hello, world"
    if args.shout:
        line = line.upper()
    print(line)
    return line


if __name__ == "__main__":
    main()
