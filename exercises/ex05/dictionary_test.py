"""Testing the dictionary functions."""

__author__ = "730607182"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_use_case_1() -> None:
    """Tests that a short dict will invert properly."""
    favorite_foods: dict = {"Anna": "cheese", "Kenny": "pizza"}
    t_result: dict = invert(favorite_foods)
    assert t_result == {"cheese": "Anna", "pizza": "Kenny"}


def test_invert_use_case_2() -> None:
    """Tests that a longer dict will invert properly."""
    favorite_foods: dict = {"Anna": "cheese", "Kenny": "pizza", "Jana": "sushi", "Mary": "boba", "Emily": "corn", "Gen": "veggies"}
    t_result: dict = invert(favorite_foods)
    assert t_result == {"cheese": "Anna", "pizza": "Kenny", "sushi": "Jana", "boba": "Mary", "corn": "Emily", "veggies": "Gen"}


def test_invert_edge_case() -> None:
    """Tests that keys that include an int instead of a string will either invert properly or raise a type error."""
    favorite_foods: dict = {1: "cheese", "Kenny": "pizza"}
    t_result: dict = invert(favorite_foods)
    assert t_result == {"cheese": 1, "pizza": "Kenny"} or TypeError


def test_favorite_color_use_case_1() -> None:
    """Tests that the most common color will be returned for a short dict."""
    colors: dict = {"Mikal": "purple", "Mary": "pink", "Jana": "green", "Neriya": "purple"}
    t_result: dict = favorite_color(colors)
    assert t_result == "purple"


def test_favorite_color_use_case_2() -> None:
    """Tests that function is case sensitive."""
    colors: dict = {"Mikal": "Purple", "Mary": "Purple", "Jana": "Purple", "Neriya": "purple"}
    t_result: dict = favorite_color(colors)
    assert t_result == "Purple"


def test_favorite_color_edge_case() -> None:
    """Tests that when two colors are tied, the color that got the most votes first is returned."""
    colors: dict = {"Mikal": "Purple", "Mary": "Purple", "Jana": "Blue", "Neriya": "Blue"}
    t_result: dict = favorite_color(colors)
    assert t_result == "Purple"


def test_count_use_case_1() -> None:
    """Checks that the function will tally the number of instances of a string in a short list."""
    attendance: list = ["here", "here", "absent", "absent", "here"]
    t_result: dict = count(attendance)
    assert t_result == {"here": 3, "absent": 2}


def test_count_use_case_2() -> None:
    """Checks that the function is case sensitive."""
    attendance: list = ["here", "here", "Here", "Here", "here"]
    t_result: dict = count(attendance)
    assert t_result == {"here": 3, "Here": 2}


def test_count_edge_case() -> None:
    """Checks that if item in list is an int instead of a string that it either funtions as normal or gives a type error."""
    attendance: list = ["here", "here", "absent", 1, "here"]
    t_result: dict = count(attendance)
    assert t_result == {"here": 3, "absent": 1, 1: 1} or TypeError


def test_alphabetizer_use_case_1() -> None:
    """Checks if a short list of words that all start with different letters will be categorized by letter."""
    words: list = ["apple", "boy", "cat", "dog"]
    t_results: dict = alphabetizer(words)
    assert t_results == {"a": ["apple"], "b": ["boy"], "c": ["cat"], "d": ["dog"]}


def test_alphabetizer_use_case_2() -> None:
    """Checks if a short list of words that start with the same letter will be categorized by letter."""
    words: list = ["apple", "ant", "app", "and"]
    t_results: dict = alphabetizer(words)
    assert t_results == {"a": ["apple", "ant", "app", "and"]}


def test_alphabetizer_edge_case() -> None:
    """Check that function works for an empty list."""
    words: list = []
    t_results: dict = alphabetizer(words)
    assert t_results == {}


def test_update_attendance_use_case_1() -> None:
    """Checks if it will update with a new day and a student that was not there."""
    t_dict: dict = {"monday": ["ted", "mary"], "tuesday": ["ted"]}
    t_day: str = "wednesday"
    t_student: str = "sarah"
    t_results: dict = update_attendance(t_dict, t_day, t_student)
    assert t_results == {"monday": ["ted", "mary"], "tuesday": ["ted"], "wednesday": ["sarah"]}


def test_update_attendance_use_case_2() -> None:
    """Checks if it will not update when the day and student are already in dict."""
    t_dict: dict = {"monday": ["ted", "mary"], "tuesday": ["ted"]}
    t_day: str = "monday"
    t_student: str = "ted"
    t_results: dict = update_attendance(t_dict, t_day, t_student)
    assert t_results == {"monday": ["ted", "mary"], "tuesday": ["ted"]}


def test_update_attendance_edge_case() -> None:
    """Checks if an empty string for student will place an empty string into the attendance."""
    t_dict: dict = {"monday": ["ted", "mary"], "tuesday": ["ted"]}
    t_day: str = "monday"
    t_student: str = ""
    t_results: dict = update_attendance(t_dict, t_day, t_student)
    assert t_results == {"monday": ["ted", "mary", ""], "tuesday": ["ted"]}