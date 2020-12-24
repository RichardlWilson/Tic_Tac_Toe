#tic_tac_toe

#Importing Modules to use
from os import system, name
import time
import random

################################################################################
#clear screen function
def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')
################################################################################
# Game Graphics

# Game Tile Page with Instructions to play 
def game_intro():
    print('''
             ######## ####  ######     ########    ###     ######     ########  #######  ########              
 ##   ##        ##     ##  ##    ##       ##      ## ##   ##    ##       ##    ##     ## ##           ##   ##  
  ## ##         ##     ##  ##             ##     ##   ##  ##             ##    ##     ## ##            ## ##   
#########       ##     ##  ##             ##    ##     ## ##             ##    ##     ## ######      ######### 
  ## ##         ##     ##  ##             ##    ######### ##             ##    ##     ## ##            ## ##   
 ##   ##        ##     ##  ##    ##       ##    ##     ## ##    ##       ##    ##     ## ##           ##   ##  
                ##    ####  ######        ##    ##     ##  ######        ##     #######  ########                     
        \n    Welcome to Tic Tac Toe!\n
        • The object of the game is to get three in a row.
        • 'X' will always go first.
        • Select a number on the grid to make your move.\n
        ''')

# Graphic to display if game is a Draw
def tie():
    print('''
:::::::::  :::::::::      :::     :::       ::: 
:+:    :+: :+:    :+:   :+: :+:   :+:       :+: 
+:+    +:+ +:+    +:+  +:+   +:+  +:+       +:+ 
+#+    +:+ +#++:++#:  +#++:++#++: +#+  +:+  +#+ 
+#+    +#+ +#+    +#+ +#+     +#+ +#+ +#+#+ +#+ 
#+#    #+# #+#    #+# #+#     #+#  #+#+# #+#+#  
#########  ###    ### ###     ###   ###   ### 
        ''')

# Graphic to display CPU wins game
def loser():
    print('''
:::   :::  ::::::::  :::    :::      :::        ::::::::   ::::::::  :::::::::: 
:+:   :+: :+:    :+: :+:    :+:      :+:       :+:    :+: :+:    :+: :+:        
 +:+ +:+  +:+    +:+ +:+    +:+      +:+       +:+    +:+ +:+        +:+        
  +#++:   +#+    +:+ +#+    +:+      +#+       +#+    +:+ +#++:++#++ +#++:++#   
   +#+    +#+    +#+ +#+    +#+      +#+       +#+    +#+        +#+ +#+        
   #+#    #+#    #+# #+#    #+#      #+#       #+#    #+# #+#    #+# #+#        
   ###     ########   ########       ########## ########   ########  ########## 
        ''')

# Graphic to display Player wins game
def winner():
    print('''
:::       ::: ::::::::::: ::::    ::: ::::    ::: :::::::::: :::::::::  
:+:       :+:     :+:     :+:+:   :+: :+:+:   :+: :+:        :+:    :+: 
+:+       +:+     +:+     :+:+:+  +:+ :+:+:+  +:+ +:+        +:+    +:+ 
+#+  +:+  +#+     +#+     +#+ +:+ +#+ +#+ +:+ +#+ +#++:++#   +#++:++#:  
+#+ +#+#+ +#+     +#+     +#+  +#+#+# +#+  +#+#+# +#+        +#+    +#+ 
 #+#+# #+#+#      #+#     #+#   #+#+# #+#   #+#+# #+#        #+#    #+# 
  ###   ###   ########### ###    #### ###    #### ########## ###    ###
        ''')

# Graphic to display game board
def display_grid():
    #clear()
    print(f'''
        Tic Tac Toe\n
        *******************\n
        *  {choice[6]}  *  {choice[7]}  *  {choice[8]}  *\n
        *******************\n
        *  {choice[3]}  *  {choice[4]}  *  {choice[5]}  *\n
        *******************\n
        *  {choice[0]}  *  {choice[1]}  *  {choice[2]}  *\n
        *******************\n
        ''')    
################################################################################
# Player Selection, CPU Assignment, Starting Turn Assignment
#The Player plays against the CPU

# Player Selection
def player_selection(player):
    valid_players = ['X', 'O']
    player = '*'
    while player not in valid_players: 

        player = input('    Do you want to be X or O: ').upper()

        if player not in valid_players:
            clear()
            print('Sorry that is not a option!')

    return player

# CPU Assignment
def cpu_assignment(cpu):
    if player == 'X':
        cpu = 'O'
    else:
        cpu = 'X'
    
    return cpu

# Turn Assignment
def turn_assignment(turn):
    if player == 'X':
        turn = True
    else:
        turn = False

    return turn            

################################################################################
# Code for Player's and CPU's Turn

# Player Turn
def players_move(turn):

    while turn == True:
        # Display the turn number
        print('turn # ' + str(len(used_choices)+1))

        # Ask Player for board position to mark
        move = input('Enter a number (1-9) to place your move: ')

        # Clear screen and display the updated board
        clear()
        display_grid()

        # Validate Players input is correct
        try:
            move = int(move)
        except:
            print('Sorry that is not (1-9)')
            continue
        
        if move-1 in used_choices:        
            print('This place has already been used')

        elif move-1 not in range(0,9):
            print('Sorry that is not (1-9)')    

        # If Players input is valid, Player's input is the index position -1 
        # of choice[index]. Then copies index number to used_choices[].
        # Turn Ends 
        else:    
            choice[move-1] = player
            used_choices.append(move-1)

            # Turn ends
            turn = False

    return turn 

#CPU turn
def cpu_move(turn):

    while turn != True:
        # Display the turn number
        print('turn # ' + str(len(used_choices)+1))
        print("CPU's turn, Please wait.")
        
        # CPU Waits a random time intrival before making a move to give a more
        # human like feel. 
        random_num = [num for num in range(0,9)]
        time.sleep(random.choice(random_num))

        # CPU selects a random value from choice_ref -1 and names it as index.
        index = int(random.choice(choice_ref))-1

        # Checks if value index is already been used
        while index in used_choices:
            index = int(random.choice(choice_ref))

        # If index has not been used use index to select position in
        # choice[index] to place a mark on the board
        used_choices.append(index)
        choice[index] = cpu

        # Turn ends
        turn = True

    return turn    

################################################################################
#check if win , lose or draw
def draw_check(draw):
    # check if Draw
    if len(used_choices)+1 > 8:
        draw = True
        return draw
    else:
        draw = False
        return draw    
        
def win_check(win):
    #Check if Win    
    if choice[:3].count(player) == 3:
        win = True
        return win    

    elif choice[3:6].count(player) == 3:
        win = True
        return win

    elif choice[6:9].count(player) == 3:
        win = True
        return win 
    elif choice[0:9:3].count(player) == 3:
        win = True
        return win
    elif choice[1:9:3].count(player) == 3:
        win = True
        return win
    elif choice[2:9:3].count(player) == 3:
        win = True
        return win            
    elif choice[0:9:4].count(player) == 3:
        win = True
        return win 
    elif choice[2:7:2].count(player) == 3:
        win = True
        return win 
    else:
        win = False
        return win                  

def lose_check(lose):
    #check if Lose    
    if choice[:3].count(cpu) == 3:
        lose = True
        return lose
    elif choice[3:6].count(cpu) == 3:
        lose = True
        return lose
    elif choice[6:9].count(cpu) == 3:
        lose = True
        return lose 
    elif choice[0:9:3].count(cpu) == 3:
        lose = True
        return lose
    elif choice[1:9:3].count(cpu) == 3:
        lose = True
        return lose
    elif choice[2:9:3].count(cpu) == 3:
        lose = True
        return lose            
    elif choice[0:9:4].count(cpu) == 3:
        lose = True
        return lose 
    elif choice[2:7:2].count(cpu) == 3:
        lose = True
        return lose
    else:
        lose = False
        return lose

################################################################################
#End of game
# Check win, Draw, or Lose Status is True
def end_status(win,draw,lose):
    print('end_status')
    print(win,draw,lose)
    if draw == True:
        tie()
    elif win == True:
        winner()
    elif lose == True:
        loser()

# Asks Player if they want to play again or leave game
def replay(game_on):
    user_input = '*'

    while user_input != 'Y' and user_input != 'N':
        user_input = input('Do you want to play again? Y or N: ').upper() 

        if user_input != 'Y' and user_input != 'N': 
            print('Sorry that is not a valid choice')  

        elif user_input == 'Y':
            game_on = True
        elif user_input == 'N':
            game_on = False
        
    return game_on

################################################################################
# Main Game Code

#initial game setup    
choice_ref = ('1','2','3','4','5','6','7','8','9')
choice = [' ' for spot in range(0,9)]
used_choices = []
player = '*'
cpu = '*'
turn= '*'
progress = True
game_on = True
draw = False
win = False
lose = False

# Run Game
while game_on:
    # Clear screen
    clear()

    # Game Title Screen
    game_intro()

    # Player Select X or O
    player = player_selection(player)

    # Assigns CPU opposite of Player's choice
    cpu = cpu_assignment(cpu)

    #sets who goes first based on Player Selection
    turn = turn_assignment(turn)

    #while playing game
    while progress == True:

        # player Turn
        while turn == True:
            clear()
            display_grid()
            win = win_check(win)
            draw = draw_check(draw)
            lose = lose_check(lose)

            if win or draw or lose:
                progress = False
                break

            # player makes move
            turn = players_move(turn)
        
        # cpu turn    
        while turn == False:
            clear()
            display_grid()

            # check status
            win = win_check(win)
            draw = draw_check(draw) 
            lose = lose_check(lose)

            if win or draw or lose:
                progress = False
                break

            # cpu makes move
            turn = cpu_move(turn)
      
    clear()               
    end_status(win,draw,lose)

    #asks if want to play again
    game_on = replay(game_on)
    if game_on == False:
        # Prints a meassage and leaves game
        clear()
        print('''Thank you for playing!!!!!!''')        
    else:
        # Resets initial game setup
        choice = [' ' for spot in range(0,9)]
        used_choices.clear()
        player = '*'
        cpu = '*'
        turn= '*'
        progress = True
        game_on = True
        draw = False
        win = False
        lose = False





