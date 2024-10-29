import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Importing the CSV Data
def diabeties_test(list):
    dataset = pd.read_csv('diabetes_dataset.csv')
    dataset.head() # Checking weather the dataset is loaded properly

    dataset.shape # Get No. of rows and Columns

    dataset['Outcome'].value_counts() #Tells Count of the values of the outcomes

    dataset.groupby('Outcome').mean()  # Get the mean around the values of the outcomes

    # Creating a new values with and without outcomes

    without_outcome = dataset.drop(columns = 'Outcome' , axis = 1)
    outcome = dataset['Outcome']
    print(without_outcome)

    scaler = StandardScaler()
    scaler.fit(without_outcome)
    standard_data = scaler.transform(without_outcome)
    print(standard_data) # All the data will have similar values

    data_without_outcome = standard_data
    data_outcome = dataset['Outcome']

    train_data_without_outcome,test_data_without_outcome ,train_with_outcome,test_with_outcome = train_test_split(data_without_outcome,data_outcome,test_size = 0.1 , stratify = data_outcome,random_state = 2)

    # VERIFICATION OF TRAINING AND TEST DATA
    print(train_data_without_outcome.shape," + ",test_data_without_outcome.shape, " = ",data_without_outcome.shape)

    trainer = svm.SVC(kernel = 'linear')
    #TRAINING THE SUPPORTED VECTOR MACHINE CLASSIFIER
    trainer.fit(train_data_without_outcome,train_with_outcome)

    without_outcome_prediction = trainer.predict(train_data_without_outcome)
    data_accuracy = accuracy_score(without_outcome_prediction,train_with_outcome)


    print("ACCURACY : " , data_accuracy)

    without_outcome_test_prediction = trainer.predict(test_data_without_outcome)
    test_data_accuracy = accuracy_score(without_outcome_test_prediction,test_with_outcome)

    print("ACCURACY WITH TEST DATA : ",test_data_accuracy)


    data_input_numpy = np.asarray(list)
    input_data_reshape = data_input_numpy.reshape(1,-1)
    std_data = scaler.transform(input_data_reshape)
    predicted_data = trainer.predict(std_data)
    print(predicted_data)

    if(predicted_data == 0):
      
      print("Do not have Diabetes")
      return 0
    else:
      print("Have Diabetes")

    return 1
# list = [4,110,92,0,0,37.6,0.191,30]
# diabeties_test(list)

