import pygame
import sys

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
                        # Output the final string
                        final_string = ""
                        for f in FACES:
                            for row in face_color_data[f]:
                                final_string += "".join([cell if cell != "" else " " for cell in row])
                        print("Kociemba input:", final_string)
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    main()
