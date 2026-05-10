
---

## 📄 README.md for CAT1 folder

```markdown
# CAT 2026 - A* Search and Vacuum Agent

## File 1: astar_search.py
**What it does:** Finds the shortest/cheapest path from start (S) to goal (G) avoiding obstacles (#).

**How A* works:**
- Uses actual cost so far + estimated remaining cost
- Always expands the most promising path first
- Finds optimal path if heuristic is good

**Run:** `python astar_search.py`

**Output:** Shows path coordinates and total resource cost.

---

## File 2: vacuum_agent.py  
**What it does:** Simulates a vacuum cleaner cleaning two rooms (A and B).

**How the agent thinks:**
- Look at current room
- If dirty → clean it
- If clean → move to the other room

**Run:** `python vacuum_agent.py`

**Output:** Prints each step showing agent location, action taken, and room status.