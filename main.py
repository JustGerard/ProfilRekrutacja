import sys

from Views.AverageView import average_view
from Views.BestTerritoryView import best_territory_view
from Views.PassingPercentageView import passing_percentage_view
from Views.RegressionView import regression_view
from Views.TerritoriesComparisonView import territories_comparison_view


def print_error():
    print("Please provide at least one valid argument, use -help argument for help")


def run_function(argument, __active_filter):
    choice = available_commands.index(argument)
    chosen_function = functions[choice]
    chosen_function(__active_filter)


if __name__ == "__main__":
    available_filters = ["men", "women", "both"]
    available_commands = ["average", "percentage", "best", "regression", "comparison"]
    active_filter = "both"
    functions = [average_view, passing_percentage_view, best_territory_view, regression_view,
                 territories_comparison_view]
    if len(sys.argv) == 1:
        print_error()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-help':
            print("Valid arguments are:\n",
                  "average  - View average number of attendants of specified territory until specified year\n",
                  "percentage - View percentage of people that passed the exam in specified territory each year\n",
                  "best - View territory with highest percentage of people that passed the exam in specified year\n",
                  "regression - View territories which had regression in percentage of people that passed the exam\n",
                  "comparison - View comparison of two specified territories\n",
                  "You can also add a filter by adding a flag -filter [argument]\n",
                  "Valid filters are: men, women, both\n",
                  "Example usage: python main.py best -filter women")
        elif sys.argv[1] in available_commands:
            run_function(sys.argv[1], active_filter)
        else:
            print_error()
    elif len(sys.argv) == 4:
        if "-filter" in sys.argv:
            filter_index = sys.argv.index("-filter")
            if sys.argv[filter_index + 1] in available_filters and sys.argv[filter_index - 1] in available_commands:
                active_filter = sys.argv[filter_index + 1]
                run_function(sys.argv[filter_index - 1], active_filter)
            elif sys.argv[filter_index + 1] in available_filters and sys.argv[filter_index + 2] in available_commands:
                active_filter = sys.argv[filter_index + 1]
                run_function(sys.argv[filter_index + 2], active_filter)
            else:
                print_error()
        else:
            print_error()
    else:
        print_error()
