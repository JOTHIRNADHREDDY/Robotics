#Robotic Simulator
import matplotlib.pyplot as plt
import math
class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0     
        self.wheel_dist = 0.5
        self.path_x = [0]
        self.path_y = [0]

    def move(self, L_speed, R_speed):
        speed = (L_speed + R_speed) / 2
        turn = (R_speed - L_speed) / self.wheel_dist
        self.x = self.x + (speed * math.cos(self.angle) * 0.1)
        self.y = self.y + (speed * math.sin(self.angle) * 0.1)
        self.angle = self.angle + (turn * 0.1)
        self.path_x.append(self.x)
        self.path_y.append(self.y)

my_robot = Robot()

for i in range(50):
    my_robot.move(1.0, 1.2) 

plt.plot(my_robot.path_x, my_robot.path_y, label="Robot")
plt.title(" Robot Class")
plt.grid(True)
plt.legend()
plt.show()