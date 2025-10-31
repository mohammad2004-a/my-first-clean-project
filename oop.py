class Dog:
    def __init__(self,name,age,color,size):
        self.name = name
        self.age = age
        self.color = color
        self.size = size
        
    def bark(self):
        print(f"{self.name} woof!")
        
    def eat(self,food):
        print(f"{self.name} eating {food}!")
        
    def sit(self,order):
        self.order = order
        if order == "sit down":
            print(f"{self.name} sit.")
            
    def hour_sleep(self):
        if self.size <= 1 :
            print(f"{self.name} dog needs six hours of sleep. ") 
        elif self.size >1 and self.size<= 2 :
            print(f"{self.name} dog needs four hours of sleep. ")
        else:
            print(f"{self.name} dog needs tow hours of sleep. ") 
 

class Germandog(Dog):
    def __init__(self, name, age, color, size,speed):
        super().__init__(name,age,color,size)
        self.speed = speed
    
    def bark(self):
        print(f"{self.name} : woof woof!")
        
    def sit(self,order):
        self.order = order
        if order == "booo":
            print(f"{self.name} sit.")
    
    def serch(self,clothes):
        self.list = ["Shawl","shirt","pants"]
        self.clothes = clothes
        if self.clothes == self.list[1]:
            print(f"{self.name} is looking for a human.")
            
                
                                
        
        
dog1 = Dog(name = "jeseei" , age = 3 , color = "wight" , size = 1.5)            
dog1.bark()
dog1.eat("meat")
dog1.sit("sit down")
dog1.hour_sleep()
print("-------------------------------------------------------------")
dog2 = Germandog(name = "joe" , age = 5 , color = "brown" , size = 3 , speed = 40)
dog2.bark()
dog2.eat("milk")
dog2.sit("booo")
dog2.hour_sleep()
dog2.serch("shirt")
