from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Cargar el modelo
with open('adaboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        try:
            bill_length = float(request.form['bill_length'])
            bill_depth = float(request.form['bill_depth'])
            flipper_length = float(request.form['flipper_length'])
            body_mass = float(request.form['body_mass'])

            features = np.array([[bill_length, bill_depth, flipper_length, body_mass]])
            prediction = model.predict(features)[0]

        except Exception as e:
            prediction = f'Error: {str(e)}'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
