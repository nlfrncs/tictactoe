import os
import common
# from common import new_board, player1_score, player2_score, game_over, win_patterns, valid_slots

board = []

def print_board(board) -> None:
    # os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print(f"{board[7]}|{board[8]}|{board[9]}")

def new_game() -> None:
    global board
    common.game_over = False
    common.game_count += 1
    board = common.new_board.copy()
    print_board(board)
    while common.game_over == False:
        if common.game_count % 2 != 0:
            board = shoot(1, board)
            if common.game_over == True:
                break
            board = shoot(2, board)
        else:
            board = shoot(2, board)
            if common.game_over == True:
                break
            board = shoot(1, board)

def shoot(player: int, gboard: list[str]) -> list[str]:
    if common.game_over == True:
        return gboard

    # nung last tumira si Player1 para sa tie, pinapatira pa rin si player 2
    if " " not in gboard[1:]:
        print("Tie game!")
        common.game_over = True
        return gboard

    print(f"Player {player}'s turn")
    while 1:
        x = input()
        if x not in common.valid_slots:
            print("Not a valid slot, valid slots are only numbers 1 to 9")
        elif board[int(x)] != " ":
            print("Slot is already taken, try again")
        else:
            x = int(x)
            break

    if player == 1:
        gboard[x] = "o"
    elif player == 2:
        gboard[x] = "x"

    print_board(gboard)
    did_player_win(player)
    return gboard

def did_player_win(player: int):
    for pattern in common.win_patterns:
        if (board[pattern[0]] == board[pattern[1]] and board[pattern[1]] == board[pattern[2]]) and board[pattern[0]] != " ":
            common.game_over = True
            print(f"Player {player} wins!")
            print(common.game_over)
            if player == 1:
                common.player1_score += 1
            else:
                common.player2_score += 1
