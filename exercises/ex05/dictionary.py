"""Practice with dictionaries."""


__author__ = "730607182"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Flips keys and values of a dictionary."""
    dict_2: dict[str, str] = {}
    for key in dict_1:
        if dict_1[key] in dict_2:
            raise KeyError("Encountered duplicate values while inverting the dictionary")
        reverse_value: str = dict_1[key]
        dict_2[reverse_value] = key
    return dict_2


def favorite_color(dict_1: dict[str, str]) -> str:
    """Returns the most popular color."""
    color_count: dict[str, int] = {}
    for person in dict_1:
        in_dict: bool = False
        dict_color: str = dict_1[person]
        for color in color_count:
            if color == dict_color:
                in_dict = True
        if in_dict:
            color_count[dict_1[person]] += 1
        else:
            color_count[dict_1[person]] = 1
    max_color: str = ""
    for color in color_count:
        if max_color == "":
            max_color = color
        if color_count[color] > color_count[max_color]:
            max_color = color
    return max_color
            

def count(list_1: list[str]) -> dict[str, int]:
    """Creates a dictionary of the strings in a list and number of times they occur."""
    the_dict: dict[str, int] = {}
    for item in list_1:
        if item in the_dict:
            the_dict[item] += 1
        else:
            the_dict[item] = 1
    return the_dict


def alphabetizer(list_1: list[str]) -> dict[str, list[str]]:
    """Returns dict of lettera and words that belong to that letter."""
    the_dict: dict[str, list[str]] = {}
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    for item in list_1:
        idx = 0
        while idx < len(alphabet):
            list_2: list[str] = []
            if item[0].lower() == alphabet[idx]:
                if alphabet[idx] in the_dict:
                    list_2 = the_dict[alphabet[idx]]
                list_2.append(item)
                the_dict[alphabet[idx]] = list_2
            idx += 1
    return the_dict


def update_attendance(dict_1: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendance."""
    if day in dict_1:
        if student not in dict_1[day]:
            dict_1[day].append(student)
    else:
        dict_1[day] = [student]
    return dict_1
