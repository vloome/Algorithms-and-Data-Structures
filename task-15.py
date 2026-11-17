def hamiltonian_cycle_check(graph):
    vertices = list(graph.keys())
    n = len(vertices)
    
    # Проверка теоремы Дирака: deg(v) >= n / 2 для всех вершин
    dirak_satisfied = all(len(graph[v]) >= n / 2 for v in vertices)
    print(f"Выполнение теоремы Дирака (deg(v) >= {n/2}): {dirak_satisfied}")

    def backtrack(path):
        if len(path) == n:
            if path[0] in graph[path[-1]]:
                return path + [path[0]]
            return None
        current = path[-1]
        for nb in sorted(graph[current]):
            if nb not in path:
                result = backtrack(path + [nb])
                if result:
                    return result
        return None

    for start in vertices:
        res = backtrack([start])
        if res:
            return res
    return None

# Входные данные для Задания 3
graph_task3 = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['A', 'D', 'E']
}

cycle = hamiltonian_cycle_check(graph_task3)
print("Найденный гамильтонов цикл:", cycle)