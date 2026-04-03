import numpy as np
from mlx90640_code import get_thermal_frame

# Thresholds (adjust based on environment)
TEMP_THRESHOLD = 35.0
TEMP_DIFF_THRESHOLD = 5.0

def detect_anomaly(frame):
    avg_temp = np.mean(frame)
    max_temp = np.max(frame)

    # Condition 1: High temperature
    if max_temp > TEMP_THRESHOLD:
        return True

    # Condition 2: Sudden variation
    if (max_temp - avg_temp) > TEMP_DIFF_THRESHOLD:
        return True

    return False

def run_detection():
    while True:
        frame = get_thermal_frame()
        if frame is None:
            continue

        if detect_anomaly(frame):
            print("🔥 Possible Landmine Detected!")
        else:
            print("✅ Normal Area")

if __name__ == "__main__":
    run_detection()