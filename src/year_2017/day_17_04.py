"""Advent of Code Year 2017, Day 4 - High-Entropy Passphrases

Problem Link: https://adventofcode.com/2017/day/4
Difficulty: XS
Tags: string
"""

from helpers.input import read_input_lines


def get_words_per_line(data: list[str]):
    """Gets words per line

    >>> get_words_per_line(['aa bb cc dd ee', 'bb cc dd'])
    [['aa', 'bb', 'cc', 'dd', 'ee'], ['bb', 'cc', 'dd']]

    """
    return list(map(lambda line: line.split(), data))


def has_duplicates(words: list) -> bool:
    """Finds duplicates in a list of words

    >>> has_duplicates(['aa', 'bb', 'cc', 'dd', 'ee'])
    False

    >>> has_duplicates(['aa', 'bb', 'cc', 'dd', 'aa'])
    True

    """
    return any(filter(lambda word: words.count(word) > 1, words))


def has_anagrams(words: list) -> bool:
    """Finds duplicates in a list of words

    >>> has_anagrams(['ba', 'ba', 'cc', 'dd', 'ee'])
    True

    >>> has_anagrams(['ba', 'ab', 'cc', 'dd', 'ee'])
    True

    >>> has_anagrams(['cc', 'dd', 'ee'])
    False

    """
    return len({"".join(sorted(word)) for word in words}) != len(words)


def get_duplicates_in_sentences(sentences):
    """Gets the duplicate words for sentences"""
    return [has_duplicates(words) for words in sentences]


def get_anagrams_in_sentences(sentences):
    """Gets the duplicate words for sentences"""
    return [has_anagrams(words) for words in sentences]


InputType = list[str]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return read_input_lines(__file__, 4)


def part_1(data: InputType) -> int:
    """Remove lines with duplicate words from data"""
    duplicates = get_duplicates_in_sentences(get_words_per_line(data))
    return len(list(filter(lambda i: not i, duplicates)))


def part_2(data: InputType) -> int:
    anagrams = get_anagrams_in_sentences(get_words_per_line(data))
    return len(list(filter(lambda i: not i, anagrams)))


def run_17_4(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_17_4(parsed_input))
