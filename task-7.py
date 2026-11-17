import heapq

def astar_graph(graph, start, goal, h_func):
    # Очередь с приоритетом: (f_score, vertex)
    open_set = [(h_func(start), start)]
    g_score = {start: 0}
    came_from = {}
    explored_order = []

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current in explored_order:
            continue
        explored_order.append(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1], g_score[goal], explored_order

        for neighbor, weight in graph[current]:
            tentative_g = g_score[current] + weight
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + h_func(neighbor)
                heapq.heappush(open_set, (f, neighbor))

    return None, float('inf'), explored_order


graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('A', 3), ('D', 4), ('E', 7)],
    'C': [('A', 5), ('D', 2), ('F', 6)],
    'D': [('B', 4), ('C', 2), ('E', 3), ('G', 8)],
    'E': [('B', 7), ('D', 3), ('H', 5)],
    'F': [('C', 6), ('G', 4)],
    'G': [('D', 8), ('F', 4), ('H', 2), ('T', 7)],
    'H': [('E', 5), ('G', 2), ('T', 6)],
    'T': [('G', 7), ('H', 6)]
}

# Условные координаты вершин для расчёта манхэттенской эвристики
coords = {
    'A': (0, 3), 'B': (3, 6), 'C': (3, 0),
    'D': (6, 3), 'E': (6, 7), 'F': (6, -1),
    'G': (9, 2), 'H': (9, 7), 'T': (12, 4)
}

def manhattan_h(v):
    return abs(coords[v][0] - coords['T'][0]) + abs(coords[v][1] - coords['T'][1])

# Запуск A*
path_a, cost_a, exp_a = astar_graph(graph, 'A', 'T', manhattan_h)
# Запуск Дейкстры (h = 0)
path_d, cost_d, exp_d = astar_graph(graph, 'A', 'T', lambda v: 0)

print("Эвристики h(v):", {v: manhattan_h(v) for v in graph})
print(f"A*:       путь = {' -> '.join(path_a)}, стоимость = {cost_a}, исследовано вершин: {len(exp_a)} {exp_a}")
print(f"Дейкстра: путь = {' -> '.join(path_d)}, стоимость = {cost_d}, исследовано вершин: {len(exp_d)} {exp_d}")