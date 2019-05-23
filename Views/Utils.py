from Controlers.DatabaseControler import DatabaseController


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
        database_controller = DatabaseController()
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
        print("Select a year until which you want to calculate average or go back('b'):")
        years = territory.years
        years_numbers = [year.year for year in years]
        for i in range(len(years_numbers)):
            print("\t%d %d" % (i, years_numbers[i]))
        year = get_choice(years)
        if year is not None:
            return year
        else:
            return None


def get_percentage_of_people_that_passed(year):
    men_passed = year.people_that_passed.men
    women_passed = year.people_that_passed.women
    men_attended = year.attendants.men
    women_attended = year.attendants.women
    sum_passed = men_passed + women_passed
    sum_attended = men_attended + women_attended
    return sum_passed / sum_attended
