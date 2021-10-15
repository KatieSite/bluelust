import os

try:
    admin = open('admin', 'r').read()
    if admin == "DEBUG":
        print("Debug")
except:
    pass

# Variables
hp = 5

# Functions
def clear():
    os.system("clear") # Clear for UNIX systems

# Main game function
def main():
    print("You wake up in a forest")
    print("There is a cave in front of you and a path to your left.")

    while True:
        pass

if __name__ == "__main__":
    main()