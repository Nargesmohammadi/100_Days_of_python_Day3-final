print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
choice1 = input('You\'re at a crossroad, where do you want to go? "left" or "right".').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to lake. there is ad island in the middle of the lake.Type "wait" to wait for a '
                    'boat.Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input('You\'re reach to the three doors.select one of them.Type "blue", "yellow", "red" ').lower()
        if choice3 == "blue" or choice3 == "red":
            print("Game over")
        elif choice3 == "yellow":
            print("You are win")
    else:
        print("Game over")
else:
    print("Game over")
