'''
Ethan Smith
11/18/2024
Basic Text Adventure
'''
def showLibrary(world):
    print("You know what a library looks like")
    print("You see a door on your left and your right choose one to go through")
    uI = input()
    if uI == "left":
        world["loc"] = "graveyard"

    else:
        if "B.F.G." not in world["inv"]:
            print("As the door opens you see a B.F.G. (Not the friendly giant)")
            print("You pick up the B.F.G. even though it is extremely heavy it looks badass")
            world["inv"].append("B.F.G.")
        else:
            print("This is where you found the B.F.G.")
            print("There seems to be a dent in the floor")

def showGraveyard(world):
    print("You see a graveyard")
    print("As you enter the graveyard you see a disturbance shaking each tomb stone")
    if "B.F.G." in world["inv"]:
        print("You blast the ever living fuck out of the ground")
    else:
        print("Zombies bust out of the ground and the door behind you seems to have locked itself")
def main():
    world = {}
    world["loc"] =  "Library"
    print("Please enter your name for this adventure")
    uI = input()
    world["playerName"] = uI
    world["inv"] = []

    while True:
        if world["loc"] == "Library":
            showLibrary(world)
            continue
        elif world["loc"] == "graveyard":
            showGraveyard(world)
            break

main()