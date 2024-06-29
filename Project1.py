#   Tic Tac Toe Game
def work_board( board ):
    print(' ' + board[6] + '|' + board[7] + '|' + board[8] )
    print('  | |' )
    print('------')
    print( " " + board[3] + '|' + board[4] + '|' + board[5] )
    print('  | |' )
    print('------')
    print( ' ' + board[0] + '|' + board[1] + '|' + board[2] )
    print('  | |' )
    print('-------')
    
test_board = ['#','O','X' , 'O','X' , 'O','X', 'O','X']
result = work_board(test_board)
print(result)
#  Take  user input whether user want to take  'O' or 'X

def player_input():
    
    
    '''
    OUTPUT = (player_1_marker , player_2_marker)
    
    '''
    marker = ''
    while marker != 'O' and marker != 'X':
        marker = input("Choose makrker value: O or X:  ").upper()
    if marker ==    'X':
        return ( 'X', 'O' )
    else:
        return ( 'O' , 'X' )
# Printing same output    
(player_1_marker, player_2_marker) = player_input()
result = player_input()
print( result )


# Step 3 Put a placehlder marker where ever we want

def place_marker(board , marker , position):
    board[position] = marker
    
print(test_board)
place_marker(test_board , '$' , 5 )
print( work_board ( test_board ) )

#  Step 4 : Wtiting a function takes a baord and marks ( X or O ) and then checks to see if mark has won or not.
def win_check(board, mark):
    # Win Tic Tac Toe
    return ((board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[6] == mark and board[3] == mark and board[0] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[6] == mark and board[4] == mark and board[2] == mark) or
            (board[8] == mark and board[4] == mark and board[0] == mark))


result = win_check(test_board, 'X')

print(result)
# Step 6:   Write a function that uses reandom module to randomly decide which player goes first. Return a string of which player goes first.

import random

def choose_first():
    flip = random.randint( 0 , 1 )
    if flip == 0:
        return 'Player_1'
    else:
        return 'Player_2'
    
# Step 6: Write a function that returns a boolean indicating whether a space on the baord is freely available.

def space_check( baord, position ):
    return baord[position] ==  ' ' 
    
#  Step7: Write a function that checks if board is full and returns a booleab value. True if full, False otherwise.
def full_baord(board):
    for i in range( 1 , 10):
        if space_check( board, i ):
            return False
         # Board is full if we return True.
    return True
# Step8:  Write a function that asks for Player's next position
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board ,  position ):
        position = int(input("Choose a position: (1-9)" ))
    return position
        
        