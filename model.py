import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score, mean_squared_error

from sklearn.preprocessing import LabelEncoder
lab = LabelEncoder()


file_path = "car_price_prediction.csv"
data = pd.read_csv(file_path)
data.head()
data.shape

# for col in data.columns:
#     print(f'Category in {col} is :\n {data[col].unique()}\n')
#     print('\\'*50)


# Data preprocessing
# dropping id and doors fields
data = data.drop(['ID', 'Doors'], axis=1)

# Levy
# Replacing '-' with 0
data['Levy'] = data['Levy'].replace('-', '0')

# Converting Levy type to float
data['Levy'] = data['Levy'].astype('float64')

# Dropping production year column and replacing with age
dtime = dt.datetime.now()
data['Age'] = dtime.year - data['Prod. year']
data = data.drop('Prod. year', axis=1)

# Milage
# Replacing 'Km' with ''
data['Mileage'] = data['Mileage'].str.replace('km', "")

# Converting Mileage type to int64
data.Mileage = data.Mileage.astype('Int64')

# Engine
# Replacing 'Turbo' with ''
data['Engine volume'] = data['Engine volume'].str.replace('Turbo', '')

# Converting Levy type to float
data['Engine volume'] = data['Engine volume'].astype('float64')

# Transform Data
# Convert all object columns to numerical by labelencoder (Because ML Model don't understand object columns)
obdata = data.select_dtypes(include=object)
numdata = data.select_dtypes(exclude=object)

for i in range(0, obdata.shape[1]):
    obdata.iloc[:, i] = lab.fit_transform(obdata.iloc[:, i])

data = pd.concat([obdata, numdata], axis=1)


x = data.drop('Price', axis=1)
y = data['Price']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=5)
