def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    # Основной цикл динамического программирования
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Проверка наличия отрицательных циклов (отрицательные элементы на главной диагонали)
    neg_cycle_vertices = [i + 1 for i in range(n) if dist[i][i] < 0]
    if neg_cycle_vertices:
        print(f"Обнаружен отрицательный цикл, проходящий через вершины: {neg_cycle_vertices}")
        return None

    return dist


INF = float('inf')

# Матрица смежности для 5 вершин (индексы 0..4 соответствуют вершинам 1..5)
graph = [
    [0,   5,   10,  INF, INF],  # 1 -> 2 (5), 1 -> 3 (10)
    [INF, 0,   3,   INF, INF],  # 2 -> 3 (3)
    [INF, INF, 0,   2,   7],    # 3 -> 4 (2), 3 -> 5 (7)
    [INF, -2,  INF, 0,   4],    # 4 -> 2 (-2), 4 -> 5 (4)
    [12,  INF, INF, INF, 0]     # 5 -> 1 (12)
]

dist = floyd_warshall(graph)

if dist is not None:
    print("Отрицательных циклов не обнаружено.")
    print("Итоговая матрица кратчайших расстояний:")
    header = "     " + "".join(f"{j+1:>6}" for j in range(5))
    print(header)
    for i, row in enumerate(dist):
        row_str = "".join(f"{val:>6}" if val != INF else f"{'INF':>6}" for val in row)
        print(f"{i+1:>3} |{row_str}")