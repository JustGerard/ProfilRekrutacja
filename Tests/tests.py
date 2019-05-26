import pytest
from sqlalchemy.orm.exc import NoResultFound

from Models.Territory import Territory
from Models.Year import Year
from Views.AverageView import view_average_of_territory
from Views.Exceptions.EmptyTerritoryException import EmptyTerritoryException
from Views.Exceptions.EmptyYearException import EmptyYearException
from Views.Utils import select_year, get_percentage_of_people_that_passed


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


@pytest.fixture(autouse=True)
def get_territory_patched(monkeypatch, empty_territory):
    from Controlers.DatabaseController import DatabaseController
    monkeypatch.setattr(DatabaseController, 'get_territory', lambda a, b: None)


def test_view_average_of_non_existing_territory(monkeypatch, empty_territory):
    with pytest.raises(NoResultFound):
        view_average_of_territory(empty_territory.name, 2137, "both")
