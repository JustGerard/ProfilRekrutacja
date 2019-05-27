import json

import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.Controlers.Utils import download_data, parse_lines_to_territories
from src.Models.BaseModel import BaseModel
from src.Models.Territory import Territory


class DatabaseController:
    def __init__(self):
        self.engine = create_engine('sqlite:///database.db')
        BaseModel.Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.update_data()

    def update_data(self):
        api_response = requests.get("https://api.dane.gov.pl/resources/17363")
        api_json = json.loads(api_response.text)
        csv_link = api_json['data']['attributes']['link']
        lines = download_data(csv_link)
        territories = parse_lines_to_territories(lines)
        self.save_data(territories)

    def save_data(self, objects):
        self.delete_data()
        self.session.add_all(objects)
        self.session.commit()

    def get_all_territories(self):
        return self.session.query(Territory).all()

    def get_all_territories_names(self):
        return self.session.query(Territory.name).all()

    def get_territory(self, territory):
        return self.session.query(Territory).filter_by(name=territory).one()

    def delete_data(self):
        BaseModel.Base.metadata.drop_all(bind=self.engine)
        BaseModel.Base.metadata.create_all(bind=self.engine)
