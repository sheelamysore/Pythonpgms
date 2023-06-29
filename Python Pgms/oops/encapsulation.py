class Parent:
    def __init__(self):
        self.__a=2
        
    def get_variable(self):
        print("Value of a is:", self._a)
        
        
obj= Parent()
# print(dir(obj))
# print(obj.a) # name mangling
# obj._a=4
# print(obj._a)

try:
    try:
        print(obj.a)
    except AttributeError as a:
        print(obj._a)
        obj._a=4
        print(obj._a)    
except:
    print(obj._Parent__a)
    
