from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load model safely
MODEL_PATH = os.path.join("model", "house_model.pkl")
model = pickle.load(open(MODEL_PATH, "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    
    price = None

    if request.method == "POST":
        try:
            area = float(request.form["area"])
            bedrooms = int(request.form["bedrooms"])
            bathrooms = int(request.form["bathrooms"])
            age = int(request.form["age"])

            prediction = model.predict([[area, bedrooms, bathrooms, age]])
            price = int(prediction[0])

        except:
            price = "Error in input values"

    return render_template("index.html", price=price)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)