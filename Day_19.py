import serial
import time

port = 'COM3' 
baud = 9600

try:
    arduino = serial.Serial(port, baud, timeout=1)
    time.sleep(2) 
    print(f"Connected to {port}")
    
    while True:
        choice = input("Enter '1' for ON, '0' for OFF, or 'q' to quit: ")

        if choice == '1':
            arduino.write(b'1')
            print("Sent: ON")
        elif choice == '0':
            arduino.write(b'0')
            print("Sent: OFF")
        elif choice == 'q':
            break
            
    arduino.close()
    print("Connection closed.")

except Exception as e:
    print(f"Error: {e}")
