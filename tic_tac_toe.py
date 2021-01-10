#Tic_Tac
import graphics
import time
from colorama import init, Fore
from os import system, name
import random

################################################################################

class Game():
    def __init__(self):
        self.on = True
        self.player_count = 0
        self.turn_counter = 1

    def clear_screen(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')        

    def inro(self):
        graphics.game_intro()

    def number_of_players(self):
        valid = (1,2)
        user_input = ''

        while user_input not in valid:
            user_input = input('How many Players? 1 or 2 : ')

            if user_input.isdigit():
                user_input = int(user_input)
            else:
                game.clear_screen()
                print('Im sorry. Please select 1 or 2')

        self.player_count = user_input 

    def player_assign(self):

        if self.player_count == 2:
            player1.marker,player2.marker = ('X','O')

            user_input = input('Player 1 is X | Player 2 is O'
                               + '.... Press Enter to Continue')

            game.clear_screen()

        else:
            player1.marker,player2.marker = ('X','O')
            player2.name = 'CPU'

            user_input = input(f'{player1.name} is X | {player2.name} is O'
                               + '.... Press Enter to Continue')

            game.clear_screen()

    def play_again(self):
        valid = ('Y','N')
        user_input = input('Play again? Y or N: ').upper()

        while user_input not in valid:
            print('Im sorry taht is not a valid answer!') 
            user_input = input('Play again? Y or N: ').upper()

        if user_input == 'Y':
            pass
        else: 
            self.on = False
            self.clear_screen()
            print('Thank you for playing!!!!!') 

################################################################################

class Board():
    def __init__(self):
        self.positions = []
        self.used_positions = []

        self.positions.append( board_position('position1'))
        self.positions.append( board_position('position2'))
        self.positions.append( board_position('position3'))
        self.positions.append( board_position('position4'))
        self.positions.append( board_position('position5'))
        self.positions.append( board_position('position6'))
        self.positions.append( board_position('position7'))
        self.positions.append( board_position('position8'))
        self.positions.append( board_position('position9'))    
        
class board_position():
    def __init__(self, name):
        self.name = name
        self.marker = ' '




    def __str__(self):
        return self.marker 

################################################################################ 

class Player():
    def __init__(self, name, marker, score = 0, turn = True):
        self.name = name
        self.marker = marker
        self.score = score
        self.turn = turn

    def win_check(self): 
    
        if (game_board.positions[0].marker == game_board.positions[1].marker
            == game_board.positions[2].marker == self.marker) or \
            (game_board.positions[3].marker == game_board.positions[4].marker
            == game_board.positions[5].marker == self.marker) or \
            (game_board.positions[6].marker == game_board.positions[7].marker
            == game_board.positions[8].marker == self.marker) or \
            (game_board.positions[6].marker == game_board.positions[0].marker
            == game_board.positions[3].marker == self.marker) or \
            (game_board.positions[7].marker == game_board.positions[4].marker
            == game_board.positions[1].marker == self.marker) or \
            (game_board.positions[8].marker == game_board.positions[5].marker
            == game_board.positions[2].marker == self.marker) or \
            (game_board.positions[0].marker == game_board.positions[4].marker
            == game_board.positions[8].marker == self.marker) or \
            (game_board.positions[2].marker == game_board.positions[4].marker
            == game_board.positions[6].marker == self.marker):
            return True
        else:
            return False

    def draw(self):
        if len(game_board.used_positions) == 9:
            return True
        else:
            return False 

    def cpu_stratagy(self):

        # Row 1
        if game_board.positions[0].marker \
            == game_board.positions[1].marker == player1.marker \
            and 3 not in game_board.used_positions:

            if game_board.positions[2].marker == ' ':
                game_board.positions[2].marker = player2.marker
                game_board.used_positions.append(3)

        elif game_board.positions[1].marker \
            == game_board.positions[2].marker == player1.marker \
            and 1 not in game_board.used_positions:

            if game_board.positions[0].marker == ' ':
                game_board.positions[0].marker = player2.marker
                game_board.used_positions.append(1)

        elif game_board.positions[0].marker \
            == game_board.positions[2].marker == player1.marker \
            and 2 not in game_board.used_positions:

            if game_board.positions[1].marker == ' ':
                game_board.positions[1].marker = player2.marker
                game_board.used_positions.append(2)

        # #.......................................................................
        # Row 2
        elif game_board.positions[3].marker \
            == game_board.positions[4].marker == player1.marker \
            and 6 not in game_board.used_positions:

            if game_board.positions[5].marker == ' ':
                game_board.positions[5].marker = player2.marker
                game_board.used_positions.append(6)


        elif game_board.positions[4].marker \
            == game_board.positions[5].marker == player1.marker \
            and 4 not in game_board.used_positions:

            if game_board.positions[3].marker == ' ':
                game_board.positions[3].marker = player2.marker
                game_board.used_positions.append(4)

        elif game_board.positions[3].marker \
            == game_board.positions[5].marker == player1.marker \
            and 5 not in game_board.used_positions:

            if game_board.positions[4].marker == ' ':
                game_board.positions[4].marker = player2.marker
                game_board.used_positions.append(5)

        # #.......................................................................
        # Row 3
        elif game_board.positions[6].marker \
            == game_board.positions[7].marker == player1.marker \
            and 9 not in game_board.used_positions:

            if game_board.positions[8].marker == ' ':
                game_board.positions[8].marker = player2.marker
                game_board.used_positions.append(9)

        elif game_board.positions[7].marker \
            == game_board.positions[8].marker == player1.marker \
            and 7 not in game_board.used_positions:

            if game_board.positions[6].marker == ' ':
                game_board.positions[6].marker = player2.marker
                game_board.used_positions.append(7)

        elif game_board.positions[6].marker \
            == game_board.positions[8].marker == player1.marker \
            and 8 not in game_board.used_positions:

            if game_board.positions[7].marker == ' ':
                game_board.positions[7].marker = player2.marker
                game_board.used_positions.append(8)
        # #.......................................................................
        #Column 1
        elif game_board.positions[6].marker \
            == game_board.positions[3].marker == player1.marker \
            and 1 not in game_board.used_positions:

            if game_board.positions[0].marker == ' ':
                game_board.positions[0].marker = player2.marker
                game_board.used_positions.append(1)

        elif game_board.positions[3].marker \
            == game_board.positions[0].marker == player1.marker \
            and 7 not in game_board.used_positions:

            if game_board.positions[6].marker == ' ':
                game_board.positions[6].marker = player2.marker
                game_board.used_positions.append(7)

        elif game_board.positions[6].marker \
            == game_board.positions[0].marker == player1.marker \
            and 4 not in game_board.used_positions:

            if game_board.positions[3].marker == ' ':
                game_board.positions[3].marker = player2.marker
                game_board.used_positions.append(4)
        # #.......................................................................
        #Column 2
        elif game_board.positions[7].marker \
            == game_board.positions[4].marker == player1.marker \
            and 2 not in game_board.used_positions:

            if game_board.positions[1].marker == ' ':
                game_board.positions[1].marker = player2.marker
                game_board.used_positions.append(2)

        elif game_board.positions[4].marker \
            == game_board.positions[1].marker == player1.marker \
            and 8 not in game_board.used_positions:

            if game_board.positions[7].marker == ' ':
                game_board.positions[7].marker = player2.marker
                game_board.used_positions.append(8)

        elif game_board.positions[7].marker \
            == game_board.positions[1].marker == player1.marker \
            and 5 not in game_board.used_positions:

            if game_board.positions[4].marker == ' ':
                game_board.positions[4].marker = player2.marker
                game_board.used_positions.append(5)

        # #.......................................................................
        #Column 3
        elif game_board.positions[8].marker \
            == game_board.positions[5].marker == player1.marker \
            and 3 not in game_board.used_positions:

            if game_board.positions[2].marker == ' ':
                game_board.positions[2].marker = player2.marker
                game_board.used_positions.append(3)

        elif game_board.positions[5].marker \
            == game_board.positions[2].marker == player1.marker \
            and 9 not in game_board.used_positions:

            if game_board.positions[8].marker == ' ':
                game_board.positions[8].marker = player2.marker
                game_board.used_positions.append(9)

        elif game_board.positions[8].marker \
            == game_board.positions[2].marker == player1.marker \
            and 6 not in game_board.used_positions:

            if game_board.positions[5].marker == ' ':
                game_board.positions[5].marker = player2.marker
                game_board.used_positions.append(6)
        # #.......................................................................
        #Diagnal 1
        elif game_board.positions[0].marker \
            == game_board.positions[4].marker == player1.marker \
            and 9 not in game_board.used_positions:

            if game_board.positions[8].marker == ' ':
                game_board.positions[8].marker = player2.marker
                game_board.used_positions.append(9)

        elif game_board.positions[4].marker \
            == game_board.positions[8].marker == player1.marker \
            and 1 not in game_board.used_positions:

            if game_board.positions[0].marker == ' ':
                game_board.positions[0].marker = player2.marker
                game_board.used_positions.append(1)

        elif game_board.positions[0].marker \
            == game_board.positions[8].marker == player1.marker \
            and 5 not in game_board.used_positions:

            if game_board.positions[4].marker == ' ':
                game_board.positions[4].marker = player2.marker
                game_board.used_positions.append(5)
        # #.......................................................................
        #Diagnal 1
        elif game_board.positions[2].marker \
            == game_board.positions[4].marker == player1.marker \
            and 7 not in game_board.used_positions:

            if game_board.positions[6].marker == ' ':
                game_board.positions[6].marker = player2.marker
                game_board.used_positions.append(7)

        elif game_board.positions[4].marker \
            == game_board.positions[6].marker == player1.marker \
            and 3 not in game_board.used_positions:

            if game_board.positions[2].marker == ' ':
                game_board.positions[2].marker = player2.marker
                game_board.used_positions.append(3)

        elif game_board.positions[2].marker \
            == game_board.positions[6].marker == player1.marker \
            and 5 not in game_board.used_positions:

            if game_board.positions[4].marker == ' ':
                game_board.positions[4].marker = player2.marker
                game_board.used_positions.append(5)

        #Random placement
        else: 
            rand_num = random.choice(range(0,9))

            while rand_num + 1 in game_board.used_positions:
                rand_num = random.choice(range(0,9))
     
            game_board.positions[rand_num].marker = player2.marker 
            game_board.used_positions.append(rand_num + 1)
 
    #.......................................................................
         
    def __str__(self):
        return f'{self.name} \nMarker: {self.marker} \n\
            Score: {self.score} \nTurn: {self.turn}'

################################################################################

def game_play(player1,player2,game_board):

    while game.on == True:

        while player1.turn == True:

            print(f'{player1.name} / Turn {game.turn_counter}')
            graphics.display_grid(game_board.positions, Fore)

            user_input = input('Please select a number from 1-9! : ')
            try:
                user_input = int(user_input)

            except TypeError():
                continue    

            if user_input in game_board.used_positions:
                print('Im sorry that position is already been used.')

            elif user_input not in range(1,10):
                print('Im sorry your number is out of range.')

            else:
                game_board.used_positions.append(user_input)
                game_board.positions[user_input - 1].marker = player1.marker
                game.turn_counter += 1

                if player1.win_check() == True:
                    game.clear_screen()
                    print(f'{player1.name} is the Winner!!!!!')
                    graphics.winner()
                    graphics.display_grid(game_board.positions, Fore)
                    game.on = False
                    break

                game.clear_screen()
                player1.turn = False 

#...............................................................................

        while player1.turn == False:

            if player2.name =='Player 2':
                print(f'{player2.name} / Turn {game.turn_counter}')
                graphics.display_grid(game_board.positions, Fore)

                if player2.draw() == True:
                    game.clear_screen()
                    print('No one wins.')
                    graphics.draw()
                    graphics.display_grid(game_board.positions, Fore)
                    game.on = False
                    break

                user_input = input('Please select a number from 1-9! : ')
                try:
                    user_input = int(user_input)

                except TypeError():
                    continue    

                if user_input in game_board.used_positions:
                    print('Im sorry that position is already been used.')

                elif user_input not in range(1,10):
                    print('Im sorry your number is out of range.')

                else:
                    game_board.used_positions.append(user_input)
                    game_board.positions[user_input - 1].marker = player2.marker
                    game.turn_counter += 1

                    if player2.win_check() == True:
                        game.clear_screen()
                        print(f'{player2.name} is the Winner!!!!!')
                        graphics.winner()
                        graphics.display_grid(game_board.positions, Fore)
                        game.on = False
                        break
     
                    game.clear_screen()
                    player1.turn = True

#...............................................................................

            else:
                print(f'{player2.name} / Turn {game.turn_counter}')
                graphics.display_grid(game_board.positions, Fore)

                if player2.draw() == True:
                    game.clear_screen()
                    print('No one wins.')
                    graphics.draw()
                    graphics.display_grid(game_board.positions, Fore)
                    game.on = False
                    break

                player2.cpu_stratagy()
                game.turn_counter += 1

                if player2.win_check() == True:
                    game.clear_screen()
                    print(f'{player2.name} is the Winner!!!!!')
                    graphics.winner()
                    graphics.display_grid(game_board.positions, Fore)
                    game.on = False
                    break

                game.clear_screen()
                player1.turn = True       
 
def replay():
    game.on = True
    game.player_count = 0
    game.turn_counter = 1

    game_board.used_positions.clear()

    del game_board
    game_board = Board()

    player1.turn = True
    game_play()
                  
################################################################################

if __name__ == '__main__':

    init(autoreset = True) #initiates colorama

    game = Game()
    game.clear_screen()
    graphics.game_intro()

    game_board = Board()

    player1 = Player('Player 1', '$')
    player2 = Player('Player 2', '$')

    game.number_of_players()
    game.player_assign()

    game_play(player1,player2,game_board)

    game.play_again()


    #restructure game loop for replay


