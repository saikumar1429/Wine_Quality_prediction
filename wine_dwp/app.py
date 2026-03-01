import pickle
import streamlit as st
import numpy as np

model=pickle.load(open('wine.pkl','rb'))
st.title("Wine Quality Production")
st.write("Enter the Details")
alchol=st.number_input("Alcohol Content")
malic_acid=st.number_input("Malic Acid")
ash=st.number_input("Ash Content")
alcalinity_of_ash=st.number_input("Alcalinity of Ash")
magnesium=st.number_input("Magnesium Content")
total_phenols=st.number_input("Total Phenols")
flavanoids=st.number_input("Flavanoids Content")
nonflavanoid_phenols=st.number_input("Nonflavanoid Phenols") 
proanthocyanins=st.number_input("Proanthocyanins Content")
color_intensity=st.number_input("Color Intensity")
hue=st.number_input("Hue Value")
od280_od315_of_diluted_wines=st.number_input("OD280/OD315 of Diluted Wines")
proline=st.number_input("Proline Content")
if st.button("Predict Quality"):
        input_data = np.array([[alchol, malic_acid, ash, alcalinity_of_ash, magnesium,total_phenols, flavanoids, nonflavanoid_phenols,proanthocyanins, color_intensity, hue,od280_od315_of_diluted_wines, proline]])

        prediction=model.predict(input_data)[0]
        st.write("The predicted quality of the wine is:", prediction)
        class_names = ["Class 0", "Class 1", "Class 2"]
        result = class_names[prediction]

        st.success(f"The predicted wine class is: {result}")


