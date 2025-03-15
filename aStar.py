import math
from queue import PriorityQueue

def manhattanDist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def euclideanDist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)    

def aStarTreeSearch(grid, start, end, heuristic="euclidean"):
    rows, cols = len(grid), len(grid[0])
    

    # هون بنختار نوع ال huristic function
    heuristicFunc = manhattanDist if heuristic == "manhattan" else euclideanDist

   


    openSet = PriorityQueue() 
    openSet.put((0, start))  
    cameFrom = {}  

    while not openSet.empty():
        _, current = openSet.get()


        if current == end:  
            path = []
            while current in cameFrom:
                path.append(current)
                current = cameFrom[current]
            path.append(start)  
            return path[::-1]  


        x, y = current
        gScore = {start: 0}  
        
           # الاتجاهات المسموحة
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)


            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                temp_g_score = gScore[current] + 1  # اي حركة تكلفتها 1 دايما
                fScore = temp_g_score + heuristicFunc(neighbor, end)

                if neighbor not in gScore or temp_g_score < gScore[neighbor]:
                    openSet.put((fScore, neighbor))
                    cameFrom[neighbor] = current
                    gScore[neighbor] = temp_g_score 

    return None  # ما في اي طريق


def mewGrid(rows, cols, obstacles):
    """Creates a grid of given size with obstacles."""
    grid = [[0] * cols for _ in range(rows)]  
    for x, y in obstacles:
        grid[x][y] = 1  # مكان المعيقات بنحط1, اذا طريق فاضية بنحط0
    return grid



rows, cols = 6, 6
obstacles = [(1, 2), (2, 2), (3, 2), (4, 2)]  


grid = mewGrid(rows, cols, obstacles)

start = (0, 0)
end = (5, 5)

#بنجرب النوعين:
path1 = aStarTreeSearch(grid, start, end, heuristic="manhattan")
path2 = aStarTreeSearch(grid, start, end, heuristic="euclidean")

print("Path using Manhattan Distance:", path1)
print("Path using Euclidean Distance:", path2)

