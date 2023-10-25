# CS122_Project

Project Title: Car Price Prediction and Analysis

Authors: Ekta Halani and Nachiketh Mamidi

Project Description (5 Sentences):
In this project, we plan on analyzing data about cars from a car auction site and using our analysis to predict the prices of the cars.
The brand, mileage, transmission, and engine would all impact the price of the car. So, analyzing these features of the car data would
be an important part of our project. We will use web scraping to obtain the data and tools such as pandas and numpy to organize the data.
Cleaning the data would also need to be done before we organize it. We will build the website using Streamlit and deploy it onto Streamlit
Cloud

Project Outline/Plan:
-  Interface Plan:
   We will create a web interface using Flask and plan on having at least two interface windows: one will be the homepage and the other one would be a pop up window that shows up when the user interacts with the homepage. To interact with the homepage, we will create some buttons to compare by price, mileage, brand etc. There will also be other buttons so that users can edit their preferences and interact with the data. We will build a simple web app using Streamlit and deploy the app using Streamlit Cloud. 

- Data Collection and Storage Plan (written by Author #1):
  We plan on scraping the data using BeautifulSoup and requests modules. We plan on getting the data from 3 different car auction websites. We will organize the scraped data using data structures such as lists
  and dictionaries. Then, we can write that data into a txt or csv file.
  
- Data Analysis and Visualization Plan (written by Author #2):
  The first step is to understand and clean the data, analyze the features in the data. Use different types of regression models on the data, such as Linear Regression, Ridge, ExtraTrees, LGBM, XGBoost, and RandomForest regressors. Pick the model with the best accuracy and use it on the website. The website will have a page where users can input the car data and submit the form; the website will return the calculated price. The website will also have a page to view different cars in the database. Visualizations, such as a graph depicting the prices of the cars in the database, and various variations, can be implemented. We will build a simple web app using Streamlit and deploy the app using Streamlit Cloud. 
