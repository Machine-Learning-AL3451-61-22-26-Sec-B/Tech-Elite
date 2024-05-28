# COVID-19 Bayesian Network Diagnosis Streamlit App

This Streamlit app utilizes a Bayesian Network to analyze and diagnose COVID-19 infection probabilities based on historical data. The app uses data from the COVID-19 dataset provided by the dataset repository.

## Features

- Load and display the COVID-19 dataset.
- Preprocess the data and create a binary infection status.
- Build and visualize a Bayesian Network.
- Perform inference to estimate the probability of infection on a selected date.

## Requirements

- Python 3.6+
- Streamlit
- pandas
- scikit-learn
- pgmpy
- networkx
- pydot

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/covid19-bayesian-network.git
    cd covid19-bayesian-network
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

3. The app will load and preprocess the COVID-19 dataset, build a Bayesian Network, and display the network structure.

4. Use the slider to select a date (encoded) and see the estimated probability of infection for that date.

## Dataset

The app uses the COVID-19 dataset from the [datasets/covid-19](https://github.com/datasets/covid-19) repository. The dataset contains daily confirmed cases, deaths, and recovered counts for various countries.

Medium link :https://medium.com/@sudeshnamahalingam2004/bayesian-network-abce28b2487d

Streamlit link : https://share.streamlit.io/app/sudeshnaweek6/

