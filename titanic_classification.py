# -*- coding: utf-8 -*-
"""TITANIC_CLASSIFICATION.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VsrFaperaSWk2HyCZ66_STOz8VMh3n-o
"""

from google.colab import files
from IPython.display import Image

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the train datasets
trn_df = pd.read_csv('train.csv')

trn_df.head()

trn_df.shape

trn_df.size

#check for non -null value in datset
trn_df.count()

# Check for missing values
missing_values = trn_df.isnull().sum()
missing_values

#visualize the missing data
sns.heatmap(trn_df.isnull(), cmap='winter', cbar=False)
plt.show()

numerical_columns = trn_df.select_dtypes(include=['int64', 'float64']).columns
trn_df[numerical_columns] = trn_df[numerical_columns].fillna(trn_df[numerical_columns].mean())

categorical_columns = trn_df.select_dtypes(include='object').columns
trn_df[categorical_columns] = trn_df[categorical_columns].fillna('Unknown')

# Chcek if any missing value is left after handling
print(trn_df.isnull().sum())

trn_df.columns

"""Factors that might influence a person's likelihood of survival in the context of the Titanic sinking for this case is Pclass(Passenger Class), sex, age,SibSp (Number of Siblings/Spouses),Parch (Number of Parents/Children),

lets visualize the dataset for Pclass, sex, age, SibSp (Number of Siblings/Spouses),Parch (Number of Parents/Children) for surived passengers
"""

# Visualizing survival based on socio-economic status (Pclass)
plt.figure(figsize=(6, 4))
sns.countplot(x='Pclass', hue='Survived', data=trn_df, palette='Oranges')
plt.title('Survival Count based on Socio-Economic Status (Pclass)')
plt.xlabel('Pclass (Passenger Class)')
plt.ylabel('Count')
plt.legend(title='Survived', loc='upper right', labels=['No', 'Yes'])
plt.show()

"""So, from here we can define 1st class passengers survived more as compared 2nd and 3rd class to"""

# Visualizing survival based on socio-economic status (Gender)
plt.figure(figsize=(6, 4))
sns.countplot(x='Sex', hue='Survived', data=trn_df, palette='Set3')
plt.title('Survival Count based on Socio-Economic Status (GENDER)')
plt.xlabel('SEX')
plt.ylabel('Count')
plt.legend(title='Survived', loc='upper right', labels=['No', 'Yes'])
plt.show()

"""So, from here we can define FEMALE passengers survived more as compared to male passengers"""

# Visualizing survival based on socio-economic status (age)
plt.figure(figsize=(7, 5))
sns.histplot(x='Age', hue='Survived', data=trn_df, kde=True, palette='coolwarm')
plt.title('Survival Count based on Socio-Economic Status Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Survived', loc='upper right', labels=['No', 'Yes'])
plt.show()

"""So, from here we can define 20-40 age passengers survived more as compared to older passengers"""

# Visualizing survival based on socio-economic status (siblings/spouses aboard (SibSp))
plt.figure(figsize=(6, 4))
sns.countplot(x='SibSp', hue='Survived', data=trn_df, palette='winter')
plt.title('Survival Count based on Number of Siblings/Spouses Aboard (SibSp)')
plt.xlabel('SibSp (Number of Siblings/Spouses)')
plt.ylabel('Count')
plt.legend(title='Survived', loc='upper right', labels=['No', 'Yes'])
plt.show()

# Visualizing survival based on socio-economic status (number of parents/children aboard (Parch))
plt.figure(figsize=(6, 4))
sns.countplot(x='Parch', hue='Survived', data=trn_df, palette='Set1')
plt.title('Survival Count based on Number of Parents/Children Aboard (Parch)')
plt.xlabel('Parch (Number of Parents/Children)')
plt.ylabel('Count')
plt.legend(title='Survived', loc='upper right', labels=['No', 'Yes'])
plt.show()

trn_df. head().T

# Drop columns that are not likely to be useful for prediction
columns_to_drop = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'Fare', 'Embarked']

trn_df1 = trn_df.drop(columns=columns_to_drop)

trn_df1

# Convert categorical features to numerical using LabelEncoder
label_encoder = LabelEncoder()
trn_df1['Sex'] = label_encoder.fit_transform(trn_df1['Sex'])

# Separate features and target variable
X = trn_df1.drop('Survived', axis=1)
y = trn_df1['Survived']

# Split the training data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
DecisionTreeClassifier()

#Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""Make Predictions
For this we have test dataset we will check for that
"""

test_df = pd.read_csv('test.csv')

test_df.head(2).T

# Drop columns that are not likely to be useful for prediction
columns_to_drop = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'Fare', 'Embarked']

test_df1 = test_df.drop(columns=columns_to_drop)

test_df1

# Convert categorical features to numerical using LabelEncoder
label_encoder = LabelEncoder()
test_df1['Sex'] = label_encoder.fit_transform(test_df1['Sex'])

test_df1.count()

"""#From above function we know that age has some missing value"""

# Check for missing values
missing_values = test_df1.isnull().sum()
missing_values

#Handle missing value
test_df1['Age'] = test_df1['Age'].fillna(test_df1['Age'].mean())

# Predict on the test Dataset
predictions = model.predict(test_df1)

"""# Create a DataFrame to store the predictions and save it as a CSV file"""

prediction_data=pd.DataFrame({'PassengerId': pd.read_csv('test.csv')['PassengerId'],'Survived': predictions})
prediction_data.to_csv('tit_prediction_df.csv', index=False)

# Load the tit_prediction_df datasets
predict_df = pd.read_csv('tit_prediction_df.csv')

predict_df.head(419)

"""So, here you can see for the test data prediction is done using decision tree classifier


Now lets do it using RandomForest cLassifier
"""

# Split the training data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the Random Forest Classifier model
model = RandomForestClassifier(random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Predict on the train dataset and check for accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""Make Predictions
For this we have test dataset we will check for that
"""

# Predict on the test set
predict_random= model.predict(test_df1)

prediction_data=pd.DataFrame({'PassengerId': pd.read_csv('test.csv')['PassengerId'],'Survived': predict_random})
prediction_data.to_csv('tit_prediction_df.csv', index=False)

# Load the tit_prediction_df datasets
predict_random_df = pd.read_csv('tit_prediction_df.csv')

predict_random_df. head(419)