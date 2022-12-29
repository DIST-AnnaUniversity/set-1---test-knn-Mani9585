import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

##read csv file
data = pd.read_csv('soc.csv')
##take the values of Gender and Estimated Salary - X as a numpy array (use .values)
X = data[["Gender","EstimatedSalary"]].to_numpy()
#take y as the last column - Purchased
y = data[["Purchased"]].to_numpy()

#use label encoder to fit X
label_encoder = preprocessing.LabelEncoder()
data['Gender'] = label_encoder.fit_transform(data["Gender"])
data['EstimatedSalary'] = label_encoder.fit_transform(data["EstimatedSalary"])
#split training and testing to 80 and 20% and set the random state as 0
X = pd.DataFrame(data,columns=['Gender','EstimatedSalary'])
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state =0)
#use standard scaler and fit the values of X

##use the k value for neighbors as 4 with euclidean distance
knn = KNeighborsClassifier(n_neigbors = 4)
##predict the test portion of 20%
knn.fit(X_trian,y_train)

##how many predictions match with true values

