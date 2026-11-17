import heapq
import math

def search_maze(grid, start, goal, heuristic_type='manhattan'):
    n, m = len(grid), len(grid[0])

    def h(pos):
        dr = abs(pos[0] - goal[0])
        dc = abs(pos[1] - goal[1])
        if heuristic_type == 'manhattan':
            return dr + dc
        elif heuristic_type == 'euclidean':
            return math.hypot(dr, dc)
        return 0  # Дейкстра

    open_set = [(h(start), start)]
    g_score = {start: 0}
    came_from = {}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1], g_score[goal], len(visited)

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                neighbor = (nr, nc)
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    heapq.heappush(open_set, (tentative_g + h(neighbor), neighbor))

    return None, float('inf'), len(visited)


maze = [
    "S..#....",
    ".#.#.##.",
    ".#....#.",
    ".####.#.",
    "....#...",
    "###.###.",
    "........",
    ".#####.G"
]

for mode, title in [
    ('manhattan', 'A* (Манхэттенская эвристика)'),
    ('euclidean', 'A* (Евклидова эвристика)   '),
    ('dijkstra',  'Алгоритм Дейкстры (h = 0)   ')
]:
    path, length, explored = search_maze(maze, (0, 0), (7, 7), mode)
    print(f"{title} | Длина: {length} | Исследовано клеток: {explored}")
    if mode != 'dijkstra':
        print(f"  Путь: {path}")