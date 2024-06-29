# print([1,2,3])
# print([4,5,6])
# print([7,8,9])
# Accepting User Input Section
def domicile(row1, row2,row3):
    print(row1)
    print(row2)
    print(row3)
example_row = [1,2,3]
# Displaying Information Section 
print(domicile(example_row,example_row,example_row))


row1 = ['','','']
row2 = ['','','']
row3 = ['','','']

def product(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
result = product(row1,row2,row3)
print(result)
# Updating Row2

row2 = ['' , 'X', '']
result = product(row1,row2,row3)
print(result)
# Updating Row3

# row3 = ['' , '', 'X']
row1[0]= 'X' 
row3[2]= 'X' 
result = product(row1,row2,row3)
print(result)


# Validating User Input Moddule Section
s = input("Enter number:")
print(f' The number is: {s} ')

def user_choice():
    choice = 'WRONG'
    acceptable_range  = range(0,10)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ")
        # Digit Check
        if choice.isdigit() == False:
          print("Sorry That is not a digit!")
        #   Range Check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
                print(f"Great you are in range (0-10): {choice}")
            else:
                 print("Hey! Sorry you are out of range")
                 within_range = False
    return int(choice)

print(user_choice())
# .isdigit() method

some_value = '100'

some_value.isdigit()

print(int(some_value))

# Simple User Interaction Centre.....

# Write a program  that :

# 1.Can dsiplay a list of three input numbers
# 2.Have a option for user to choose an index positon and an input value.
# 3.Replace value at index position with user's choosend input Value.

#   Is game me h8m input number enter kre ge jo k replaceable hoga. Jab replace ho jae ga to new string uski replace wali jaga pe enter karna hoga. Phir Agar game k proceed karna hai to us k liye option "Yes or No" ka hoga. Is me ye optio agar UYes select kre ge to game me aik new replaced list ajae gi aur game continue rhe gi.

# Steps 
# 1. Display the game
# 2. Choose a Position
# 3. Replacement of Choice
# 4. gameon_choice


# Game Logic Step1
game_list = [ 0 , 1, 2 ] 

def display_game( game_list ):
    
    print( " Here is the current list:  " )
    
    print( game_list )
    
result = display_game( game_list )

print( display_game )

# Game Logic Step2 : Choice Position
def position_choice( ):
    mylist = [ '0' , '1' , '2' ]
    choice = ''
    while choice not in mylist:
        choice = input( "Pick a position: ( 0 , 1 , 2 ):  ")
        if choice not in mylist:
            print("Sorry! Invalid Choice. '\n' Try Again!")
    return int(choice)
position = position_choice()
print(position_choice)

# Game Logic Step3 : Replacement_choice
# Replacement_choice  has two input parameters ( game_list, position )

def replacement_choice( game_list , position ):
    user_placement = input("Type a string to place at position:  ")
    game_list[ position ] = user_placement
    return game_list
result = replacement_choice(game_list , 0)
result = replacement_choice(game_list , 1)
result = replacement_choice(game_list , 2)
print(result)

# Game Logic Step4 : Gameon_choice( I eant to continue game or Not)
def gameon_choice():
    choice = 'WRONG'
    mychoice = [ 'Y' , 'N' ]
    while choice not in  mychoice:
        choice = input( "Keep Playing ? ( Y or N )" )
        if choice not in mychoice:
            print("Sorry I dont understand , Please choose Y or N " )
    if choice == "Y":
        return True
    else:
        return False
result_alpha = gameon_choice()
print( result_alpha)

    # Combining all together

game_on = True
game_list = [ 0 , 1 , 2 ]
while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list , position)
    display_game(game_list)
    game_on = gameon_choice()
    
     
     
    