import random


def roll_dice():
    return random.randint(1, 6)

ip1= int(input("enter your choice - 1. for a number less than 7, 2. For a number greater than 7, 3. for 7" ))

roll1 = roll_dice()
roll2 = roll_dice()
sum = roll1 + roll2
print("sum of 2 rolls is:", sum)

if sum < 7:
    if ip1 == 1:
        print("Nice work - You win")
    else:    
        print("Better luck next time")
if sum > 7:
    if ip1 == 2:
        print("Nice work - You win")
    else:    
        print("Better luck next time")    
if sum == 7:
    if ip1 == 3:
        print("Nice work - You win")     
    else:    
        print("Better luck next time")               
  


