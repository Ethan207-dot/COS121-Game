import random
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
             if random.randint(1,5) == 5:
                 board[row].append("M")
             else:
                board[row].append(row*size+col)
    return board

def printBoard(world):
    board = world["board"]
    loc = world["playerLoc"]
    outputString = ""
    for row in range(len(board)):
        for col in range (len(board)):
            cell = " "
            if loc["x"] == col and loc["y"] == row:
                cell = "X"
            outputString += f"[{cell:2}]"
        outputString += "\n"
    print(outputString)

def userName():
    while True:
        user = input("What would you like your user name to be?\n")
        user = user.lower().strip()
        if len(user) > 12:
            print("12 characters or less please")
            continue
        if len(user) == 0:
            print("You need a name ")
            continue
        return user
    

def main():
    x=getDirection()
    print()
    print(x)
    b = createBoard(10)
    print()
    print(b)
    printBoard(b)