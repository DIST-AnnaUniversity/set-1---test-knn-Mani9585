import pandas as pd
import numpy as np

#read csv file
data = pd.read_csv('soc.csv')
#take the values of Gender and Estimated Salary as a numpy array (use .values)
X = data[['Gender','EstimatedSalary']].to_numpy()
#take y as the last column - Purchased
y = data[['Purchased']].to_numpy()
#print the dimension of training set
dims = (len(X),X.ndim)
print(dims)
