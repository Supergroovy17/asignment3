
#task1
place = input("Choose a place: forest or cave? ")

if place == "forest":    
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":     
        print("You found a boat!")
elif place == "cave":    
    print("You find a hidden treasure!")


#task2
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark?")
    if cave_action == "light a torch":
        print("you run into Dragon!")
    elif cave_action == "proceed in the dark":
        print("You Died!")


#task 3
        place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        "pass" #fin---------------------------------------------------------------------
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark?")
    if cave_action == "light a torch":
        print("you run into Dragon!")
    elif cave_action == "proceed in the dark":
        print("You Died?!")
    else:
        "pass"#fin-----------------------------------------------------------------------