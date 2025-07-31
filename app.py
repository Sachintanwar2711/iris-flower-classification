from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return "Iris Flower Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]
    prediction = model.predict([features])
    classes = ['Setosa', 'Versicolor', 'Virginica']
    return jsonify({'prediction': classes[prediction[0]]})

if __name__ == '__main__':
    app.run(debug=True)
