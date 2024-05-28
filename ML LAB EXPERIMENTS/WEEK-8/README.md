# k-Nearest Neighbors Classifier for Iris Dataset Streamlit App

This Streamlit app classifies the Iris dataset using a k-Nearest Neighbors (k-NN) classifier. The app allows users to adjust the number of neighbors and displays model performance metrics and sample predictions.

## Features

- Load and display the Iris dataset.
- Split the dataset into training and testing sets.
- Train a k-Nearest Neighbors classifier with a user-defined number of neighbors.
- Display model accuracy and a classification report.
- Display sample predictions, highlighting correct and incorrect predictions.

## Requirements

- Python 3.6+
- Streamlit
- pandas
- scikit-learn

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/knn-iris-classifier.git
    cd knn-iris-classifier
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

3. Use the sidebar slider to adjust the number of neighbors for the k-NN classifier.

4. The app will display the dataset, model accuracy, a classification report, and sample predictions.

## Example Dataset

The app uses the Iris dataset from the `sklearn` library. The dataset contains 150 samples of iris flowers, with each sample having 4 features and a target label indicating the species.


Medium Link :https://medium.com/@prithi6305/an-investigation-using-the-iris-dataset-to-learn-about-the-k-nearest-neighbors-algorithm-61c05b90b270

Streamlit link :https://share.streamlit.io/app/sudeshnaweek8/

