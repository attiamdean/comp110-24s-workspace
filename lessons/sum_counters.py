"""Summing the elements of a list using different loops."""

__author__ = "730607182"


def w_sum(the_list: list[float]) -> float:
    """Uses while loops to sum a list of floats."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(the_list):
        sum = the_list[idx] + sum
        idx += 1
    return sum


def f_sum(the_list: list[float]) -> float:
    """Uses for ... in ... loops to sum a list of floats."""
    sum: float = 0.0
    for number in the_list:
        sum = sum + number
    return sum


def f_range_sum(the_list: list[float]) -> float:
    """Uses for ... in range loops to sum a list of floats."""
    sum: float = 0.0
    for idx in range(0, len(the_list)):
        sum = sum + the_list[idx]
    return sum