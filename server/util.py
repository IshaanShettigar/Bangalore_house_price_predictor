import json
import pickle
import sklearn
import numpy as np

__locations = None
__data_columns = None
__model = None


def predict_price(bath, bhk, location, sqft):
    """ If the index isn't found it'll throw error therefore try except"""
    try:
        location_index = __data_columns.index(location.lower())
    except:
        location_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location_index >= 0:
        x[location_index] = 1

    return round(__model.predict([x])[0],2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/bangalore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts...done")



load_saved_artifacts()
print(get_location_names())
print(predict_price(3,3,'1st phase jp nagar',1000))
print(predict_price(2,2,'1st phase jp nagar',1000))
print(predict_price(3,3,'ejipura',1500)) #other
print(predict_price(3,3,'whitefield',1500)) #other

