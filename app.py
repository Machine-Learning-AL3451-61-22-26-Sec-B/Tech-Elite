import streamlit as st
import numpy as np
import pandas as pd

def learn(concepts, target): 
    specific_h = concepts[0].copy()
    general_h = [["?" for _ in range(len(specific_h))] for _ in range(len(specific_h))] 

    for i, h in enumerate(concepts):
        if target[i] == "yes":
            for x in range(len(specific_h)): 
                if h[x] != specific_h[x]:                    
                    specific_h[x] ='?'                     
                    general_h[x][x] ='?'                   
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
    st.title("Concept Learning Algorithm")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        st.write("Preview of the dataset:")
        st.write(data.head())

        concepts = np.array(data.iloc[:,0:-1])
        target = np.array(data.iloc[:,-1])

        if st.button("Run Learning Algorithm"):
            s_final, g_final = learn(concepts, target)
            st.write("Final Specific_h:")
            st.write(s_final)
            st.write("Final General_h:")
            st.write(g_final)

if _name_ == "_main_":
    main()
