import serial
import time
import csv
import matplotlib.pyplot as plt

try:
    s = serial.Serial('COM1', 9600, timeout=0.1)
except Exception as e:
    print("could not open port:", e)
    exit()

t_data = []
p1_data = []
p2_data = []
p3_data = []

f = open('sensor_data.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['Time', 'Pot1', 'Pot2', 'Pot3'])
plt.ion()
fig, image = plt.subplots()

print("reading data... press Ctrl+C to stop")

try:
    while True:
        if s.in_waiting > 0:
            line = s.readline().decode('utf-8').strip()
            parts = line.split()
            
            if len(parts) == 6:
                try:
                    t = time.time()
                    p1 = int(parts[1])
                    p2 = int(parts[3])
                    p3 = int(parts[5])
                    
                    writer.writerow([t, p1, p2, p3])
                    
                    t_data.append(t)
                    p1_data.append(p1)
                    p2_data.append(p2)
                    p3_data.append(p3)
                    
                    image.clear()
                    image.plot(t_data[-50:], p1_data[-50:], 'r-', label="pot 1")
                    image.plot(t_data[-50:], p2_data[-50:], 'g-', label="pot 2")
                    image.plot(t_data[-50:], p3_data[-50:], 'b-', label="pot 3")
                    image.legend(loc="upper left")
                    plt.pause(0.01)
                    
                except ValueError:
                    pass
        else:
            plt.pause(0.01)
            
except KeyboardInterrupt:
    print("\nuser stopped the program.")

s.close()
f.close()
plt.close('all')
if len(t_data) > 0:
    print("saving final report and image...")
    
    plt.ioff()
    plt.figure()
    plt.plot(t_data, p1_data, 'r-')
    plt.plot(t_data, p2_data, 'g-')
    plt.plot(t_data, p3_data, 'b-')
    plt.title("Sensor Data")
    plt.savefig('summary_plot.png')
    plt.close()
    
    with open('final_report.txt', 'w') as out:
        out.write("--- Final Sensor Report ---\n")
        out.write(f"Total samples taken: {len(t_data)}\n")
        out.write(f"Pot 1 -> min: {min(p1_data)}, max: {max(p1_data)}, avg: {sum(p1_data)/len(p1_data):.2f}\n")
        out.write(f"Pot 2 -> min: {min(p2_data)}, max: {max(p2_data)}, avg: {sum(p2_data)/len(p2_data):.2f}\n")
        out.write(f"Pot 3 -> min: {min(p3_data)}, max: {max(p3_data)}, avg: {sum(p3_data)/len(p3_data):.2f}\n")
        
    print("all done!")
else:
    print("didn't get any data to save.")
