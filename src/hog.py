#!/usr/bin/env python3
from typing import List

from utils import (
    parse_args,
    get_logcategory,
    get_filenames,
    print_logs,
    list_logcategories,
)


def main() -> None:
    args = parse_args()
    logcategories = list_logcategories()
    logcategory: str = get_logcategory(
        query=args.logcategory, logcategories=logcategories
    )
    filenames: List[str] = get_filenames(
        logcategory=logcategory, interval=args.interval
    )
    print_logs(filenames)


if __name__ == "__main__":
    main()
