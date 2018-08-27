import os
from typing import List, Iterator

from const import SCRIBE_ROOT


def list_logcategories() -> List[str]:
    return os.listdir(SCRIBE_ROOT)


def get_logcategory(query: str, logcategories: List[str]) -> str:
    query_words: List[str] = query.split("-")
    logcategories_with_n_words: Iterator[str] = filter(
        lambda logcategory: len(_get_words_from_name(logcategory)) == len(query_words),
        logcategories,
    )
    matching_logcategories = list(
        filter(
            lambda logcategory: does_name_match_pattern(
                name=logcategory, pattern=query_words
            ),
            logcategories_with_n_words,
        )
    )
    if len(matching_logcategories) == 0:
        raise Exception("no matching log category found")
    elif len(matching_logcategories) > 1:
        raise Exception("multiple matching log categories found")
    else:
        return matching_logcategories[0]


def does_name_match_pattern(name: str, pattern: List[str]) -> bool:
    words = _get_words_from_name(name)
    pattern_words_by_length = sorted(pattern, key=lambda w: -len(w))
    try:
        for pattern_word in pattern_words_by_length:
            words = get_word_list_without_matching_word(words, pattern_word)
    except Exception:
        return False
    else:
        return True


def get_word_list_without_matching_word(
    word_list: List[str], word_prefix: str
) -> List[str]:
    for i, word in enumerate(word_list):
        if word.startswith(word_prefix):
            word_list_without_matching_word = word_list[:i] + word_list[i + 1 :]
            return word_list_without_matching_word
    raise Exception("word prefix not found in word list")


def _get_words_from_name(name: str) -> List[str]:
    return name.replace("_", "-").split("-")
