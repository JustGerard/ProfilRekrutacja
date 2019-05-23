import json

import requests
from sqlalchemy import create_engine

from Controlers.DatabaseControler import DatabaseController, download_data, parse_lines_to_territories

engine = create_engine('sqlite:///database.db')
database_controller = DatabaseController(engine)

api_response = requests.get("https://api.dane.gov.pl/resources/17363")
api_json = json.loads(api_response.text)
csv_link = api_json['data']['attributes']['link']
lines = download_data(csv_link)
territories = parse_lines_to_territories(lines)
database_controller.saveData(territories)
test = database_controller.getData()
pass