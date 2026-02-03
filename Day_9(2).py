# Vehicle Hierarchy
class vehicle():
    def __init__(self, type, company, surface_type):
        self.type = type
        self.company = company
        self.surface_type = surface_type
        
    def surface(self):
        print("the vehicle is going on ", self.surface_type)

class car(vehicle):
    def __init__(self, type, company, surface_type):
        super().__init__(type, company, surface_type)

class bike(vehicle):
    def __init__(self, type, company, surface_type):
        super().__init__(type, company, surface_type)

class boat(vehicle):
    def __init__(self, type, company, surface_type):
        super().__init__(type, company, surface_type)

class plane(vehicle):
    def __init__(self, type, company, surface_type):
        super().__init__(type, company, surface_type)

x1 = car("car", "Toyota", "Road")
x2 = bike("bike", "Honda", "Road")
x3 = boat("boat", "Yamaha", "Water")
x4 = plane("plane", "Boeing", "Air")

for i in (x1, x2, x3, x4):
    i.surface()

