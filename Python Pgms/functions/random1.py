import random
import string

print(random.randint(1, 10))
b = [1, 2, 3.0, 4.556, "abc"]
print(random.choice(b))
print(random.randrange(1, 100, 9))
print(random.choices(string.digits, k=10))