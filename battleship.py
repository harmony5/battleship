from random import randint

def game():

    board = []

    grid=input("Grid size: ") #ask for the size of a NxN grid.

    if grid.isalpha():
        if grid=='exit':
            exit()
        else:
            print("Enter a number or 'exit', please.")
            game()
    elif grid=='':
        print("Enter a number or 'exit', please.")
        game()
    else:
        grd=int(grid)

        for x in range(grd):           #builds the grid
            board.append(["O"] * grd)

        #function to print the grid coreectly
        def print_board(board):
            for row in board:
                print("  ".join(row))

        def random_row(board):
            return randint(0, len(board) - 1)

        def random_col(board):
            return randint(0, len(board[0]) - 1)

        ship_row = random_row(board)
        ship_col = random_col(board)

        print("Battleship!")
        print_board(board)

        #print(ship_row) \for debugging only. Prints the position of the ship
        #print(ship_col) /

        #Starts the game with 4 turns.
        
        for turn in range(4):
            print("Turn", turn+1)
            
            row = input("Guess Row: ")
            if row=='exit':
                exit()
            elif row=='show':
                print("(%s,%s)"%(ship_row,ship_col))
                row=0
            elif row=='':
                row=0

            col = input("Guess Col: ")
            if col.isalpha():
                if col=='exit':
                    exit()
                elif col=='show':
                    print("(%s,%s)"%(ship_row,ship_col))
                    col=0
            elif col=='':
                col=0

            guess_row=int(row)
            guess_col=int(col)

            if guess_row == ship_row and guess_col == ship_col:
                print("Congrats! You spotted my battleship!")
                board[guess_row][guess_col] = "@"
                print_board(board)
                print("You won!")
                break

            else:
                
                if guess_row not in range(grd) or guess_col not in range(grd):
                    print("Not permitted! That position is outside the grid.")
                    print_board(board)
                    
                    if turn == 3:
                        print("Game Over")

                elif board[guess_row][guess_col] == "X":
                    print("You guessed that one already.")
                    print_board(board)
                
                    if turn == 3:
                        print("Game Over.")
                
                else:
                    print("You missed.")
                    board[guess_row][guess_col] = "X"
                    print_board(board)
                
                    if turn == 3:
                        print("Game Over")

    i=input("Continue?[y/n]")
    if i.isalpha():
        i=i.lower()
        if i=='y' or i=='yes':
            game()
        elif i=='n' or i=='no':
            exit()
        else:
            print("'y' or 'n'.")
    else:
        print("y or n")

game()