"""Breadth First Search (BFS) Implementation
Finds the shortest path from initial node to goal state"""

from collections import deque
import time

class BFS:
    def __init__(self):
        # Defining a graph (can be modified for different problems)
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B', 'G'],
            'E': ['B', 'H', 'I'],
            'F': ['C', 'J'],
            'G': ['D'],
            'H': ['E'],
            'I': ['E', 'K'],
            'J': ['F'],
            'K': ['I', 'L'],
            'L': ['K']
        }
        
    def bfs_shortest_path(self, start_node, goal_node):
        """Finding shortest path using BFS algorithm
        Returns: path from start to goal, and number of nodes visited"""
        # Keeping track of visited nodes
        visited = set()
        
        # Queue stores tuples of (current_node, path_to_current_node)
        queue = deque([(start_node, [start_node])])
        
        # Tracking visited nodes count
        nodes_visited = 0
        
        print(f"\nStarting BFS from '{start_node}' to '{goal_node}'")
        print("-" * 50)
        
        while queue:
            current_node, path = queue.popleft()
            nodes_visited += 1
            
            print(f"Visiting node: {current_node}, Path so far: {' -> '.join(path)}")
            
            # Checking if we reached the goal
            if current_node == goal_node:
                print(f"\n✓ Goal '{goal_node}' found!")
                return path, nodes_visited
            
            # Marking as visited
            if current_node not in visited:
                visited.add(current_node)
                
                # Exploring neighbours
                for neighbour in self.graph.get(current_node, []):
                    if neighbour not in visited:
                        new_path = path + [neighbour]
                        queue.append((neighbour, new_path))
        
        print(f"\n✗ Goal '{goal_node}' not reachable from '{start_node}'")
        return None, nodes_visited
    
    def bfs_all_paths(self, start_node, goal_node):
        """Finding all possible paths using BFS"""
        queue = deque([(start_node, [start_node])])
        all_paths = []
        
        while queue:
            current_node, path = queue.popleft()
            
            if current_node == goal_node:
                all_paths.append(path)
                continue
            
            for neighbour in self.graph.get(current_node, []):
                if neighbour not in path:  # Avoid cycles
                    new_path = path + [neighbour]
                    queue.append((neighbour, new_path))
        
        return all_paths
    
    def bfs_level_order(self, start_node):
        """Performing level-order traversal (shows BFS layers)"""
        visited = set()
        queue = deque([(start_node, 0)])  # (node, level)
        levels = {}
        
        while queue:
            node, level = queue.popleft()
            
            if node not in visited:
                visited.add(node)
                
                if level not in levels:
                    levels[level] = []
                levels[level].append(node)
                
                for neighbour in self.graph.get(node, []):
                    if neighbour not in visited:
                        queue.append((neighbour, level + 1))
        
        return levels
    
    def print_bfs_levels(self, levels):
        """Printing the BFS level order traversal"""
        print("\n" + "=" * 50)
        print("BFS Level Order Traversal")
        print("=" * 50)
        for level, nodes in levels.items():
            print(f"Level {level}: {', '.join(nodes)}")

class BFSDemo:
    @staticmethod
    def run_demo():
        """Running BFS demonstrations"""
        print("=" * 60)
        print("BREADTH FIRST SEARCH (BFS) IMPLEMENTATION")
        print("=" * 60)
        
        bfs = BFS()
        
        # Demo 1: Finding shortest path from A to K
        print("\n" + "=" * 60)
        print("DEMO 1: Finding shortest path from 'A' to 'K'")
        print("=" * 60)
        
        start_time = time.time()
        shortest_path, nodes_visited = bfs.bfs_shortest_path('A', 'K')
        end_time = time.time()
        
        if shortest_path:
            print(f"\n✓ SHORTEST PATH FOUND:")
            print(f"   Path: {' -> '.join(shortest_path)}")
            print(f"   Path length: {len(shortest_path) - 1} edges")
            print(f"   Nodes visited: {nodes_visited}")
            print(f"   Time taken: {(end_time - start_time)*1000:.4f} ms")
        else:
            print("No path found!")
        
        # Demo 2: Finding all paths
        print("\n" + "=" * 60)
        print("DEMO 2: Finding all paths from 'A' to 'K'")
        print("=" * 60)
        
        all_paths = bfs.bfs_all_paths('A', 'K')
        print(f"\nFound {len(all_paths)} path(s):")
        for i, path in enumerate(all_paths, 1):
            print(f"Path {i}: {' -> '.join(path)}")
        
        # Demo 3: Leveling order traversal
        print("\n" + "=" * 60)
        print("DEMO 3: BFS Level Order Traversal from 'A'")
        print("=" * 60)
        
        levels = bfs.bfs_level_order('A')
        bfs.print_bfs_levels(levels)
        
        # Demo 4: Different start and goal
        print("\n" + "=" * 60)
        print("DEMO 4: Finding path from 'B' to 'L'")
        print("=" * 60)
        
        path2, nodes2 = bfs.bfs_shortest_path('B', 'L')
        if path2:
            print(f"\n✓ PATH FOUND:")
            print(f"   Path: {' -> '.join(path2)}")
            print(f"   Nodes visited: {nodes2}")
        
        # Demo 5: Custom graph - City navigation
        print("\n" + "=" * 60)
        print("DEMO 5: City Navigation Problem")
        print("=" * 60)
        
        city_graph = BFS()
        city_graph.graph = {
            'Nairobi': ['Mombasa Road', 'Thika Road'],
            'Mombasa Road': ['Nairobi', 'Athi River', 'Airport'],
            'Thika Road': ['Nairobi', 'Kiambu', 'Ruiru'],
            'Athi River': ['Mombasa Road', 'Kitengela'],
            'Airport': ['Mombasa Road', 'Embakasi'],
            'Kiambu': ['Thika Road'],
            'Ruiru': ['Thika Road', 'Juja'],
            'Kitengela': ['Athi River'],
            'Embakasi': ['Airport', 'Donholm'],
            'Juja': ['Ruiru'],
            'Donholm': ['Embakasi', 'Buruburu'],
            'Buruburu': ['Donholm']
        }
        
        path3, nodes3 = city_graph.bfs_shortest_path('Nairobi', 'Buruburu')
        if path3:
            print(f"\n✓ Route found:")
            print(f"   {' -> '.join(path3)}")

if __name__ == "__main__":
    BFSDemo.run_demo()