# import the Flask class from the flask module
from flask import Flask

# import the render_template function
from flask import render_template

# import the request function
from flask import request

# create a Flask object called app
app = Flask(__name__)

# file_name = 'countries.csv'

# define a route to the home page
# create a fillable_get_form function
@app.route("/")
@app.route("/home")
def main_page():
    return render_template('car_price_prediction.html')


# add a main method to run the app
# as a typical Python script
if __name__ == '__main__':
    app.run()
