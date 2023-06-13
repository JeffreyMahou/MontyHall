######## IMPORTS ######

from random import randint

######## CODE ########

def game(n=100):
    
    win = [0,0]
    lose = [0,0]
    
    dic = {0:"A",1:"B",2:"C"}
    
    for i in range(n):
        
        print("the 3 doors are in front of you")
        print("A   B   C")
        print("")
        
        doors = [0,1,2]
        door = randint(0,2)
        gift = randint(0,2)
        
        print("You picked door ",dic[door])
        
        push = [0,1,2]
        push.remove(door)
        
        if door != gift:
            push.remove(gift)
            
        push_ind = randint(0,len(push)-1)
        pushed = push[push_ind]
        doors.remove(pushed)
        
        print("Behind the door ",dic[pushed],"there is ........ nothing")
        print()
        print("The remaining doors are ......")
        print()
        print(dic[doors[0]],"  ",dic[doors[1]])
        
        changed = randint(0,1)
        
        if changed == 0:
            print("You don't change")
            print("Your door still is ",dic[door])
            print()
            
            if door == gift:
                win[0] += 1
                print("you win !!")
                
            else:
                lose[0] += 1
                print("you lose :(")
                print("the gift was in door ",gift)
            print()
        
        else:
            doors.remove(door)
            print("you change")
            print("you made the right choice even though Rosi doesn't believe it")
            print("your door now is ",dic[doors[0]])
            print()
            
            if doors[0] == gift:
                win[1] +=1
                print("you win !!")
                
            else:
                lose[1] += 1
                print("you lose :(")
                print("the gift was in door ",gift)
            print()
    
    print("you played ",n,"games")
    print()
    print("you changed ",win[1]+lose[1],"times")
    if win[1]+lose[1] > 0 :
        print("when you changed you won ",win[1],"times")
        print("the frequency of win is ",win[1]/(win[1]+lose[1]))
    
    print()
    print("you kept the door ",win[0]+lose[0])
    if win[0]+lose[0] > 0 :
        print("when doing this you won ",win[0],"times")
        print("the frequency of win is ",win[0]/(win[0]+lose[0]))











