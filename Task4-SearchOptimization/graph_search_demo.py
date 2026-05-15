"""Combined BFS and DFS Demo with visualization and comparison"""

from bfs_search import BFS
from dfs_search import DFS
import time

class SearchComparison:
    def __init__(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'H'],
            'E': ['B', 'I'],
            'F': ['C', 'J'],
            'G': ['C', 'K'],
            'H': ['D'],
            'I': ['E'],
            'J': ['F'],
            'K': ['G', 'L'],
            'L': ['K']
        }
    
    def compare_searches(self, start, goal):
        """Comparing BFS and DFS performance"""
        print("=" * 60)
        print(f"SEARCH COMPARISON: {start} → {goal}")
        print("=" * 60)
        
        # BFS
        bfs_solver = BFS()
        bfs_solver.graph = self.graph
        
        start_time = time.time()
        bfs_path, bfs_nodes = bfs_solver.bfs_shortest_path(start, goal)
        bfs_time = time.time() - start_time
        
        # DFS
        dfs_solver = DFS()
        dfs_solver.graph = self.graph
        
        start_time = time.time()
        dfs_path, dfs_nodes = dfs_solver.dfs_iterative(start, goal)
        dfs_time = time.time() - start_time
        
        # Displaying results
        print("\n" + "-" * 40)
        print("RESULTS COMPARISON")
        print("-" * 40)
        
        if bfs_path:
            print(f"BFS - Path: {' → '.join(bfs_path)}")
            print(f"      Length: {len(bfs_path)-1} edges")
            print(f"      Nodes explored: {bfs_nodes}")
            print(f"      Time: {bfs_time*1000:.4f} ms")
        else:
            print("BFS: No path found")
        
        print()
        
        if dfs_path:
            print(f"DFS - Path: {' → '.join(dfs_path)}")
            print(f"      Length: {len(dfs_path)-1} edges")
            print(f"      Nodes explored: {dfs_nodes}")
            print(f"      Time: {dfs_time*1000:.4f} ms")
        else:
            print("DFS: No path found")
        
        # Analysis
        print("\n" + "-" * 40)
        print("ANALYSIS")
        print("-" * 40)
        
        if bfs_path and dfs_path:
            if len(bfs_path) <= len(dfs_path):
                print("✓ BFS found the SHORTEST path")
            else:
                print("✗ DFS found a longer path than necessary")
            
            if bfs_nodes <= dfs_nodes:
                print("✓ BFS explored fewer nodes")
            else:
                print("✗ DFS explored more nodes (may be less efficient)")
        
        print("\nRecommendation:")
        print("- Use BFS when shortest path is critical")
        print("- Use DFS when memory is limited or deep paths are desired")

def interactive_search():
    """Interactive search interface"""
    print("\n" + "=" * 50)
    print("INTERACTIVE GRAPH SEARCH")
    print("=" * 50)
    
    graph = {
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
    
    print("\nAvailable nodes:", list(graph.keys()))
    
    start = input("\nEnter start node: ").upper().strip()
    goal = input("Enter goal node: ").upper().strip()
    
    if start not in graph or goal not in graph:
        print("Invalid node(s)!")
        return
    
    print("\nChoose search algorithm:")
    print("1. Breadth First Search (BFS)")
    print("2. Depth First Search (DFS)")
    print("3. Compare Both")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == '1':
        solver = BFS()
        solver.graph = graph
        path, nodes = solver.bfs_shortest_path(start, goal)
        if path:
            print(f"\nBFS Path: {' → '.join(path)}")
    
    elif choice == '2':
        solver = DFS()
        solver.graph = graph
        path, nodes = solver.dfs_iterative(start, goal)
        if path:
            print(f"\nDFS Path: {' → '.join(path)}")
    
    elif choice == '3':
        comparator = SearchComparison()
        comparator.graph = graph
        comparator.compare_searches(start, goal)
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    print("GRAPH SEARCH ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    print("\n1. Run pre-defined demonstrations")
    print("2. Run interactive search")
    
    mode = input("\nChoose mode (1/2): ")
    
    if mode == '1':
        print("\n" + "=" * 60)
        print("RUNNING PRE-DEFINED DEMONSTRATIONS")
        print("=" * 60)
        
        # Running BFS demo
        from bfs_search import BFSDemo
        BFSDemo.run_demo()
        
        print("\n\n")
        
        # Running DFS demo
        from dfs_search import DFSDemo
        DFSDemo.run_demo()
        
        # Running comparison
        print("\n\n")
        comparator = SearchComparison()
        comparator.compare_searches('A', 'K')
    
    elif mode == '2':
        interactive_search()
    
    else:
        print("Invalid choice!")