class Robot :
    def __init__(self,name,model,country):
        self.name = name
        self.model = model
        self.country = country

    def introduction(self):
        print("My name is " + self.name)
        print("My model is " + self.model)
        print("I was made in " + self.country)


robot1 = Robot("IRB_6700","INDUSTRIAL","SWITZERLAND")
robot1.introduction()