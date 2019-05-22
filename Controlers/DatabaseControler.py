import requests
from sqlalchemy.orm import sessionmaker

from Models.BaseModel import BaseModel


def decode_polish_letters(text):
    letters = {r"\xa5": "A", r"\xc6": "C", r"\xca": "E", r"\xa3": "L", r"\xd1": "N", r"\xd3": "O",
               r"\x8c": "S", r"\x8f": "Z", r"\xaf": "Z", r"\xb9": "a", r"\xe6": "c", r"\xea": "e",
               r"\xb3": "l", r"\xf1": "n", r"\xf3": "o", r"\x9c": "s", r"\x9f": "z", r"\xbf": "z"}
    for letter in letters.keys():
        if letter in text:
            text = text.replace(letter, letters[letter])
    return text


class DatabaseController:
    def __init__(self, engine):
        BaseModel.Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def download_data(self, link):
        response = requests.get(link)
        data = response.content.splitlines()[1:]
        lines = []
        for line in data:
            lines.append(line.decode(errors='backslashreplace').split(';'))
        lines = lines[1:]
        from Models.Territory import Territory
        territory = Territory('Polska')
        pass
        for line in lines:
            territory = decode_polish_letters(line[0])
            attendants_type = decode_polish_letters(line[1])
