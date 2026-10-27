from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['E', 'G'],
    'G': ['F'],
    'H': [],
    'I': ['J', 'L'],
    'J': ['I', 'K'],
    'K': ['J', 'L'],
    'L': ['I', 'K']
}

def find_components(graph):
    visited = set()
    components = []
    for vertex in graph:
        if vertex not in visited:
            component = set()
            stack = [vertex]
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    component.add(v)
                    for nb in graph[v]:
                        if nb not in visited:
                            stack.append(nb)
            components.append(component)
    return components

def is_bipartite(graph, start_node):
    color = {start_node: 0}
    queue = deque([start_node])
    while queue:
        v = queue.popleft()
        for nb in graph[v]:
            if nb not in color:
                color[nb] = 1 - color[v]
                queue.append(nb)
            elif color[nb] == color[v]:
                return False, None
    return True, color

components = find_components(graph)
print("Компоненты связности:")
for comp in components:
    print(comp)

print("\nПроверка двудольности:")
for comp in components:
    start_node = list(comp)[0]
    if len(graph[start_node]) == 0:
        is_bip, coloring = True, {start_node: 0}
    else:
        is_bip, coloring = is_bipartite(graph, start_node)
    if is_bip:
        print(f"Компонента {comp} - двудольная. Раскраска: {coloring}")
    else:
        print(f"Компонента {comp} - НЕ двудольная (содержит цикл нечетной длины, треугольник).")