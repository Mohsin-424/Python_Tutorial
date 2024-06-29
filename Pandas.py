# Pandas an open source Python library for fast analysis and data cleaning and preperation. It has buit in visualization features.
# Pandas main topics are :   Series , DataFrames , MissingData , GroupBy , Merging ,Joining and Concatenating, Operations , Data Inputs and Outputs

# Series............................
import numpy as np
from numpy.random  import rand
import pandas as pd

labels = ['a' , 'b' , 'c', 'd']
my_data = [12,32,43,4,544]
arr = np.array(my_data)
d = {'a':23 , 'b':34 , 'c':343}
print(labels , my_data , arr , d)
Series = pd.Series(data = my_data)

print(my_data )
print(Series)
print(f'This is Python Series:....  \n{Series} ')


# Pandas Practice

ser1 = pd.Series([1,2,3,4] ,['USA' , 'Germany' , 'Italy' , 'Japan'])
ser2 = pd.Series([1,2,3,4] ,['USA' , 'UK' , 'USSR' , 'Japan'])
# print(ser1)
print( ser1 + ser2 )

# Data Frames...........................................
np.seed(101)
df = pd.DataFrame(rand(5,4), ['A' ,'B' , 'C' ,'D','E'] , ['W','X' ,'Y','Z'])
print(df)
"git branch -m main Branch1
git fetch origin
git branch -u origin/Branch1 Branch1
git remote set-head origin -a"