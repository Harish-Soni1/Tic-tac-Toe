from random import randint
from IPython.display import clear_output
def display_board(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-|-|-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-|-|-")
    print(board[1]+"|"+board[2]+"|"+board[3])
    clear_output()
def player_input():
    '''
    output = (player1 marker, player2 marker)
    '''
    marker=" "
    while marker!="X" and marker!="O":
        marker=input("player1, choose X or O : ")
    if marker == "X":
        return ("X","O")
    else:
        return ("O","X")

def place_marker(board, marker, position):
    board[position]= marker

def win_check(board, mark):
    return((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    flip = randint(0,1)
    if flip==0:
        return "player1"
    else:
        return "player2"
def space_check(board, position):
    return board[position] == " "

def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def next_pos(board):
    position = 0
    if position not in [1,2,3,4,5,6,7,8,9] or space_check(board, position):
        position=int(input("enter position [1-9]: "))
    return position

def replay():
     choice=input("play again? enter Y or N? ")
     return choice == "Y"

game_on=" "
print("#"*30)
print("    Welcome to Tic Tac Toe")
print("#"*30)
while True:
    tb=[" "]*10
    player1_marker , player2_marker = player_input()
    turn = choose_first()
    print(turn,"play first")
    play_game=input("Ready to play? Y or N ? ")
    if play_game == "Y":
        game_on == True
    else:
        game_on == False
    while game_on:
        if turn=="player1":
            display_board(tb)
            p = next_pos(tb)
            place_marker(tb, player1_marker, p)
            if win_check(tb, player1_marker):
                display_board(tb)
                print("Player1 has won.")
                game_on=False
            else:
                if full_check(tb):
                    display_board(tb)
                    print("Game Tie.")
                    game_on=False
                else:
                    turn="player2"
        else:
            display_board(tb)
            position = next_pos(tb)
            place_marker(tb, player2_marker, position)
            if win_check(tb, player2_marker):
                display_board(tb)
                print("Player2 has won.")
                game_on=False
            else:
                if full_check(tb):
                    display_board(tb)
                    print("Game Tie.")
                    game_on=False
                else:
                    turn="player1"
    if not replay():
        break