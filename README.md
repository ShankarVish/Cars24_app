# 🚗 Used Car Price Prediction – CARS24

A machine learning-powered web app that predicts the price of a used car based on selected features. Trained on the **CARS24 dataset** and deployed using **Streamlit**.

🔗 **Live Demo**: [cars24app.streamlit.app](https://cars24app.streamlit.app/)

---

## ⚙️ Features

- 🔍 Predicts car resale price using a trained regression model
- 🧾 Based on real-world data from `cars24-car-price.csv`
- 📊 Interactive UI for choosing:
  - Fuel type
  - Transmission
  - Engine size
  - Seat count
- 📋 Displays sample of the dataset and prediction result

---

## 🧠 Model Overview

- Trained using selected features with scikit-learn
- Model saved using `pickle` and loaded on runtime
- Prediction input:
  - Year: 2018 (fixed)
  - Kilometers Driven: 40,000 (fixed)
  - Fuel Type, Transmission, Engine, Seats (user input)

---

## 📦 App Structure

```
used-car-price-prediction/
├── app.py                  # Streamlit app
├── car_pred                # Pickled regression model
├── cars24-car-price.csv    # Source dataset
└── README.md
```

---

## ▶️ How to Run Locally

```bash
pip install streamlit pandas scikit-learn
streamlit run app.py
```

Ensure `car_pred` and `cars24-car-price.csv` are in the same directory as `app.py`.

---

## 🖼️ Sample Output

```
The Predicted Price Of The Car Is : ₹ 4.72 Lakhs
```

---
