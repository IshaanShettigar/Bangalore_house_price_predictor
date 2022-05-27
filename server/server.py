from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control_Allow-Origin','*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = float(request.form['location'])
    bhk = float(request.form['bhk'])
    bath = float(request.form['bath'])

    response = jsonify({
        'estimated_price':util.predict_price(bath,bhk,location,total_sqft)
    })

    return response

"""We need to create 2 routines, first we need to get all the locations in Bangalore City
util will contain all the core routines where as the server will just do the routing for
request and response
"""


if __name__ == "__main__":
    print('Starting Python Flask Server For Home Price Prediction...')
    app.run()
