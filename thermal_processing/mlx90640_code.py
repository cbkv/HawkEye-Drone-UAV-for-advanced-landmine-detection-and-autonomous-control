import board
import busio
import adafruit_mlx90640
import numpy as np

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

# Initialize sensor
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ

frame = [0] * 768  # 32x24 pixels

def get_thermal_frame():
    try:
        mlx.getFrame(frame)
        data = np.array(frame).reshape((24, 32))
        return data
    except ValueError:
        return None

if __name__ == "__main__":
    while True:
        temp_data = get_thermal_frame()
        if temp_data is not None:
            print("Max Temp:", np.max(temp_data))