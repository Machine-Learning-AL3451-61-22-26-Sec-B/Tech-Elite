Naive Bayes Classifier

Overview
This is a simple Streamlit web application for training and testing a Naive Bayes classifier on a dataset provided by the user via CSV file upload. The app preprocesses the data, trains the classifier, and then tests it to compute accuracy.

Requirements
Python 3.x
Streamlit
pandas
scikit-learn

You can install the required Python packages via pip:
pip install streamlit pandas scikit-learn


Usage
Clone this repository or download the main.py file.
Install the required Python packages as mentioned above.
Run the Streamlit app using the following command:
streamlit run app.py


Once the app is running, you will see a file uploader prompting you to upload your training data CSV file.
Upload your CSV file containing your training data. Make sure the target variable is in the last column.
The app will preprocess the data, train the Naive Bayes classifier, test it, and display the accuracy.


Files
main.py: Contains the Streamlit app code.
README.md: Instructions and information about the app.