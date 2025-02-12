import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    # Get the center coordinates of the frame
    cx = int(width / 2)
    cy = int(height / 2)

    # Extract HSV values from the center pixel
    pixel_center_hsv = hsv_frame[cy, cx]
    hue_value = pixel_center_hsv[0]
    saturation = pixel_center_hsv[1]
    value = pixel_center_hsv[2]

    # Determine color classification based on Hue and Value
    color = "Undefined"
    if 0 <= hue_value < 10 or 170 <= hue_value <= 180:
        color = "Red" if value > 100 else "Dark Red"
    elif 10 <= hue_value < 25:
        color = "Orange" if value > 100 else "Dark Orange"
    elif 25 <= hue_value < 35:
        color = "Yellow" if value > 100 else "Dark Yellow"
    elif 35 <= hue_value < 85:
        color = "Light Green" if value > 150 else "Green" if value > 100 else "Dark Green"
    elif 85 <= hue_value < 100:
        color = "Light Cyan" if value > 150 else "Cyan" if value > 100 else "Dark Cyan"
    elif 100 <= hue_value < 130:
        color = "Light Blue" if value > 150 else "Blue" if value > 100 else "Dark Blue"
    elif 130 <= hue_value < 150:
        color = "Light Violet" if value > 150 else "Violet" if value > 100 else "Dark Violet"
    elif 150 <= hue_value < 170:
        color = "Light Pink" if value > 150 else "Pink" if value > 100 else "Dark Pink"

    # Get BGR values to use for text color
    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    # Display the detected color name
    cv2.putText(frame, f"Color: {color}", (10, 78), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (b, g, r), 2)

    # Draw a small circle at the center
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

    if key == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()