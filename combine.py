import pygame
import sys
import kociemba

# Define constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 50
MARGIN = 10
ROWS, COLS = 3, 3
FACES = ["U", "R", "F", "D", "L", "B"]
COLORS = {
    "W": (255, 255, 255),  # White
    "R": (255, 0, 0),      # Red
    "B": (0, 0, 255),      # Blue
    "G": (0, 255, 0),      # Green
    "Y": (255, 255, 0),    # Yellow
    "O": (255, 165, 0)     # Orange
}
color_keys = list(COLORS.keys())
center_colors = {
    "U": "W",  # White
    "R": "R",  # Red
    "F": "G",  # Green
    "D": "Y",  # Yellow
    "L": "O",  # Orange
    "B": "B"   # Blue
}
face_color_data = {
    face: [["", "", ""], ["", center_colors[face], ""], ["", "", ""]]
    for face in FACES
}

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rubik's Cube Color Input")
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

current_face_index = 0
selected_color = color_keys[0]  # Start with the first color


def draw_face_grid(face, face_data, top_left):
    x_start, y_start = top_left
    for row in range(ROWS):
        for col in range(COLS):
            # Pre-filled middle piece color
            if row == 1 and col == 1:
                cell_color = COLORS[face_data[row][col]]
            else:
                cell_color = COLORS.get(face_data[row][col], (200, 200, 200))  # Default gray
            rect = pygame.Rect(
                x_start + col * (GRID_SIZE + MARGIN),
                y_start + row * (GRID_SIZE + MARGIN),
                GRID_SIZE,
                GRID_SIZE
            )
            pygame.draw.rect(screen, cell_color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)  # Border


def convert_to_kociemba_format(cube_state):
    # Mapping from user input colors to cube notation
    color_mapping = {
        "W": "U",  # White to Up
        "G": "F",  # Green to Front
        "Y": "D",  # Yellow to Down
        "O": "L",  # Orange to Left
        "R": "R",  # Red to Right
        "B": "B"   # Blue to Back
    }

    # Convert the string by applying the color mapping
    converted_state = ""
    for color in cube_state:
        if color != " ":
            converted_state += color_mapping.get(color, color)

    return converted_state


def solve_rubik_cube(cube_state):
    try:
        # Convert the cube state to the correct format for Kociemba
        formatted_state = convert_to_kociemba_format(cube_state)
        print(f"Formatted Cube State for Kociemba: {formatted_state}")


        # Use Kociemba's algorithm to get the solution
        solution = kociemba.solve(formatted_state)
        moves = solution.split()
        print("Total moves:", len(moves))
        print("\nSolution moves:")

        # Provide instructions for the moves
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
                print("R - Move red clockwise")
            elif move == "R'":
                print("R' - Move red counterclockwise")
            elif move == "R2":
                print("R2 - Move red clockwise twice")
            elif move == "F":
                print("F - Move green clockwise")
            elif move == "F'":
                print("F' - Move green counterclockwise")
            elif move == "F2":
                print("F2 - Move green clockwise twice")
            elif move == "D":
                print("D - Move yellow clockwise")
            elif move == "D'":
                print("D' - Move yellow counterclockwise")
            elif move == "D2":
                print("D2 - Move yellow clockwise twice")
            elif move == "L":
                print("L - Move orange clockwise")
            elif move == "L'":
                print("L' - Move orange counterclockwise")
            elif move == "L2":
                print("L2 - Move orange clockwise twice")
            elif move == "B":
                print("B - Move blue clockwise")
            elif move == "B'":
                print("B' - Move blue counterclockwise")
            elif move == "B2":
                print("B2 - Move blue clockwise twice")
            else:
                print("ERROR: Unrecognized move")

    except Exception as e:
        print("Error solving the cube:", e)


def main():
    global current_face_index, selected_color

    while True:
        screen.fill((50, 50, 50))

        # Display the current face and instructions
        face = FACES[current_face_index]
        face_data = face_color_data[face]
        title = font.render(f"Face: {face}", True, (255, 255, 255))
        screen.blit(title, (10, 10))
        instruction = font.render("Use 1-6 to pick a color, click to assign, Enter to proceed", True, (255, 255, 255))
        screen.blit(instruction, (10, 50))

        # Add color mapping instructions
        color_instructions = [
            "1: White, 2: Red, 3: Blue, 4: Green, 5: Yellow, 6: Orange"
        ]
        for i, line in enumerate(color_instructions):
            instruction_text = small_font.render(line, True, (255, 255, 255))
            screen.blit(instruction_text, (10, 90 + i * 30))

        # Draw the grid
        draw_face_grid(face, face_data, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Check if the click is within the grid
                top_left = (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100)
                grid_x = (x - top_left[0]) // (GRID_SIZE + MARGIN)
                grid_y = (y - top_left[1]) // (GRID_SIZE + MARGIN)
                if 0 <= grid_x < COLS and 0 <= grid_y < ROWS and not (grid_x == 1 and grid_y == 1):
                    face_color_data[face][grid_y][grid_x] = selected_color

            if event.type == pygame.KEYDOWN:
                # Use number keys 1-6 to select a color
                if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6):
                    selected_color = color_keys[event.key - pygame.K_1]

                # Move to the next face with Enter
                elif event.key == pygame.K_RETURN:
                    current_face_index += 1
                    if current_face_index >= len(FACES):
                        # Construct the cube state string
                        cube_state = ""
                        for f in FACES:
                            for row in face_color_data[f]:
                                cube_state += "".join([cell if cell else " " for cell in row])
                        # Prompt the user to place the cube in the machine
                        print("\nEnter the cube into the machine.")
                        input("Press Enter to confirm that the cube is placed...")
                        # Solve the cube with the converted state
                        print("Cube state for solving:", cube_state)
                        # solve_rubik_cube(cube_state)  # Pass the input state here
                        formatted_state = convert_to_kociemba_format(cube_state)
                        print(f"Formatted Cube State for Kociemba: {formatted_state}")
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    main()
