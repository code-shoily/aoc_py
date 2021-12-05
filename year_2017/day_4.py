"""Advent of Code Year 2017, Day 4 - High-Entropy Passphrases

Problem Link: https://adventofcode.com/2017/day/4
"""
from typing import Any

from helpers.input import read_input_lines


def get_input_data() -> list[str]:
    return read_input_lines(__file__, 4)


def get_words_per_line(data: list[str]):
    """Gets words per line
    
    >>> get_words_per_line(['aa bb cc dd ee', 'bb cc dd'])
    [['aa', 'bb', 'cc', 'dd', 'ee'], ['bb', 'cc', 'dd']]

    """
    return list(map(lambda line: line.split(), data))


def find_duplicates(words: list) -> set:
    """Finds duplicates in a list of words
    
    >>> find_duplicates(['aa', 'bb', 'cc', 'dd', 'ee'])
    set()

    """
    return set(filter(lambda word: words.count(word) > 1, words))


def find_anagrams(words: list) -> set:
    """Finds duplicates in a list of words

    >>> find_anagrams(['ba', 'ba', 'cc', 'dd', 'ee'])
    {'ab'}

    >>> find_anagrams(['ba', 'ab', 'cc', 'dd', 'ee'])
    {'ab'}

    >>> find_anagrams(['cc', 'dd', 'ee'])
    set()

    """
    anagrams = set()
    visited = set()
    for i in words:
        sorted_word = "".join(sorted(i))
        if sorted_word in visited:
            anagrams.add(sorted_word)
        visited.add(sorted_word)

    return anagrams


def get_duplicates_in_sentences(sentences):
    """Gets the duplicate words for sentences"""
    return [find_duplicates(words) for words in sentences]


def get_anagrams_in_sentences(sentences):
    """Gets the duplicate words for sentences"""
    return [find_anagrams(words) for words in sentences]


def part_1() -> int:
    """Remove lines with duplicate words from data"""
    data = get_input_data()
    duplicates = get_duplicates_in_sentences(get_words_per_line(data))
    return len(list(filter(lambda i: not i, duplicates)))


def part_2() -> int:
    data = get_input_data()
    anagrams = get_anagrams_in_sentences(get_words_per_line(data))
    return len(list(filter(lambda i: not i, anagrams)))


def run():
    """
    Solution runner
    :return: The solutions of both parts of day 1 for year 2017

    >>> run()
    {'part_1': 455, 'part_2': 186}

    """
    return {
        "part_1": part_1(),
        "part_2": part_2()
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(run())
