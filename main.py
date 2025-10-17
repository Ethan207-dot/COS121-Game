from board import *
from inputProcess import *

def main():
    world = {}
    loc = {
        "x":0,
        "y":0
    }
    world["board"] = createBoard(5)
    world["playerLoc"] = loc
    world["playerName"] = userName()
    print(f"Your name is: {world['playerName']}")
    b = createBoard(4)
    #name = userName()
    while True:
        printBoard(world)
        u = getDirection()
        if u == "east" \
            and world["playerLoc"]["x"] < len(world["board"])-1:
            world["playerLoc"]["x"] += 1
        if u == "south" \
            and world["playerLoc"]["y"] < len(world["board"])-1:
            world["playerLoc"]["y"] += 1
        if u == "north" \
             and world["playerLoc"]["y"] < len(world["board"])+1:
            world["playerLoc"]["y"] -= 1
        if u == "west"\
              and world["playerLoc"]["x"] < len(world["board"])+1:
            world["playerLoc"]["x"] -= 1
main()



