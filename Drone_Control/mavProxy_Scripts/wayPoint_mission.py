from dronekit import connect, LocationGlobalRelative

vehicle = connect('/dev/ttyAMA0', baud=57600)

# Example waypoint
point1 = LocationGlobalRelative(13.0827, 80.2707, 5)

vehicle.simple_goto(point1)
print("Going to waypoint...")
