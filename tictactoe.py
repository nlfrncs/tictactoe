from game import new_game
from common import player1_score, player2_score

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

def menu() -> None:
    while 1:
        if player1_score == 0 and player2_score == 0:
            print("")
            print("GAME MENU")
            print("Input:")
            print("'n' to start game")
            print("'h' how to play")
            print("'q' to quit")
            print("")
            print("SCORE:")
            print(f"Player 1: {player1_score}   Player 2: {player2_score}")
            print("")

        # hindi mo pa maayos yung pag update ng player score
        # else:
        #     print("")
        #     print("SCORE:")
        #     print(f"Player 1: {player1_score}   Player 2: {player2_score}")
        #     print("")
        #     print("GAME MENU")
        #     print("Input:")
        #     print("'n' to start game")
        #     print("'h' how to play")
        #     print("'q' to quit")
        #     print("")

        option = input()
        if option == "n":
            new_game()
        elif option == "h":
            how_to_play()
        elif option == "q":
            pass

main()
