import streamlit as st
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def predict(X):
    h_ip = np.dot(X, wh) + bh
    h_act = sigmoid(h_ip)
    o_ip = np.dot(h_act, wout) + bout
    output = sigmoid(o_ip)
    return output

# Define neural network parameters
input_neurons = 2
hidden_neurons = 3
output_neurons = 1
wh = np.random.uniform(size=(input_neurons, hidden_neurons))  # 2x3
bh = np.random.uniform(size=(1, hidden_neurons))  # 1x3
wout = np.random.uniform(size=(hidden_neurons, output_neurons))  # 3x1
bout = np.random.uniform(size=(1, output_neurons))  # 1x1

# Generate synthetic dataset
np.random.seed(0)
X = np.random.rand(100, 2)  # 100 samples with 2 features
y = np.random.randint(0, 2, size=(100, 1))  # Binary classification target

# Normalize the dataset
X_normalized = (X - X.min()) / (X.max() - X.min())

# Define Streamlit app
def main():
    st.title('Neural Network Prediction')
    st.write('Enter normalized input values:')
    input_values = []
    for i in range(input_neurons):
        val = st.number_input(f'Input {i+1}', step=0.01)
        input_values.append(val)
    input_array = np.array([input_values])

    # Make predictions and display the result
    if st.button('Predict'):
        prediction = predict(input_array)
        st.write(f'Predicted Output: {prediction[0][0]}')

if __name__ == "__main__":
    main()
