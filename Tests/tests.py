import pytest
from sqlalchemy.orm.exc import NoResultFound

from Models.Attendants import Attendants
from Models.Territory import Territory
from Models.Year import Year
from Views.AverageView import view_average_of_territory
from Views.Exceptions.EmptyTerritoryException import EmptyTerritoryException
from Views.Exceptions.EmptyYearException import EmptyYearException
from Views.Exceptions.InvalidItemSelectedException import InvalidItemSelectedException
from Views.Utils import select_year, get_percentage_of_people_that_passed


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


def test_select_year_in_empty_territory(empty_territory):
    with pytest.raises(EmptyTerritoryException):
        select_year(empty_territory)


def test_percentage_of_people_that_passed_in_empty_year(empty_year):
    with pytest.raises(EmptyYearException):
        get_percentage_of_people_that_passed(empty_year, "both")


def test_view_average_of_non_existing_territory(monkeypatch, empty_territory):
    from Controlers.DatabaseController import DatabaseController
    monkeypatch.setattr(DatabaseController, 'get_territory', lambda a, b: None)
    with pytest.raises(NoResultFound):
        view_average_of_territory(empty_territory.name, 2137, "both")


def test_view_average_of_year_non_existing_in_territory(monkeypatch):
    territory = Territory("Zimbabwe")
    attendants = Attendants(2137, 2137)
    year1 = Year(2018)
    year1.attendants = year1.people_that_passed = attendants
    year2 = Year(2019)
    year2.attendants = year2.people_that_passed = attendants
    territory.years = [year1, year2]
    from Controlers.DatabaseController import DatabaseController
    monkeypatch.setattr(DatabaseController, 'get_territory', lambda a, b: territory)
    with pytest.raises(InvalidItemSelectedException):
        view_average_of_territory(territory, 2017, "both")
