# Color Detection using OpenCV

## Overview
This Python script detects and classifies colors in real-time using OpenCV. It captures video from a webcam, extracts the HSV (Hue, Saturation, Value) values of the center pixel, and determines the color name, including light and dark variations.

## Features
- Detects basic colors: Red, Orange, Yellow, Green, Cyan, Blue, Violet, and Pink.
- Identifies light and dark variations of colors (e.g., Light Blue, Dark Green).
- Displays the detected color name on the video feed.
- Draws a small circle at the center of the frame to indicate the sampled pixel.

## Installation
### Prerequisites
Ensure you have Python installed along with the following dependencies:

```sh
pip install opencv-python numpy
```

## Usage
1. Run the script:
   ```sh
   python color_detection.py
   ```
2. The webcam feed will open, detecting and displaying the color of the center pixel.
3. Press `ESC` to exit.

## How It Works
1. Captures a video frame from the webcam.
2. Converts the frame to HSV format.
3. Extracts the HSV values from the center pixel.
4. Uses predefined hue ranges to classify the color.
5. Adjusts classification based on the Value (brightness) to differentiate light and dark shades.
6. Displays the detected color name on the video feed.

## Color Ranges
The script classifies colors based on the Hue value and further differentiates them based on brightness (Value component in HSV):

| Color | Hue Range | Variations |
|--------|-----------|--------------|
| Red | 0-10, 170-180 | Dark Red, Red |
| Orange | 10-25 | Dark Orange, Orange |
| Yellow | 25-35 | Dark Yellow, Yellow |
| Green | 35-85 | Dark Green, Green, Light Green |
| Cyan | 85-100 | Dark Cyan, Cyan, Light Cyan |
| Blue | 100-130 | Dark Blue, Blue, Light Blue |
| Violet | 130-150 | Dark Violet, Violet, Light Violet |
| Pink | 150-170 | Dark Pink, Pink, Light Pink |

## License
This project is open-source and free to use under the MIT License.

