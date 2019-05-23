import json

import requests

from Controlers.DatabaseControler import DatabaseController
from Views.PassingPercentageView import passing_percentage_view

api_response = requests.get("https://api.dane.gov.pl/resources/17363")
api_json = json.loads(api_response.text)
csv_link = api_json['data']['attributes']['link']
database_controller = DatabaseController()
database_controller.update_data(csv_link)
# average_view()
passing_percentage_view()
