# -*- coding: utf-8 -*-
import json

import requests
from sqlalchemy import create_engine

from Controlers.DatabaseControler import DatabaseController

engine = create_engine('sqlite:///database.db')
database_controller = DatabaseController(engine)

api_response = requests.get("https://api.dane.gov.pl/resources/17363")
api_json = json.loads(api_response.text)
csv_link = api_json['data']['attributes']['link']
database_controller.download_data(csv_link)
pass