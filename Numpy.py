mylist1 = [ 1 , 2 , 3 , 3 ]
# Import Numpy 
import numpy as np
arr = np.array(mylist)
print(arr)

mymat = [ [1,2,3],[4,5,6],[7,8,9]]
mat = np.array(mymat)
print(mat)
# Syntax to create any matrix.......
mat1 = np.arange(0,34,3)
print(mat1)

mat2 = np.zeros((23,32))
print(mat2)

mat3 = np.ones((3,4))
print(mat3)
# Even spaced numbers Linspace
mat4 = np.linspace(0,5,10)
print(mat4)
# How to create an identity matrix using Numpy
mat5 = np.eye(5)
print(mat5)
# To create Random Numbers 
mat6 = np.random.rand(3)
print(f'The is random function generated matrix:  {mat6}')
mat7 = np.random.rand(3,5)
print(f'This is an example of rand:   {mat7}')
mat8 = np.random.randn(3)
print(f'This is an example of randn:   {mat8}')
mat9 = np.random.randint(1,100,23)
print(f'This is an example of randint:   {mat9}')


# genrate any array of random numebrs 
mat10 = np.random.randint( 0 , 50 , 5)
print(f'This is randomly gereated 20 numebrs array:   {mat10}')
# Reshape array
mat11 = mat10.reshape(5)
print(f' This is redhaped content:   {mat11}')


# Max , Min 
# Argmax and argmin will give us max and min value's position..
mat12 = mat10.argmax()
mat13 = mat11.argmin()
print(f' The max is {mat12} and min is: {mat13} ')



# Lecture 2:  NumPy Indexing and Selection...............
array = np.arange(0,10)
print(array)
print(array[0:6])
# array[:] = [10]
# print(array)
print(array[0:-1])
print(array[6:])
print(array[:6])
# Copy array
copy = array.copy()
print(f'The copy of {array} is :    {copy}')


# Create a 2d array
 
arr_2d = np.array([[2,3,4,5,5] , [4,5,6,6,7] , [2,3,4,5,6]])
print(f'The 3D matrix is: \n  {arr_2d}')

print(f'The 3D matrix indexed  is: \n  { arr_2d[:2 , 1:] }')

# Coditional Selection in NumPy.............................
new_list = [[2,3,4,5,7,45,98,78],[76,7,8,9,56,4,3,43]]
arr = np.array(new_list)
print(f'This is numpy array: \n {arr}')
print(f'This is numpy array: \n {arr > 45}')
print(f'This is numpy array: \n {arr < 45}')
print(f'This is numpy array: \n {arr == 45}')

numpyy = np.arange(100).reshape(10,10)
print(f"The numppy array is:{numpyy}")
print(f"The numppy  choosed array is:{ numpyy [5:9 , 8:6]}")


# Numpy Operations ..............................

# Array with array 
# array with scalars 
# Universal array Functions

new   = np.arange(0,10)

new1  = new - new 
new2  = new + new 
new3  = new / 100 
new4  = new * new
new5  = new - 100
new6  = new ** 2
new7  = np.sqrt(new)
new8  = np.max(new)
new9  = np.min(new)
newA= np.sin(new)
print(f'The  array is {new } subtraction :{new1} addistion is {new2} division : {new3} , multiplication: {new4} , arithematic {new5} , Power Exponent: {new6} , square root:{new7} , max : {new8}  , min: {min} , Trignometry : {newA} ')

# Overview of Quiz..................................

# Creat an array of 10 zeros
alpha  = np.ones(10)
alpha1  = np.zeros(10)
print( alpha , alpha1 )
# Createa an array of 0 fives...
alpha2 = np.zeros(10) + 5
print(alpha2)

# Create an array of all numbers from 10 to 50....
alpha3 = np.arange(10,51)
print(alpha3)
# Create an array of all even numbers from 10 to 50....
alpha4 = np.arange(10,52,2)
print(alpha4)

# Create a 3*3 matrix values ranging from  0 to 8
alpha5 = np.arange(9).reshape(3,3)
print(alpha5)
# Or
a = np.arange(9)
print(a.reshape(3,3))

# Create an identity matrix 3*3
alpha6 = np.eye(3)
print(alpha6)
# Use NumPy to generate random numbers between 0 and 1

alpha7 = np.random.randn(25)
print(alpha7)

alpha8 = np.random.randint(0,1)
print(alpha8)
# Create numbers from 0 and 1 

alpha9 = np.arange( 1 , 101 ).reshape( 10 , 10 ) / 100
print(alpha9)


# Cerate 20 lineraly spaced nmbers from 0 and 1......

alpha10 = np.linspace( 0 , 1 , 20 )
print( alpha10 )

# Indexing and Slicing ...............................
mat = np.arange( 1 , 26 ).reshape( 5 , 5)
print(mat)
print( mat[ 2: , 1: ] )
print( mat [ 3,4 ] )

# Write a "NumPy" program to create an array as output......

mat12 = mat.sum()
print(f'The sum is :   {mat12}')
# Get stadnard deviation of values in mat....
mat13 = mat.std()
print(f'The standard devaition is :  {mat13}')

# Give sum of all columns in mat......
mat14 = mat.sum( axis = 1 )
mat14 = mat.sum( axis = 0 )
print(f' The sum of all columns is :   {mat14}')



# Goraya Notes ......................
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr = np.array([[1, 2, 3], [4, 5, 6]])
# Similarly for 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# If we want to confirm dimensions of our Array, we can use:
print(arr.ndim)
# If we want to create 5 dimensional Array, we can use
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)

# NUMPY ARRAY INDEXING.....................................
Arr = np.array([1, 2, 3, 4])
print(f'This is NumPy array indexing position 1:  {Arr[1]} ')

# Negative Indexing:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])
# NUMPY ARRAY SLICING:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])


# Slicing 2-D Array:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f'This is 2D array indexing:   {arr[1, 1:4]}')
print(arr[0:2, 2])
print(arr[0:2, 1:4])

arr = np.array([1, 2, 3, 4])
print(arr.dtype)
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='i4')
# i1=8bit, i2=16bit, i4=32bit, i8=64bit
print(arr)
print(arr.dtype)

# NUMPY COPY & VIEW.............................
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(f'This is Copy:  ...  {x}')
# This will make a copy of original Array and display it

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
arr[0] = 98765
print(arr)
print(x)
print(f'Base of x.....  {x.base}')
print(f'Base of y.....  {y.base}')


# SHAPE OF AN ARRAY:
 
# output in the form of tuple.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f'This is shape of array:    {arr.shape}')


# RESHAPE OF AN ARRAY:
# Reshaping means changing the shape of an array. The shape of an array is the 
# number of elements in each dimension. By reshaping we can add or remove 
# dimensions or change number of elements in each dimension.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
newarr = arr.reshape(2, 3, 2)
print(f'This is reshaped array:  \n  {newarr}')

# Own Practice Sin ,Cos,Tan = Trigonometric functions.....
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)
print( arr2 + 10 )
print( np.sin( arr2 ) )
print( np.cos( arr2 ) )
print( np.tan( arr2 ) )
print( np.sinh( arr2 ) )
print( np.cosh( arr2 ) )
print( np.isinf( arr2 ) )
print( arr2.reshape( -1 , 1 ) )
print( np.isnan( arr2 ) )
print( f'This is transpose:.... \n{np.transpose( arr2 ) }')
print( f'This is Means value:.... \n{np.mean( arr2 ) }')
print( f'This is length :.... \n{ len( arr2 ) }')
# Dpt and Cross Product.........................
reshaped_arr = np.random.randn(3,3)
print(f" This is reshaped array:   {reshaped_arr} ")
product = np.dot(reshaped_arr, arr2)
print(f" This is Dot Product: \n  {np.dot(reshaped_arr,arr2)} ")
print(f" This is Cross Product: \n  {np.cross(reshaped_arr,arr2)} ")

arr = np.array([[1, 2, 3], [4, 5, 6]])
average = np.mean(arr)
# Axis = 1 for Rows...........
row_means = np.mean(arr, axis=1)
print(average) # Output: 3.5
print(row_means) # Output: [2. 5.]

arr = np.array([[1, 2, 3], [4, 5, 6]])
max_val = np.max(arr)
# Axis = 0 for Coulmns.............
col_min = np.min(arr, axis=0)
print(max_val) # Output: 6
print(col_min) # Output: [1 2 3]
# Top create a Linera Space........ Liek wise used in Army intial Intelligence Test...
values = np.linspace(0, 10, num=5)
print(f'This is Linear Space:....... \n{values}')
# Array Concatenation
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
# Concatenate along the 0th axis (default)
result = np.concatenate((arr1, arr2, arr3))
result1 = np.vstack((arr1, arr2, arr3))
result2 = np.hstack((arr1, arr2, arr3))

print(f'This is Concatenated Array:....{result}')
print(f'This is Vertically Stack arrays Array:....\n{result1}')
print(f'This is Horizontally Stack arrays Array:....\n{result2}')

# Inversse of a matrix
matrix = np.array([[1, 2], [3, 4]])
# Calculate the inverse of the matrix
print(f'This is a matrix \n {matrix}')
inverse = np.linalg.inv(matrix)
print(f'This is Inverse of a Matrix:...\n{inverse}')
#  Perform eigenvalue decomposition
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f'These are eigenvalues: \n{eigenvalues}')
print(f'These are eigenvectors: \n{eigenvectors}')

# Perform singular value decomposition
U, s, V = np.linalg.svd(matrix)
print("U:", U)
print("s:", s)
print("V:", V)
# Split an array
arr5 = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr5, 3)
print(f'This array is splitted:  {split_arr}')


# Concatenate arrays
arr3 = np.array([1, 2, 3])
arr4 = np.array([4, 5, 6])
concatenated_arr = np.concatenate((arr3, arr4))
print(concatenated_arr)
# Output: [1 2 3 4 5 6]
# Split an array
arr5 = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr5, 2)
print(split_arr)
# Output: [array([1, 2, 3]), array([4, 5, 6])]
# Stack arrays vertically (row-wise)
arr6 = np.array([1, 2, 3])
arr7 = np.array([4, 5, 6])
vertical_stack = np.vstack((arr6, arr7))
print(vertical_stack)
# Output:
# [[1 2 3]
# [4 5 6]]
# Stack arrays horizontally (column-wise)
arr8 = np.array([1, 2, 3])
arr9 = np.array([4, 5, 6])
horizontal_stack = np.hstack((arr8, arr9))
print(horizontal_stack)


# Calculating Mean , Median ,Mode in NumPy
import numpy as np
from scipy import stats
dataset = np.array([10,12,12, 15, 18, 20,19, 22,33, 25,33, 30, 35, 40, 45,33])
# Mean
mean = np.mean(dataset)
print("Mean:", mean)
# Median
median = np.median(dataset)
print("Median:", median)
# Mode
mode = stats.mode(dataset)
print("Mode:", mode.mode)

# Example dataset
dataset = np.array([10, 12, 15, 18, 20, 22, 25, 30, 35, 40, 45])
# Range
range_val = np.max(dataset) - np.min(dataset)
print("Range:", range_val)
# Variance
variance = np.var(dataset)
print("Variance:", variance)
# Standard Deviation
std_dev = np.std(dataset)
print("Standard Deviation:", std_dev)
  
  
# Example dataset
dataset = np.array([12, 18, 20, 23, 29, 32, 36, 40, 42, 50])
# Percentiles
percentile_75 = np.percentile(dataset, 75)
print("75th Percentile:", percentile_75)
# Quartiles
quartiles = np.percentile(dataset, [25, 50, 75])
q1, median, q3 = quartiles
print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
# Z-scores
mean = np.mean(dataset)
std_dev = np.std(dataset)
value = 32
z_score = (value - mean) / std_dev
print("Z-score:", z_score)







import numpy as np
import matplotlib.pyplot as plt
# Generate some random data
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)
# Univariate plot (Histogram)
plt.figure(figsize=(8, 4))
plt.hist(x, bins=20, color='blue', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Frequency')
plt.title('Univariate Plot')
plt.show()
# Bivariate plot (Scatter plot)
plt.figure(figsize=(6, 6))
plt.scatter(x, y, color='red', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bivariate Plot')
plt.show()
# Multi-plots (Line plot and Bar plot)
plt.figure(figsize=(10, 4))
# Line plot
plt.subplot(1, 2, 1)
x_line = np.linspace(0, 10, 100)
y_line = np.sin(x_line)
plt.plot(x_line, y_line, color='green')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plot')
# Bar plot
plt.subplot(1, 2, 2)
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 15]
plt.bar(categories, values, color='purple')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.tight_layout()
plt.show()

