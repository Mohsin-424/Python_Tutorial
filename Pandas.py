# Pandas an open source Python library for fast analysis and data cleaning and preperation. It has buit in visualization features.
# Pandas main topics are :   Series , DataFrames , MissingData , GroupBy , Merging ,Joining and Concatenating, Operations , Data Inputs and Outputs

# Series............................
import numpy as np
import pandas as pd

labels = ['a' , 'b' , 'c', 'd']
my_data = [12,32,43,4,544]
arr = np.array(my_data)
d = {'a':23 , 'b':34 , 'c':343}
print(labels , my_data , arr , d)
Series = pd.Series(data = my_data)
print(Series)






