def bellman_ford_with_path(edges, n, start, target):
    INF = float('inf')
    dist = [INF] * n
    prev = [None] * n  # Массив предшественников для восстановления пути
    dist[start] = 0

    # V - 1 проходов релаксации
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:
            break

    # Проверка на наличие отрицательного цикла
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None, None

    # Восстановление пути от start до target
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()

    return dist, path


# Входные данные: S=0, A=1, B=2, C=3, D=4, T=5
names = ['S', 'A', 'B', 'C', 'D', 'T']
edges = [
    (0, 1, 4),   # S -> A
    (0, 2, 3),   # S -> B
    (1, 2, -2),  # A -> B
    (1, 3, 7),   # A -> C
    (2, 3, 5),   # B -> C
    (2, 4, 8),   # B -> D
    (3, 4, -1),  # C -> D
    (3, 5, 6),   # C -> T
    (4, 5, 3)    # D -> T
]
n = 6

dist, path = bellman_ford_with_path(edges, n, 0, 5)

print("Отрицательный цикл:", "обнаружен" if dist is None else "отсутствует")
print("Массив расстояний от S:", dict(zip(names, dist)))
print("Кратчайший путь от S до T:", " -> ".join(names[i] for i in path))
print("Длина пути до T:", dist[5])