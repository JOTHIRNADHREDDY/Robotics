class differential_robot():
    def __init__(self,name,type,company):
        self.name = name
        self.type = type
        self.company = company
    def move(self):
        print("The robot is moving")
    def stop(self):
        print("The robot is stopping")
    def turn(self):
        print("The robot is turning")
    def display(self):
        print("Name: ",self.name)
        print("Type: ",self.type)
        print("Company: ",self.company)

class omni_directional_robot(differential_robot):
    def __init__(self,name,type,company):
        super().__init__(name,type,company)
    def move(self):
        print("The robot is moving")
    def stop(self):
        print("The robot is stopping")
    def turn(self):
        print("The robot is turning")
    def display(self):
        print("Name: ",self.name)
        print("Type: ",self.type)
        print("Company: ",self.company) 

class Mecanum_robot(differential_robot):
    def __init__(self,name,type,company):
        super().__init__(name,type,company)
    def move(self):
        print("The robot is moving")
    def stop(self):
        print("The robot is stopping")
    def turn(self):
        print("The robot is turning")
    def display(self):
        print("Name: ",self.name)
        print("Type: ",self.type)
        print("Company: ",self.company) 

class Soft_robot(differential_robot):
    def __init__(self,name,type,company):
        super().__init__(name,type,company)
    def move(self):
        print("The robot is moving")
    def stop(self):
        print("The robot is stopping")
    def turn(self):
        print("The robot is turning")
    def display(self):
        print("Name: ",self.name)
        print("Type: ",self.type)
        print("Company: ",self.company)


x1 = differential_robot("Differential Robot","Differential","ABB")
x1.display()
x1.move()
x1.stop()
x1.turn()

x2 = omni_directional_robot("Omni Directional Robot","Omni Directional","ABB")
x2.display()
x2.move()
x2.stop()
x2.turn()

x3 = Mecanum_robot("Mecanum Robot","Mecanum","ABB")
x3.display()
x3.move()
x3.stop()
x3.turn()

x4 = Soft_robot("Soft Robot","Soft","ABB")
x4.display()
x4.move()
x4.stop()
x4.turn()