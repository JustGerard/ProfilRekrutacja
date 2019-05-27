import pytest

from src.Models.Territory import Territory
from src.Models.Year import Year
from src.Views.Exceptions.EmptyTerritoryException import EmptyTerritoryException
from src.Views.Exceptions.EmptyYearException import EmptyYearException
from src.Views.Utils import select_year, get_percentage_of_people_that_passed


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.fixture()
def empty_territory():
    return Territory("Zimbabwe")


@pytest.fixture()
def empty_year():
    return Year(2137)


def test_select_year_in_empty_territory(empty_territory):
    with pytest.raises(EmptyTerritoryException):
        select_year(empty_territory)


def test_percentage_of_people_that_passed_in_empty_year(empty_year):
    with pytest.raises(EmptyYearException):
        get_percentage_of_people_that_passed(empty_year, "both")
