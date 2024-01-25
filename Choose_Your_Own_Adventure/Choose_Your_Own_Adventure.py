# This takes on the form of a pick your own story book

name = input("Please tell me your name: ")
print("Welcome", name, "to this adventure!")

answer = input('''You are on a dirt road, but it has come to an end and you can either go left or right.
Which way would you prefer to go? ''').lower()

if answer == "left":
    answer_two = input('''You come to a river point, you can walk around (walk) it or swim across(swim)?
     Type walk or swim: ''').lower()

    if answer == "swim":
        print("You swam across the river and got bitten by a river snake")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("That is not a valid option. You lose.")

elif answer == "right":
    answer = input('''You have come to a bridge, it looks wobbly, 
    would you like to cross it or head back (cross / back )''').lower()

    if answer == "back":
        print("You go back and You LOSE!.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)?")

        if answer == "yes":
            print("You talk to the stranger and they decide to reward you with gold. You are a WINNER!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("That is not a valid option. You lose.")

else:
    print("That is not a valid option. You lose.")

print("Thank you for trying!", name)
