# print( ' / ' * 100 ,' * ' * 100 , ' / ' * 100)
# # print( ' * ' * 100 )

# Step 1 Createa function for 3 by 3 board.

def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])
test_board = ['# ' , 'X' , 'O','X' , 'O','X' , 'O','X' , 'O' ,'X' ]
print(display_board(test_board))
# Another APPROACH
def display_board(board):
    
    print(board[7] +'--' + board[8] + '--' + board[9])
    
    print('|  |  |')
    
    print(board[4] + '--' + board[5] +   '--' + board[6])
    
    print('|  |  |')
    
    print(board[1] + '--' + board[2] + '--' +  board[3])
    
test_board = ['# ' , 'X' , 'O','X' , 'O','X' , 'O','X' , 'O' ,'X' ]

print(display_board(test_board))

#  Function to print player_input()
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Choose input markter: X or O")
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return(player1,player2)
result = player_input()
print(result)


        
