from machine import Pin, ADC
import time

pot1 = ADC(Pin(26))   
pot2 = ADC(Pin(27))   
pot3 = ADC(Pin(28))   

led = Pin(13, Pin.OUT)

while True:
    val1 = pot1.read_u16()   
    val2 = pot2.read_u16()
    val3 = pot3.read_u16()

    val1_scaled = val1 // 64
    val2_scaled = val2 // 64
    val3_scaled = val3 // 64

    print("Pot1:", val1_scaled,
          "Pot2:", val2_scaled,
          "Pot3:", val3_scaled)

    led.value(1)
    time.sleep(0.1)
    led.value(0)
    time.sleep(0.1)