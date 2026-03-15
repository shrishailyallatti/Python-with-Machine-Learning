gamelist=[0,1,2]
#display function
def display(gamelist):
    print('here is the current list:')
    print(gamelist)
    
#getting position
def pos():
    choice='wrong'
    withinrange=False
    while choice.isdigit()==False or withinrange==False:
        choice=input('enter the index position:')
        if choice.isdigit()==False:
            print('Invalid...! Try again')
        if choice.isdigit()==True:
            if int(choice) in [0,1,2]:
                withinrange=True
                
            else:
                withinrange=False
                
    return int(choice)

#getting replacement value frm+om the user

def repl(gamelist,position):
    value=input('enter the repl value:')
    gamelist[position]=value
    
    return gamelist

#gameon
def gameon():
    choice='wrong'
    while choice not in ['y','n']:
        choice=input('do u want to continue the game:').lower()
        if choice not in ['y','n']:
            print('yes or no.....?')
            
    if choice=='y' :
        return True
    else:
        return False
    
    
#putting all together
gamelist=[0,1,2]
game_on=True

while game_on==True:
    display(gamelist)
    
    position=pos()
    
    gamelist=repl(gamelist,position)
    
    from IPython.display import clear_output
    clear_output()
    
    display(gamelist)
    
    game_on=gameon()
    