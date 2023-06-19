from functions import addition as a

a.sum(2, 4)



a = 2 #declaring single variable
print(a)
print(id(a))

a, b, c= 3, 2, 5 # declaring multiple variables in single line
print(a)
print(id(a))
print(b)
print(id(b))
print(c)
print(type(a))
print(type(b))
print(type(c))
b=b+1
print(id(b))
# print(dir(c))

'''declaring multiple variables with same value'''
a=b=c=10 # declaring multiple variables with same value
print(a)
print(b)
print(c)