from Views.Utils import get_percentage_of_people_that_passed, get_all_territories


def get_regression_years(territory, active_filter):
    regression_years = []
    years = territory.years
    for i in range(len(years) - 1):
        value_one = get_percentage_of_people_that_passed(years[i], active_filter)
        value_two = get_percentage_of_people_that_passed(years[i + 1], active_filter)
        if value_one > value_two:
            regression_years.append([years[i], years[i + 1]])
    return regression_years


def regression_view(active_filter):
    territories = get_all_territories()
    for territory in territories:
        regression_years = get_regression_years(territory, active_filter)
        for regression_year in regression_years:
            print("Territory %s: %d -> %d" %
                  (territory.name, regression_year[0].year_number, regression_year[1].year_number))
