#count the number of male members in the file
import pandas as pd
data = pd.read_csv('soc.csv')
male = data['Gender].count_values()['Male']
print(male)
