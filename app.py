import uvicorn
from fastapi import FastAPI
from Month_Star import Month_Star

import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open('model.pkl', 'rb')
regressor = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message':"Hello World"}

@app.get('/{name}')
def get_name(name:str):
    return {'message':f'Hello, {name}'}

@app.post('/predict')
def predict_price(data:Month_Star):
    input_data = [[data.month, data.star]]
    prediction = regressor.predict(input_data)
    return {
        'prediction': prediction.tolist() 
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)