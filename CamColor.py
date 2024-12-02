import cv2
import numpy as np
import kociemba

# Refined HSV color ranges for Rubik's Cube stickers
color_ranges = {
    'W': ([0, 0, 150], [180, 70, 255]),  # White
    'Y': ([25, 150, 150], [30, 255, 255]),  # Yellow
    'R1': ([0, 150, 100], [10, 255, 255]),  # Lower Red
    'R2': ([170, 150, 100], [180, 255, 255]),  # Upper Red
    'O': ([11, 150, 150], [24, 255, 255]),  # Orange
    'G': ([45, 120, 120], [75, 255, 255]),  # Refined Green
    'B': ([90, 120, 100], [130, 255, 255])  # Blue
}

# Hardcoded middle square colors for each scan
hardcoded_colors = ['W', 'R', 'G', 'Y', 'O', 'B']

# Helper function to detect the dominant color based on HSV
def detect_color(hsv_pixel, color_ranges):
    min_distance = float('inf')
    detected_color = '?'
    for color, (lower, upper) in color_ranges.items():
        lower_bound = np.array(lower, dtype=np.uint8)
        upper_bound = np.array(upper, dtype=np.uint8)
        range_center = (np.array(lower) + np.array(upper)) // 2
        distance = np.linalg.norm(hsv_pixel - range_center)
        if distance < min_distance:
            min_distance = distance
            detected_color = 'R' if color in ['R1', 'R2'] else color
    return detected_color

# Real-time Rubik's cube face scanner
def scan_face(cap, color_ranges, scan_index):
    print("Position the cube face within the grid. Press 'n' when ready to proceed to the next side.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break
        
        # Flip the frame horizontally for convenience
        frame = cv2.flip(frame, 1)

        # Draw a larger 3x3 grid on the frame
        height, width, _ = frame.shape
        grid_size = 150  # Increased grid size for better accuracy
        start_x = (width - 3 * grid_size) // 2
        start_y = (height - 3 * grid_size) // 2

        # Convert the frame to HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        face_colors = []

        for i in range(3):  # Process rows from top (0) to bottom (2)
            row_colors = []
            for j in range(2, -1, -1):  # Process columns from right (2) to left (0)
                x = start_x + j * grid_size + grid_size // 2
                y = start_y + i * grid_size + grid_size // 2

                # Draw grid rectangles
                cv2.rectangle(frame, (x - grid_size // 2, y - grid_size // 2), 
                              (x + grid_size // 2, y + grid_size // 2), (255, 255, 255), 3)

                # Hardcode the middle square color
                if i == 1 and j == 1:
                    detected_color = hardcoded_colors[scan_index]
                else:
                    # Detect the average HSV in a small region around the grid center
                    region_size = 20  # Averaging region size
                    hsv_region = hsv_frame[y-region_size:y+region_size, x-region_size:x+region_size]
                    average_hsv = np.mean(hsv_region.reshape(-1, 3), axis=0).astype(np.uint8)

                    # Detect the color
                    detected_color = detect_color(average_hsv, color_ranges)
                
                row_colors.append(detected_color)

                # Display the detected color in the grid center
                cv2.putText(frame, detected_color, (x - 30, y + 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 4)
            
            face_colors.extend(row_colors)

        # Display the frame
        cv2.imshow("Rubik's Cube Scanner", frame)

        # Wait for user input to proceed to the next side
        key = cv2.waitKey(1) & 0xFF
        if key == ord('n'):  # Proceed to the next side
            return face_colors
        elif key == ord('q'):  # Quit scanning
            return None

# Function to map scanned colors to Kociemba face notations
def convert_to_kociemba(cube_string):
    color_to_face = {
        'W': 'U',  # White -> Up
        'G': 'F',  # Green -> Front
        'Y': 'D',  # Yellow -> Down
        'O': 'L',  # Orange -> Left
        'R': 'R',  # Red -> Right
        'B': 'B'   # Blue -> Back
    }
    return ''.join(color_to_face[color] for color in cube_string)

# Solve the cube and print the steps
def solve_cube(cube_string):
    try:
        
        solution = kociemba.solve(cube_string)
        moves = solution.split()
        print("Total moves:", len(moves))
        print("Solution steps:")
        for move in moves:
            if move == "U":
                # print("U - Move white clockwise")
                input("U - Move white clockwise")
            elif move == "U'":
                # print("U' - Move white counterclockwise")
                input("U' - Move white counterclockwise")

            elif move == "U2":
                # print("U2 - Move white clockwise twice")
                input("U2 - Move white clockwise twice")
                
            elif move == "R":
                print("R")
                print("Move red clockwise")
            elif move == "R'":
                print("R'")
                print("Move red counterclockwise")
            elif move == "R2":
                print("R2")
                print("Move red clockwise twice")
                
            elif move == "F":
                print("F")
                print("Move green clockwise")
            elif move == "F'":
                print("F'")
                print("Move green counterclockwise")
            elif move == "F2":
                print("F2")
                print("Move green clockwise twice")
                
            elif move == "D":
                print("D")
                print("Move yellow clockwise")
            elif move == "D'":
                print("D'")
                print("Move yellow counterclockwise")
            elif move == "D2":
                print("D2")
                print("Move yellow clockwise twice")
            
            elif move == "L":
                print("L")
                print("Move orange clockwise")
            elif move == "L'":
                print("L'")
                print("Move orange counterclockwise")
            elif move == "L2":
                print("L2")
                print("Move orange clockwise twice")
                
            elif move == "B":
                print("B")
                print("Move blue clockwise")
            elif move == "B'":
                print("B'")
                print("Move blue counterclockwise")
            elif move == "B2":
                print("B2")
                print("Move blue clockwise twice")
            
            else:
                print("ERROR")
    except Exception as e:
        print("Error solving the cube:", e)
        

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
            face_colors = scan_face(cap, color_ranges, side)
            if face_colors is None:
                print("Scanning interrupted. Exiting.")
                break
            scanned_faces.extend(face_colors)
        
        if len(scanned_faces) == 54:
            # Combine scanned faces into a single string
            cube_string = ''.join(scanned_faces)
            print("Rubik's Cube scan complete!")
            print("Cube representation (original):")
            print(cube_string)

            # Convert the cube string to Kociemba notation
            kociemba_string = convert_to_kociemba(cube_string)
            # Prompt the user to confirm the Kociemba string or input a corrected one
            print("Cube representation (for Kociemba):")
            print(kociemba_string)
            user_input = input("\nIs this the correct cube representation? (y/n): ").strip().lower()

            if user_input == 'n':
                kociemba_string = input("Please enter the corrected cube representation string: ").strip()
                # Optionally validate the corrected string here
                if len(kociemba_string) != 54:
                    print("Error: The corrected string must be exactly 54 characters long.")
                    return  # Exit or handle error appropriately
                print("\nUsing the corrected cube representation.")

            # Prompt the user to place the cube in the machine
            print("\nEnter the cube into the machine.")
            input("Press Enter to confirm that the cube is placed...")
            # Solve and print the solution
            # solve_cube(kociemba_string)
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
