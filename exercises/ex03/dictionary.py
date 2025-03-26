"""Dictionary Practice"""

__author__ = "730571325"


def invert(words: dict[str, str]) -> dict[str, str]:
    return dict((words[key], key) for key in words)


def count(values: list[str]) -> dict[str, int]:
    result = {}
    for key in values:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result


def favorite_color(fav: dict[str, str]) -> str:
    colors = []
    for f in fav:
        colors.append(fav[f])
    count_colors = count(colors)
    max = 0
    most_common = ""

    for f in fav:
        color = fav[f]
        if count_colors[color] > max:
            max = count_colors[color]
            most_common = color
    return most_common


def bin_len(words: list[str]) -> dict[int, set[str]]:
    result = {}

    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}
    return result
