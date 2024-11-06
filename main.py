import cv2
import numpy as np

# Define HSV color ranges for typical Rubik's cube colors
color_ranges = {
    'red': [(0, 120, 70), (10, 255, 255)],
    'green': [(35, 100, 100), (85, 255, 255)],
    'blue': [(100, 150, 0), (140, 255, 255)],
    'yellow': [(20, 100, 100), (30, 255, 255)],
    'orange': [(10, 100, 20), (25, 255, 255)],
    'white': [(0, 0, 200), (180, 20, 255)]
}

# Load the image
image_path = "rubiks_cube.jpg"  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image loaded successfully
if image is None:
    print("Error loading image.")
else:
    # Convert the image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Detect colors
    for color, (lower, upper) in color_ranges.items():
        lower_np = np.array(lower, dtype="uint8")
        upper_np = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower_np, upper_np)

        # Find contours for the detected colors
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Filter small areas
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(image, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Display the result
    cv2.imshow("Rubik's Cube Color Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
