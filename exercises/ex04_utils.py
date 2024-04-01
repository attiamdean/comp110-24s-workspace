"""List utils."""

__author__ = "730607182"


def all(the_list: list[int], the_number: int) -> bool:
    """Determines if all the ints in the list are the same as a given int."""
    all_same: bool = True
    for number in the_list:
        if number != the_number:
            all_same = False
    if len(the_list) <= 0:
        all_same = False
    return all_same


def max(a_list: list[int]) -> int:
    """Finds the maximum out of a list of values."""
    if len(a_list) == 0:
        raise ValueError("max() arg is an empty list")
    my_max = a_list[0]
    for number in a_list:
        if my_max < number:
            my_max = number
    return my_max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if one list is equal to another."""
    idx: int = 0
    equal: bool = True
    if len(list_1) != len(list_2):
        equal = False
    else:
        for item in list_1:
            if item != list_2[idx]:
                equal = False
            idx += 1
    return equal


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Adds a second list to the end of a list."""
    for item in list_2:
        list_1.append(item)