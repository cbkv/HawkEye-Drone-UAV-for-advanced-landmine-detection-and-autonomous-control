import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    value = int(ser.readline().decode().strip())
    
    if value > 500:
        print("Metal Detected!")
    else:
        print("No Metal")