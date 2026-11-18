"""Print a greeting."""

import argparse
import sys

from colorama import Fore, Style, just_fix_windows_console


def main(argv=None):
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("--name", default="world", help="who to greet (default: world)")
    parser.add_argument("--shout", action="store_true", help="print the greeting in red capitals")
    parser.add_argument("--times", type=int, default=1, metavar="N", help="print the greeting N times (default: 1)")
    args = parser.parse_args(argv)
    line = f"Hello, {args.name}"
    if args.shout:
        line = line.upper()
    out = line
    if args.shout and sys.stdout.isatty():
        just_fix_windows_console()
        out = f"{Fore.RED}{line}{Style.RESET_ALL}"
    print(" ".join([out] * args.times))
    return line


if __name__ == "__main__":
    main()
