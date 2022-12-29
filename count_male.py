#count the number of male members in the file
import pandas as pd
data = pd.read_csv('soc.csv')
male = sum((data['Gender'] == 'Male'))
print(male)
