import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

# Load your dataset
data = pd.read_csv('dataset.csv')
print(data.head())

# Select relevant features and target variable
features = data[['Marital status', 'Application mode', 'Application order', 'Course', 'Daytime/evening attendance',
                 'Previous qualification', "Mother's qualification", "Father's qualification", "Father's occupation",
                 'Displaced', 'Debtor', 'Tuition fees up to date', 'Gender', 'Scholarship holder', 'Age at enrollment']]
target = data['Target']

# Perform label encoding if needed (e.g., for 'Gender' column)
le = preprocessing.LabelEncoder()
features['Gender'] = le.fit_transform(features['Gender'])

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=100)

# Create and train the RandomForestClassifier
classify = RandomForestClassifier(n_estimators=10, criterion="entropy")
classify.fit(x_train, y_train)

# Save the trained model to a file
pickle.dump(classify, open('model.pkl', 'wb'))

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))
print(type(model))
# Make a prediction using the loaded model
#prediction = model.predict([[1, 1, 1, 2, 1, 1, 13, 10, 6, 10, 1, 0, 0, 1, 1, 0, 20]])
# Use a row from your dataset for prediction
prediction = model.predict([[1, 1, 1, 2, 1, 1, 13, 10, 6, 10, 1, 0, 0, 1, 1]])

print(prediction)
