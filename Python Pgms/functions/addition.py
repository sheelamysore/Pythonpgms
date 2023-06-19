def say_hello():
    name=input("Please enter your name:")
    print("hello.. welcome!", name)




# say_hello(name)

def sum(a, b):
    print("a",a)
    print("b", b)
    print(a+b)

# sum(2, 3)
# sum(b=-8, a=7)

def sample(**a):
    print(a)
    for i in a.values():
        print(i)


# sample(a=2, b=3, c=4)

