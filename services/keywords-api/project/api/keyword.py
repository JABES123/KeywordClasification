from flask import Blueprint, jsonify, request, render_template
from flask_cors import cross_origin

from sqlalchemy import exc
import numpy as np
from project import db
from project.api.utils import make_prediction_single
from project.api.utils import text_labels
from project.api.models import Keyword
import pandas as pd
from datetime import datetime

keywords_blueprint = Blueprint('keyword', __name__)


@keywords_blueprint.route('/keyword/predict', methods=['GET', 'POST'])
def predict_keyword():
    # get post data
    post_data = request.get_json()
    keyword = post_data['keyword']
    probability =  make_prediction_single(keyword)
    prob = float(str(probability[0][0]))
    category = text_labels[np.argmax([probability])]
    predicted_on = datetime.now()
    db.session.add(Keyword(
        keyword=keyword,
        probability=prob,
        category=category,
        predicted_on= datetime.now()
    ))
    db.session.commit()
    """Get all keywords"""
    response_object = {
        'status': 'success',
        'data': {
            'probability': str(probability[0][0]),
            'category': text_labels[np.argmax([probability])]
        }
    }
    return jsonify(response_object), 200

@keywords_blueprint.route('/keyword/list', methods=['GET', 'POST'])
def list_keyword():
    response_object2 = {
        'status': 'success',
        'data': {
            'keywords': [keyword.to_json() for keyword in Keyword.query.all()]
        }
    }
    return jsonify(response_object2), 200



