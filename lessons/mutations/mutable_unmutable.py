"""Functions for lesson about mutability"""
# functions that either mutate a list or not

def remove_first(the_list: list[str]) -> None:
    """Remove first element of input list"""
    the_list.pop(0) 

def get_first(the_list: list[str]) -> str:
    """Return first element of input list without mutating"""
    first: str = the_list[0]
    return first

def get_and_remove_first(the_list: list(str)) -> str:
    first: str = the_list[0]
    the_list.pop(0)
    return first