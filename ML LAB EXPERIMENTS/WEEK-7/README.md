# Clustering with EM Algorithm and k-Means Streamlit App

This Streamlit app compares clustering results using the Expectation-Maximization (EM) algorithm via Gaussian Mixture Models (GMM) and k-Means on the Iris dataset. It also calculates and displays silhouette scores to evaluate the clustering performance.

## Features

- Load and display the Iris dataset.
- Apply Gaussian Mixture Model (EM algorithm) for clustering.
- Apply k-Means algorithm for clustering.
- Calculate and display silhouette scores for both clustering methods.
- Visualize clustering results using scatter matrix plots.

## Requirements

- Python 3.6+
- Streamlit
- pandas
- scikit-learn
- plotly

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/clustering-comparison.git
    cd clustering-comparison
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

3. The app will load the Iris dataset, apply both clustering algorithms, and display the results along with silhouette scores.

## Example Dataset

The app uses the Iris dataset from the `sklearn` library. The dataset contains 150 samples of iris flowers, with each sample having 4 features and a target label indicating the species.

Medium link :https://medium.com/@sudeshnamahalingam2004/em-algorithm-c2c12a395928

Streamlit link :https://share.streamlit.io/app/sudeshnaweek7/
