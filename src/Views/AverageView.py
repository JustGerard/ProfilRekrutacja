from sqlalchemy.orm.exc import NoResultFound

from src.Views.Exceptions.EmptyTerritoryException import EmptyTerritoryException
from src.Views.Utils import select_territory, select_year, calculate_average_of_territory


def view_average_of_territory(territory_name, to_year, active_filter):
    average = calculate_average_of_territory(territory_name, to_year, active_filter)
    print("Average number of attendants for %s until year %d is %f" % (territory_name, to_year, average))


def average_view(active_filter):
    try:
        territory = select_territory()
        if territory is not None:
            year = select_year(territory)
            if year is not None:
                view_average_of_territory(territory.name, year.year_number, active_filter)
    except NoResultFound:
        print("There is no such territory in database")
    except EmptyTerritoryException:
        print("Territory has no years.")
