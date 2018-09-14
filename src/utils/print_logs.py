import gzip
from typing import List


def print_logs(filenames: List[str]) -> None:
    for filename in filenames:
        if filename.endswith(".gz"):
            with gzip.open(filename, "rt") as file:
                for line in file.read().split("\n"):
                    print(line)
        else:
            with open(filename) as file:
                print(file.read())
