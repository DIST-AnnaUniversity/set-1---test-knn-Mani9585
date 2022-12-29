import pandas as pd
import numpy as np

#read csv file
data = pd.read_csv('soc.csv')
#take the values of Gender and Estimated Salary as a numpy array (use .values)
X = pd.DataFrame(data,columns=['Gender','EstimatedSalary'])
X = np.array(X)


#take y as the last column - Purchased
y = pd.DataFrame(data['Purchased'])
#print the dimension of training set
print(X.shape())
