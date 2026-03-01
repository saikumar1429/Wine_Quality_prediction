
# Wine Quality Prediction using Machine Learning

This project is a Streamlit-based web application that predicts the class of wine based on its chemical properties. The model is trained using a supervised machine learning algorithm and saved as a serialized file (wine.pkl).

The application allows users to input various wine features and receive a predicted wine class instantly.

---

## Project Overview

The system uses a pre-trained machine learning model to classify wine into one of three categories based on chemical analysis.

The prediction is based on multiple input features such as alcohol content, acidity levels, phenols, and other chemical properties.

---

## Features

- Interactive Streamlit web interface
- Real-time prediction
- Pre-trained machine learning model (wine.pkl)
- Numerical feature input for wine characteristics
- Instant classification output

---

## Input Features

The model takes the following 13 features as input:

1. Alcohol
2. Malic Acid
3. Ash
4. Alcalinity of Ash
5. Magnesium
6. Total Phenols
7. Flavanoids
8. Nonflavanoid Phenols
9. Proanthocyanins
10. Color Intensity
11. Hue
12. OD280/OD315 of Diluted Wines
13. Proline

---

## Output

The model predicts one of the following wine classes:

- Class 0
- Class 1
- Class 2

The predicted class is displayed after clicking the "Predict Quality" button.

---

## Technologies Used

- Python
- Streamlit
- NumPy
- Scikit-learn (for model training)
- Pickle (for model serialization)

---

## Project Structure
