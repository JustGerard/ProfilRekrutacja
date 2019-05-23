from Views.Utils import select_territory, get_percentage_of_people_that_passed


def passing_percentage_view():
    territory = select_territory()
    if territory is not None:
        years = territory.years
        print("Percentage of people that passed each year in %s" % territory.name)
        for year in years:
            percentage = get_percentage_of_people_that_passed(year)
            print("%d - %f%%" % (year.year, percentage * 100))
    else:
        return 1
