#tic_tac_toe

#Importing Modules to use
from os import system, name
import time
import random
import graphics_mod

################################################################################
#clear screen function
def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

################################################################################
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

# eight different win combinations:
def read_combos(update_combos):
    combinations = [
        choice[:3],
        choice[3:6],
        choice[6:9],
        choice[0:9:3],
        choice[1:9:3],
        choice[2:9:3],
        choice[0:9:4],
        choice[2:7:2]
        ]

    return combinations

def draw_check(draw, combinations):
    # check if Draw
    if len(used_choices)+1 > 8:
        draw = True
    else:
        draw = False
    
    return draw    
        
def win_check(win, combinations):
    #Check if Win  
    for combo in combinations:
        #print(f'combo : {combo}') / This line for debugging
        if combo.count(player) == 3:
            win = True
            break
        else:
            win = False

    return win                 

def lose_check(lose, combinations):
    #check if Lose    
    for combo in combinations:
        if combo.count(cpu) == 3:
            lose = True
            break 
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
        graphics_mod.tie()
    elif win == True:
        graphics_mod.winner()
    elif lose == True:
        graphics_mod.loser()

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
combinations = []
# Run Game
while game_on:
    # Clear screen
    clear()

    # Game Title Screen
    graphics_mod.game_intro()

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
            combinations = read_combos(combinations)
            win = win_check(win,combinations)
            draw = draw_check(draw,combinations)
            lose = lose_check(lose,combinations)

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
            combinations = read_combos(combinations)
            win = win_check(win,combinations)
            draw = draw_check(draw,combinations) 
            lose = lose_check(lose, combinations)

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
        #clear()
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





