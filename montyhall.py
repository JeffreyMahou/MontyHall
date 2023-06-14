######## IMPORTS ######

from random import choice

######## CODE ########

def game(n=1000):
    
    results_strat1 = {"win":0, "lose":0}
    results_strat2 = {"win":0, "lose":0}
    
    for i in range(n):
        
        doors = ["A", "B", "C"]
        print("the 3 doors are in front of you")
        print("A   B   C")
        print("")
        
        door = choice(doors)
        gift = choice(doors)
        
        print("You picked door ", door)
        
        if door == gift:
            door_pushed = choice([d for d in doors if d != door])
        else:
            door_pushed = [d for d in doors if d != door and d != gift][0]
        doors.remove(door_pushed)
        
        print("Behind the door ", door_pushed, "there is ........ nothing")
        print()
        print("The remaining doors are ......")
        print()
        print(doors[0], "  ", doors[1])
        
        
        print("If you don't change")
        print("Your door still is ", door)
        print()
        
        if door == gift:
            results_strat1["win"] += 1
            print("you win !!")
            
        else:
            results_strat1["lose"] += 1
            print("you lose :(")
            print("the gift was in door ",gift)
        print()
    
        doors.remove(door)
        print("If you change")
        print("you made the right choice even though Rosi doesn't believe it")
        print("your door now is ", doors[0])
        print()
        
        if doors[0] == gift:
            results_strat2["win"] +=1
            print("you win !!")
            
        else:
            results_strat2["lose"] += 1
            print("you lose :(")
            print("the gift was in door ",gift)
        print()
    
    print("you played ", n, "games")
    print()
    print("when you changed you won ", results_strat2["win"],"times")
    print("the frequency of win is ", results_strat2["win"]/(results_strat2["win"]+results_strat2["lose"]))
    
    print()
    print("when you didn't change, you won ", results_strat1["win"], "times")
    print("the frequency of win is ", results_strat1["win"]/(results_strat1["win"]+results_strat1["lose"]))

game()









