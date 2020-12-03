def green_room():
    print("You are in the green room.")
    choose_room()


def blue_room():
    print("You are in the blue room.")
    choose_room()

    
def unknown_response():
    print("I don't know what that is.")
    choose_room()


def choose_room():
    choice = input("Would you like to go to the green room or the blue room?\n")
    if choice == "green":
        green_room()
    elif choice == "blue":
        blue_room()
    else:
        unknown_response()
        

choose_room()