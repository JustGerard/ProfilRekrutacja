from Controlers.DatabaseControler import DatabaseController


def view_average_of_territory(territory_name, to_year):
    database_controller = DatabaseController()
    average = database_controller.calculate_average_of_territory(territory_name, to_year)
    print("Average for %s until year %d is %f" % (territory_name, to_year, average))


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
