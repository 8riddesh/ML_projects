from flask import Flask, request, jsonify
from get_Data import get_data as gt
import numpy as np

app = Flask(__name__)


@app.route('/home')
def home():
    return 'Welcome to Home Page'


@app.route('/api/data', methods=['POST'])
def sample_data():
    ans, value = gt()

    gen_health_map = {
        0: 'Excellent',
        1: 'Fair',
        2: 'Good',
        3: 'Poor',
        4: 'Very Good'
    }

    gen = gen_health_map.get(value[9], 'Unknown')

    sample = {
        'Bmi': value[0],
        'PhyHlt': value[1],
        'Age': value[2],
        'Has a HighBp': value[3],
        'Has a Highcol': value[4],
        'is a smoker': value[5],
        'eats Fruits': value[6],
        'eats veggies': value[7],
        'Has High Alcohol Consumption': value[8],
        'General Health': gen,
        'Gender of Patient': value[10]
    }
    return jsonify(sample)


@app.route('/get_prediction')
def get_answer():
    ans, _ = gt()  # Recalling get_data for consistency, avoid using globals directly

    if isinstance(ans, np.generic):
        ans = int(ans)  # Convert numpy scalar to native Python int

    prediction = 'Non-Diabetic' if ans == 1 else 'Diabetic'

    return jsonify({"prediction": prediction})


if __name__ == '__main__':
    app.run(debug=True)
