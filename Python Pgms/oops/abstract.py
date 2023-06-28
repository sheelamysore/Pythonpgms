from abc import *

class Car(ABC):
    wheels = 4
    
    def __init__(self, model, company, color):
        self.model = model
        self.company = company
        self.color = color
         
    def mycar(self):     
        print("My car is:", self.model + self.company )
    
    @abstractmethod   
    def display_length(self):
        pass
        
# car1 = Car("Innova", "Toyota", "Grey")
# car1.mycar()         

class SUV(Car):
    
    def display_length(self):
        print("Length of SUV is 2mts")
        
    def length(self):
        print("The length of an SUV ")
        
suv1 = SUV("Yaris", "Toyota", "Grey")
suv1.mycar()      
suv1.length()