"""Map of Australia Coloring Constraint Program
No two adjacent regions can have the same color"""

class AustraliaColoring:
    def __init__(self):
        # Defining the regions (states)
        self.regions = ['WA', 'NT', 'SA', 'QLD', 'NSW', 'VIC', 'TAS']
        
        # Defining the colors available
        self.colors = ['Blue', 'Red', 'Green']
        
        # Defining neighbours for each region
        self.adjacency = {
            'WA': ['NT', 'SA'],
            'NT': ['WA', 'SA', 'QLD'],
            'SA': ['WA', 'NT', 'QLD', 'NSW', 'VIC'],
            'QLD': ['NT', 'SA', 'NSW'],
            'NSW': ['QLD', 'SA', 'VIC'],
            'VIC': ['SA', 'NSW'],
            'TAS': []  # Tasmania has no mainland neighbors
        }
        
        self.solution = {}
        
    def is_safe(self, region, color):
        """Checking if assigning a color to a region is safe"""
        for neighbor in self.adjacency[region]:
            if neighbor in self.solution and self.solution[neighbor] == color:
                return False
        return True
    
    def solve_backtracking(self, region_index=0):
        """Solving the coloring problem using backtracking"""
        if region_index == len(self.regions):
            return True
        
        current_region = self.regions[region_index]
        
        # Trying each color for the current region
        for color in self.colors:
            if self.is_safe(current_region, color):
                self.solution[current_region] = color
                
                # Recursively assigning colors to remaining regions
                if self.solve_backtracking(region_index + 1):
                    return True
                
                # Backtrackinng
                del self.solution[current_region]
        
        return False
    
    def display_solution(self):
        """Displaying the coloring solution"""
        print("\n" + "=" * 50)
        print("AUSTRALIA MAP COLORING SOLUTION")
        print("=" * 50)
        print(f"Colors used: {', '.join(self.colors)}")
        print("\nRegion Color Assignments:")
        print("-" * 30)
        
        for region in self.regions:
            color = self.solution.get(region, "Not assigned")
            print(f"{region:5} -> {color}")
        
        # Verifying constraints
        print("\n" + "=" * 50)
        print("VERIFYING CONSTRAINTS")
        print("=" * 50)
        violations = 0
        for region in self.regions:
            for neighbour in self.adjacency[region]:
                if neighbour in self.solution and self.solution[region] == self.solution[neighbour]:
                    print(f"VIOLATION: {region} and {neighbour} have same color: {self.solution[region]}")
                    violations += 1
        
        if violations == 0:
            print("✓ All constraints satisfied! No adjacent regions share the same color.")
        else:
            print(f"✗ Found {violations} constraint violations!")
    
    def visualize_map(self):
        """Simple text visualization of the map"""
        print("\n" + "=" * 50)
        print("MAP VISUALIZATION (Text-based)")
        print("=" * 50)
        
        # Creating a simple ASCII representation
        color_codes = {'Blue': '\033[94m', 'Red': '\033[91m', 'Green': '\033[92m'}
        reset_code = '\033[0m'
        
        # Western Australia connections
        print(f"WA ({color_codes.get(self.solution.get('WA', 'White'), '')}{self.solution.get('WA', '?')}{reset_code}) --- NT ({color_codes.get(self.solution.get('NT', 'White'), '')}{self.solution.get('NT', '?')}{reset_code})")
        print(" |                      |")
        print(" |                      |")
        print(f"SA ({color_codes.get(self.solution.get('SA', 'White'), '')}{self.solution.get('SA', '?')}{reset_code}) --- QLD ({color_codes.get(self.solution.get('QLD', 'White'), '')}{self.solution.get('QLD', '?')}{reset_code})")
        print(" |                      |")
        print(" |                      |")
        print(f"NSW ({color_codes.get(self.solution.get('NSW', 'White'), '')}{self.solution.get('NSW', '?')}{reset_code}) --- VIC ({color_codes.get(self.solution.get('VIC', 'White'), '')}{self.solution.get('VIC', '?')}{reset_code})")
        print("\nTasmania is separated but colored as well:")
        print(f"TAS ({color_codes.get(self.solution.get('TAS', 'White'), '')}{self.solution.get('TAS', '?')}{reset_code})")

class MapColoringDemo:
    @staticmethod
    def run_demo():
        """Run the map coloring demonstration"""
        print("\n" + "=" * 60)
        print("TASK 2(A): AUSTRALIA MAP COLORING PROBLEM")
        print("=" * 60)
        print("\nProblem Statement:")
        print("- Color the regions of Australia using 3 colors: Blue, Red, Green")
        print("- No two adjacent regions can have the same color")
        
        # Creating and solving the problem
        solver = AustraliaColoring()
        
        print("\nSolving...")
        if solver.solve_backtracking():
            solver.display_solution()
            solver.visualize_map()
        else:
            print("No solution found!")

# Running the demonstration
if __name__ == "__main__":
    MapColoringDemo.run_demo()