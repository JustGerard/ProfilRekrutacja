from sqlalchemy.orm.exc import NoResultFound

from src.Views.Exceptions.EmptyYearException import EmptyYearException
from src.Views.Utils import select_territory, get_percentage_of_people_that_passed


def passing_percentage_view(active_filter):
    try:
        territory = select_territory()
        if territory is not None:
            years = territory.years
            print("Percentage of people that passed each year in %s" % territory.name)
            for year in years:
                percentage = get_percentage_of_people_that_passed(year, active_filter)
                print("%d - %f%%" % (year.year_number, percentage * 100))
    except NoResultFound:
        print("There are no territories in database")
    except EmptyYearException:
        print("Year has no attendants")
