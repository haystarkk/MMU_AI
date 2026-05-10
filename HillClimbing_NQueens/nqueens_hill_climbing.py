import pygame
import random
import sys

class NQueens:
    def __init__(self, n):
        self.n = n
        self.state = [random.randint(0, n-1) for _ in range(n)]

    def copy(self):
        new = NQueens(self.n)
        new.state = self.state[:]
        return new

    def heuristic(self):
        conflicts = 0
        n = self.n
        for i in range(n):
            for j in range(i+1, n):
                if self.state[i] == self.state[j]:
                    conflicts += 1
                if abs(self.state[i] - self.state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def get_neighbors(self):
        neighbors = []
        n = self.n
        for col in range(n):
            current_row = self.state[col]
            for new_row in range(n):
                if new_row == current_row:
                    continue
                neighbor = self.copy()
                neighbor.state[col] = new_row
                h = neighbor.heuristic()
                neighbors.append((h, neighbor))
        return neighbors

class HillClimbingSolver:
    def __init__(self, n, max_restarts=100, max_sideways=10):
        self.n = n
        self.max_restarts = max_restarts
        self.max_sideways = max_sideways
        self.iterations = 0

    def solve(self, visualizer=None):
        for restart in range(self.max_restarts):
            current = NQueens(self.n)
            current_h = current.heuristic()
            self.iterations = 0
            sideways_moves = 0

            while True:
                if visualizer:
                    visualizer.draw_board(current.state, current_h, self.iterations)
                    pygame.event.pump()

                if current_h == 0:
                    return current.state, self.iterations, restart+1

                neighbors = current.get_neighbors()
                if not neighbors:
                    break
                best_h = min(h for h, _ in neighbors)
                best_neighbors = [state for h, state in neighbors if h == best_h]

                if best_h >= current_h:
                    if best_h == current_h and sideways_moves < self.max_sideways:
                        current = random.choice(best_neighbors)
                        sideways_moves += 1
                        self.iterations += 1
                        continue
                    else:
                        break

                current = random.choice(best_neighbors)
                current_h = best_h
                sideways_moves = 0
                self.iterations += 1

        return None, self.iterations, self.max_restarts

class Visualizer:
    def __init__(self, n, cell_size=60):
        self.n = n
        self.cell_size = cell_size
        self.width = n * cell_size
        self.height = n * cell_size + 50
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(f"N-Queens Hill Climbing (N={n})")
        self.font = pygame.font.SysFont("Arial", 18)
        self.clock = pygame.time.Clock()

    def draw_board(self, state, heuristic, iterations):
        self.screen.fill((255, 255, 255))
        n = self.n
        cell = self.cell_size

        for row in range(n):
            for col in range(n):
                color = (240, 217, 181) if (row+col) % 2 == 0 else (181, 136, 99)
                pygame.draw.rect(self.screen, color, (col*cell, row*cell, cell, cell))
                pygame.draw.rect(self.screen, (0,0,0), (col*cell, row*cell, cell, cell), 1)

        for col, row in enumerate(state):
            center_x = col * cell + cell//2
            center_y = row * cell + cell//2
            radius = cell // 3
            pygame.draw.circle(self.screen, (128, 0, 128), (center_x, center_y), radius)
            pygame.draw.circle(self.screen, (255, 215, 0), (center_x, center_y), radius-4)

        info_text = f"Heuristic (conflicts): {heuristic}   Iterations: {iterations}   Solving..."
        text_surf = self.font.render(info_text, True, (0,0,0))
        self.screen.blit(text_surf, (10, self.height - 35))

        pygame.display.flip()
        self.clock.tick(30)

    def draw_final(self, state, heuristic, iterations, restarts):
        self.draw_board(state, heuristic, iterations)
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(180)
        overlay.fill((0,0,0))
        self.screen.blit(overlay, (0,0))
        
        font_big = pygame.font.SysFont("Arial", 30)
        if heuristic == 0:
            msg = f"SUCCESS! Solution found after {iterations} moves, {restarts} restart(s)."
            color = (0, 255, 0)
        else:
            msg = f"FAILED. Best heuristic = {heuristic} after {iterations} moves, {restarts} restart(s)."
            color = (255, 0, 0)
        text = font_big.render(msg, True, color)
        self.screen.blit(text, (self.width//2 - text.get_width()//2, self.height//2 - 20))
        pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    N = 8
    MAX_RESTARTS = 100
    MAX_SIDEWAYS = 10

    visual = Visualizer(N)
    solver = HillClimbingSolver(N, max_restarts=MAX_RESTARTS, max_sideways=MAX_SIDEWAYS)
    solution, iterations, restarts = solver.solve(visualizer=visual)

    if solution is not None:
        final_board = NQueens(N)
        final_board.state = solution
        visual.draw_final(solution, final_board.heuristic(), iterations, restarts)