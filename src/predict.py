import requests

data = {
    "temperature": 80,
    "vibration": 5,
    "current": 10
}

response = requests.post("http://127.0.0.1:5000/predict", json=data)

print(response.json())