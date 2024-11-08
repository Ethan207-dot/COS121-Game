def getDirection():
    userInput = ""
    validInput = ["north", "east", "south", "west"]
    while True:
        userInput = input("Which way do you want to go?\n \nNorth \nEast\nSouth\nWest\n\n")
        userInput = userInput.lower().strip()
        if userInput not in validInput:
            print("\ninvalid input\n")
            continue
        else: 
            break
    return userInput

def createBoard(size):
    board = []
    for row in range(size):
        board.append([])
        for col in range(size):
             board[row].append(row*size+col)
    return board

def printBoard(board):
    outputString = ""
    for row in board:
        for col in row:
            '''
            print(f"[{col:3}]", end="")
            '''
            outputString += f"[{col:5}]"
        #print()
        outputString += "\n"
    print(outputString)

def main():
    x=getDirection()
    print()
    print(x)
    b = createBoard(100)
    print()
    print(b)
    printBoard(b)

main()