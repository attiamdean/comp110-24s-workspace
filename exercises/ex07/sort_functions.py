"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    i: int = 0
    while i < len(x) - 1:
        j: int = i + 1
        while j > 0 and x[j] < x[j-1]:
            x[j], x[j-1] = x[j-1], x[j]
            j -= 1
        i += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    # find index of min value in unsroted portion
    i: int = 0
    while i < len(x):
        min_index: int = i
        i_2: int = i + 1
        while i_2 < len(x):
            if x[i_2] < x[min_index]:
                min_index = i_2
            i_2 += 1
        # swap minimum element with current element
        x[i], x[min_index] = x[min_index], x[i]
        i += 1 
    return None
    
list1: list[int] = [2, 4, 3, 6]
insertion_sort(list1)
print(list1)

list2: list[int] = [-7, -8, -9, -10]
insertion_sort(list2)
print(list2)