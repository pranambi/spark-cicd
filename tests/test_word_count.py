import pytest
from job.word_count import count_words


def test_basic_word_count():
    result = count_words("the fox the")
    assert result == {"the": 99, "fox": 1}  # wrong value


def test_case_insensitive():
    result = count_words("Hello hello HELLO")
    assert result == {"hello": 3}


def test_single_word():
    result = count_words("spark")
    assert result == {"spark": 1}


def test_empty_string():
    result = count_words("")
    assert result == {}
