import heapq
import itertools

def dijkstra(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        (cost, u, path) = heapq.heappop(pq)
        if u == goal:
            return cost, path
        if u in visited:
            continue
        visited.add(u)
        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (cost + weight, v, path + [v]))
    return float('inf'), []

# Представление графа в виде списка смежности с весами: {u: [(v, weight), ...]}
weighted_graph = {
    'A': [('B', 6), ('C', 3), ('D', 8)],
    'B': [('A', 6), ('D', 5), ('E', 4)],
    'C': [('A', 3), ('D', 2), ('F', 7)],
    'D': [('A', 8), ('B', 5), ('C', 2), ('E', 3), ('F', 6)],
    'E': [('B', 4), ('D', 3), ('F', 4), ('G', 5)],
    'F': [('C', 7), ('D', 6), ('E', 4), ('G', 2)],
    'G': [('E', 5), ('F', 2)]
}

# Шаг 1: Нахождение нечётных вершин
odd_nodes = [v for v, nb in weighted_graph.items() if len(nb) % 2 != 0]
print("Нечётные вершины:", odd_nodes)

# Шаг 2: Кратчайшие расстояния между всеми парами нечётных вершин
import itertools
pairs = list(itertools.combinations(odd_nodes, 2))
pair_distances = {}
for u, v in pairs:
    cost, path = dijkstra(weighted_graph, u, v)
    pair_distances[(u, v)] = (cost, path)
    print(f"Кратчайший путь {u} - {v}: вес = {cost}, путь = {path}")

# Шаг 3: Минимальное паросочетание для 4 нечётных вершин
# Возможные разбиения на 2 пары:
# Вариант 1: (p1, p2) и (p3, p4)
# Вариант 2: (p1, p3) and (p2, p4)
# Вариант 3: (p1, p4) and (p2, p3)
best_matching = None
min_weight = float('inf')

# Пусть odd_nodes = [o1, o2, o3, o4]
o = odd_nodes
matchings = [
    ((o[0], o[1]), (o[2], o[3])),
    ((o[0], o[2]), (o[1], o[3])),
    ((o[0], o[3]), (o[1], o[2]))
]

for m in matchings:
    w1, _ = pair_distances.get((m[0][0], m[0][1])) or pair_distances.get((m[0][1], m[0][0]))
    w2, _ = pair_distances.get((m[1][0], m[1][1])) or pair_distances.get((m[1][1], m[1][0]))
    total_w = w1 + w2
    if total_w < min_weight:
        min_weight = total_w
        best_matching = m

print("\nОптимальное паросочетание нечётных вершин:", best_matching)
print("Минимальная стоимость дублирования путей:", min_weight)

# Суммарный вес всех рёбер исходного графа
total_edges_weight = sum(w for u in weighted_graph for _, w in weighted_graph[u]) // 2
print("Суммарный вес исходных рёбер:", total_edges_weight)
print("Итоговая минимальная длина маршрута китайского почтальона:", total_edges_weight + min_weight)