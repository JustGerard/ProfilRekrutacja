from Controlers.DatabaseController import DatabaseController

database_controller = DatabaseController()


def get_choice(item_list):
    choice = input()
    if choice == 'b':
        return None
    else:
        try:
            choice = int(choice)
            if choice not in range(len(item_list)):
                raise ValueError
            else:
                return item_list[choice]
        except ValueError:
            print("Please select valid item")


def select_territory():
    while True:
        print("Select territory or go back('b'):")
        territories = database_controller.get_all_territories()
        territories_names = [territory.name for territory in territories]
        for i in range(len(territories_names)):
            print("\t%d %s" % (i, territories_names[i]))
        territory = get_choice(territories)
        if territory is not None:
            return territory
        else:
            return None


def select_year(territory):
    while True:
        print("Select year or go back('b'):")
        years = territory.years
        years_numbers = [year.year_number for year in years]
        for i in range(len(years_numbers)):
            print("\t%d %d" % (i, years_numbers[i]))
        year = get_choice(years)
        if year is not None:
            return year
        else:
            return None


def get_percentage_of_people_that_passed(year, active_filter):
    men_passed = year.people_that_passed.men
    women_passed = year.people_that_passed.women
    men_attended = year.attendants.men
    women_attended = year.attendants.women
    if active_filter == "both":
        sum_passed = men_passed + women_passed
        sum_attended = men_attended + women_attended
        return sum_passed / sum_attended
    elif active_filter == "men":
        return men_passed / men_attended
    else:
        return women_passed / women_attended


def calculate_average_of_territory(territory_name, to_year, active_filter):
    query = database_controller.get_territory(territory_name)
    territory = query.one()
    values = []
    for year in territory.years:
        if year.year_number <= to_year:
            men = year.attendants.men
            women = year.attendants.women
            both = men + women
            if active_filter == "both":
                values.append(both)
            elif active_filter == "men":
                values.append(men)
            else:
                values.append(women)
    result_sum = 0
    for value in values:
        result_sum += value
    return result_sum / len(values)


def get_all_territories():
    return database_controller.get_all_territories()
