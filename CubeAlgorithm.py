import kociemba
# pip install kociemba

def get_cube_colors():
    """
    Prompt the user to input the cube colors in the specific format.
    Returns:
        str: A 54-character string representing the cube's state.
    """
    # print(
    #     "Enter the cube colors in the following order:\n"
    #     "U1U2U3U4U5U6U7U8U9 R1R2R3R4R5R6R7R8R9 F1F2F3F4F5F6F7F8F9 "
    #     "D1D2D3D4D5D6D7D8D9 L1L2L3L4L5L6L7L8L9 B1B2B3B4B5B6B7B8B9\n"
    #     "Use the following notation:\n"
    #     "U (white), R (red), F (green), D (yellow), L (orange), B (blue)\n"
    # )
    print("The string needs to be in the correct format.")
    cube_colors = input("Enter the 54-character string for the cube state: ")
    if len(cube_colors) != 54:
        raise ValueError("Invalid input! Ensure the input is exactly 54 characters long.")
    return cube_colors

def solve_rubik_cube():
    try:
        # Get the cube state from the user
        cube_state = get_cube_colors()

        # Solve the cube using Kociemba's algorithm
        solution = kociemba.solve(cube_state)
        moves = solution.split()
        print("Total moves:", len(moves))
        print("Solution steps:")
        print("\nSolution moves:")
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
        
        # Here, add code to execute moves with robot actuators
    except Exception as e:
        print("Error solving the cube:", e)

# Run the solver
solve_rubik_cube()
