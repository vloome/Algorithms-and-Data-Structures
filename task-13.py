from collections import deque

def analyze_eulerian(graph):
    degrees = {v: len(nb) for v, nb in graph.items()}
    odd_vertices = [v for v, d in degrees.items() if d % 2 != 0]
    
    print("Степени вершин:", degrees)
    print("Вершины нечётной степени:", odd_vertices)
    
    if len(odd_vertices) == 0:
        return "Граф Эйлеров (существует эйлеров цикл)"
    elif len(odd_vertices) == 2:
        return "Граф Полуэйлеров (существует эйлеров путь)"
    else:
        return f"Граф НЕ является эйлеровым или полуэйлеровым (нечётных вершин: {len(odd_vertices)})"

def fleury(graph):
    g = {v: list(nb) for v, nb in graph.items()}
    
    def is_bridge(u, v):
        g[u].remove(v)
        g[v].remove(u)
        visited = {u}
        q = deque([u])
        while q:
            x = q.popleft()
            for y in g[x]:
                if y not in visited:
                    visited.add(y)
                    q.append(y)
        g[u].append(v)
        g[v].append(u)
        return v not in visited

    odd_vertices = [v for v, nb in g.items() if len(nb) % 2 != 0]
    if len(odd_vertices) == 2:
        start = odd_vertices[0]
    elif len(odd_vertices) == 0:
        start = next(iter(g))
    else:
        return "Эйлеров путь/цикл невозможен из-за нечётных вершин."

    path = [start]
    current = start
    
    while any(g.values()):
        neighbors = g[current]
        next_v = None
        for nb in neighbors:
            if not is_bridge(current, nb):
                next_v = nb
                break
        if next_v is None and neighbors:
            next_v = neighbors[0]
        if next_v is None:
            break
        g[current].remove(next_v)
        g[next_v].remove(current)
        current = next_v
        path.append(current)
    return path

# Входные данные для Задания 1
graph_task1 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E', 'F'],
    'D': ['A', 'C', 'F'],
    'E': ['B', 'C', 'F', 'G'],
    'F': ['C', 'D', 'E', 'G'],
    'G': ['E', 'F']
}

print(analyze_eulerian(graph_task1))
print("Результат работы Флёри:", fleury(graph_task1))