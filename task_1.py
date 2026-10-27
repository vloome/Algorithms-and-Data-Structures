graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6', '7'],
    '4': ['2', '8'],
    '5': ['2', '8'],
    '6': ['3', '9'],
    '7': ['3', '9'],
    '8': ['4', '5', '10'],
    '9': ['6', '7', '10'],
    '10': ['8', '9']
}

# Реализация DFS (рекурсивная)
def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# Реализация BFS (через очередь)
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

print("DFS обход от вершины 1:")
dfs(graph, '1')
print("\nBFS обход от вершины 1:")
print(bfs(graph, '1'))