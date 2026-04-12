from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("models/model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    features = np.array([[data['temperature'],
                          data['vibration'],
                          data['current']]])

    prediction = model.predict(features)[0]

    return jsonify({
        "failure": bool(prediction)
    })

if __name__ == '__main__':
    app.run(debug=True)