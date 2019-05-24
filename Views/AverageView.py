from Views.Utils import select_territory, select_year, calculate_average_of_territory


def view_average_of_territory(territory_name, to_year, active_filter):
    average = calculate_average_of_territory(territory_name, to_year, active_filter)
    print("Average number of attendants for %s until year %d is %f" % (territory_name, to_year, average))


def average_view(active_filter):
    territory = select_territory()
    if territory is not None:
        year = select_year(territory)
        if year is not None:
            view_average_of_territory(territory.name, year.year_number, active_filter)
            return 0
        else:
            return 1
    else:
        return 1
