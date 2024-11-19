import kociemba
#pip install kociemba

def scan_cube():
    # Replace this with your camera scanning logic using OpenCV
    # For example: return a string like 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
  
    cube_colors = "URDBUUUDLFRLBRRRFFFLDUFDUDDRRBDDURLDLULLLLBFFBFBBBBRFU" #example of it solved
    # the colors go from left to right and top and down, starts with White(U), red(R), Green(F), Yellow(D), orange (L), blue(B)
    #U1U2U3U4U5U6U7U8U9 R1R2R3R4R5R6R7R8R9 F1F2F3F4F5F6F7F8F9 D1D2D3D4D5D6D7D8D9 L1L2L3L4L5L6L7L8L9 B1B2B3B4B5B6B7B8B9
    # the input will use U, R, F, D, L, B but in the order above to represent the colors of the cube
    return cube_colors

def solve_rubik_cube():
    # Scan cube to get the current state
    cube_state = scan_cube()
    
    try:
        # Use Kociemba's algorithm to get the solution
        solution = kociemba.solve(cube_state)
        moves = solution.split()
        print("Solution moves:")
        #need to just add motor movements
        for move in moves:
            if move == "U":
                print("U")
            elif move == "U'":
                print("U'")
            elif move == "U2":
                print("U2")
                
            elif move == "R":
                print("R")
            elif move == "R'":
                print("R'")
            elif move == "R2":
                print("R2")
                
            elif move == "F":
                print("F")
            elif move == "F'":
                print("F'")
            elif move == "F2":
                print("F2")
                
            elif move == "D":
                print("D")
            elif move == "D'":
                print("D'")
            elif move == "D2":
                print("D2")
            
            elif move == "L":
                print("L")
            elif move == "L'":
                print("L'")
            elif move == "L2":
                print("L2")
                
            elif move == "B":
                print("B")
            elif move == "B'":
                print("B'")
            elif move == "B2":
                print("B2")
            
            else:
                print("ERROR")
            # print(move)
        
        # Here, add code to execute moves with robot actuators
    except Exception as e:
        print("Error solving the cube:", e)

# Run the solver
solve_rubik_cube()
# A single letter by itself means to turn that face clockwise 90 degrees.
# A letter followed by an apostrophe means to turn that face counterclockwise 90 degrees.
# A letter with the number 2 after it means to turn that face 180 degrees.


