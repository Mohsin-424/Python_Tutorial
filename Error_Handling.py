# a =34
# b = 90
# print(a  + b )
# def Add( n1,n2):
#     print( n1 + n2 )
# print(Add(23,32))

# Try , Except
try:
    # Wnat to attempt this code
    # It may have an error
    result = 10 + 1
except:
    print(" Hey it looks like you are'nt adding Correctly! ")
else:
    print("Addition went well!")
    print(result)
    
# Try , Except , Finally

try:
    f = open( 'testfile' , 'w' )
    f = open( 'testfile' , 'r' )
    f.write("Write a test line")
except TypeError:
    print(" There was a type Error ")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I always run")


#  try , except , finally

def ask_for_init():
    while True:
        try:
            result = int(input("Please provide a number:  "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes Thank you")
            break
        finally:
            print( " End of try/except/finally " )
            print( " I will always run at the end. " )
            
pak = ask_for_init()
print(pak)


# Error Handling  Home-work

try:
    for i in ['a' , 'b' , 'c']:
        print(i**2)
except:
    print("General Error! Watch Out!")
    
    
#   Example 2
try:
    a = 9
    b = 0
    c = a / b
except:
    print("Error!")
finally:
    print("All Done!")
    
# Example 3  

def ask():
    while True:
        try:
            n = int(input("Enter a number"))
        except:
            print("Please try again!  ")
            continue
        else:
            break
    print("Your number squared is :  ")
    print(n**2)
a = ask()
print(a)
