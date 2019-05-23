from Controlers.DatabaseControler import DatabaseController
from Views.Utils import select_territory, select_year


def view_average_of_territory(territory_name, to_year):
    database_controller = DatabaseController()
    average = database_controller.calculate_average_of_territory(territory_name, to_year)
    print("Average for %s until year %d is %f" % (territory_name, to_year, average))


def average_view():
    territory = select_territory()
    if territory is not None:
        year = select_year(territory)
        if year is not None:
            view_average_of_territory(territory.name, year.year)
            return 0
        else:
            return 1
    else:
        return 1
