from dronekit import connect, VehicleMode
import time

vehicle = connect('/dev/ttyAMA0', baud=57600, wait_ready=True)

def arm_and_takeoff(target_altitude):
    while not vehicle.is_armable:
        print("Waiting for vehicle...")
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)

arm_and_takeoff(5)
