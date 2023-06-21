import random


def roll_dice():
    return random.randint(1, 6)

ip1= int(input("enter your choice - a number less than 7"))

if ip1 == 0:
  ip2 = int(input("enter your choice - a number greater than 7"))
if ip2 == 0:  
   ip3 = int(input("enter your choice - number 7"))


roll1 = roll_dice()
roll2 = roll_dice()
sum = roll1 + roll2
print("sum of 2 rolls is:", sum)

if sum < 7:
    if sum == ip1:
        print("Nice work - You win")
    else:    
        print("Better luck next time")
if sum > 7:
    if sum == ip2:
        print("Nice work - You win")
    else:    
        print("Better luck next time")    
if sum == 7:
    if sum == ip3:
        print("Nice work - You win")     
    else:    
        print("Better luck next time")               
  


