# Write a functon that return lesser of two given numbers if both number are Even , but returns the greater if one or both numbers are Odd.

def Even( a , b ):
    if a % 2 == 0 and b % 2 == 0 :
        if a < b :
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return result
# Checking Lesser of Even Numbres 
result = Even(2,5)

print(result)  # Hurrah! its Working Fine


# Write a Fuction that take a two word string and retuns True if both words being with same letter.
# animal_cracker("Levelheadeed Llama") --> True
# animal_cracker("Crazy Kangaroo") --> False

def animal_cracker(text):
    wordlist = text.split()
    first = wordlist[0]
    second = wordlist[1]
    return first[0] == second[0]
check = animal_cracker("Levelheadeed Llama")
# check = animal_cracker("Crazy Kangaroo")
print(check)

#  Write a functions that return True if sum of the integers is 20 or if one of the integers is 20. If not , return False.

def makes_twenty( n1, n2 ):
    if n1+n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif 2 == 20:
        return True
    else:
         return False   
     
alpha = makes_twenty(20,12)
print(alpha)  
# Working Nice 
        
      
# Fuction Level1 Problems

# Write a function that capitalizes first and foruth letter of a name

def old_macdonald(name):
    # name.split()
    first = name[:3]
    second = name[3:]
    return first.capitalize() + second.capitalize()
# Check 
check = old_macdonald('tesla')
print(check) # Hurrah ! Working Fine.

# Write a function Given a sentence that return a sentence with Words reversed.

def master_yoda(sentence):
    wordlist = sentence.split()
    reversed_wordlist = wordlist[::-1]
    return reversed_wordlist
# Checking Reversed wordlist
bravo = master_yoda("The quick brown fox jumps over a lazy Dog.")
print(bravo)

# # Write a program that given an integer "n" retrun True if n is within 10 or either 100 or 200.

def almost_there( n ):
    return ( abs ( 100 - n ) <= 10 ) or ( abs ( 200 - n ) <= 10 )
# Checking 
almond = almost_there(209) 
print(almond)

# # Level-2 Problems

# # Write a function that counts the number of times given a pattern appears in a string inclding overlap.

# # Write a function that is given a list of integers, return True if array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range( 0 , len ( nums ) - 1 ):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        # else:
    return False
#  Check Answer   
result = has_33([1,3,1,3])
print(result) # Yeah Working Fine.

# Another Approach to do the same.

def has_33(nums):
    for i in range( 0 , len ( nums ) - 1 ):
        if nums[i:i+2 ] == [3,3]:
            return True
    return False
#  Check Answer   
result = has_33([1,3,3,2,2])
print(result) # Yeah Working Fine.



# Write a function that given a string , return a string where for every in the original there are three characters.

def paper_doll(string):
    # Declare stringn as an empty in text 
    result = ''
    for characters in string:
        # characters = characters*3
        result += characters*3 # this will add value in above empty string result.
    return result
# result1 = paper_doll("Mississipi")
result1 = paper_doll("Masacheusets")
print(result1)
    
    
    
# Write a function that take three integers between 1 and 11, if ther sum <= 21 return their   Sum. if sum exceeds 21 and there is an 11, reduce total sum by 10.Finally if sum exceeds 21 ,Return ""Bust"".

def Black_Jack( a , b , c ):
    if a + b + c <= 21:
        return a + b + c  
    elif a + b + c > 21 and a == 11 or b == 11 or c == 11:
        return a + b + c - 10
    elif a + b + c > 21:
        
        return "Bust"
result = Black_Jack(11,2,10) 
# Mohsin this approach failed.

                   
# Again attempt
def Black_Jack( a , b , c ):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [ a , b , c ] and sum([ a , b , c ]) <= 31:
        return sum([a,b,c]) - 10
    else: 
        return "Bust"
boom = Black_Jack(11,1,3) 
boom = Black_Jack(11,1,3) 
boom = Black_Jack(11,11,1) 
print(boom)

# Write a function that returns the sum of numbers in array, except ignore sections of numbers startin with a 6 and exteding to next 9 every 6 will be followed by atleast 9.Return 0 for no numbers.
def summer_69(arr):
    total = 0 
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add= False
            while not add:
                if num !=9:
                    break
                else:
                    add = True
                    break
    return total

summmer = summer_69([1,3,5])
print(summmer) # Kuch samj ni ayi is ki bas dekh k likh lia hai


# Challenging Problems 
# SpyGame : Write a function that takes in a list of integers and returns True if it contains 007 in order.

def spy_game( nums ):
    code = [ 0 , 0 , 7 , 'x' ]
    # [0,7,'x]
    # [7,'x]
    # ['x] length == 1
    for num in nums:
        if num == code[0]:
            code.pop(0)
            
    return len ( code ) == 1

spy_master = spy_game([1,2,4,0,0,7,5])
spy_master = spy_game([1,2,0,10,5,0,3,7])
spy_master = spy_game([1,2,3,4,0,0,7])
spy_master = spy_game([7,2,3,4,0,0])
print(spy_master)

# Write a function that returns the number of prime numbers that exists up to and including a given number.


def count_primes(num):
     # Check for 0 or 1 as input
    if num < 2:
        return 0
    # for 2 or greater numbers
    # A list to store prime numbers
    primes = [2]
    # Couner going up to input number.
    x = 3
    # x is going through every number upto input num
    while x <= num:
        # Check if x is prime or not
        # for y in range( 3 , x , 2):
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
        print(primes)
        
    return(len(primes))
result = count_primes(12)
# result = count_primes(100)
print(result)

   
                
# write a function that takes un a signle letter and returns 5 by 5 resperesntation of letter "A".


def print_big(letter):
    patterns = { 1:' * ' , 2: ' * * ', 3: ' *  * ', 4: ' ***** ', 5: ' **** ' , 6: '    *' , 7: '  *   ', 8: '*    *' , 9: ' *    '}
    alphabet = { 'A':[1,2,4,3,3] , 'B':[5,3,5,3,5], 'C':[4,9,9,9,4] , 'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
result_alpha = print_big('A')
print(result_alpha)


# Python HomeWork Assignment Questions

# Write a function that cann compute Volume of a sphere.
def vol(rad):
    return (4/3)*3.14*rad**3
volume = vol(3)
print('The volume of Sphere is :' , volume)


# Write a program that checks whether a number is in a given range (iclusive high or low)


for item in range(0,50):
    print(item)
    
def ran_check( num , low , high ):
    if num in range( low , high+1 ):
        print(f'{num} is in range of {low} and {high}')
    else:
        print('not in range')    
        
ran = ran_check(5,2,7)
print(ran)

# Write a python Function that accepts a string and caluclates the number of uppercase and lowercase letters.
def up_lows(str):
     uppercase = 0
     lowercase = 0
     for char in str:
         if char.isupper():
             uppercase += 1
         elif char.islower():
             lowercase += 1
         else:
             pass
     print(f"Original String: {str}")
     print(f"Lowercase String: {lowercase}")
     print(f"Uppercase String: {uppercase}")
str = "The Quick Brown Fox Jumos Over a lazy doG."
print(up_lows(str)) # Yeah Working Fine
           
# Write a python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    set = [ ]
    for number in lst: 
        if number not in set:
            set.append(number)
    return set
result = unique_list([3,4,5,6,7,8,8,34,45,5,5,5,5,6,6,7,7,8,8,9,2])
print(result)


     
    # Write a python Fuction that can multiply all numbers in a list.
    
def multiply( nums ) :
    total = 1
    for num in nums:
        total = total * num
    return total
result = multiply([1,2,3,4,-4,5,6])
print(result)

#  Wrtie a function to check a word is Plaindrome or not.

def palindrome(s):
    # Remove spaces from s
     s = s.replace('','')
    #  Check is string == revrsed version of the string.
     return s == s[::-1]
check = palindrome('maham')
print(f' Palindrome: {check} ')
 

# Wrte a function that check ehether a string is a pangram or not.

import string
def ispangram( str1 , alphabet = string.ascii_lowercase):
    # Creating a set of alphbet 
    alphaset = set( alphabet )
    print(alphaset)
    # Remove any spcaes from input string
    str1 = str1.replace( ' ', ' ' )
    # Convert all to lowercase.
    str1 = str1.lower()
    # Grab all unique letters from string set()
    str1 = set ( str1 )
    # Alpha set == string set input 
    return str1 == alphaset

pangram = ispangram("The quick brown fox jumps over the lazy dog")
pangram = ispangram("Pack my box with five dozen liquor jugs")
print(f' The is a pangram: {pangram}')
