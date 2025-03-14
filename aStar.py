import math
from queue import PriorityQueue

def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def euclidean_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)    

def a_star_tree_search(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    open_set = PriorityQueue()
    open_set.put((0, start)) 
    came_from = {}  
    g_score = {start: 0}

    while not open_set.empty():
        _, current = open_set.get()

        if current == end:  
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]  


        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
            neighbor = (x + dx, y + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0 :
                temp_g_score = g_score[current] + 1  
                f_score = temp_g_score + euclidean_distance(neighbor, end) 
                
                if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                  # Only add to open_set or update if it's a better path
                  open_set.put((f_score, neighbor))
                  came_from[neighbor] = current
                  g_score[neighbor] = temp_g_score 


    return None  

# Rest of your code (grid, start, end, calling the function) remains the same

grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (0, 4)

path = a_star_tree_search(grid, start, end)
print("Shortest Path:", path)
