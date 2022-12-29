import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

##read csv file
##take the values of Gender and Estimated Salary - X as a numpy array (use .values)
#take y as the last column - Purchased


#use label encoder to fit X

#split training and testing to 80 and 20% and set the random state as 0
#use standard scaler and fit the values of X

##use the k value for neighbors as 4 with euclidean distance

##predict the test portion of 20%

##how many predictions match with true values

