#!/usr/bin/env python3
from typing import List

from utils.args import parse_args
from utils.get_filenames import get_filenames
from utils.get_logcategory import list_logcategories, get_logcategory
from utils.print_logs import print_logs


def main() -> None:
    args = parse_args()
    logcategories = list_logcategories()
    logcategory: str = get_logcategory(
        query=args.logcategory, logcategories=logcategories
    )
    filenames: List[str] = get_filenames(
        logcategory=logcategory, interval=args.interval
    )
    print_logs(logcategory, filenames)


if __name__ == "__main__":
    main()
