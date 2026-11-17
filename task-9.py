import heapq

def dijkstra_all(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def astar(graph, start, goal, h):
    open_set = [(h[start], start)]
    g_score = {start: 0}
    came_from = {}
    explored = []

    while open_set:
        _, current = heapq.heappop(open_set)
        if current in explored:
            continue
        explored.append(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1], g_score[goal], explored

        for neighbor, weight in graph[current]:
            tentative_g = g_score[current] + weight
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                heapq.heappush(open_set, (tentative_g + h[neighbor], neighbor))

    return None, float('inf'), explored


graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 5)],
    'C': [('A', 4), ('D', 1), ('E', 7)],
    'D': [('B', 5), ('C', 1), ('F', 3)],
    'E': [('C', 7), ('F', 2), ('G', 6)],
    'F': [('D', 3), ('E', 2), ('H', 4)],
    'G': [('E', 6), ('H', 3)],
    'H': [('F', 4), ('G', 3), ('T', 5)],
    'T': [('H', 5)]
}

h_given = {'A': 8, 'B': 7, 'C': 6, 'D': 5, 'E': 4, 'F': 3, 'G': 3, 'H': 2, 'T': 0}

# 1. Проверка допустимости: истинные кратчайшие расстояния до T (граф неориентированный)
true_dist_to_T = dijkstra_all(graph, 'T')
print("Проверка допустимости эвристики (условие h(v) <= d(v, T)):")
all_admissible = True
for v in graph:
    ok = h_given[v] <= true_dist_to_T[v]
    if not ok:
        all_admissible = False
    print(f"  {v}: h={h_given[v]}, d({v}, T)={true_dist_to_T[v]} -> {'Допустима' if ok else 'НЕ допустима'}")

# 2. A* с заданной эвристикой
path_a, cost_a, exp_a = astar(graph, 'A', 'T', h_given)
print(f"\nA* (заданная h): путь = {' -> '.join(path_a)}, стоимость = {cost_a}")
print(f"  Исследовано вершин ({len(exp_a)}): {exp_a}")

# 3. A* при h = 0 (Дейкстра)
h_zero = {v: 0 for v in graph}
path_d, cost_d, exp_d = astar(graph, 'A', 'T', h_zero)
print(f"\nA* (h = 0 / Дейкстра): путь = {' -> '.join(path_d)}, стоимость = {cost_d}")
print(f"  Исследовано вершин ({len(exp_d)}): {exp_d}")