import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

def heartAttack(list):
    dataset = pd.read_csv('Heart_Attack.csv') # IMPORTING THE DATASET
    dataset.head() # CHECKING THE DATASET IS IMPORTED SUCCESSFULLY

    dataset.shape # CHECKING NO OF ROWS AND COLUMNS

    dataset['class'].value_counts()

    dataset.groupby('class').mean()

    without_class = dataset.drop(columns = 'class' , axis = 1)
    only_class = dataset['class']
    print(only_class)

    scaler = StandardScaler()
    scaler.fit(without_class)
    standard_data = scaler.transform(without_class)
    print(standard_data) # All the data will have similar values

    data_1_copy = standard_data
    data_2_copy = only_class

    train_data_without_class,test_data_without_class ,train_with_class,test_with_class = train_test_split(data_1_copy,data_2_copy,test_size = 0.1 , stratify = data_2_copy,random_state = 2)

    # VERIFICATION OF TRAINING AND TEST DATA
    print(train_data_without_class.shape," + ",test_data_without_class.shape, " = ",without_class.shape)

    trainer = svm.SVC(kernel = 'linear')
    #TRAINING THE SUPPORTED VECTOR MACHINE CLASSIFIER
    trainer.fit(train_data_without_class,train_with_class)

    without_class_prediction = trainer.predict(train_data_without_class)
    data_accuracy = accuracy_score(without_class_prediction,train_with_class)

    print("ACCURACY : " , data_accuracy)

    without_outcome_test_prediction = trainer.predict(test_data_without_class)
    test_data_accuracy = accuracy_score(without_outcome_test_prediction,test_with_class)

    print("ACCURACY WITH TEST DATA : ",test_data_accuracy)

    data_input_numpy = np.asarray(list)
    input_data_reshape = data_input_numpy.reshape(1,-1)
    std_data = scaler.transform(input_data_reshape)
    predicted_data = trainer.predict(std_data)
    print(predicted_data)

    if(predicted_data[0] == 0):
      print("No Heart Issue")
      return 0
    else:
      print("Have Heart Issue")
    return 1