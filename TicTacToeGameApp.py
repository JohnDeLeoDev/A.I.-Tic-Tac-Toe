# John DeLeo
# CS534
# Individual Project Assignment 3
# Tic Tac Toe Game App
############################################################################################################
# This is the main file for the Tic Tac Toe Game App. It imports the TicTacToe class from TicTacToeClass.py
# and runs the game. The game allows the user to play against a random player, a MiniMax player, an Alpha Beta Pruning
# player, a Heuristic Alpha Beta Pruning player, an MCTS player, or a Query player. The user can choose the type of player
# for each player. The game will print the board, ask the user to choose a player type for each player, and then play the game.
# The game will print the board after each move and will print the winner of the game. The user can choose to play again or quit.
############################################################################################################
# The game board is numbered as follows:

# Columns:
#        1 | 2 | 3
#       -----------
#          |   |
#       ----------- 
#          |   |

# Rows:
#       1  |   |
#       -----------
#       2  |   |
#       -----------
#       3  |   |
# The game will print the board after each move and will print the winner of the game. The user can choose to play again or quit.
############################################################################################################
from TicTacToeClass import TicTacToe
import random

# main function to run the game
def main():
    keep_playing = True
    print()
    print("Welcome to Python Tic Tac Toe!")
    print()
    print("The board is numbered as follows:")
    print()
    print("Columns:")
    print()
    print(" 1 | 2 | 3 ")
    print("-----------")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print()
    print("Rows:")
    print()
    print("1  |   |   ")
    print("-----------")
    print("2  |   |   ")
    print("-----------")
    print("3  |   |   ")
    print()

    while keep_playing:
        print()
        print("Player 1 types:")
        print("1 - Random Player")
        print("2 - MiniMax Player")
        print("3 - Alpha Beta Player")
        print("4 - Heuristic Alpha Beta Player")
        print("5 - MCTS Player")
        print("6 - Query Player")
        print()

        # Tic Tac Toe Object
        game = TicTacToe()
        player1 = int(input("Enter player 1 type: "))
        # check if player 1 type is valid
        while player1 not in [1, 2, 3, 4, 5, 6]:
            player1 = int(input("Could not find your player, please try again: "))
        player2 = int(input("Enter player 2 type: "))
        # check if player 2 type is valid
        while player2 not in [1, 2, 3, 4, 5, 6]:
            player2 = int(input("Could not find your player, please try again: "))

        game.set_players(player1, player2)    
        print()
        print("Player 1 is: ", game.player1.type_str)
        print("Player 2 is: ", game.player2.type_str)
        print()
        print(f"Player {game.current_player.number} ({game.current_player.player_shape}) goes first.")
        print()
        input("Press Enter to start the game...")
        print()
        game.play_game()
        print()
        play_again= input("Do you want to play again? (y/n): ")
        print()
        if play_again == "n":
            keep_playing = False
    print()
    print("Thanks for playing Tic Tac Toe!")
    print()

if __name__ == "__main__":
    main()