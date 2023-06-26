class MathOperation:
        
    def sum(self, a=0, b=0, c=0):
        print(a+b+c)
        
    def add(self, *a):
        total=0
        for x in a:
            total=total+x
        print(total)
        
        
obj=MathOperation()
obj.sum(2, 3, 5)
obj.add(4, 5, 6, 7, 5)


# class ConstructorOverloading:
#     def __init__(self):
#         print("This is NO arg constructor")
#
#     def __init__(self, a):
#         print("This is single arg constructor")