import requests

response = requests.post(
    "https://fastapi-ln.herokuapp.com/predict", 
    json={"model_key": "Toyota",
  "mileage": 200000,
  "engine_power": 190,
  "fuel": "diesel",
  "paint_color": "green",
  "car_type": "suv",
  "private_parking_available": True,
  "has_gps": True,
  "has_air_conditioning": True,
  "automatic_car": True,
  "has_getaround_connect": True,
  "has_speed_regulator": True,
  "winter_tires": True
})
print(response.json())