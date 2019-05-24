from Views.AverageView import average_view
from Views.BestTerritoryView import best_territory_view
from Views.PassingPercentageView import passing_percentage_view
from Views.RegressionView import regression_view
from Views.TerritoriesComparisonView import territories_comparison_view

if __name__ == "__main__":
    available_filters = ["men", "women", "both"]
    active_filter = "both"
    functions = [average_view, passing_percentage_view, best_territory_view, regression_view,
                 territories_comparison_view]
    while True:
        print("Type 'f' to change filter and 'q' to quit")
        print("Please choose on of the following functions: ")
        print("1 View average number of attendants of specified territory until specified year")
        print("2 View percentage of people that passed the exam in specified territory each year")
        print("3 View territory with highest percentage of people that passed the exam in specified year")
        print("4 View territories which had regression in percentage of people that passed the exam")
        print("5 View comparison of two specified territories")
        choice = input()
        if choice == "f":
            while True:
                print("Please choose one of the filters: man/women/both: ")
                chosen_filter = input()
                if chosen_filter not in available_filters:
                    print("Please choose a valid filter")
                else:
                    active_filter = chosen_filter
                    break
        elif choice == 'q':
            exit(0)
        else:
            try:
                choice = int(choice)
                if choice in range(1, 6):
                    choice -= 1
                    chosen_functions = functions[choice]
                    chosen_functions(active_filter)
                else:
                    raise ValueError
            except ValueError:
                print("Please pick a valid value")
