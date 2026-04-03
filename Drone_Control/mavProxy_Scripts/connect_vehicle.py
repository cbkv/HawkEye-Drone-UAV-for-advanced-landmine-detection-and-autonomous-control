from dronekit import connect

# Connect to Pixhawk (Raspberry Pi)
vehicle = connect('devttyAMA0', baud=57600, wait_ready=True)

print(Connected to vehicle)
print(GPS, vehicle.gps_0)
print(Battery, vehicle.battery)
