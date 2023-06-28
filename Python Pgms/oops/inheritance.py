class GrandFather:
    def gf_display(self):
        print("This is grand father method")
        
class Father(GrandFather):
    def __init__(self):
        print("This is father constructor")
        
    def father_display(self):
        print("This is father method")
        
class Mother():
    def __init__(self):
        print("This is mother constructor")
        
    def mother_display(self):
        print("This is mother method")
        
class Child(Mother, Father):
    def __init__(self):
        print("This is child construtor")
        super().__init__()
        
        
    def child_display(self):
        print("This is child class")
        

obj=Child()
print(Child.mro()) #MRO - Method resolution Order
print(dir(obj))


# obj.gf_display()
# obj.father_display()
# obj.child_display()
# obj.mother_display()