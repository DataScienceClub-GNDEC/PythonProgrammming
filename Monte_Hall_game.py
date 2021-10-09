#  3 doors and choose 1

import random
doorskey = [1,2,3]
doorsval = []
doors = {}
x = random.choice(doorskey)   # Randomly choosed the door name from the list doorskey
doors[x] = "BMW"    
doorskey.remove(x)    # Removed that door that contains 'BMW'
for i in doorskey:
    doors[i] = "GOAT"   # Assigned other doors the value 'GOAT'
    
choose_door = int(input("Enter your choice: "))    # user pic out 1 door

door_open = random.choice(doorskey)     # We will randomly open a 'GOAT' door

while door_open == choose_door:     # If randomly opened door matches with the user choiced door 
    door_open = random.choice(doorskey)    # then we will again randomly open the 'GOAT' door
    
ch = input("Do you want to swap? y/n :")    # user choose to swap his/her choice or not
if ch=='y':
    if doors[choose_door] == "GOAT":    # If swapped and initial choosed choice was 'GOAT' then user wins
        print("You Won!")
    else:
        print("You Lose!")
if ch=='n':
    if doors[choose_door] == "GOAT":
        print("You Lose!")
    else:
        print("You Won!")