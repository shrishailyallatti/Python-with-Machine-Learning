#tic tac toe game
testboard=['#','x','o','x','o','x','o','x','o','x']

#function to display board
from IPython.display import clear_output
def display(board):
    clear_output()
    print(' | |  ')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' | |  ')
    print('------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' | |  ')
    print('------')
    print(board[1]+'|'+board[2]+'|'+board[3]) 
    print(' | |  ')
    
#assigning mark
def player_input():
    choice=' '
    while choice!='X' and choice!='O':
        choice=input('player1, choose X or O :').upper()
        if choice!='X' and choice!='O':
            print('Invalid! Choose X or O')
    if choice=='X':
        print("player1 marker:'X'")
        print("player2 Marker:'O'")
        return ('X','O')
    else:
        print("player1 marker:'O'")
        print("player2 Marker:'X'")
        return ('O','X')
    
#function place marker
def place_marker(board,mark,position):
    board[position]=mark
    

#function for win check
def win_check(board,mark):
    return (board[1]==mark and board[2]==mark and board[3]==mark or #bottom row
            board[4]==mark and board[5]==mark and board[6]==mark or #mid row
            board[7]==mark and board[8]==mark and board[9]==mark or #top row
            board[1]==mark and board[4]==mark and board[7]==mark or #across the 1st column
            board[2]==mark and board[5]==mark and board[8]==mark or #across the mid column
            board[3]==mark and board[6]==mark and board[9]==mark or #across the last column
            board[1]==mark and board[5]==mark and board[9]==mark or #across the diagnol
            board[3]==mark and board[5]==mark and board[7]==mark)   #across the diagnol



#function to decide who is first
import random
def choose_first():
    num=random.randint(0,1)
    if num==0:
        return 'player_2'
    else:
        return 'player_1'
    

#function to check place is free or not
def space_check(board,position):
    return board[position]==' '


#func to check board is full or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False #not full
    return True #board is full

#func for players choice
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or  space_check(board,position)==False:
        position=int(input('enter the position :(1-9)'))

    return position


#func to gameon or func to ask want to play again
def replay():
    choice=input('want to continue the game:(yes or No)').lower()
    return choice=='yes'


#putting all together
print('welcome to the tic tac toe game')
while True:
    board=[' ']*10
    player1_mark,player2_mark=player_input()
    turn=choose_first()
    print(turn+' will go first')
    play_ready=input('ready to play:(yes or no)')
    if play_ready[0].lower()=='y':
        gameon=True
    else:
        gameon=False
    while gameon:
        #player1 turn
        display(board)
        position=player_choice(board)
        place_marker(board,player1_mark,position)
        
        
        
        #win check
        if win_check(board,player1_mark):
            display(board)
            print('congrats player1 has won......')
            gameon=False
        else:
        #tie check
            if full_board_check(board):
                display(board)
                print('the game is draw')
                break
            else:
                turn='player_2'

        #player2 turn
        
        display(board)
        position=player_choice(board)
        place_marker(board,player2_mark,position)
        
        
        
        #win check
        if win_check(board,player2_mark):
            display(board)
            print('congrats player2 has won......')
            gameon=False
        else:
        #tie check
            if full_board_check(board):
                display(board)
                print('the game is draw')
                break
            else:
                turn='player_1'






        
    if not replay():
        break





















