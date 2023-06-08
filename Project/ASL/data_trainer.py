import pickle
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#Loads data from pickle file
data_dict = pickle.load(open('./ASL/data.pickle', 'rb'))

#Changes data into array
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

#Keeps equal number of mixed data in y_train and y_test, equal division of all labels
#x_train, x_test keeps 6:4 data per label to test and check
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.4, shuffle=True, stratify=labels)

#Trains data using fit function
model = RandomForestClassifier()
model.fit(x_train, y_train)

#Performs preditctions on test dataset
y_predict = model.predict(x_test)

#Checks accuracy, predicted vs actual
score = accuracy_score(y_predict, y_test)

print('{}% accuracy of tested models !'.format(score * 100))

#Saves the trained model into a binary file
file = open('./ASL/trained_model.p', 'wb')
pickle.dump({'model': model}, file)
file.close()
