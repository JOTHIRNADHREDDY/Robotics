import serial
import csv
import time
import matplotlib.pyplot as plt

ser = serial.Serial('COM1', 9600)

csv_file = open('data_log.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(['Time', 'Pot1', 'Pot2', 'Pot3'])

plt.ion()
fig, ax = plt.subplots()

times, pot1, pot2, pot3 = [], [], [], []

print("Reading data... Close the plot or press Ctrl+C to stop.")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            
            parts = line.split()
            if len(parts) == 6:
                try:
                    t = time.time()
                    p1, p2, p3 = int(parts[1]), int(parts[3]), int(parts[5])
                    
                    writer.writerow([t, p1, p2, p3])
                    
                    times.append(t)
                    pot1.append(p1)
                    pot2.append(p2)
                    pot3.append(p3)
                    
                    ax.clear()
                    ax.plot(times[-50:], pot1[-50:], label="Pot 1")
                    ax.plot(times[-50:], pot2[-50:], label="Pot 2")
                    ax.plot(times[-50:], pot3[-50:], label="Pot 3")
                    ax.legend(loc="upper left")
                    plt.pause(0.01)
                    
                except ValueError:
                    continue 
                    
except KeyboardInterrupt:
    print("\nStopped.")
finally:
    ser.close()
    csv_file.close()
    
    print(f"\nFinal Summary:")
    print(f"Pot 1 -> Min: {min(pot1)}, Max: {max(pot1)}, Avg: {sum(pot1)/len(pot1):.1f}")
    print(f"Pot 2 -> Min: {min(pot2)}, Max: {max(pot2)}, Avg: {sum(pot2)/len(pot2):.1f}")
    print(f"Pot 3 -> Min: {min(pot3)}, Max: {max(pot3)}, Avg: {sum(pot3)/len(pot3):.1f}")
