"""Depth First Search (DFS) Implementation
Finds a path from initial node to goal state using recursion"""

import time
from collections import defaultdict

class DFS:
    def __init__(self):
        # Defining a graph (same structure as BFS for comparison)
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
        
        self.visited_nodes = set()
        self.search_path = []
        
    def dfs_recursive(self, current_node, goal_node, path, visited_count):
        """Recursive DFS implementation
        Returns: (path_found, path, nodes_visited)"""
        # Marking current node as visited
        if current_node not in self.visited_nodes:
            self.visited_nodes.add(current_node)
            visited_count[0] += 1
            
            # Adding to current path
            current_path = path + [current_node]
            
            print(f"Visiting node: {current_node}, Path so far: {' -> '.join(current_path)}")
            
            # Checking if we reached the goal
            if current_node == goal_node:
                return True, current_path, visited_count[0]
            
            # Exploring neighbours
            for neighbour in self.graph.get(current_node, []):
                if neighbour not in self.visited_nodes:
                    found, result_path, _ = self.dfs_recursive(
                        neighbour, goal_node, current_path, visited_count
                    )
                    if found:
                        return True, result_path, visited_count[0]
            
            return False, None, visited_count[0]
    
    def dfs_iterative(self, start_node, goal_node):
        """Iterative DFS implementation using a stack
        Returns: path and number of nodes visited"""
        visited = set()
        stack = [(start_node, [start_node])]
        nodes_visited = 0
        
        print(f"\nStarting Iterative DFS from '{start_node}' to '{goal_node}'")
        print("-" * 50)
        
        while stack:
            current_node, path = stack.pop()
            nodes_visited += 1
            
            print(f"Visiting node: {current_node}, Path so far: {' -> '.join(path)}")
            
            if current_node == goal_node:
                print(f"\n✓ Goal '{goal_node}' found!")
                return path, nodes_visited
            
            if current_node not in visited:
                visited.add(current_node)
                
                # Adding neighbours to stack (reverse order for same order as recursive)
                for neighbour in reversed(self.graph.get(current_node, [])):
                    if neighbour not in visited:
                        new_path = path + [neighbour]
                        stack.append((neighbour, new_path))
        
        print(f"\n✗ Goal '{goal_node}' not reachable from '{start_node}'")
        return None, nodes_visited
    
    def dfs_find_all_paths(self, start_node, goal_node):
        """Finding all paths from start to goal using DFS"""
        all_paths = []
        
        def dfs_paths(current, goal, path):
            if current == goal:
                all_paths.append(path)
                return
            
            for neighbour in self.graph.get(current, []):
                if neighbour not in path:
                    dfs_paths(neighbour, goal, path + [neighbour])
        
        dfs_paths(start_node, goal_node, [start_node])
        return all_paths
    
    def reset(self):
        """Reseting visited nodes for new search"""
        self.visited_nodes = set()
        self.search_path = []

class DFSDemo:
    @staticmethod
    def run_demo():
        """Running DFS demonstrations"""
        print("=" * 60)
        print("DEPTH FIRST SEARCH (DFS) IMPLEMENTATION")
        print("=" * 60)
        
        # Demo 1: Recursive DFS
        print("\n" + "=" * 60)
        print("DEMO 1: Recursive DFS from 'A' to 'K'")
        print("=" * 60)
        
        dfs = DFS()
        visited_count = [0]
        
        start_time = time.time()
        found, path, nodes_visited = dfs.dfs_recursive('A', 'K', [], visited_count)
        end_time = time.time()
        
        if found:
            print(f"\n✓ PATH FOUND (DFS Recursive):")
            print(f"   Path: {' -> '.join(path)}")
            print(f"   Path length: {len(path) - 1} edges")
            print(f"   Nodes visited: {nodes_visited}")
            print(f"   Time taken: {(end_time - start_time)*1000:.4f} ms")
        else:
            print("No path found!")
        
        # Demo 2: Iterative DFS
        print("\n" + "=" * 60)
        print("DEMO 2: Iterative DFS from 'A' to 'K'")
        print("=" * 60)
        
        dfs.reset()
        start_time = time.time()
        path2, nodes2 = dfs.dfs_iterative('A', 'K')
        end_time = time.time()
        
        if path2:
            print(f"\n✓ PATH FOUND (DFS Iterative):")
            print(f"   Path: {' -> '.join(path2)}")
            print(f"   Time taken: {(end_time - start_time)*1000:.4f} ms")
        
        # Demo 3: Finding all paths
        print("\n" + "=" * 60)
        print("DEMO 3: Finding all paths from 'A' to 'K' using DFS")
        print("=" * 60)
        
        all_paths = dfs.dfs_find_all_paths('A', 'K')
        print(f"\nFound {len(all_paths)} path(s):")
        for i, path in enumerate(all_paths, 1):
            print(f"Path {i}: {' -> '.join(path)}")
        
        # Demo 4: Different start and goal
        print("\n" + "=" * 60)
        print("DEMO 4: DFS from 'B' to 'L'")
        print("=" * 60)
        
        dfs.reset()
        visited_count = [0]
        found2, path3, nodes3 = dfs.dfs_recursive('B', 'L', [], visited_count)
        
        if found2:
            print(f"\n✓ PATH FOUND:")
            print(f"   Path: {' -> '.join(path3)}")
            print(f"   Nodes visited: {nodes3}")
        
        # Demo 5: Maze solving problem
        print("\n" + "=" * 60)
        print("DEMO 5: Maze Solving Problem")
        print("=" * 60)
        
        maze_graph = DFS()
        maze_graph.graph = {
            'S': ['A', 'B'],
            'A': ['S', 'C'],
            'B': ['S', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B', 'G'],
            'E': ['B', 'H'],
            'F': ['C', 'I'],
            'G': ['D', 'J'],
            'H': ['E', 'K'],
            'I': ['F', 'G'],
            'J': ['G', 'L'],
            'K': ['H', 'L'],
            'L': ['J', 'K']
        }
        
        dfs.reset()
        visited_count = [0]
        found3, path4, nodes4 = maze_graph.dfs_recursive('S', 'L', [], visited_count)
        
        if found3:
            print(f"\n✓ Maze solved!")
            print(f"   Path from start (S) to goal (L):")
            print(f"   {' -> '.join(path4)}")
        
        # Comparison with BFS
        print("\n" + "=" * 60)
        print("COMPARISON: BFS vs DFS")
        print("=" * 60)
        print("BFS finds the SHORTEST path but may use more memory")
        print("DFS finds A path (not necessarily shortest) but uses less memory")
        print("BFS explores level by level, DFS goes deep first")

if __name__ == "__main__":
    DFSDemo.run_demo()