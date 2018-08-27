import argparse
import re

from const import QUERY_RE_PATTERN, INTERVAL_RE_PATTERN


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Easily specify some log files and print their contents to stdout."
    )
    parser.add_argument(
        "logcategory", help="glob-like string to specify the log category"
    )
    parser.add_argument(
        "interval",
        nargs="?",
        default="0",
        help="specify which log files should be read",
    )
    args = parser.parse_args()
    if are_args_valid(args.logcategory, args.interval):
        return args
    else:
        raise Exception("Invalid args")


def are_args_valid(logcategory: str, interval: str) -> bool:
    return (
        re.match(QUERY_RE_PATTERN, logcategory) is not None
        and re.match(INTERVAL_RE_PATTERN, interval) is not None
    )
