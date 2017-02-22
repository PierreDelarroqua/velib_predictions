from flask import render_template, request, jsonify
from velib_modules.app import app
from velib_modules.api.predict import predict_available_bikes
from velib_modules.utils.io import load_pickle

import pandas as pd

# Todo: include Velib logo
# Todo : handle errors in javascripts

# Todo: create tests
# Todo : create auth in api


# Load model
model = load_pickle("files/app_model/model.pkl")

# Load list of stations
list_stations = pd.read_csv('files/input/list_stations.csv', encoding='utf-8')


# request example : curl -i http://localhost:5000/prediction/4006
@app.route('/prediction', methods=['POST'])
def ask_prediction():
    number_station = request.form['number_station']
    time_prediction = request.form["time_prediction"]
    available_bikes, bike_stands = predict_available_bikes(model, number_station, time_prediction)
    return jsonify({'available_bikes': available_bikes, 'bike_stands': bike_stands})


@app.route('/')
def index():
    number_station_index = 4006
    return render_template('prediction.html', list_stations=list_stations.values.tolist(),
                           number_station=number_station_index)
