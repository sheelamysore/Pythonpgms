import random


def roll_dice():
    return random.randint(1, 6)

ip1= int(input("enter a number"))


roll1 = roll_dice()
roll2 = roll_dice()
sum = roll1 + roll2
print("sum of 2 rolls is:", sum)

if sum < 7:
    if sum == ip1:
        print("Nice work")
  


