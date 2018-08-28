import os
from typing import List, Tuple, Optional

from const import SCRIBE_ROOT


def list_logfiles(directory: str) -> List[str]:
    return list(
        filter(
            lambda filename: filename != directory + "_current", os.listdir(directory)
        )
    )


def get_filenames(logcategory: str, interval: str) -> List[str]:
    filenames = list_logfiles(SCRIBE_ROOT + "/" + logcategory)
    return select_filenames_for_interval(filenames, interval)


def select_filenames_for_interval(filenames: List[str], interval: str) -> List[str]:
    if ":" in interval:
        start_index, end_index = _get_indexes_for_interval(*interval.split(":"))
        return filenames[start_index:end_index]
    else:
        index = _get_index_for_single(interval)
        return [filenames[index]]


def _get_index_for_single(specifier: str) -> int:
    return int(specifier)


def _get_indexes_for_interval(
    start_specifier: str, end_specifier: str
) -> Tuple[Optional[int], Optional[int]]:
    start_index = int(start_specifier) if start_specifier != "" else None
    end_index = int(end_specifier) + 1 if end_specifier != "" else None
    if end_index == 0:
        end_index = None
    return start_index, end_index
