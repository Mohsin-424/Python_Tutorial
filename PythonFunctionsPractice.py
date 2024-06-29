list = [ 1, 2 , 3, 4, 5, 6, 7, 8, 9 , 10]
list.append(423)
list.reverse()
a = min(list)
print(a)
list.pop()
list.sort()
print(list)

example = [ 3 ,2 , 1 , 4, 5, 6, 7, 8, 9, 10 ]
from random import shuffle
shuffle(example)

# Same using Fucntions

def shuffled_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffled_list([2.4,4,5,35,6,754])
print(result)

#  Game Ball Find by Guess
mylist = [ '' , '' , 'O' ]
result1 = shuffled_list(mylist)
print(result1)

# Player_Guess function 
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: ")
# Return guess 
    return int(guess)
# Function Calling Back
myindex = player_guess()
print( myindex )


#  Function for Checking about  Guess
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct Guess")
    else:
        print("Incorrect Guess, Try Again")  
    return mylist
        # print(mylist)  
        
# Initial Guess 
mylist = [ '' , '' , 'O' ]
# Shuffle List 
mixed_list = shuffled_list(mylist)
# User_guess
guess = player_guess()
# Check Guess
check_guess(mixed_list,guess)

    
    
# *args  and **kwargs
# *args  

def myfunc(*args):
    for item in args:
        print(item)
func = myfunc((40,50,89,43.423,12))
print(func)

# Kwargs
def jelly(**jelly):
    print(jelly)
    if 'spade' in jelly:
        print("My fruit of choice is {}".format(jelly['spade']))
    else:
        print("No Spade found")
myjelly = jelly( spade = 'spade' , maggie = 'Noodles')
print(myjelly) 


# # Functions Basics
# def name_of_function(name ):
#     ""
#     Docstringg explains a function
#     ""
#     print("Hwellow" + name )
# name_of_function(Mohsin)
# def add_numbers( a, b ):
#     retrurn a + b
# result = add_numbers(32,32) 
# print(result)  


# def say():
#     print("Hello")
#     print("How")
#     print("are")
#     print("you")
# say()


def say(name):
    print(f"{name}")
    # return {name}  #  This line causes error here because reurn is ot used this way.
say("Hello Mohsin How are You?")



# Return stores value of output in a new variable. 
def function( a , b , c ):
    d = a + b + c
    return  d

result = function(12,23,4)
print(result)

# Write a Program to return even numbers in a number list.


# numlist = range(0,100)
def check_numbers( numlist ):
    for num in numlist:
        if num % 2 == 0:
            return True
        else:
            pass
    return False
# a = check_numbers([2,3,4,4,5,5,20,7,20,8,9,6])
# a = check_numbers([5,3])
a = check_numbers([5,3,2])
# a = check_numbers([2,3,4,4,5,5,20,7,20,8,9,6])
print(a)    
     
            
# Return All Even numbers of an array but find no even number then return anempty list.
even = []
def check(numlist):
    for num in numlist:
        if num  % 2 == 0:
            even.append(numlist)
        else:
            pass
    return even
a = check([2,3])
print(a)

# Tuple Unpacking with Python
 
stock_prices = [('Apple',320) , ('Banana',320) ,('Grapes',230),('Mango',600) ]
for item,price in stock_prices:
    # print(item)
    print([item,price])

        
employee_data = [('Apple',320) , ('Banana',320) , ('Grapes',230) , ('Mango',600) ]

def employee_check():
 current_max = 0
 employee_of_the_month = ''
for employee , hours in employee_check:
    if hours > current_max:
        current_max = hours
        employee_of_the_month = employee
    else:
        pass  
# return 
#     employee_of_the_month
#     current_max
            
# employee_check( work_hours )


    
  # Create a program that print word that start with character 's'.
st = ['Mohsin','AliRaza','Sara','Fariya']
for x in st:
    if x[0] == 'S':
        print(f'{x}')
    else:
        print("does ot start with 's'")   
 
#  AnotHER APPROACH USING .split method ,For Loop and If Codition
str = [ 'Mohsin' , 'Shoaib' , 'Saad' , 'Saeed' , 'Hamna' , 'Maham' ]
for y in str:
    y.split()
    if y[0] == 'S' or y[0] == 's':
        print(y)
    else:
        print(' Not start with "S" ')    
#  Another Approach  told by Programmer
string = "Pirint words that start with a charater   's'.Some People Have a sicnere Heart."
for word in string.split():
    if word[0].lower() == 's':
        print(f"{word}")
    else:
        print('Not start with "s" ')  
    
    
# Write  a program that uses range to print "Fizz"
alpha = range(0,10,2)
for i in alpha:
    print(i)
#   Write a program that can print all numbers bwteeen 0 and 50 divisible by 3
mylist = []
bravo = range(0,50)
for i in bravo:
    if i % 3 == 0:
        mylist.append(i)
        print(mylist)
        print(i)
        
# Solution both above problems by Prgrammer in Video

list(range(0,10,2))
# or
for i in range(0,10,2):
    print([i])
    print(i)
    
   #   Write a program that can print all numbers bwteeen 0 and 50 divisible by 3
 
[ x for bux in range(1,51) if bux % 3 == 0 ]
print(x)

# Go to string below and if length of word is even that print "Even".

mystrings = "Print every word in this sentence that has an even number of letters"
for word in mystrings.split():
    if len(word) %2 ==0:
        print(word) 
        print( word + "is even ") 
# Fizz Buzz Numbers Program 
list = range(1,100)
for num in list:
    
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz-Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    
    
    
# Use List Comprehension to create a list of first letter of every word given below in a string.
mylist = []
Pakistan = 'Create a list of first letters of every word in this string'    
for letter in mylist:
    
    mylist.append(Pakistan)

mystring = 'Mohsin'
buck = []
for letter in mystring:
    buck.append(letter)
    print(letter)
    print(buck)
    buck.reverse()
    print(buck)
    # print(mystring)
    
# Another Approach
# mylist = ['Mohsin' , 'Nouman','Hamza']
mylist = 'AlphaBravoCharlie'
myexam = []
for exam in mylist:
    myexam.append(exam)
    # print(myexam)
    print(exam)
    
    
# Another Approach
for um in range(0,100,2):
    
    if um % 2 == 0 or um % 3 == 0:
        print("Fizz")
    elif  um % 5 == 0 or um % 10 == 0:
        print("Buzz")    
    else:
        print("Fizz Buzz")
print(um) 
       
# Convert Fahrenheit to Celcius Degree Scale

Celcius = [ 32 , 37 , 98.6 , 273.1589 ]
Fahrenheit = [ ((9/5) * Cel + 32) for Cel in Celcius ]
print(Celcius)
print(Fahrenheit)
# Convert Fahrenheit to Celcus Scale
Fahrenheit = []
for Cel in Celcius:
    Fahrenheit.append((9/5)*Cel + 32)
    # print(Cel)
    print(Fahrenheit)
# Reattempt cECLIUS TO fAHRENHEIT sCALE
    # Celcius = input("Enter Celcius value")
    Celcius = []
    for Fahn in Fahrenheit:
        Celcius.append((5/9*Fahn - 32 ))
        print(Fahn)
        print(Fahrenheit)
        
        
# New List Mutliplcation Mehtods
my_list= [] 
for x in [2,3,4,5,5,6]:
    for y in [32,3232,13,10,20,32]:
        my_list.append( x*y )
print(my_list)
# ANother way to do same 
mylist = [x*y for x in [23,32,43,34,10] for y in [32,76,667,45,34]]




mystring = 'Mohsin'
buck = []
for letter in mystring:
    buck.append(letter)
    print(letter)
    print(buck)
    buck.reverse()
    print(buck)
    # print(mystring)
    
# Another Approach
# mylist = ['Mohsin' , 'Nouman','Hamza']
mylist = 'AlphaBravoCharlie'
myexam = []
for exam in mylist:
    myexam.append(exam)
    # print(myexam)
    print(exam)
    
    
# Another Approach
for um in range(0,100,2):
    
    if um % 2 == 0 or um % 3 == 0:
        print("Fizz")
    elif  um % 5 == 0 or um % 10 == 0:
        print("Buzz")    
    else:
        print("Fizz Buzz")
print(um) 
       
# Convert Fahrenheit to Celcius Degree Scale

Celcius = [ 32 , 37 , 98.6 , 273.1589 ]
Fahrenheit = [ ((9/5) * Cel + 32) for Cel in Celcius ]
print(Celcius)
print(Fahrenheit)
# Convert Fahrenheit to Celcus Scale
Fahrenheit = []
for Cel in Celcius:
    Fahrenheit.append((9/5)*Cel + 32)
    # print(Cel)
    print(Fahrenheit)
# Reattempt cECLIUS TO fAHRENHEIT sCALE
    # Celcius = input("Enter Celcius value")
    Celcius = []
    for Fahn in Fahrenheit:
        Celcius.append((5/9*Fahn - 32 ))
        print(Fahn)
        print(Fahrenheit)
        
        
# New List Mutliplcation Mehtods
my_list= [] 
for x in [2,3,4,5,5,6]:
    for y in [32,3232,13,10,20,32]:
        my_list.append( x*y )
print(my_list)
# ANother way to do same 
mylist = [x*y for x in [23,32,43,34,10] for y in [32,76,667,45,34]]


# Go to string below and if length of word is even that print "Even".

# mystrings = "Print every word in this sentence that has an even number of letters."
# for word in mystrings.split():
#     if len(word) %2 ==0:
#         # print(word) 
#         print( word + "is even" )
        
        
        
# mylist = []
st = 'Create a list of first letters of every word in this string'    
# for letter in mylist:
#     mylist.append(Pakistan)
#     print(letter)
[word[0] for word in st.split()]

    
    
    # Mohin Approach
mohsinlist = []
str = 'Create a list of first letters of every word in this string'
for word in str.split():
    mohsinlist.append(word[0])
    print(mohsinlist)
    
    
 
 
# Pythiin Basics Practice
def square(num):
    return num**2
mynums = [1,2,3,4,5,6,7,8,9,10]
for item in map(square,mynums):
    print(item)
print(list(map(square,mynums)))



# MAP Fucntion 
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]

# result = splicer(['Andrew', 'Mirathi','Blama','LLava'])
# result = splicer(['Mira', 'Mirathi','LLava'])
# print(result)

names = ['Andy' , 'LLAMA', 'LLAVA' ]
print(list(map(splicer,names)))

# Filter Function
def check_even(num):
    return num % 2 == 0
mynums = [ 1, 2, 12, 3 , 4 , 5 ]
a= list(filter(check_even,mynums))
print(a)

for i in filter(check_even,mynums):
    print(i)
    
    
# Lambda Functions 
def square(num):
    return num ** 2
print(square(12))

# Also same way ternary 
def square(num): return num**2
print(square(13))
#Same above using Lmabda Expression
a = lambda num: num **2
print(a(20))
# Lambda functions are used with map and filter functions
# Lambda with map function

alpha = list(map(lambda num:num**2, mynums))
print(alpha)

# Lambda with filter function

bravo = list(filter(lambda num: num %2 ==0 , mynums))
print(bravo)
# Lambda is an anonymous functions used with map annd filter functions. Like wee know if else can be written as ternary operators same way functions can be written as lambda funtions in a short way.


# Nestetd Statements and Scopes
# LEGB rule (Local variable, Enclosing Functions locals, Global Module, Buitl-in (Python))



x =  25
def placer():
    x = 50
    return x
result = print("This is a Local Funtuons" , x )
result1 = placer()
print(f'This is a global varible scope.  {result1}')

# Example following LEGB rule

# Global Variable Scope
name = "This is a global variable scope."
def greet():
    # Enclosing Function Variable Scope.
    name = 'This is Sammy.'
    def hello():
        # Local VarIable Scope
        name = 'This is now local'
        print('Hello' + name)
    hello()
greet()

#  Another Approach 
x = 50
def func(x):
    print(f' X is {x}')
    # Local reassignment of x
    x = 200
    print(f'I just locally changed value of X  = {x}')
    
print(func(x))
print(x)
#  Another Approach 
x = 50
def func():
    global x
    print(f' X is {x}')
    # Local reassignment of  global "x"
    x = "New Value"
    print(f'I just globally changed value of X  to {x}')
    
print(x)
print(func())
print(x)







