from machine import Pin, PWM
import time

led = PWM(Pin(9))
led.freq(1000) 

button = Pin(2, Pin.IN, Pin.PULL_UP)

brightness = 0
fade = 20  

while True:
    if button.value() == 0: 
        led.duty(brightness)

        brightness += fade

        if brightness <= 0 or brightness >= 1023:
            fade = -fade

        time.sleep(0.03)
    else:
        led.duty(0)