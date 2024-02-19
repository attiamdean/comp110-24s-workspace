"""Mutating functions."""

__author__ = "730607182"

a: list[int] = [1, 2, 3]


def manual_append(intlist: list[int], num: int) -> None:
    """Append!"""
    intlist.append(int(num))


def double(numlist: list[int]) -> None:
    """Double!"""
    counter: int = 1
    while counter < 2:
        numcounter: int = 0
        while numcounter < len(numlist):
            numlist[numcounter] = numlist[numcounter] * 2
            numcounter += 1
            counter += 1