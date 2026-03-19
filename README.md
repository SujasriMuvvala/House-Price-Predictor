# House-Price-Predictor
# House Price Predictor with Location Map

A full-stack machine learning web application that predicts house prices based on user inputs and displays the selected location on an interactive map.

---

## Features

* Predict house prices using a machine learning model
* Model trained using Linear Regression
* Web interface built with Flask
* Clean and responsive user interface
* Interactive map using Leaflet and OpenStreetMap
* Ability to select house location on the map

---

## Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn

### Backend

* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Map Integration

* Leaflet.js
* OpenStreetMap

---

## Project Structure

```
House_Price_Predictor/
│
├── data/
│   └── housing.csv
│
├── model/
│   ├── train_model.py
│   └── house_model.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
└── README.md
```

---

## Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor
```

---

### 2. Install dependencies

```
pip install pandas numpy scikit-learn flask
```

---

### 3. Train the model

```
cd model
python train_model.py
```

---

### 4. Run the application

```
cd ..
python app.py
```

---

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## Input Features

* Area (square feet)
* Number of bedrooms
* Number of bathrooms
* Age of the house

---

## How It Works

1. The user enters house details through the web interface
2. The data is sent to the Flask backend
3. The trained machine learning model predicts the price
4. The predicted price is displayed on the webpage
5. The user can select a location using the map

---

## Future Improvements

* Use real-world housing datasets
* Incorporate location into the prediction model
* Add data visualization features
* Deploy the application to a cloud platform
* Improve mobile responsiveness
* Upgrade to advanced machine learning models such as Random Forest or XGBoost

---

## Author

Sujasri Muvvala

---

## License

This project is open-source and available under the MIT License.
