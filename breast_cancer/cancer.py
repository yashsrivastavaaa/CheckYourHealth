import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

def b_cancer(list):
    # IMPORTING THE DATASET
    x = pd.read_csv('data_breast-cancer-wiscons.csv')  
    # Replace 'B' and 'M' with 0 and 1 in the 'diagnosis' column
    x.iloc[:, 1].replace({'B': 0, 'M': 1}, inplace=True)  

    # Select relevant features and the target variable
    dataset = x[['diagnosis', 'texture_mean', 'area_mean', 'concavity_mean', 'area_se', 'concavity_se','fractal_dimension_se', 'smoothness_worst', 'concavity_worst', 'symmetry_worst','fractal_dimension_worst']]

    # Separate features and target variable
    X = dataset.drop(columns='diagnosis', axis=1)
    y = dataset['diagnosis']

    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.1, stratify=y, random_state=2)

    # Train the SVM classifier
    classifier = svm.SVC(kernel='linear') 
    classifier.fit(X_train, y_train)

    # Evaluate the model on training data
    y_train_pred = classifier.predict(X_train)
    train_accuracy = accuracy_score(y_train_pred, y_train)
    print("Accuracy on training data:", train_accuracy)

    # Evaluate the model on testing data
    y_test_pred = classifier.predict(X_test)
    test_accuracy = accuracy_score(y_test_pred, y_test)
    print("Accuracy on testing data:", test_accuracy)

    data_input_numpy = np.asarray(list)
    input_data_reshape = data_input_numpy.reshape(1,-1)
    std_data = scaler.transform(input_data_reshape)
    predicted_data = classifier.predict(std_data)
    print(predicted_data)

    if(predicted_data[0] == 0):
      print("You May have benign")
      return 0
    else:
      print("Malignant")
    return 1