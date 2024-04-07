import streamlit as st
import numpy as np 
import pandas as pd

def learn(concepts, target): 
    specific_h = concepts[0].copy()
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]

    for i, h in enumerate(concepts):
        if target[i] == "yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
                   
        if target[i] == "no":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    return specific_h, general_h 

def main():
    st.title('Candidate elimination algorithm with Streamlit')

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        concepts = np.array(data.iloc[:, 0:-1])
        target = np.array(data.iloc[:, -1])

        st.write("Input Data:")
        st.write(data)

        s_final, g_final = learn(concepts, target)

        st.write("Final Specific_h:")
        st.write(s_final)

        st.write("Final General_h:")
        st.write(g_final)

if __name__ == "__main__":
    main()