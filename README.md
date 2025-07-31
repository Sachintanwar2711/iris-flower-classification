# Iris Flower Classification

This is a simple machine learning project that classifies iris flowers into three species: Setosa, Versicolor, and Virginica using the popular Iris dataset.

## Files
- `iris_model.ipynb`: Jupyter Notebook to train and save the model.
- `app.py`: Flask web API to serve the model.
- `model.pkl`: Saved machine learning model.
- `requirements.txt`: List of required Python packages.

## Running the Project

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Train the model by running the notebook (`iris_model.ipynb`).

3. Run the Flask app:

```
python app.py
```

4. Use an API tool like Postman or curl to send a POST request to `/predict`:

```
POST /predict
Content-Type: application/json

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```
