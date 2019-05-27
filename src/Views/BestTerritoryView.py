from sqlalchemy.orm.exc import NoResultFound

from src.Views.Exceptions.EmptyListException import EmptyListException
from src.Views.Exceptions.EmptyYearException import EmptyYearException
from src.Views.Exceptions.InvalidItemSelectedException import InvalidItemSelectedException
from src.Views.Utils import get_percentage_of_people_that_passed, select_year, get_all_territories


def get_best_territory(territories, year, active_filter):
    if len(territories) == 0:
        raise EmptyListException
    territories_with_values = {}
    year_name = year.year_number
    for territory in territories:
        years_names = [year.year_number for year in territory.years]
        years = territory.years
        year_index = years_names.index(year_name)
        percentage = get_percentage_of_people_that_passed(years[year_index], active_filter)
        territories_with_values[territory] = percentage
    best_territory = sorted(territories_with_values, key=territories_with_values.get, reverse=True)[0]
    best_percentage = territories_with_values[best_territory]
    return best_territory, best_percentage


def best_territory_view(active_filter):
    try:
        territories = get_all_territories()
        year = select_year(territories[0])
        if year is not None:
            best_territory, best_percentage = get_best_territory(territories, year, active_filter)
            print("Best territory in year %d is %s with score: %f%%" %
                  (year.year_number, best_territory.name, best_percentage * 100))
    except EmptyListException:
        print("There are no territories in database")
    except NoResultFound:
        print("There are no territories in database")
    except InvalidItemSelectedException:
        print("Selected year is not in territory")
    except EmptyYearException:
        print("Year has no attendants")
