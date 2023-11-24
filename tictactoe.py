from random import randrange




def display_board(board):
    x = 0
    for row in board:
        print ("+","-"*9,"+ ",end="")
        print ("-"*9,"+ ",end="")
        print ("-"*9,"+ ")

        print ("|"," "*9,"| ",end="")
        print (" "*9,"| ",end="")
        print (" "*9,"| ")
        for cell in row:
            print ("|    ",cell,"    ",end="")
        print("|")
        print ("|"," "*9,"| ",end="")
        print (" "*9,"| ",end="")
        print (" "*9,"| ")
    print ("+","-"*9,"+ ",end="")
    print ("-"*9,"+ ",end="")
    print ("-"*9,"+ ")

           

    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):

    move = int(input("Enter your move:"))
    free_cells = make_list_of_free_fields(board)
    for i, x in enumerate(board):
        if move in x:
            if board[i][x.index(move)] != "X" or board[i][x.index(move)] != "O":
                board[i][x.index(move)] = "O"


    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board accor1
    # ding to the user's decision.


def make_list_of_free_fields(board):
    free_cells = []
    row_count = 0

    for row in board:
        for cell in row:
            if cell != "X" and cell != "O":
                free_cells.append((row_count,cell))
            
        row_count +=1
        
    return free_cells
            
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):

    #verticle check
    RowID = 0
    winCount = 0
    while RowID < 3:
        Column = 0
        while Column < 3:
            if board[RowID][Column] == sign:
                winCount += 1
                print("Verticle: ",sign,winCount)
            elif winCount == 3:
                print ("Player: ",sign," WINS!!!!")
                return True
            Column += 1
        RowID += 1


    #Horizontal Check
    for row in board:
        counter = 0
        for cell in row:
                if cell == sign:
                 counter += 1
                 print("Horizontal: ",sign,winCount)
                 if counter == 3:
                    print ("Player: ",sign," WINS!!!!")
                    return True

    
            
    #Diagonal Check 
    if board[0][0] == sign and board [1][1] == sign and board[2][2] == sign:
        print ("Player: ",sign," WINS!!!!")
        return True
    elif board[0][2] == sign and board [1][1] == sign and board[2][0] == sign:
        print ("Player: ",sign," WINS!!!!")
        return True
    
    return False




            
        



    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    turn  = True
    free_cells = make_list_of_free_fields(board)

    while turn == True:
        move = randrange(10)
        for i, x in enumerate(board):
            if move in x:
                if board[i][x.index(move)] != "X" or board[i][x.index(move)] != "O":
                    board[i][x.index(move)] = "X"
                    turn = False
                # The function draws the computer's move and updates the board.

def Play_Game():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    win = False
    player = "x"
    while win != True:
        #Game Loop
        draw_move(board)
        display_board(board)
        enter_move(board)

        win = victory_for(board,"X")
        if win == True:
            display_board(board)
            return False
        
        win = victory_for(board,"O")
        if win == True:
            display_board(board)
            return False
        Remaining_Moves = make_list_of_free_fields(board)
        if len(Remaining_Moves) == 0:
            print("Uh-OH Stalemate")
            return False


print("Hello")
#Game Controller
End_Game = False
while End_Game == False:
    play = input("Are you ready to play? enter Y/N")
    if play == "Y":
        Play_Game()
        input("Do you ant to play again Y/N")
    else:
        End_Game = True






