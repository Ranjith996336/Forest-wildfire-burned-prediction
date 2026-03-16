import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

data = pd.read_csv("forestfires.csv")

# Remove categorical columns
data = data.drop(["month","day"], axis=1)

X = data.drop("area", axis=1)
y = data["area"]

print("Feature count:", X.shape[1])   # should print 10

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train,y_train)

pickle.dump(model, open("wildfire_model.pkl","wb"))

print("Model saved")