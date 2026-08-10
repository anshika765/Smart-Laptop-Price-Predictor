# 💻 Smart Laptop Price Predictor

A Machine Learning based web application that predicts the estimated price of a laptop based on its hardware and technical specifications.

The project uses a **Random Forest Regression** model and provides an interactive **Streamlit** interface for making laptop price predictions.

---

## 📌 Project Overview

Laptop prices depend on several hardware and technical specifications such as:

- RAM
- Processor
- CPU frequency
- SSD/HDD storage
- Screen size
- Display resolution
- GPU
- Laptop type
- Weight
- Operating system

This project analyzes these factors and trains a machine learning regression model to estimate laptop prices.

---

## 🎯 Objective

The main objectives of this project are:

1. Understand the laptop price dataset.
2. Perform Exploratory Data Analysis (EDA).
3. Clean and preprocess the data.
4. Perform feature engineering.
5. Train a Random Forest regression model.
6. Evaluate model performance.
7. Analyze important features affecting price.
8. Deploy the trained model using Streamlit.

---

## 📊 Dataset

The project uses a laptop price dataset containing **1275 laptop records**.

### Important Features

| Feature | Description |
|---|---|
| Company | Laptop manufacturer |
| Product | Laptop product name |
| TypeName | Type of laptop |
| Inches | Screen size |
| ScreenResolution | Display resolution |
| CPU_Company | CPU manufacturer |
| CPU_Type | Processor type |
| CPU_Frequency (GHz) | CPU frequency |
| RAM (GB) | RAM capacity |
| Memory | Original storage information |
| GPU_Company | GPU manufacturer |
| GPU_Type | Graphics processor |
| OpSys | Operating system |
| Weight (kg) | Laptop weight |
| Price (Euro) | Target variable |

---

## 🔧 Feature Engineering

The original dataset was transformed into additional useful features.

### Storage Features

- `SSD_GB`
- `HDD_GB`
- `Flash_GB`
- `Hybrid_GB`
- `Total_Storage_GB`
- `Storage_Type`

### Display Features

- `Resolution_Width`
- `Resolution_Height`
- `Touchscreen`
- `IPS`

### Processor Features

- `CPU_Family`

### Graphics Features

- `GPU_Family`

### Operating System

- `OS_Family`

---

## 📈 Exploratory Data Analysis

EDA was performed to understand relationships between laptop specifications and price.

Some important observations:

- RAM has a strong relationship with laptop price.
- Higher-end processors are generally associated with higher prices.
- SSD storage contributes to price differences.
- Laptop type affects pricing.
- Display specifications also contribute to price.
- Different laptop companies have significantly different average prices.

---

## 🤖 Machine Learning Model

The main model used in this project is:

### Random Forest Regressor

Random Forest was selected because it:

- Handles nonlinear relationships.
- Works well with mixed numerical and categorical features.
- Can capture interactions between different laptop specifications.
- Provides feature importance for model interpretation.

Categorical variables were transformed using preprocessing techniques before training.

---

## 📊 Model Evaluation

The model was evaluated using:

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted prices.

### Root Mean Squared Error (RMSE)

Penalizes larger prediction errors more heavily.

### R² Score

Measures how much variation in laptop prices is explained by the model.

### Final Model Performance

| Metric | Result |
|---|---:|
| MAE | ~€178 |
| RMSE | ~€268 |
| R² | ~0.855 |

The exact values may vary slightly depending on the final trained model and evaluation split.

---

## 🔍 Model Interpretation

Feature importance analysis was performed using the trained Random Forest model.

### Top Features

| Rank | Feature | Importance |
|---:|---|---:|
| 1 | RAM (GB) | 0.5183 |
| 2 | Weight (kg) | 0.0947 |
| 3 | Notebook Type | 0.0617 |
| 4 | CPU Frequency | 0.0431 |
| 5 | Core i7 | 0.0408 |
| 6 | SSD (GB) | 0.0254 |
| 7 | Inches | 0.0228 |
| 8 | Resolution Width | 0.0217 |
| 9 | Core i5 | 0.0187 |
| 10 | Total Storage | 0.0140 |

RAM was the most important feature used by the Random Forest model.

> Feature importance represents the model's reliance on features during tree splitting. It should not be interpreted as direct causation.

---

## 🌐 Web Application

The trained model is integrated into a Streamlit web application.

The application allows users to enter laptop specifications such as:

- Company
- Laptop type
- Screen size
- CPU
- CPU frequency
- RAM
- Storage
- GPU
- Display resolution
- Touchscreen
- IPS display
- Operating system
- Weight

The application then generates an estimated laptop price.

---

## 🖥️ Application Features

- Interactive laptop specification form
- Machine learning price prediction
- Estimated price display
- Selected specification summary
- Prediction history
- Price comparison chart
- Model information
- User-friendly Streamlit interface

---

## 📂 Project Structure

```text
Smart-Laptop-Price-Predictor/
│
├── data/
│   ├── laptop_prices.csv
│   ├── laptop_processed.csv
│   ├── feature_importance.csv
│   └── day9_feature_importance.csv
│
├── models/
│   ├── laptop_price_model.pkl
│   ├── final_laptop_price_model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── day5_prediction.ipynb
│   ├── day6_feature_importance.ipynb
│   ├── day7_model_evaluation.ipynb
│   ├── day8_hyperparameter_tuning.ipynb
│   └── day9_model_interpretation.ipynb
│
├── src/
│   └── predict.py
│
├── static/
│
├── templates/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore