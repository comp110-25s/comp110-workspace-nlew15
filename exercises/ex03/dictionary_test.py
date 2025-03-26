"""Dictionary Testing"""

__author__ = "730571325"
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

"""Invert Tests"""


def test_invert_use():
    assert invert({"apple": "fruit", "green bean": "vegetable"}) == {
        "fruit": "apple",
        "vegetable": "green bean",
    }


def test_invert_use2():
    assert invert({"a": "z", "b": "y"}) == {"z": "a", "y": "b"}


def test_invert_edge():
    assert invert({}) == {}


"""Count Tests"""


def test_count_use():
    assert count(["apple", "green bean", "apple"]) == {"apple": 2, "green bean": 1}


def test_count_use2():
    assert count(["x", "y", "z"]) == {"x": 1, "y": 1, "z": 1}


def test_count_edge():
    assert count([]) == {}


"""Favorite Color Tests"""


def test_favorite_color_use():
    faves = {"John": "blue", "Nik": "red", "Stacy": "red"}
    assert favorite_color(faves) == "red"


def test_favorite_color_use2():
    faves = {"John": "blue", "Nik": "red", "Stacy": "red", "Robert": "blue"}
    assert favorite_color(faves) == "blue"


def test_favorite_color_edge():
    assert favorite_color({}) == ""


"""bin_len tests"""


def test_bin_len_use():
    words = ["pie", "darkness", "lie"]
    assert bin_len(words) == {3: {"pie", "lie"}, 8: {"darkness"}}


def test_bin_len_use2():
    words = ["pie", "pie", "lie"]
    assert bin_len(words) == {3: {"pie", "lie"}}


def test_bin_edge():
    assert bin_len([]) == {}
