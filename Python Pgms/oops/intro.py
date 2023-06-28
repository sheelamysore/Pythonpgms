from abc import *

class Sample(ABC):
    def display(self):
        print("This is sample class")
     
    @abstractmethod    
    def sum(self,a ,b):
        pass
        
        
obj=Sample()
obj.display()
# obj2=Sample()
# obj2.display()
# print(type(obj2))
# print(id(obj))
# print(id(obj2))
# print(dir(obj))

# class Student:
#
#     school="abc" # class variables
#     def __init__(self, name, roll_no):
#         self.name=name #instance/ object variables
#         self.roll_no= roll_no
#         print(f"name of the student is {self.name} and roll no, is {self.roll_no} and school is {Student.school}")
#
#     def display_details(self):
#         print("This is display method")
#
#     def sum_of_subjects(self, kannada, english):
#         print(f"Total marks obtained by {self.name}",kannada+english) #method variables
#
#
#
#
# std1=Student("vivek", 1)
# std1.name="Manju"
# std1.sum_of_subjects(100, 99)
# print(dir(std1))
# std2=Student("sheela", 2)
# print(std2.name)
# print(std1.name)
# std.display_details()