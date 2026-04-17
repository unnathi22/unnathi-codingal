def printBoard(b):
    print(b[7]+'|'+b[8]+'|'+b[9])
    print('-+-+-')
    print(b[4]+'|'+b[5]+'|'+b[6])
    print('-+-+-')
    print(b[1]+'|'+b[2]+'|'+b[3])


def checkWin(board):
    wins=[(7,8,9),(4,5,6),(1,2,3),(7,4,1),(8,5,2),(9,6,3),(7,5,3),(1,5,9)]
    return any(board[a]==board[b]==board[c]!=' '  for a,b,c in wins) 
    
def game():
    board={i:str(i) for i in range(1,10)}
    turn='X'

    for i in range(9):
        printBoard(board)
        move =int(input(f"player{turn}choose bw 1-9:"))
        if board[move] in ['X','O']:
            print("Taken! Try again.")
            continue
        board[move]=turn
        if checkWin(board) :
            printBoard(board)
            print(f"{turn} wins!")
            return

       
        if turn == 'X':
            turn='O'
        else:
            turn='X'
            

    printBoard(board)
    print("It's a tie!")

while True:
    game()
    if input("Play again? (y/n): ").lower() != 'y':
        break