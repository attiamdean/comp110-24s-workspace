"""Tests my mutating functions."""

from lessons.mutations.mutable_unmutable import remove_first, get_first, get_and_remove_first

def test_remove_first_use_case() -> None:
    """Test basic use cases for the remove_first function"""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    remove_first(t)
    assert t == ["rainy", "sunny"]

def test_get_first_use_case() -> None:
    """Test basic use case for get_first function."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    ret_value: str = get_first(t)
    get_first(t)
    # test that it doesnt mutate input
    assert t == ["cloudy", "rainy", "sunny"]
    assert ret_value == "cloudy"

def test_get_and_remove_first_use_case() -> None:
    """Test basic use case for get_and_remove_first function."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    ret_value: str = get_and_remove_first(t)
    get_first(t)
    # test that it mutates input
    assert t == ["rainy", "sunny"]
    assert ret_value == "cloudy"