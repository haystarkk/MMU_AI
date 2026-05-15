"""Python wrapper for running Prolog family tree queries
Requires: pip install pyswip"""

import subprocess
import sys

def run_prolog_queries():
    """Run Prolog queries using subprocess"""
    print("=" * 60)
    print("PROLOG FAMILY TREE PROGRAM")
    print("=" * 60)
    
    try:
        # Run swipl with the family tree file
        result = subprocess.run(
            ['swipl', '-s', 'family_tree.pl', '-g', 'main', '-t', 'halt'],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
            
    except FileNotFoundError:
        print("SWI-Prolog not found. Please install SWI-Prolog first.")
        print("\nInstallation instructions:")
        print("  Windows: Download from https://www.swi-prolog.org/download/stable")
        print("  Mac: brew install swi-prolog")
        print("  Linux: sudo apt-get install swi-prolog")
        
def run_interactive():
    """Running interactive Prolog session"""
    print("\nStarting interactive Prolog session...")
    print("Type queries directly or type 'halt.' to exit\n")
    
    try:
        subprocess.run(['swipl', '-s', 'family_tree.pl'])
    except FileNotFoundError:
        print("SWI-Prolog not found")

if __name__ == "__main__":
    print("Choose option:")
    print("1. Run pre-defined queries")
    print("2. Run interactive session")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == '1':
        run_prolog_queries()
    elif choice == '2':
        run_interactive()
    else:
        print("Invalid choice")