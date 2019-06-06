from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preporcessing import StandardScaler
from sklearn import metrics
import pandas as pd
import numpy as np

dataset = pd.read_csv()

dataset.head()

X = dataset[:, 0:4].values
Y = dataset..iloc[:, 4].values

sc = StandardScaler()
X_train = sc.fir_transform(X_train)
X_test = sc.transform(X_test)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
