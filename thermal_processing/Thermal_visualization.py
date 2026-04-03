import cv2
import numpy as np
from mlx90640_code import get_thermal_frame

def visualize_thermal():
    while True:
        frame = get_thermal_frame()
        if frame is None:
            continue

        # Normalize data
        normalized = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
        normalized = normalized.astype(np.uint8)

        # Resize for better visibility
        resized = cv2.resize(normalized, (320, 240), interpolation=cv2.INTER_CUBIC)

        # Apply heatmap
        heatmap = cv2.applyColorMap(resized, cv2.COLORMAP_JET)

        cv2.imshow("Thermal View", heatmap)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    visualize_thermal()