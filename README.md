
# Financial Inclusion Prediction System  
**Predicting Bank Account Ownership to Support Data-Driven Financial Inclusion**

## Executive Summary
This project delivers a machine learning–powered decision support system that predicts whether an individual is likely to own a bank account based on demographic and socioeconomic factors. The solution is designed to help **financial institutions, NGOs, and policymakers** identify underserved populations and design targeted inclusion strategies. The system is deployed as an **interactive Streamlit web application**, enabling non-technical stakeholders to explore predictions easily.

## Business Problem
Financial exclusion remains a major challenge in many developing regions. A significant portion of the population lacks access to formal banking services, limiting economic growth and social inclusion.
**Key challenges:**
- Difficulty identifying unbanked populations at scale
- Limited data-driven targeting for inclusion programs
- Inefficient allocation of financial resources

## Solution Overview
This application uses a trained machine learning model to estimate the probability that an individual owns a bank account based on their profile.
**Input:** Demographic and socioeconomic characteristics (age, education, employment, location, etc.)  
**Output:** A clear prediction indicating whether the individual is likely to have a bank account.  
The solution is packaged in a **user-friendly web interface**, making it accessible to non-technical users.

## Key Features
- Predicts bank account ownership with a trained ML model
- Simple and intuitive web interface (Streamlit)
- Handles both demographic and socioeconomic indicators
- Ready for extension to additional regions or datasets

## Input Variables
- **Demographics:** Age, household size, marital status
- **Socioeconomic status:** Education level, job type
- **Living conditions:** Urban or rural location
- **Access indicators:** Cellphone ownership
- **Geography:** Country of residence

## Technology Stack
- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Web Interface:** Streamlit
- **Model Serialization:** Pickle

## Application Architecture
User Input → Data Preprocessing → ML Model → Prediction → Web Interface

## How to Run the Application

1. **Clone the repository**:

    ```bash
    git clone https://github.com/bettahar-mehdi/financial-inclusion-prediction.git
    cd financial-inclusion-prediction
    ```

2. **Install dependencies**:

    Make sure you have `streamlit` installed. If not, you can install it using:

    ```bash
    pip install streamlit
    ```

    If you have a `requirements.txt`, you can run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:

    Run the Streamlit app by executing the following command in your terminal:

    ```bash
    streamlit run app.py
    ```

4. **Access the app**:

    Once the app is running, open your browser and go to `http://localhost:8501` to interact with the app.

## Model

The model used for prediction is a pre-trained machine learning model (`model.pkl`). This model was trained on historical data to predict whether an individual is likely to have a bank account based on the input features.

The model file is included in the repository and can be used as is. If you'd like to retrain the model, you can do so by modifying the Python script and training a new model with your dataset.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Streamlit for the easy-to-use web framework.
- The dataset and resources used for building the prediction model.
