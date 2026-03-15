# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 09:40:31 2026

@author: Y S
"""

#--------Guesssing game------

gamelist=[' ','o',' ']
print('welcome to the guessing game')
print('guess the string position in the shuffled list')
def guess():
    user='false'
    withinrange=False
    while user.isdigit()==False or withinrange==False:
        user=input('enter the index postion(0,1,2):')
        if user.isdigit()==False:
            print('invalid...! enter number(0,1,2)')
        if user.isdigit()==True:
            if user in [0,1,2]:
                withinrange=True
            else:
                withinrange=False
                
        return int(user)
        
        
        
        
        
def guess_check(user_guess):
    if gamelist[user_guess]=='o':
        print('correct.......')
    else :
        print('wrong....!better luck next time.....')
        
        
def gameon_choice():
    
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y','N']:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Would you like to keep playing? Y or N ").upper()

        
        if choice not in ['Y','N']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
        
            
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
            
    
    # Optionally you can clear everything after running the function
    # clear_output()
    
    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False
    
    
#putting all together
from random import shuffle
gameon=True
gamelist=[' ','o',' ']
while gameon==True:
    
    print(f'here is the current game list:{gamelist}')
    shuffle(gamelist)
    position=guess()
    guess_check(position)
    print(gamelist)
    gameon=gameon_choice()
    







