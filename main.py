import os

# Variables
starting = "forest"

# Classes
class Stats:
    hp = 5
    atk = 3

class Rooms:
    def forest():
        name = "forest"
        # N, W, S, E
        places = ['chest', 'cave', '', '']

        return name, places

# Functions
def clear():
    os.system("clear") # Clear for UNIX systems

# Main game function
def main():
    if starting == "forest":
        name, places = Rooms.forest()
    else:
        print("ERR: 001: Starting point: changed")
        quit()
    
    if Stats.hp / Stats.atk != 2.5:
        print("ERR: 002: Stats: changed")
        quit()

    while True:
        pass

if __name__ == "__main__":
    main()