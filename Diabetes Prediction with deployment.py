# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14YFdmIlJXj2vbxk-KvfVYz0atqbhxXts
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset= pd.read_csv('diabetes.csv')

dataset_copy= dataset.copy(deep=True)

dataset_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = dataset_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

dataset_copy.isnull().sum()

dataset_copy.head()

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(dataset_copy.iloc[:, 1:-3])
dataset_copy.iloc[:, 1:-3] = imputer.transform(dataset_copy.iloc[:, 1:-3])

print(dataset_copy)

dataset_copy.head()

x= dataset_copy.iloc[:, : -1].values
y= dataset_copy.iloc[:, -1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

print(x_train)

print(x_test)

print(y_train)

print(y_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 150, criterion = 'entropy', random_state = 0)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

import pickle
filename = 'diabetes-prediction-rfc-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))