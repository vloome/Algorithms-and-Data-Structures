import math

def find_arbitrage(rates, start_capital=1000):
    # Список уникальных валют и сопоставление с индексами
    currencies = ['USD', 'EUR', 'GBP', 'JPY']
    idx = {c: i for i, c in enumerate(currencies)}
    n = len(currencies)

    # Преобразование курсов в веса: w = -log(rate)
    edges = [(idx[u], idx[v], -math.log(rate)) for u, v, rate in rates]
    rate_map = {(u, v): rate for u, v, rate in rates}

    # Инициализируем расстояния нулями, чтобы найти отрицательный цикл в любой компоненте
    dist = [0.0] * n
    prev = [-1] * n

    # Выполняем n итераций; на n-й итерации фиксируем вершину, попавшую в релаксацию
    last_updated = -1
    for i in range(n):
        last_updated = -1
        for u, v, w in edges:
            if dist[u] + w < dist[v] - 1e-12:
                dist[v] = dist[u] + w
                prev[v] = u
                last_updated = v

    if last_updated == -1:
        print("Арбитражная возможность отсутствует.")
        return

    # Сдвигаемся на n шагов назад по предшественникам, чтобы гарантированно попасть внутрь цикла
    curr = last_updated
    for _ in range(n):
        curr = prev[curr]

    # Восстанавливаем сам цикл
    cycle_indices = []
    node = curr
    while True:
        cycle_indices.append(node)
        node = prev[node]
        if node == curr and len(cycle_indices) > 1:
            cycle_indices.append(node)
            break
    cycle_indices.reverse()

    cycle_names = [currencies[i] for i in cycle_indices]

    # Вычисляем произведение курсов по найденному циклу
    total_multiplier = 1.0
    for i in range(len(cycle_names) - 1):
        u, v = cycle_names[i], cycle_names[i + 1]
        total_multiplier *= rate_map[(u, v)]

    final_amount = start_capital * total_multiplier
    profit = final_amount - start_capital

    print("Арбитражная возможность обнаружена!")
    print("Выгодный цикл обмена:", " -> ".join(cycle_names))
    print(f"Коэффициент умножения за круг: {total_multiplier:.6f}")
    print(f"Стартовый капитал: {start_capital:.2f}")
    print(f"Итоговая сумма: {final_amount:.2f}")
    print(f"Чистая прибыль: {profit:.2f} единиц (+{(total_multiplier - 1) * 100:.4f}%)")


rates = [
    ('USD', 'EUR', 0.85),
    ('EUR', 'GBP', 1.15),
    ('USD', 'JPY', 145),
    ('JPY', 'GBP', 0.0075),
    ('GBP', 'USD', 1.05)
]

find_arbitrage(rates, start_capital=1000)