import pytest

from src.Models.Territory import Territory
from src.Models.Year import Year
from src.Views.Exceptions.EmptyTerritoryException import EmptyTerritoryException
from src.Views.Exceptions.EmptyYearException import EmptyYearException
from src.Views.RegressionView import get_regression_years


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.fixture()
def empty_territory():
    return Territory("Zimbabwe")


@pytest.fixture()
def empty_year():
    return Year(2137)


def test_get_regression_years_if_territory_is_empty(empty_territory):
    with pytest.raises(EmptyTerritoryException):
        get_regression_years(empty_territory, "both")


def test_get_regression_years_if_year_is_empty(empty_territory, empty_year):
    empty_territory.years = [empty_year, empty_year]
    with pytest.raises(EmptyYearException):
        get_regression_years(empty_territory, "both")
