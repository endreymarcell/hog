import gzip
from typing import List
from os.path import join


def print_logs(logcategory: str, filenames: List[str]) -> None:
    for filename in filenames:
        if filename.endswith(".gz"):
            with gzip.open(join(logcategory, filename), "rt") as file:
                for line in file.read().split("\n"):
                    print(line)
        else:
            with open(join(logcategory, filename)) as file:
                print(file.read())
