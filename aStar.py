import math
from queue import PriorityQueue

def manhattan_distance(p1, p2):
    """Calculates Manhattan distance between two points."""
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean_distance(p1, p2):
    """Calculates Euclidean distance between two points."""
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)    

def a_star_tree_search(grid, start, end, heuristic="euclidean"):
    """A* tree search with dynamic heuristic selection and flexible grid handling."""
    rows, cols = len(grid), len(grid[0])
    open_set = PriorityQueue()  
    open_set.put((0, start))  
    came_from = {}  
    g_score = {start: 0}  

    # Select heuristic function
    heuristic_func = manhattan_distance if heuristic == "manhattan" else euclidean_distance

    # Define movement directions (Up, Down, Left, Right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    while not open_set.empty():
        _, current = open_set.get()

        # If goal reached, reconstruct path
        if current == end:  
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)  
            return path[::-1]  

        x, y = current
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)

            # Check if neighbor is within grid and not an obstacle
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                temp_g_score = g_score[current] + 1  # Movement cost is always 1
                f_score = temp_g_score + heuristic_func(neighbor, end)

                if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                    open_set.put((f_score, neighbor))
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score 

    return None  # No path found

# Function to create a flexible grid
def create_grid(rows, cols, obstacles):
    """Creates a grid of given size with obstacles."""
    grid = [[0] * cols for _ in range(rows)]  # Initialize empty grid
    for x, y in obstacles:
        grid[x][y] = 1  # Place obstacles
    return grid

# Define grid size and obstacles
rows, cols = 6, 6
obstacles = [(1, 2), (2, 2), (3, 2), (4, 2)]  # Walls in column 2

# Generate the grid dynamically
grid = create_grid(rows, cols, obstacles)

start = (0, 0)
end = (5, 5)

# Run with different heuristics
path1 = a_star_tree_search(grid, start, end, heuristic="manhattan")
path2 = a_star_tree_search(grid, start, end, heuristic="euclidean")

print("Path using Manhattan Distance:", path1)
print("Path using Euclidean Distance:", path2)

