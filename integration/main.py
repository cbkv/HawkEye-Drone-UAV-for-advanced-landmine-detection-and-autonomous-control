from gps_mapping import get_location
from alert_system import send_alert
from data_logging import log_data

def detect_landmine(metal, thermal):
    if metal or thermal:
        return True
    return False

while True:
    metal_detected = False  # from metal module
    thermal_detected = True  # from AI model

    if detect_landmine(metal_detected, thermal_detected):
        location = get_location()
        send_alert(location)
        log_data(location, "LANDMINE DETECTED")