from game import new_game
import common
import sys
import os

def main() -> None:
    startup()
    while 1:
        menu()

def startup() -> None:
    print("Let's play TicTacToe!")

def how_to_play() -> None:
    print("")
    print("How to play:")
    print("Displayed on the board are numbers which represent slots for the players to put their symbols. (Player 1: 'x', Player 2: 'o')")
    print("First player to create a 3-symbol line wins!")
    print("1|2|3")
    print("4|4|6")
    print("7|8|9")
    print("")
    print("First turn alternates to each player each game.")
    print("")

def menu() -> None:
    while 1:
        print("")
        print("GAME MENU")
        print("Input:")
        print("'n' to start game")
        print("'h' how to play")
        print("'q' to quit")
        print("")
        print("SCORE:")
        print(f"Player 1: {common.player1_score}   Player 2: {common.player2_score}")
        print("")

        option = input()
        if option == "n":
            new_game()
        elif option == "h":
            os.system('cls' if os.name == 'nt' else 'clear')
            how_to_play()
        elif option == "q":
            sys.exit(0)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Not a valid menu option, please try input again.")
            print("")

main()
