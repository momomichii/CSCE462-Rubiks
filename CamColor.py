import cv2
import numpy as np

# Define color ranges (HSV) for Rubik's Cube colors
color_ranges = {
    'W': ([0, 0, 200], [180, 50, 255]),  # White
    'Y': ([20, 100, 100], [30, 255, 255]),  # Yellow
    'R': ([0, 100, 100], [10, 255, 255]),  # Red
    'O': ([10, 100, 100], [20, 255, 255]),  # Orange
    'G': ([40, 50, 50], [80, 255, 255]),  # Green
    'B': ([90, 50, 50], [130, 255, 255])  # Blue
}

# Helper function to detect the dominant color in a given region
def detect_color(hsv_pixel, color_ranges):
    for color, (lower, upper) in color_ranges.items():
        lower_bound = np.array(lower, dtype=np.uint8)
        upper_bound = np.array(upper, dtype=np.uint8)
        if cv2.inRange(hsv_pixel.reshape(1, 1, 3), lower_bound, upper_bound).any():
            return color
    return '?'  # Unknown color

# Real-time Rubik's cube face scanner
def scan_face(cap, color_ranges):
    print("Position the cube face within the grid. Press 'n' when ready to proceed to the next side.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break
        
        # Draw a larger 3x3 grid on the frame
        height, width, _ = frame.shape
        grid_size = 150  # Increased grid size
        start_x = (width - 3 * grid_size) // 2
        start_y = (height - 3 * grid_size) // 2
        
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        face_colors = []

        for i in range(3):
            row_colors = []
            for j in range(3):
                x = start_x + i * grid_size + grid_size // 2
                y = start_y + j * grid_size + grid_size // 2
                
                # Draw grid rectangles
                cv2.rectangle(frame, (x - grid_size // 2, y - grid_size // 2), 
                              (x + grid_size // 2, y + grid_size // 2), (255, 255, 255), 3)
                
                # Detect the color in the grid center
                hsv_pixel = hsv_frame[y, x]
                detected_color = detect_color(hsv_pixel, color_ranges)
                row_colors.append(detected_color)
                
                # Display the detected color in the center of each grid (bigger letters)
                cv2.putText(frame, detected_color, (x - 30, y + 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 4)
            
            face_colors.append(row_colors)

        # Display the frame
        cv2.imshow("Rubik's Cube Scanner", frame)

        # Wait for user input to proceed to the next side
        key = cv2.waitKey(1) & 0xFF
        if key == ord('n'):  # Proceed to the next side
            return face_colors
        elif key == ord('q'):  # Quit scanning
            return None

# Main program
def main():
    cap = cv2.VideoCapture(0)  # Open laptop camera
    if not cap.isOpened():
        print("Could not open the camera.")
        return

    print("Scanning Rubik's cube faces. Follow the prompts.")
    scanned_faces = []
    try:
        for side in range(6):
            print(f"Scanning side {side + 1}. Position the cube and press 'n' when ready.")
            face_colors = scan_face(cap, color_ranges)
            if face_colors is None:
                print("Scanning interrupted. Exiting.")
                break
            scanned_faces.append(face_colors)
        
        if len(scanned_faces) == 6:
            # Flatten the scanned faces into a single string
            cube_string = ''.join([''.join(row) for face in scanned_faces for row in face])
            print("Rubik's Cube scan complete!")
            print("Cube representation (for Kociemba):")
            print(cube_string)
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
