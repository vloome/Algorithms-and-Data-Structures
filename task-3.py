from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E', 'F'],
    'D': ['G'],
    'E': ['G', 'H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

# 1. Топологическая сортировка (DFS)
def topological_sort(graph):
    visited = set()
    result = []

    def dfs(v):
        visited.add(v)
        for nb in graph.get(v, []):
            if nb not in visited:
                dfs(nb)
        result.append(v)

    for v in graph:
        if v not in visited:
            dfs(v)
    return result[::-1]  # Разворачиваем результат

# 2. Поиск кратчайшего пути (BFS)
def bfs_shortest_path(graph, start, end):
    visited = {start}
    queue = deque([start])
    parents = {start: None}

    while queue:
        vertex = queue.popleft()
        if vertex == end:
            break
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = vertex
                queue.append(neighbor)

    # Восстановление пути
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents.get(current)
    
    path.reverse()
    return path

# Выполнение
print("Топологическая сортировка:", topological_sort(graph))

shortest_path = bfs_shortest_path(graph, 'A', 'H')
print("Кратчайший путь от A до H:", " -> ".join(shortest_path))
print("Длина пути (число рёбер):", len(shortest_path) - 1)