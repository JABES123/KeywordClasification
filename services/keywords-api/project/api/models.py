# services/users/project/api/models.py

import datetime
from flask import current_app

from project import db, bcrypt


class Keyword(db.Model):
    __tablename__ = 'keyword_catalog'
    keyword_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    keyword = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.String(400), nullable=False)
    probability = db.Column(db.Float(), nullable=False)
    predicted_on = db.Column(db.DateTime())


    def __init__(self, keyword,probability,category, predicted_on):
        self.keyword = keyword
        self.probability = probability
        self.category = category
        self.predicted_on = predicted_on

    def to_json(self):
        return{
            'id': self.keyword_id,
            'keyword':self.keyword,
            'category':self.category,
            'probability':self.probability,
            'predicted_on': self.predicted_on
        }

