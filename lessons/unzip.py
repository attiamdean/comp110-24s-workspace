"""Splitting a dictionary into two lists."""


__author__ = "730607182"


def get_keys(the_dict: dict[str, int]) -> list[str]: 
    """Returns list of keys."""
    key_list: list[str] = []
    for key in the_dict:
        key_list.append(key)
    return key_list


def get_values(the_dict: dict[str, int]) -> list[int]:
    """Returns list of values."""
    key_list: list[int] = []
    for key in the_dict:
        key_list.append(the_dict[key])
    return key_list