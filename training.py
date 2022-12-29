import pandas as pd
import numpy as np

#read csv file
data = pd.read_csv('soc.csv')
#take the values of Gender and Estimated Salary as a numpy array (use .values)
X = np.array(data,columns=['Gender','EstimatedSalary'])


#take y as the last column - Purchased
y = pd.DataFrame(data['Purchased'])
#print the dimension of training set
print(X.ndim())
