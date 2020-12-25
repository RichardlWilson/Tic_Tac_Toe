# Tic_Tac_Toe
This was just a tic tac toe game I made while learning python.
Future changes I want to do:
  • Re-work draw_check, win_check and lose_check to be more efficent.
  • Re-work CPU turn to be more challenging.
  • Find Bug in CPU turn that results in index out of range error.
  • Maybe make different difficult settings.

Original Game logic design:
Tic Tac Toe game logic

game_on = True

while game_on:

    display title page

    player selection
        if player selection is *
            cpu selection is !*
        else:
            cpu selection is *

    turn assignment
        if player == *
            turn == True
        else:
            turn == False    
            
    while in progress

        player turn

            check status

            if status is done

                determine winner
                if winner determined
                    end progress

            else:
                turn ends 

        cpu turn

            check status
            if status is done

                determine winner
                if winner determined
                    end progress

            else:
                turn ends 
    
    show determined winner
    ask for another game
        if another game
            pass
        else:
            game_on = False

if game on = False
    print('Thanks for playing!!!!') 
