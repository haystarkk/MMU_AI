import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    closed_set = set()
    
    start_node = (0, start, None)  # (cost, position, parent)
    heapq.heappush(open_set, start_node)
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_set:
        current_f, current, _ = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            total_cost = sum(grid[r][c] for (r,c) in path)
            return path, total_cost
        
        closed_set.add(current)
        
        for delta in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current[0] + delta[0], current[1] + delta[1])
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if neighbor in closed_set:
                    continue
                
                if grid[neighbor[0]][neighbor[1]] == float('inf'):
                    continue
                
                tentative_g = g_score[current] + grid[neighbor[0]][neighbor[1]]
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor, current))
    
    return None, None

if __name__ == "__main__":
    grid = [
        [1, 1, 1, 5],
        [1, float('inf'), 1, 5],
        [1, 1, 1, 5],
        [1, 1, 1, 1]
    ]
    start = (0, 0)
    goal = (3, 3)
    path, cost = a_star(grid, start, goal)
    print("Path:", path)
    print("Total cost:", cost)