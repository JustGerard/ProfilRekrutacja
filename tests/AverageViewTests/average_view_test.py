import pytest
from sqlalchemy.orm.exc import NoResultFound

from src.Models.Attendants import Attendants
from src.Models.Territory import Territory
from src.Models.Year import Year
from src.Views.AverageView import view_average_of_territory
from src.Views.Exceptions.InvalidItemSelectedException import InvalidItemSelectedException


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.fixture()
def empty_territory():
    return Territory("Zimbabwe")


def test_view_average_of_non_existing_territory(monkeypatch, empty_territory):
    from src.Controlers.DatabaseController import DatabaseController
    monkeypatch.setattr(DatabaseController, 'get_territory', lambda a, b: None)
    with pytest.raises(NoResultFound):
        view_average_of_territory(empty_territory.name, 2137, "both")


@pytest.mark.parametrize("year", [2017, 2020])
def test_view_average_of_year_non_existing_in_territory(monkeypatch, year):
    territory = Territory("Zimbabwe")
    attendants = Attendants(2137, 2137)
    year1 = Year(2018)
    year1.attendants = year1.people_that_passed = attendants
    year2 = Year(2019)
    year2.attendants = year2.people_that_passed = attendants
    territory.years = [year1, year2]
    from src.Controlers.DatabaseController import DatabaseController
    monkeypatch.setattr(DatabaseController, 'get_territory', lambda a, b: territory)
    with pytest.raises(InvalidItemSelectedException):
        view_average_of_territory(territory, year, "both")
