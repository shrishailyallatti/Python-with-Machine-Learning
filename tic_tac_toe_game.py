from IPython.display import clear_output
board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#func to display board
def display(board):
    clear_output()
    print('here is the current board:')
    print('--|---|--')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('--|---|--')

#fun to assign 'x' and 'o' to player
def player_input():
    choice=' '
    while choice not in ['X','O']:
        choice=input('player1, choose mark u want to be assigned as:').upper()
        if choice not in ['X','O']:
            print('invalid...! choose X or O..')
    if choice=='X':
        return ('X','O')
    else:
        return ('O','X')
    
#func to decide who is first
from random import randint
def who_first():
    num=randint(0,1)
    if num==0:
        return 'player 1'
    else:
        return 'player 2'
    
 #func to know given pos is empty or not
def space_check(board,position):
    if board[position]==' ':
        return True
    else:
        False
    
           
#func to get pos to mark
    
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or  not space_check(board,position):
        position=int(input('enter the position :(1-9)'))
        if (position) not in range(1,10) or not space_check(board,position):
            print('invalid position ! enter valid position')
    return int(position)


#func to check board is full or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False #not full
    return True #board is full
        
        

#func to mark
def marking(board,mark,position):
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
    

            
    
#func to play again
def replay():
    choice=input('do u want play again ?(yes or no)')
    return choice[0].lower()=='y'

#putting all together

#set up or declaring variable using func
while True:
    print('-----------------------------------------')
    print('welcome to the tic tac toe game')
    
    #player1 turn
    board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_mark,player2_mark=player_input()
    print('player1 mark:'+player1_mark)
    print('player2 mark:'+player2_mark)
    turn=who_first()
    print(turn+' will go first....')
    clear_output()
    choice=input('ready to play:(yes or no)')
    if choice[0].lower()=='y':
        gameon=True
    else:
        gameon=False
        break
    while gameon==True:
        display(board)
        if turn=='player 1':
            print('player 1 turn')
            position=player_choice(board)
            marking(board,player1_mark,position)
            
            if win_check(board,player1_mark):
                display(board)
                print('congrats ....player 1 has won')
                break
            else:
                if full_board_check(board):
                    display(board)
                    print('the game is draw')
                    break
                else:
                    turn='player 2'
                


#player2 turn

        display(board)
        if turn=='player 2':
             print('player 2 turn')
             position=player_choice(board)
             marking(board,player2_mark,position)
         
             if win_check(board,player2_mark):
                 display(board)
                 print('congrats ....player 2 has won')
                 
                 break
             else:
                 if full_board_check(board):
                     display(board)
                     print('the game is draw')
                     break
                     
                     break
                 else:
                     turn='player 1'



    if not replay():
        
        clear_output()
        print('-----------------------------------------')
        break
    



















