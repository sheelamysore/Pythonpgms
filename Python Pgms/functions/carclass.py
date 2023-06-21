class Car:
    wheels = 4
    
    def __init__(self, model, company, color):
        self.model = model
        self.company = company
        self.color = color
         
    def mycar(self):     
        print("My car is:", self.model + self.company )
        
car1 = Car("Innova", "Toyota", "Grey")
car1.mycar()         

class SUV(Car):
    
    def length(self):
        print("The length of an SUV ")
        
suv1 = SUV("Yaris", "Toyota", "Grey")
suv1.mycar()      
suv1.length()  
    
    