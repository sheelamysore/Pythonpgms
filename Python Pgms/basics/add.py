def sum(a, b):
    print("a",a)
    print("b", b)
    print(a+b)

# sum(2, 3)
# sum(b=-8, a=7)

def sample(*a):
    for i in a:
        print(i)


sample(2, 3, 4)
