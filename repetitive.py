def gold(gc):
    print(("You now have "+str(gc)+" gold coins.").center(150))
def death():
    dead = 1
    print("Would you like to start over?")
    while dead == 1:
        again = input("")
        if again == "y":
            dead = 0
            While_2 = 0