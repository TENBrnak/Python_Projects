#First larger project, the game of tic-tac-toe
game = True


def displayboard(board):
    print("  0 1 2")
    for count, i in enumerate(board):
        print()
        print(count, end=" ")
        for j in i:
            print(j, end=" ")
    print()


def modify_board(turn):
    if turn % 2 != 0:
        print("Player1's turn!")
    elif turn % 2 == 0:
        print("Player2's turn!")
    row = int(input("What row do you want to play in? (0-2)"))
    column = int(input("What column do you want to play in? (0-2)"))
    if row not in range(3) or column not in range(3):
        print("Invalid input.....turn skipped")
        return
    if board[row][column] == 0:
        if turn % 2 != 0:
            board[row][column] = 1
        elif turn % 2 == 0:
            board[row][column] = 2
    else:
        print("Place already taken.....turn skipped")
        return


def detect_3(board, victory):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            victory = board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            victory = board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        victory = board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        victory = board[0][2]
    return victory


while game:
    board = [[0, 0, 0],  [0, 0, 0], [0, 0, 0]]
    victory = 0
    check = 1
    displayboard(board)
    while victory == 0:
        modify_board(check)
        displayboard(board)
        victory = detect_3(board, victory)
        check += 1
    print("Player", victory, "won!")
    if input("Do you want to play another game? (y/n)") in "yY":
        game = True
    else:
        game = False
