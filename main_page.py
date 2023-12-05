# import the Flask class from the flask module
from flask import Flask
# import the render_template function
from flask import render_template
import pandas as pd
# import the request function
from flask import request

# create a Flask object called app
app = Flask(__name__)

file_name = 'Cleaned_Car_data.csv'
cars = pd.read_csv(file_name)

companies = sorted(cars['company'].unique())
car_models = sorted(cars['name'].unique())
years = sorted(cars['year'].unique(), reverse=True)
fuel_types = cars['fuel_type'].unique()


# define a route to the home page
# create a main page function
@app.route("/")
@app.route("/home")
def main_page():
    return render_template('car_price_prediction.html', company='default',
                           car_model='default', year='default',
                           fuel_type='default', companies=companies,
                           car_models=car_models, years=years, mileage='0',
                           fuel_types=fuel_types)


# define a route to the predict page
# add 'GET' to the methods
# create a predict_price
@app.route("/predict", methods=['POST'])
def predict_price():
    company = request.args['company']
    car_model = request.args['model']
    year = request.args['year']
    fuel_type = request.args['fuel']
    mileage = request.args['mileage']
    return render_template('car_price_prediction.html', company=company,
                           car_model=car_model, year=year, fuel_type=
                           fuel_type, companies=companies,
                           car_models=car_models, mileage = mileage,
                           years=years, fuel_types=fuel_types)


# add a main method to run the app
# as a typical Python script
if __name__ == '__main__':
    app.run()
