import tkinter
import time

# Define the size of each cell in the maze
CELL_SIZE = 40

# Global variables for path positions and length
global path_positions
global Length
Length = 0
path_positions = []

# Time interval for controlling animation speed
SLEEP_TIME = 0.1

# Possible directions for movement in the maze (up, right, down, left)
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

###################################################################################################################################################

def maze_UI(maze):  # Function to render the maze UI
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            color = "white"  # Default cell color
            outline = "black"  # Default outline color
            width = 1  # Default line width

            # Adjust cell appearance based on maze content
            if maze[i][j] == -1:  # Wall cell
                color = "black"
                outline = "white"
                width = 1
            if maze[i][j] == 1:  # Start cell
                color = "red"
                outline = "black"
                width = 1
            if maze[i][j] == 2:  # Goal cell
                color = "green"
                outline = "black"
                width = 1

            # Create rectangle representing maze cells
            canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE,(j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE, fill=color, outline=outline, width=width)

###################################################################################################################################################
def DepthFirstSearch(maze, start, goal):
    
    if (path_positions) != []: # Clear the maze from used cells
        for pos in path_positions:
                x, y = pos
                canvas.create_rectangle(y * CELL_SIZE, x * CELL_SIZE, (y + 1) * CELL_SIZE, (x + 1) * CELL_SIZE, fill="white")
                window.update()
    path_positions.clear() # Empty the array
    stack = [start] # Stack collection for DFS
    global Length # Calculate the number of cells passed
    close = [] # Check for free cells to pass through
    
    while stack: # Main loop
        (x, y)= stack.pop()
        if (x, y) == goal: # When we reach the goal, turn color to green
             for pos in path_positions:
                x, y = pos
                canvas.create_rectangle(y * CELL_SIZE, x * CELL_SIZE, (y + 1) * CELL_SIZE, (x + 1) * CELL_SIZE, fill="green")
                Length = len(path_positions)
                window.update()
             return True
        if (x, y) not in close: # Change color of cells passed by
            close.append((x, y))
            path_positions.append((x, y))
            canvas.create_rectangle(y * CELL_SIZE, x * CELL_SIZE, (y + 1) * CELL_SIZE, (x + 1) * CELL_SIZE, fill="red")
            window.update()
            time.sleep(SLEEP_TIME)

            # Check which cells can be passed through or if it's a dead end
            for Offset_x, Offset_y in DIRECTIONS: 
                new_x = x + Offset_x
                new_y = y + Offset_y
                IsaWall = maze[new_x][new_y] == -1
                open =  (new_x, new_y) not in close
                if not IsaWall and open:
                    stack.append((new_x, new_y))

    return False
###################################################################################################################################################
def BreadthFirstSearch(maze, start, goal):
    global Length  # Global variable for path length
    queue = [start]  # Initialize the queue with the starting position
    close = [] # Set to track visited positions
    
    if (path_positions) != []:  # Clear the maze from used cells
        for pos in path_positions:
                canvas.create_rectangle(pos[1] * CELL_SIZE, pos[0] * CELL_SIZE, (pos[1] + 1) * CELL_SIZE, (pos[0] + 1) * CELL_SIZE, fill="white")
                window.update()
    path_positions.clear()  # Empty the array
   
    while queue:  # Main loop
        x, y = queue.pop(0)  # Dequeue the first element from the queue
        if (x, y) == goal:  # Check if we reached the goal
            for pos in path_positions:
                canvas.create_rectangle(pos[1] * CELL_SIZE, pos[0] * CELL_SIZE, (pos[1] + 1) * CELL_SIZE, (pos[0] + 1) * CELL_SIZE, fill="green")
                Length = len(path_positions)
                window.update()
            return True
        
        if (x, y) not in close:  # Check if the position is not visited
            close.append((x, y))  # Mark the position as visited
            path_positions.append((x, y))  # Add the position to the path
            canvas.create_rectangle(y * CELL_SIZE, x * CELL_SIZE, (y + 1) * CELL_SIZE, (x + 1) * CELL_SIZE, fill="red")  # Change color of cells passed by
            window.update()
            time.sleep(SLEEP_TIME)  # Control animation speed
            
        for Offset_x, Offset_y in DIRECTIONS:  # Explore neighboring positions
                
                new_x = Offset_x + x
                new_y = Offset_y + y
                IsaWall = maze[new_x][new_y] == -1
                open =  (new_x, new_y) not in close
                if not IsaWall and open:
                    queue.append((new_x, new_y)) # Enqueue neighboring position
    
    return False

###################################################################################################################################################
def start_DepthFirstSearch():
    global Length  # Global variable for path length
    DepthFirstSearch(maze, start, goal)  # Call Depth First Search function
    Len.config(text="number of cells traversed = {:}".format(Length))  # Update label with number of cells traversed

###################################################################################################################################################

def start_BreadthFirstSearch():
    global Length  # Global variable for path length
    BreadthFirstSearch(maze, start, goal)  # Call Breadth First Search function
    Len.config(text="number of cells traversed = {:}".format(Length))  # Update label with number of cells traversed

###################################################################################################################################################
# Define the maze structure using a 2D list
maze = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, -1],
        [-1, 0, -1, 0, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, -1, -1, 0, -1],
        [-1, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1, 0, -1],
        [-1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, -1],
        [-1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1],
        [-1, 0, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0, -1],
        [-1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1],
        [-1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0, -1, -1, -1, -1, -1, -1, -1],
        [-1, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1],
        [-1, -1, -1, -1, -1, 0, -1, 0, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1],
        [-1, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1],
        [-1, 0, -1, 0, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, -1, 0, -1],
        [-1, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1],
        [-1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1],
        [-1, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0, -1, 0, -1],
        [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

# Define the start and goal positions in the maze
start = (17, 1)
goal = (1, 17)

#                                         UI

# Create the main window using tkinter
window = tkinter.Tk()

# Create a canvas for drawing the maze
canvas = tkinter.Canvas(window, width=len(maze[0]) * CELL_SIZE, height=len(maze) * CELL_SIZE)
canvas.pack()

# Set the title of the window
window.title("Solving Maze Problem")

# Call the maze_UI function to render the maze on the canvas
maze_UI(maze)

# Create a label to display the number of cells traversed
Len = tkinter.Label(window, text="number of cells traversed = 0", font=('Arial', 18))
Len.pack()

# Create a button to start the Depth First Search algorithm
DepthFirstSearch_button = tkinter.Button(window, text="Start DFS", font=('Arial', 18), command=start_DepthFirstSearch)
DepthFirstSearch_button.pack(side=tkinter.LEFT)  # Position the button on the left side of the window

# Create a button to start the Breadth First Search algorithm
BreadthFirstSearch_button = tkinter.Button(window, text="Start BFS", font=('Arial', 18), command=start_BreadthFirstSearch)
BreadthFirstSearch_button.pack(side=tkinter.RIGHT)  # Position the button on the right side of the window

# Start the tkinter event loop to display the window and handle user interactions
window.mainloop()




