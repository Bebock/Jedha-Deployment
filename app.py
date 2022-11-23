import mlflow 
import uvicorn
import pandas as pd 
from pydantic import BaseModel
from typing import Literal, List, Union
from fastapi import FastAPI, File, UploadFile
import joblib
import numpy as np


app = FastAPI()

class ListIn(BaseModel):
    model_key : str
    mileage : int
    engine_power : int
    fuel : str
    paint_color : str
    car_type : str
    private_parking_available : bool
    has_gps : bool
    has_air_conditioning : bool
    automatic_car : bool
    has_getaround_connect : bool
    has_speed_regulator : bool
    winter_tires : bool

class PredictionOut(BaseModel):
    prix: float

def predict_price(values):
    predict_array = np.zeros((1,13))
    im_df = pd.DataFrame(predict_array, columns=['model_key', 'mileage', 'engine_power', 'fuel', 'paint_color',
    'car_type', 'private_parking_available', 'has_gps',
    'has_air_conditioning', 'automatic_car', 'has_getaround_connect',
    'has_speed_regulator', 'winter_tires'])

    im_df[0:1] = values

    loaded_model = joblib.load('finalized_model.sav')
    pipeline = joblib.load('finalized_prepoc.sav')
    result = loaded_model.predict(pipeline.transform(im_df))
    return result[0]

@app.get("/")
async def index():

    message = "Hello world! This `/` is the most simple and default endpoint. If you want to learn more, check out documentation of the api at `/docs`"

    return message

@app.get("/hello")
async def hi():
    return 'Hello there 🤗'

@app.post("/predict", response_model=PredictionOut)
def predict(values: ListIn):
    test = [[values.model_key,
    values.mileage,
    values.engine_power,
    values.fuel,
    values.paint_color,
    values.car_type,
    values.private_parking_available,
    values.has_gps,
    values.has_air_conditioning,
    values.automatic_car,
    values.has_getaround_connect,
    values.has_speed_regulator,
    values.winter_tires]]
    prix = predict_price(test)
    return {"prix": round(prix,2)}

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000) # Here you define your web server to run the `app` variable (which contains FastAPI instance), with a specific host IP (0.0.0.0) and port (4000)