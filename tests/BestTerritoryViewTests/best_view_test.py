import pytest

from src.Models.Attendants import Attendants
from src.Models.Territory import Territory
from src.Models.Year import Year
from src.Views.BestTerritoryView import get_best_territory
from src.Views.Exceptions.EmptyListException import EmptyListException
from src.Views.Exceptions.EmptyYearException import EmptyYearException


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.fixture()
def empty_territory():
    return Territory("Zimbabwe")


@pytest.fixture()
def good_year():
    people_that_passed = attendants = Attendants(2137, 2137)
    year = Year(2137)
    year.people_that_passed = people_that_passed
    year.attendants = attendants
    return year


@pytest.fixture()
def good_territory():
    year = good_year()
    territory = Territory("Zimbabwe")
    territory.years = [year]


@pytest.fixture()
def empty_year():
    return Year(2137)


def test_get_best_territory_if_there_are_no_territories(good_year):
    with pytest.raises(EmptyListException):
        get_best_territory([], good_year, "both")


def test_get_best_territory_if_year_is_empty(empty_territory, empty_year):
    territory = empty_territory
    territory.years = [empty_year]
    with pytest.raises(EmptyYearException):
        get_best_territory([territory], empty_year, "both")
