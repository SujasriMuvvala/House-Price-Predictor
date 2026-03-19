import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# load dataset
data = pd.read_csv("../data/housing.csv")

# features
X = data[["area","bedrooms","bathrooms","age"]]

# target
y = data["price"]

# train model
model = LinearRegression()
model.fit(X,y)

# save model
pickle.dump(model, open("house_model.pkl","wb"))

print("Model trained and saved!")
