#snake water gun
import random
lst = ['s','w','g']
chance = 5
no_of_chance = 0
comp_pt = 0
user_pt = 0
print("enter s for snake w for water and g for gun")
while no_of_chance < chance:
    input_by_ur = input("snake, water and gun :")
    _random = random.choice(lst)
    
    if input_by_ur ==_random:
        print("Tie Both 0 point to each\n")
    elif (input_by_ur == 's' and _random == 'w') or (input_by_ur == 'g' and _random == 's') or (input_by_ur == 'w' and _random == 'g') :
        comp_pt = comp_pt + 0
        user_pt = user_pt + 1
        print(f"your point {user_pt} and computer pt is {comp_pt}")
    elif (input_by_ur == 's' and _random == 'g') or (input_by_ur == 'g' and _random == 'w') or (input_by_ur == 'w' and _random == 's') :
        comp_pt = comp_pt + 1
        user_pt = user_pt + 0
        print(f"your point {user_pt} and computer pt is {comp_pt}")
    else:
        print("your input is wrong")
    no_of_chance = no_of_chance + 1
    print(f" {chance-no_of_chance} is left out of {chance}\n")
print("GAME OVER")

if comp_pt > user_pt:
    print("computer win")
if comp_pt < user_pt:
    print("you win")
print(f"your point {user_pt} and computer point {comp_pt}")