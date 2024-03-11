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


