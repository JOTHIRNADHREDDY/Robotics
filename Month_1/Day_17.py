from machine import Pin
import time

trigger = Pin(9, Pin.OUT)
echo = Pin(10, Pin.IN)

def get_distance():
  
    trigger.value(0)
    time.sleep_us(2)

    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    while echo.value() == 0:
        pass
    start = time.ticks_us()

    while echo.value() == 1:
        pass
    end = time.ticks_us()

    duration = time.ticks_diff(end, start)

    distance = (duration * 0.034) / 2
    return distance

while True:
    dist = get_distance()
    print("Distance:", dist, "cm")
    time.sleep(0.5)