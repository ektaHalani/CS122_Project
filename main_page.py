from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data.csv')


@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()

    return render_template('car_price_prediction.html', company='default',
                           car_model='default', year='default',
                           fuel_type='default', companies=companies,
                           car_models=car_models, years=years,
                           fuel_types=fuel_types)


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    driven = request.form.get('kilo_driven')

    data = np.array([car_model, company, year, driven, fuel_type])
    print(data.shape)
    prediction = model.predict(pd.DataFrame(
        columns=['name', 'company', 'year', 'miles_driven', 'fuel_type'],
        data=np.array([car_model, company, year, driven, fuel_type]).reshape(1,
                                                                             5)))
    print(prediction)
    return str(np.round(prediction[0], 2))


@app.route('/about_page', methods=['GET', 'POST'])
def about_page():
    return render_template('about_page.html')


if __name__ == '__main__':
    app.run()
