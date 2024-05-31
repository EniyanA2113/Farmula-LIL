import serial
import time

ser = serial.Serial('COM3', 9600)
time.sleep(2)

while True:
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    if line:
        temperature = float(ser.readline().decode('utf-8').rstrip())
        humidity = float(ser.readline().decode('utf-8').rstrip())
        ph = float(ser.readline().decode('utf-8').rstrip())
        rainfall = float(ser.readline().decode('utf-8').rstrip())
        break
    print("Temperature: ",temperature," Humidity: ",humidity," Ph: ",ph," Rainfall: ",rainfall)