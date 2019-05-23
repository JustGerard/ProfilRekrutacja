import requests
from sqlalchemy.orm import sessionmaker

from Models.Attendants import Attendants
from Models.BaseModel import BaseModel
from Models.Territory import Territory
from Models.Year import Year


def decode_polish_letters(text):
    letters = {r"\xa5": "A", r"\xc6": "C", r"\xca": "E", r"\xa3": "L", r"\xd1": "N", r"\xd3": "O",
               r"\x8c": "S", r"\x8f": "Z", r"\xaf": "Z", r"\xb9": "a", r"\xe6": "c", r"\xea": "e",
               r"\xb3": "l", r"\xf1": "n", r"\xf3": "o", r"\x9c": "s", r"\x9f": "z", r"\xbf": "z"}
    for letter in letters.keys():
        if letter in text:
            text = text.replace(letter, letters[letter])
    return text


def download_data(link):
    response = requests.get(link)
    data = response.content.splitlines()[1:]
    lines = []
    for line in data:
        lines.append(line.decode(errors='backslashreplace').split(';'))
    return lines


def parse_lines_to_territories(lines):
    territory_lines = {}
    for line in lines:
        territory_name = decode_polish_letters(line[0])
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
        attendants_type = decode_polish_letters(line[0])
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
            gender = decode_polish_letters(line[0])
            if gender == "mezczyzni":
                men = int(line[1])
            else:
                women = int(line[1])
        attendants = Attendants(men, women)
        if attendants_type == 'przystapilo':
            year_object.attendants = attendants
        else:
            year_object.people_that_passed = attendants
    return year_object


class DatabaseController:
    def __init__(self, engine):
        BaseModel.Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def saveData(self, objects):
        self.deleteData()
        self.session.add_all(objects)
        self.session.commit()

    def getData(self):
        from Models.Territory import Territory
        return self.session.query(Territory).all()

    def deleteData(self):
        from Models.Territory import Territory
        self.session.query(Territory).delete()
        self.session.commit()
