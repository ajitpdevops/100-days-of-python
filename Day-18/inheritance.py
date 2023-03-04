# Learn Inheritance 

class Animal:
    
    def __init__(self):
        self.num_eyes = 2
        
    def move(self):
        print("Moves forward")
    
    def breathe(self):
        print("Inhale, Exhale")
        

class Fish(Animal):
    
    def __init__(self):
        super().__init__()
        
    def swim(self):
        print("moving in water")
        
    def breathe(self):
        super().breathe()
        print("doing this underwater")
        

nemo = Fish()
nemo.breathe()