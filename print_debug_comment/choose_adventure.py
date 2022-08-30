
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
rooms = ["Your're at a cross road. Where do you want to go? Type 'left' to go left, 'right' to go right.\n","You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n", "You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"]
ans = input(rooms[0])
if ans == 'left':
    ans=input(rooms[1])
    if ans == 'wait':
        match(input(rooms[2])):
            case 'yellow':
                print("Congratulations! You found the treasure!")
            case 'blue':
                print("You fall into a vat of acidic concoction. Game Over.")
            case 'red':
                print("You succumb in a pit of fire. Game Over.")
            case _:
                print("You did not choose a valid colour, and starved to death waiting for something to happen. Game Over.")
    elif ans =='swim':
        print("Your leg got caught in a tangle of seaweed in the murky depths, the night was silent and not a single soul came to your aid. Game Over.")
    else:
        print("You did not choose a valid choice, and starved to death waiting for something to happen. Game Over.")
elif ans =='right':
    print("A venomous snake awaits you at the turn of the corner, striking you heel with its needle-like fangs before you even noticed. Before long, you slump to the ground, your soul seeping back out into the soil beneath you. Game Over.")
else:
    print("You did not choose a valid choice, and starved to death waiting for something to happen. Game Over.")
