import os
import pandas as pd
import joblib

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model paths
MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "final_laptop_price_model.pkl"
)

PREPROCESSOR_PATH = os.path.join(
    BASE_DIR,
    "models",
    "preprocessor.pkl"
)

# Load trained model and preprocessor
model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)


def predict_laptop_price(laptop_data):
    """
    Predict laptop price from laptop specifications.
    """

    laptop_df = pd.DataFrame([laptop_data])

    processed_data = preprocessor.transform(laptop_df)

    prediction = model.predict(processed_data)

    return prediction[0]


if __name__ == "__main__":

    laptop = {
        "Company": "HP",
        "TypeName": "Notebook",
        "Inches": 15.6,
        "CPU_Company": "Intel",
        "CPU_Frequency (GHz)": 2.5,
        "RAM (GB)": 8,
        "GPU_Company": "Intel",
        "Weight (kg)": 2.0,
        "SSD_GB": 256,
        "HDD_GB": 0,
        "Flash_GB": 0,
        "Hybrid_GB": 0,
        "Total_Storage_GB": 256,
        "Storage_Type": "SSD",
        "Resolution_Width": 1920,
        "Resolution_Height": 1080,
        "Touchscreen": 0,
        "IPS": 0,
        "CPU_Family": "Core i5",
        "GPU_Family": "Intel HD",
        "OS_Family": "Windows"
    }

    price = predict_laptop_price(laptop)

    print(f"Predicted Price: €{price:,.2f}")