#tic_tac_toe

#Importing Modules to use
from os import system, name
import time
import random
import graphics_mod

################################################################################
#Clear screen
def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

################################################################################
# Player Selection, CPU Assignment, Starting Turn Assignment
#The Player plays against the CPU

# Player Selection
def player_selection():
    valid_players = ['X', 'O']
    player = '*'
    while player not in valid_players: 

        player = input('    Do you want to be X or O: ').upper()

        if player not in valid_players:
            clear()
            print('Sorry that is not a option!')
        elif player == 'X':
            cpu = 'O'
        else:
            cpu = 'X'    

    return (player, cpu)

# Turn Assignment
def turn_assignment():
    if player == 'X':
        turn = True
    else:
        turn = False

    return turn            

################################################################################
# Code for Player's and CPU's Turn

# Turn Counter
def turn_counter(counter):
    counter += 1
    return counter

# Player Turn
def players_move(turn, counter):

    while turn == True:
        print(f'turn # {counter}')

        move = input('Enter a number (1-9) to place your move: ')

        clear()
        graphics_mod.display_grid(positions)

        try:
            move = int(move)
        except:
            print('Sorry that is not (1-9)')
            continue
        
        if move in used_positions:        
            print('This place has already been used')

        elif move not in range(1,10):
            print('Sorry that is not (1-9)')    

        else:    
            positions[str(move)] = player
            used_positions.append(move)
            # Turn ends
            turn = False

    return turn 

#CPU turn
def cpu_move(turn, counter):

    while turn == False:
        print(f'turn # {counter}')

        print("CPU's turn, Please wait.")
        
        random_num = [num for num in range(0,9)]
        time.sleep(random.choice(random_num))
        ###

        #need a stratagy here

        ###
        index = int(random.choice(range(1,10)))
        
        while index in used_positions:
            index = int(random.choice(range(1,10)))

        used_positions.append(index)
        positions[str(index)] = cpu

        turn = True

    return turn    

################################################################################
#check if win , lose or draw

# eight different win combinations:
def read_combos():
    position_values = list(positions.values())

    combinations = [
        position_values[:3],
        position_values[3:6],
        position_values[6:9],
        position_values[0:9:3],
        position_values[1:9:3],
        position_values[2:9:3],
        position_values[0:9:4],
        position_values[2:7:2]
        ]

    return combinations

# Draw Check
def draw_check(draw, counter):
    if counter > 9:
        draw = True
    else:
        draw = False
    
    return draw    

# Win Check       
def win_check(win, combinations): 
    for combo in combinations:
        if combo.count(player) == 3:
            win = True
            break
        else:
            win = False

    return win 

# Lose Check
def lose_check(lose, combinations):  
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
    print(win,draw,lose)
    if draw == True:
        graphics_mod.tie()
    elif win == True:
        graphics_mod.winner()
    elif lose == True:
        graphics_mod.loser()

# Play again?
def replay():
    user_input = '*'

    while user_input != 'Y' and user_input != 'N':
        user_input = input('Do you want to play again? Y or N: ').upper() 

        if user_input != 'Y' and user_input != 'N': 
            clear()
            print('Sorry that is not a valid choice')  

        elif user_input == 'Y':
            game_on = True
        elif user_input == 'N':
            game_on = False
        
    return game_on

################################################################################
# Main Game Code

#initial game setup
positions = {
    "1" : ' ',
    "2" : ' ',
    "3" : ' ',
    "4" : ' ',
    "5" : ' ',
    "6" : ' ',
    "7" : ' ',
    "8" : ' ',
    "9" : ' ',
    } 

used_positions = []     
turn= '*'
progress = True
game_on = True
draw = False
win = False
lose = False
counter = 0

# Run Game
while game_on:
    clear()

    # Game Title Screen
    graphics_mod.game_intro()

    # Player selection
    player, cpu = player_selection()
    turn = turn_assignment()

    #game play
    while progress == True:

        # player Turn
        while turn == True:
            clear()
            graphics_mod.display_grid(positions)
            combinations = read_combos()
            win = win_check(win,combinations)
            draw = draw_check(draw, counter)
            lose = lose_check(lose,combinations)

            if win or draw or lose:
                progress = False
                break

            counter = turn_counter(counter)
            turn = players_move(turn, counter)
        
        # cpu turn    
        while turn == False:
            clear()
            graphics_mod.display_grid(positions)
            combinations = read_combos()
            win = win_check(win, combinations)
            draw = draw_check(draw,counter) 
            lose = lose_check(lose, combinations)

            if win or draw or lose:
                progress = False
                break

            counter = turn_counter(counter)
            turn = cpu_move(turn, counter)
      
    clear()               
    end_status(win,draw,lose)

    #play again?
    game_on = replay()
    if game_on == False:

        clear()
        print('''Thank you for playing!!!!!!''')        
    else:
        #reset game
        # Resets initial game setup
        positions = {
            "1" : ' ',
            "2" : ' ',
            "3" : ' ',
            "4" : ' ',
            "5" : ' ',
            "6" : ' ',
            "7" : ' ',
            "8" : ' ',
            "9" : ' ',
            }

        choice = [' ' for spot in range(0,9)]
        used_positions.clear()
        turn= '*'
        progress = True
        game_on = True
        draw = False
        win = False
        lose = False
        combinations = []
        counter = 0





