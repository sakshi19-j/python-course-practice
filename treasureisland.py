print("Welcome to the Treasure Island!")

choice = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice == "left":

    swim = input("You've come to a lake. There is an island in the middle. Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()

    if swim == "wait":

        door = input("You have 3 doors in this house. Which one will you choose? Red, Blue or Yellow? ").lower()

        if door == "yellow":
            print("Congratulations! You win the game!")

        elif door == "red":
            print("Burned by fire. Game Over!")

        elif door == "blue":
            print("Eaten by beasts. Game Over!")

        else:
            print("You chose a door that doesn't exist. Game Over!")

    else:
        print("Attacked by trout. Game Over!")

else:
    print("Fall into a hole. Game Over!")