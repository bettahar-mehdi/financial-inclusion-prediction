
# Financial Inclusion Prediction App

This Streamlit web application predicts whether an individual is likely to have a bank account based on various demographic and socioeconomic features. The prediction model is powered by a trained machine learning model (`model.pkl`), and the app allows users to input relevant features to get a prediction.

## Features

- Predict whether an individual has a bank account or not.
- Input features include age, household size, education level, marital status, job type, and more.
- The model is trained to recognize patterns in the provided data and predict bank account ownership.

## Features List

- **Age of Respondent**: The age of the individual.
- **Household Size**: The number of people in the household.
- **Job Type**: Categorized job types, including employed, self-employed, and other.
- **Education Level**: Different levels, from no formal education to tertiary education.
- **Marital Status**: Marital status, including options like single, married, and widowed.
- **Relationship with Head of Household**: The individual's relationship to the head of household.
- **Country**: The country where the respondent is located (Uganda, Tanzania, Rwanda).
- **Location Type**: Whether the individual resides in an urban or rural area.
- **Cellphone Access**: Whether the individual has access to a cellphone.

## Requirements

- Python 3.x
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle

You can install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain the necessary packages like this:

```
streamlit
scikit-learn
pandas
numpy
```

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
