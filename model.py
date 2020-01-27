import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('diabetes.csv')


x= dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x=sc_x.fit_transform(x)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2)
classifier.fit(x,y)

pickle.dump(classifier, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
