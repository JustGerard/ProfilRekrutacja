import requests

from Models.Attendants import Attendants
from Models.Territory import Territory
from Models.Year import Year


def download_data(link):
    response = requests.get(link)
    data = response.content.splitlines()[1:]
    lines = []
    for line in data:
        lines.append(str(line, 'windows-1250').split(';'))
    return lines


def parse_lines_to_territories(lines):
    territory_lines = {}
    for line in lines:
        territory_name = line[0]
        if territory_name not in territory_lines.keys():
            tab = [line[1:]]
            territory_lines[territory_name] = tab
        else:
            tab = territory_lines[territory_name]
            tab.append(line[1:])
            territory_lines[territory_name] = tab
    territories = []
    for territory in territory_lines.keys():
        territory_object = get_territory_object(territory, territory_lines)
        territories.append(territory_object)
    return territories


def get_territory_object(territory, territory_lines):
    territory_object = Territory(territory)
    year_lines = {}
    for line in territory_lines[territory]:
        year = int(line[2])
        if year not in year_lines.keys():
            line.pop(2)
            tab = [line]
            year_lines[year] = tab
        else:
            tab = year_lines[year]
            line.pop(2)
            tab.append(line)
            year_lines[year] = tab
    years = []
    for year in year_lines.keys():
        year_object = get_year_object(year, year_lines)
        years.append(year_object)
    territory_object.years = years
    return territory_object


def get_year_object(year, year_lines):
    year_object = Year(year)
    attendants_lines = {}
    for line in year_lines[year]:
        attendants_type = line[0]
        if attendants_type not in attendants_lines.keys():
            tab = [line[1:]]
            attendants_lines[attendants_type] = tab
        else:
            tab = attendants_lines[attendants_type]
            tab.append(line[1:])
            attendants_lines[attendants_type] = tab
    for attendants_type in attendants_lines.keys():
        women = 0
        men = 0
        for line in attendants_lines[attendants_type]:
            gender = line[0]
            if gender == "mężczyźni":
                men = int(line[1])
            else:
                women = int(line[1])
        attendants = Attendants(men, women)
        if attendants_type == 'przystąpiło':
            year_object.attendants = attendants
        else:
            year_object.people_that_passed = attendants
    return year_object
