# Locally Weighted Regression Streamlit App

This Streamlit app demonstrates Locally Weighted Regression (LWR) on the Boston Housing dataset. LWR is a non-parametric regression method that assigns different weights to training points based on their distance to the test point, allowing for more flexible fitting.

## Features

- Load and display the Boston Housing dataset.
- Apply Locally Weighted Regression to predict house prices.
- Visualize the original data and regression results.
- Allow users to adjust the tau (bandwidth) parameter using a sidebar slider.

## Requirements

- Python 3.6+
- Streamlit
- pandas
- numpy
- matplotlib
- scikit-learn

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/lwr-boston-housing.git
    cd lwr-boston-housing
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

3. Use the sidebar slider to adjust the tau (bandwidth) parameter.

4. The app will display the original training data, and the true and predicted values for the test set.

## Example Dataset

The app uses the Boston Housing dataset from the [CMU StatLib repository](http://lib.stat.cmu.edu/datasets/boston). The dataset contains 506 samples of houses, with each sample having 13 features and a target variable indicating the median value of owner-occupied homes.

## File Structure

lwr-boston-housing/
├── app.py # Main Streamlit app
├── requirements.txt # Required Python packages
└── README.md # This readme file

MEDIUM LINK :https://thirishashalini12.medium.com/examining-locally-weighted-non-parametric-regression-an-effective-instrument-for-adaptable-data-ca687aa5ef88


STREAMLIT LINK :https://share.streamlit.io/app/sudeshnaweek9/
