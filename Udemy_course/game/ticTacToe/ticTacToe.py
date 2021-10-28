"""Display the board of game"""
def display(board):
    for row in board:
        print("{0:<1} | {1:^1} | {2:<1}".format(row[0],row[1],row[2]))

def place_mark():
    row = int(input("You choice, row?"))
    while row < 0 or row > 2:
        row = int(input("You choice, row 0,1 or 2?"))
    colomn = int(input("You choice, colomn?"))
    while colomn < 0 or colomn > 2:
        colomn = int(input("You choice, colomn 0,1 or 2?"))
    return row, colomn
def check_game(board,mark):
    #Win check
    if board[0][0]==board[0][1]==board[0][2]==mark or board[0][0]==board[1][0]==board[2][0]==mark or \
        board[1][0] == board[1][1] == board[1][2]==mark or board[0][1]==board[1][2]==board[2][1]==mark or\
        board[2][0] == board[2][1] == board[2][2]==mark or board[0][2]==board[1][2]==board[2][2]==mark or\
        board[0][0]==board[1][1]==board[2][2]==mark or board[0][2]==board[1][1]==board[2][0]==mark:
        print("Game over. {} wins".format(mark) )
        return True
    #Empty cell for choice
    for row in board:
        if " " in row:
            return False
    # If no win and no empty cell for choice, game over
    print("Game over. No one wins")
    return True

"""Assign mark for players"""
def select_mark():
    mark_pl1 = ''
    while not (mark_pl1=="X" or mark_pl1 == "O"):
      mark_pl1 = input("Player 1, do you want to play with X or O?:").upper()
    if mark_pl1 == "X":
        mark_pl2 = "O"
    else:
        mark_pl2 = "X"
    print("Player's 2 mark is " + mark_pl2)
    return mark_pl1, mark_pl2

def main():
    print("Let's play")
    mark_pl1,mark_pl2 = select_mark()
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    display(board)
    while check_game(board,mark_pl1)==False or check_game(board,mark_pl2)==False:
        row_g,colomn_g = place_mark()
        while board[row_g][colomn_g]!=" ":
            print("This cell is not empty")
            row_g, colomn_g = place_mark()
        board[row_g][colomn_g] = mark_pl1
        display(board)
        if check_game(board,mark_pl1)==True or check_game(board,mark_pl2)==True:
            break
        row_m,column_m = place_mark()
        while board[row_m][column_m]!=" ":
            print("This cell is not empty")
            row_m, column_m = place_mark()
        board[row_m][column_m] = mark_pl2
        display(board)


if __name__ =="__main__":
    main()