# Naive Bayes Document Classification Streamlit App

This Streamlit app classifies SMS messages as spam or ham using a Naive Bayes classifier. The app uses the SMS Spam Collection dataset from the UCI Machine Learning Repository.

## Features

- Load and display the dataset.
- Preprocess the text data and vectorize it using TF-IDF.
- Train a Multinomial Naive Bayes classifier.
- Display model performance metrics (accuracy, precision, recall).
- Display sample predictions.

## Requirements

- Python 3.6+
- Streamlit
- pandas
- scikit-learn
- requests

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/naive-bayes-classification.git
    cd naive-bayes-classification
    ```

2. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. The app will load the SMS Spam Collection dataset, preprocess the text data, train the Naive Bayes classifier, and display the model performance metrics.

4. Use the slider to adjust the number of sample predictions displayed.

## Example Dataset

The app uses the SMS Spam Collection dataset from the UCI Machine Learning Repository. The dataset contains SMS messages labeled as 'spam' or 'ham' (not spam).

## File Structure

naive-bayes-classification/
├── app.py # Main Streamlit app
├── requirements.txt # Required Python packages
└── README.md # This readme file

MEDIUM LINK :

STREAMLIT LINK :
