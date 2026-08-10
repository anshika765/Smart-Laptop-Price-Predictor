import streamlit as st
import pandas as pd
import sys
import os


# =========================================================
# PROJECT PATH
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

sys.path.insert(0, SRC_DIR)

from predict import predict_laptop_price


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Laptop Price Predictor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# SESSION STATE
# =========================================================

if "history" not in st.session_state:
    st.session_state.history = []


# =========================================================
# TITLE
# =========================================================

st.title("💻 Smart Laptop Price Predictor")

st.write(
    "Estimate the market price of a laptop using "
    "hardware specifications and a trained machine learning model."
)

st.divider()


# =========================================================
# MODEL INFORMATION
# =========================================================

st.subheader("🤖 Model Information")

info1, info2, info3, info4 = st.columns(4)

with info1:
    st.metric(
        "Model",
        "Random Forest"
    )

with info2:
    st.metric(
        "Problem",
        "Regression"
    )

with info3:
    st.metric(
        "Prediction",
        "Laptop Price"
    )

with info4:
    st.metric(
        "Currency",
        "Euro (€)"
    )


st.divider()


# =========================================================
# BASIC INFORMATION
# =========================================================

st.header("💻 Basic Information")

st.caption(
    "Enter the basic details of the laptop."
)

col1, col2, col3 = st.columns(3)


with col1:

    company = st.selectbox(
        "Laptop Company",
        [
            "Acer",
            "Asus",
            "Chuwi",
            "Dell",
            "HP",
            "Lenovo",
            "Mediacom",
            "MSI",
            "Razer",
            "Toshiba"
        ]
    )


with col2:

    type_name = st.selectbox(
        "Laptop Type",
        [
            "Notebook",
            "Gaming",
            "Ultrabook",
            "2 in 1 Convertible",
            "Netbook",
            "Workstation"
        ]
    )


with col3:

    inches = st.number_input(
        "Screen Size (Inches)",
        min_value=10.0,
        max_value=18.4,
        value=15.6,
        step=0.1
    )


# =========================================================
# PROCESSOR
# =========================================================

st.header("⚙️ Processor")

st.caption(
    "Configure the processor specifications."
)

col1, col2, col3 = st.columns(3)


with col1:

    cpu_company = st.selectbox(
        "CPU Company",
        [
            "Intel",
            "AMD",
            "Samsung"
        ]
    )


with col2:

    cpu_family = st.selectbox(
        "CPU Family",
        [
            "Core i7",
            "Core i5",
            "Core i3",
            "Atom",
            "Pentium",
            "Celeron",
            "A12-Series",
            "E-Series",
            "A9-Series",
            "A6-Series",
            "A10-Series",
            "A8-Series",
            "FX",
            "Ryzen",
            "Core M",
            "Xeon",
            "Other"
        ]
    )


with col3:

    cpu_frequency = st.number_input(
        "CPU Frequency (GHz)",
        min_value=0.9,
        max_value=3.6,
        value=2.5,
        step=0.1
    )


# =========================================================
# MEMORY AND WEIGHT
# =========================================================

st.header("🧠 Memory & Weight")

col1, col2 = st.columns(2)


with col1:

    ram = st.selectbox(
        "RAM (GB)",
        [
            2,
            4,
            6,
            8,
            12,
            16,
            24,
            32,
            64
        ],
        index=3
    )


with col2:

    weight = st.number_input(
        "Weight (kg)",
        min_value=0.69,
        max_value=4.70,
        value=2.0,
        step=0.1
    )


# =========================================================
# STORAGE
# =========================================================

st.header("💾 Storage")

st.caption(
    "Configure the storage configuration of the laptop."
)

col1, col2, col3 = st.columns(3)


with col1:

    ssd = st.selectbox(
        "SSD (GB)",
        [
            0,
            128,
            256,
            512,
            1000
        ],
        index=2
    )


with col2:

    hdd = st.selectbox(
        "HDD (GB)",
        [
            0,
            500,
            1000,
            2000
        ]
    )


with col3:

    storage_type = st.selectbox(
        "Storage Type",
        [
            "SSD",
            "HDD",
            "Flash",
            "SSD + HDD",
            "Hybrid"
        ]
    )


col1, col2, col3 = st.columns(3)


with col1:

    flash = st.selectbox(
        "Flash Storage (GB)",
        [
            0,
            64,
            128,
            256,
            512
        ]
    )


with col2:

    hybrid = st.selectbox(
        "Hybrid Storage (GB)",
        [
            0,
            500,
            1000
        ]
    )


with col3:

    total_storage = st.number_input(
        "Total Storage (GB)",
        min_value=8,
        max_value=2512,
        value=256,
        step=1
    )


# =========================================================
# GRAPHICS
# =========================================================

st.header("🎮 Graphics")

col1, col2 = st.columns(2)


with col1:

    gpu_company = st.selectbox(
        "GPU Company",
        [
            "Intel",
            "Nvidia",
            "AMD",
            "ARM"
        ]
    )


with col2:

    gpu_family = st.selectbox(
        "GPU Family",
        [
            "Intel HD",
            "Intel UHD",
            "Nvidia GTX",
            "Nvidia MX",
            "Nvidia GeForce",
            "AMD Radeon",
            "Other"
        ]
    )


# =========================================================
# DISPLAY
# =========================================================

st.header("🖥️ Display")

col1, col2 = st.columns(2)


with col1:

    resolution_width = st.number_input(
        "Resolution Width",
        min_value=1366,
        max_value=3840,
        value=1920,
        step=1
    )


with col2:

    resolution_height = st.number_input(
        "Resolution Height",
        min_value=768,
        max_value=2160,
        value=1080,
        step=1
    )


col1, col2 = st.columns(2)


with col1:

    touchscreen = st.checkbox(
        "📱 Touchscreen Display"
    )


with col2:

    ips = st.checkbox(
        "🎨 IPS Display"
    )


# =========================================================
# OPERATING SYSTEM
# =========================================================

st.header("🪟 Operating System")

os_family = st.selectbox(
    "Operating System",
    [
        "Windows",
        "Linux",
        "No OS",
        "Chrome OS",
        "Android",
        "macOS"
    ]
)


# =========================================================
# PREDICT BUTTON
# =========================================================

st.divider()

predict_button = st.button(
    "🚀 Predict Laptop Price",
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # -----------------------------------------------------
    # CREATE INPUT DATA
    # -----------------------------------------------------

    laptop_data = {

        "Company": company,

        "TypeName": type_name,

        "Inches": inches,

        "CPU_Company": cpu_company,

        "CPU_Frequency (GHz)": cpu_frequency,

        "CPU_Family": cpu_family,

        "RAM (GB)": ram,

        "GPU_Company": gpu_company,

        "GPU_Family": gpu_family,

        "Weight (kg)": weight,

        "SSD_GB": ssd,

        "HDD_GB": hdd,

        "Flash_GB": flash,

        "Hybrid_GB": hybrid,

        "Total_Storage_GB": total_storage,

        "Storage_Type": storage_type,

        "Resolution_Width": resolution_width,

        "Resolution_Height": resolution_height,

        "Touchscreen": int(touchscreen),

        "IPS": int(ips),

        "OS_Family": os_family
    }


    # -----------------------------------------------------
    # PREDICT
    # -----------------------------------------------------

    try:

        with st.spinner(
            "🤖 Running the machine learning model..."
        ):

            predicted_price = predict_laptop_price(
                laptop_data
            )


        predicted_price = float(
            predicted_price
        )


        # -------------------------------------------------
        # SAVE TO HISTORY
        # -------------------------------------------------

        st.session_state.history.append({

            "Company": company,

            "Type": type_name,

            "RAM (GB)": ram,

            "CPU": cpu_family,

            "Storage (GB)": total_storage,

            "GPU": gpu_company,

            "Predicted Price (€)": round(
                predicted_price,
                2
            )
        })


        # -------------------------------------------------
        # SUCCESS
        # -------------------------------------------------

        st.success(
            "Prediction generated successfully! 🎉"
        )


        # -------------------------------------------------
        # PRICE
        # -------------------------------------------------

        st.subheader(
            "💰 Estimated Laptop Price"
        )

        price_col1, price_col2, price_col3 = st.columns(
            [1, 2, 1]
        )

        with price_col2:

            st.metric(
                "Predicted Price",
                f"€{predicted_price:,.2f}"
            )


        # -------------------------------------------------
        # SELECTED SPECIFICATIONS
        # -------------------------------------------------

        st.divider()

        st.subheader(
            "📋 Selected Specifications"
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "Company",
                company
            )

        with c2:

            st.metric(
                "RAM",
                f"{ram} GB"
            )

        with c3:

            st.metric(
                "Storage",
                f"{total_storage} GB"
            )

        with c4:

            st.metric(
                "Screen",
                f"{inches}\""
            )


        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "CPU",
                cpu_family
            )

        with c2:

            st.metric(
                "GPU",
                gpu_company
            )

        with c3:

            st.metric(
                "OS",
                os_family
            )

        with c4:

            st.metric(
                "Weight",
                f"{weight} kg"
            )


        # -------------------------------------------------
        # MODEL MESSAGE
        # -------------------------------------------------

        st.info(
            "🤖 This price was predicted using the "
            "trained Random Forest regression model."
        )


    except Exception as e:

        st.error(
            "❌ Unable to generate prediction."
        )

        st.exception(e)


# =========================================================
# PREDICTION HISTORY
# =========================================================

if st.session_state.history:

    st.divider()

    st.subheader("📊 Prediction History")

    st.caption(
        "Previous laptop price predictions from this session."
    )

    history_df = pd.DataFrame(
        st.session_state.history
    )

    # -----------------------------------------------------
    # HISTORY TABLE
    # -----------------------------------------------------

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # PRICE COMPARISON
    # -----------------------------------------------------

    st.subheader("📈 Price Comparison")

    chart_data = history_df[
        ["Company", "Predicted Price (€)"]
    ].copy()

    chart_data = chart_data.set_index("Company")

    st.bar_chart(
        chart_data,
        use_container_width=True
    )

    # -----------------------------------------------------
    # HISTORY STATISTICS
    # -----------------------------------------------------

    st.subheader("📌 History Summary")

    h1, h2, h3 = st.columns(3)

    with h1:
        st.metric(
            "Total Predictions",
            len(history_df)
        )

    with h2:
        st.metric(
            "Average Price",
            f"€{history_df['Predicted Price (€)'].mean():,.2f}"
        )

    with h3:
        st.metric(
            "Highest Price",
            f"€{history_df['Predicted Price (€)'].max():,.2f}"
        )

    # -----------------------------------------------------
    # CLEAR HISTORY
    # -----------------------------------------------------

    if st.button(
        "🗑️ Clear Prediction History",
        use_container_width=True
    ):

        st.session_state.history = []

        st.rerun()

# =========================================================
# MODEL INSIGHTS
# =========================================================

st.divider()

st.subheader("🧠 Model Insights")

st.write(
    "The laptop price is estimated from multiple hardware "
    "specifications such as RAM, processor, storage, GPU, "
    "display and other features."
)

i1, i2, i3 = st.columns(3)

with i1:
    st.info(
        "🧠 **RAM**\n\n"
        "Higher RAM capacity can generally be associated "
        "with higher-priced laptops."
    )

with i2:
    st.info(
        "⚙️ **Processor**\n\n"
        "CPU family and frequency are important hardware "
        "features considered by the model."
    )

with i3:
    st.info(
        "💾 **Storage**\n\n"
        "SSD/HDD configuration and total storage contribute "
        "to the laptop's predicted price."
    )
# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "💻 Smart Laptop Price Predictor  |  "
    "Python • Pandas • Scikit-learn • Random Forest • Streamlit"
)