"""Test my garden functions."""

__author__ = "730607182"

from lessons.garden.garden_helpers import add_by_date, add_by_kind, lookup_by_kind_and_date


def test_add_by_kind_use_case() -> None:
    """Tests that new types are being added to the dictionary."""
    t_dict: dict = {"flowers": ["poppy", "rose"]}
    t_new_kind: str = "veggies"
    t_new_plant: str = "eggplant"
    add_by_kind(t_dict, t_new_kind, t_new_plant)
    assert t_dict == {"flowers": ["poppy", "rose"], "veggies": ["eggplant"]}


def test_add_by_kind_edge_case() -> None:
    """Tests that plants are added even if type is already in dictionary."""
    t_dict: dict = {"flowers": ["poppy", "rose"]}
    t_new_kind: str = "flowers"
    t_new_plant: str = "tulip"
    add_by_kind(t_dict, t_new_kind, t_new_plant)
    assert add_by_kind == {"flowers": ["poppy", "rose", "tulip"]}


def test_add_by_date_use_case() -> None:
    """Checks that function adds new month and plant to dictionary."""
    t_dict: dict = {"December": ["peas", "corn"]}
    t_month: str = "May"
    t_plant: str = "peppers"
    add_by_date(t_dict, t_month, t_plant)
    assert t_dict == {"December": ["peas", "corn"], "May": "peppers"}


def test_add_by_date_edge_case() -> None:
    """Checks that function works correctly when plant is already in dictionary."""
    t_dict: dict = {"December": ["peas", "corn"]}
    t_month: str = "May"
    t_plant: str = "peas"
    add_by_date(t_dict, t_month, t_plant)
    assert t_dict == {"December": ["peas", "corn"], "May": "peas"}

    
def test_lookup_by_kind_and_dates_use_case() -> None:
    """Checks that function returns str that describes what plants to plant in a given month."""
    t_plants_by_kind: dict = {"flowers": ["poppy", "rose"]}
    t_plants_by_date: dict = {"December": ["poppy", "corn"]}
    t_kind: str = "flowers"
    t_date: str = "December"
    t_output: str = lookup_by_kind_and_date(t_plants_by_kind, t_plants_by_date, t_kind, t_date)
    assert t_output == "flowers to plant in December: poppy"


def test_lookup_by_kind_and_dates_edge_case() -> None:
    """Checks that function will not return anything if month is not in dict."""
    t_plants_by_kind: dict = {"flowers": ["poppy", "rose"]}
    t_plants_by_date: dict = {"December": ["poppy", "corn"]}
    t_kind: str = "flowers"
    t_date: str = "January"
    t_output: str = lookup_by_kind_and_date(t_plants_by_kind, t_plants_by_date, t_kind, t_date)
    assert t_output == None