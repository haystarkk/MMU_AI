"""Nairobi Sub-counties Coloring Constraint Program
No two adjacent sub-counties can have the same color"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

class NairobiColoring:
    def __init__(self):
        # Defining Nairobi's 17 sub-counties
        self.sub_counties = [
            'Westlands', 'Dagoretti North', 'Dagoretti South', 'Langata', 'Kibra',
            'Roysambu', 'Kasarani', 'Ruaraka', 'Embakasi North', 'Embakasi South',
            'Embakasi Central', 'Embakasi East', 'Embakasi West', 'Makadara',
            'Kamukunji', 'Starehe', 'Mathare'
        ]
        
        # Defining adjacency based on geographical boundaries
        self.adjacency = {
            'Westlands': ['Dagoretti North', 'Dagoretti South', 'Starehe', 'Mathare', 'Kasarani'],
            'Dagoretti North': ['Westlands', 'Dagoretti South', 'Langata', 'Kibra'],
            'Dagoretti South': ['Westlands', 'Dagoretti North', 'Langata'],
            'Langata': ['Dagoretti North', 'Dagoretti South', 'Kibra', 'Embakasi West'],
            'Kibra': ['Langata', 'Dagoretti North', 'Makadara', 'Embakasi West'],
            'Roysambu': ['Kasarani', 'Ruaraka', 'Embakasi North', 'Embakasi Central'],
            'Kasarani': ['Westlands', 'Roysambu', 'Ruaraka', 'Mathare', 'Embakasi North'],
            'Ruaraka': ['Kasarani', 'Roysambu', 'Embakasi North', 'Mathare'],
            'Embakasi North': ['Roysambu', 'Kasarani', 'Ruaraka', 'Embakasi Central', 'Embakasi East'],
            'Embakasi South': ['Embakasi Central', 'Embakasi East', 'Embakasi West', 'Makadara'],
            'Embakasi Central': ['Roysambu', 'Embakasi North', 'Embakasi South', 'Embakasi East'],
            'Embakasi East': ['Embakasi North', 'Embakasi Central', 'Embakasi South', 'Kamukunji'],
            'Embakasi West': ['Langata', 'Kibra', 'Makadara', 'Embakasi South'],
            'Makadara': ['Kibra', 'Embakasi West', 'Embakasi South', 'Kamukunji', 'Starehe', 'Mathare'],
            'Kamukunji': ['Embakasi East', 'Makadara', 'Starehe', 'Mathare'],
            'Starehe': ['Westlands', 'Kamukunji', 'Makadara', 'Mathare'],
            'Mathare': ['Westlands', 'Kasarani', 'Ruaraka', 'Makadara', 'Kamukunji', 'Starehe']
        }
        
        self.solution = {}
        
    def is_safe(self, sub_county, color, assignment):
        """Checking if assigning a color to a sub-county is safe"""
        for neighbour in self.adjacency[sub_county]:
            if neighbour in assignment and assignment[neighbour] == color:
                return False
        return True
    
    def solve_chromatic_number(self):
        """Finding the minimum number of colors needed"""
        print("\n" + "=" * 60)
        print("FINDING MINIMUM COLORS FOR NAIROBI")
        print("=" * 60)
        
        # Trying from 2 colors upwards
        for num_colors in range(2, 11):
            colors = [f'Color_{i+1}' for i in range(num_colors)]
            print(f"\nAttempting with {num_colors} colors...")
            
            solution = {}
            if self.solve_backtracking(0, colors, solution):
                self.solution = solution
                print(f"✓ SUCCESS! Map can be colored with {num_colors} colors")
                return num_colors
            else:
                print(f"✗ Failed with {num_colors} colors")
        
        print("Max colors reached - check adjacency definition")
        return None
    
    def solve_backtracking(self, sub_county_index, colors, assignment):
        """Solving the coloring problem using backtracking with given colors"""
        if sub_county_index == len(self.sub_counties):
            return True
        
        current_sub_county = self.sub_counties[sub_county_index]
        
        for color in colors:
            if self.is_safe(current_sub_county, color, assignment):
                assignment[current_sub_county] = color
                
                if self.solve_backtracking(sub_county_index + 1, colors, assignment):
                    return True
                
                del assignment[current_sub_county]
        
        return False
    
    def display_solution(self, colors_used):
        """Displaying the coloring solution"""
        print("\n" + "=" * 60)
        print("NAIROBI SUB-COUNTIES COLORING SOLUTION")
        print("=" * 60)
        print(f"Total sub-counties: {len(self.sub_counties)}")
        print(f"Colors used: {colors_used}")
        
        unique_colors = set(self.solution.values())
        print(f"Minimum number of colors needed: {len(unique_colors)}")
        
        print("\nSub-county Color Assignments:")
        print("-" * 40)
        
        color_groups = {}
        for sub_county, color in self.solution.items():
            if color not in color_groups:
                color_groups[color] = []
            color_groups[color].append(sub_county)
        
        for color, sub_counties_list in color_groups.items():
            print(f"\n{color}:")
            for sc in sorted(sub_counties_list):
                print(f"  - {sc}")
        
        # Verifying constraints
        print("\n" + "=" * 60)
        print("VERIFYING CONSTRAINTS")
        print("=" * 60)
        violations = 0
        
        for sub_county in self.sub_counties:
            for neighbor in self.adjacency[sub_county]:
                if neighbor in self.solution and self.solution[sub_county] == self.solution[neighbor]:
                    print(f"VIOLATION: {sub_county} and {neighbor} share same color")
                    violations += 1
        
        if violations == 0:
            print("✓ ALL CONSTRAINTS SATISFIED!")
            print("  No adjacent sub-counties share the same color")
        else:
            print(f"✗ Found {violations} constraint violations!")
    
    def get_statistics(self):
        """Generating statistics about the coloring"""
        print("\n" + "=" * 60)
        print("COLORING STATISTICS")
        print("=" * 60)
        
        color_counts = {}
        for color in self.solution.values():
            color_counts[color] = color_counts.get(color, 0) + 1
        
        print("\nColor Distribution:")
        for color, count in sorted(color_counts.items()):
            percentage = (count / len(self.sub_counties)) * 100
            print(f"  {color}: {count} sub-counties ({percentage:.1f}%)")
        
        max_neighbors = 0
        max_sub_county = ""
        for sc, neighbors in self.adjacency.items():
            if len(neighbors) > max_neighbors:
                max_neighbors = len(neighbors)
                max_sub_county = sc
        
        print(f"\nMost connected sub-county: {max_sub_county} (connected to {max_neighbors} others)")
        print(f"\nTheoretical lower bound: ≥ {max_neighbors + 1}")
        print(f"Actually used: {len(set(self.solution.values()))} colors")
    
    def visualize_map(self):
        """Creating a graphical visualization of Nairobi sub-counties"""
        print("\n" + "=" * 60)
        print("GENERATING GRAPHICAL MAP VISUALIZATION...")
        print("=" * 60)
        
        fig, ax = plt.subplots(figsize=(14, 10))
        
        # Approximating positions (x, y) for each sub-county
        positions = {
            'Westlands': (2, 8), 'Dagoretti North': (1, 7), 'Dagoretti South': (1, 6),
            'Langata': (2, 5), 'Kibra': (3, 5), 'Roysambu': (7, 9), 'Kasarani': (6, 8),
            'Ruaraka': (5, 7), 'Embakasi North': (8, 6), 'Embakasi South': (9, 4),
            'Embakasi Central': (7, 5), 'Embakasi East': (8, 3), 'Embakasi West': (5, 4),
            'Makadara': (4, 4), 'Kamukunji': (5, 3), 'Starehe': (4, 2), 'Mathare': (4, 6)
        }
        
        color_map_display = {
            'Color_1': 'red', 'Color_2': 'blue', 'Color_3': 'green', 'Color_4': 'purple',
            'Color_5': 'orange', 'Color_6': 'brown', 'Color_7': 'pink', 'Color_8': 'cyan',
        }
        
        # Drawing sub-counties as circles
        for sub_county, (x, y) in positions.items():
            color_name = self.solution.get(sub_county, 'Color_1')
            display_color = color_map_display.get(color_name, 'gray')
            
            circle = patches.Circle((x, y), 0.4, facecolor=display_color, 
                                     edgecolor='black', linewidth=2, alpha=0.7)
            ax.add_patch(circle)
            ax.text(x, y, sub_county, ha='center', va='center', fontsize=7, fontweight='bold')
        
        # Drawing edges (adjacent connections)
        for sub_county, neighbors in self.adjacency.items():
            if sub_county in positions:
                x1, y1 = positions[sub_county]
                for neighbor in neighbors:
                    if neighbor in positions and neighbor > sub_county:
                        x2, y2 = positions[neighbor]
                        ax.plot([x1, x2], [y1, y2], 'gray', linewidth=0.5, alpha=0.5)
        
        ax.set_xlim(0, 11)
        ax.set_ylim(0, 11)
        ax.set_aspect('equal')
        ax.set_title('Nairobi Sub-Counties Map Coloring', fontsize=16, fontweight='bold')
        ax.axis('off')
        
        # Adding legend
        unique_colors = set(self.solution.values())
        legend_elements = []
        for color in sorted(unique_colors):
            display_color = color_map_display.get(color, 'gray')
            count = list(self.solution.values()).count(color)
            legend_elements.append(patches.Patch(facecolor=display_color, 
                                                  edgecolor='black', 
                                                  label=f'{color} ({count} sub-counties)'))
        
        ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1), 
                  title='Colors Used')
        
        plt.tight_layout()
        plt.savefig('nairobi_map_coloring.png', dpi=150, bbox_inches='tight')
        plt.show()
        print("\n✓ Map saved as 'nairobi_map_coloring.png'")

class NairobiColoringDemo:
    @staticmethod
    def run_demo():
        """Running the Nairobi coloring demonstration"""
        print("\n" + "=" * 60)
        print("TASK 2(B): NAIROBI SUB-COUNTIES COLORING PROBLEM")
        print("=" * 60)
        print("\nProblem Statement:")
        print("- Color Nairobi's 17 sub-counties with the minimum number of colors")
        print("- No two adjacent sub-counties can share the same color")
        
        solver = NairobiColoring()
        min_colors = solver.solve_chromatic_number()
        
        if min_colors:
            solver.display_solution(min_colors)
            solver.get_statistics()
            solver.visualize_map()  
        else:
            print("No valid coloring found!")

# Running the demonstration
if __name__ == "__main__":
    NairobiColoringDemo.run_demo()