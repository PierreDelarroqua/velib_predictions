from flask import render_template, request, jsonify
from velib_modules.app import app
from velib_modules.api.predict import predict_available_bikes
from velib_modules.utils.io import load_pickle


# Todo : Create list_stations.csv file, and load it to views.py
# Todo : Integrate a Google Map with every velib stations on it

# Todo: create tests
# Todo : create auth in api

# Todo : Store a model.pkl in the S3 bucket, and change the query accordingly
# Todo : Faire un package (setup.py)



# Load model
model = load_pickle("files/model.pkl")

# Load list of stations
# list_stations = pd.read_csv('list_stations.csv')

# request example : curl -i http://localhost:5000/prediction/4006
@app.route('/prediction', methods=['POST'])
def ask_prediction():
    number_station = request.form['number_station']
    print(number_station)
    prediction = predict_available_bikes(model, number_station)
    return jsonify({'prediction': prediction})


@app.route('/')
def index():
    return render_template('prediction.html') # list_stations=list_stations


# @app.route('/prediction', methods=['GET'])
# def ask_prediction_old():
#     # number_station = request.args.get('number_station')
#     if (number_station.isdigit()):
#         number_station = int(number_station)
#         prediction = predict_available_bikes(model, number_station)
#     else:
#         prediction = -1
#     return render_template('prediction.html', number_station=number_station, prediction=prediction) # list_stations=list_stations