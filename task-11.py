class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskal(n, edges):
    '''edges: [(weight, u, v), ...]'''
    edges.sort()
    dsu = DSU(n)
    mst = []
    total = 0
    for w, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == n - 1:
                break
    return mst, total


# Список городов и их индексы
cities = [
    "SPb", "Moscow", "NNovgorod", "Kazan", "Ufa", 
    "Ekaterinburg", "Tyumen", "Samara", "Volgograd", "Rostov", "Krasnodar"
]
c_idx = {name: i for i, name in enumerate(cities)}

# Рёбра графа (расстояние, город1, город2)
road_edges = [
    (650, "SPb", "Moscow"),
    (1200, "SPb", "NNovgorod"),
    (400, "Moscow", "NNovgorod"),
    (800, "Moscow", "Kazan"),
    (1100, "Moscow", "Rostov"),
    (400, "NNovgorod", "Kazan"),
    (500, "Kazan", "Ufa"),
    (450, "Kazan", "Samara"),
    (550, "Ufa", "Ekaterinburg"),
    (350, "Ekaterinburg", "Tyumen"),
    (450, "Ufa", "Samara"),
    (900, "Samara", "Rostov"),
    (850, "Samara", "Volgograd"),
    (400, "Rostov", "Volgograd"),
    (250, "Rostov", "Krasnodar")
]

# Преобразуем текстовые названия городов в числовые индексы для алгоритма
formatted_edges = [(w, c_idx[u], c_idx[v]) for w, u, v in road_edges]
n = len(cities)

# Запуск алгоритма Краскала
mst, total_length = kruskal(n, formatted_edges)

# Вывод результатов
print(f"Минимальная общая длина сети: {total_length} км")
print("Выбранные участки дорог в MST:")
degrees = {i: 0 for i in range(n)}
for u, v, w in mst:
    degrees[u] += 1
    degrees[v] += 1
    print(f"  {cities[u]} — {cities[v]}: {w} км")

print("\nСтепени вершин (количество связей в MST):")
for i, deg in sorted(degrees.items(), key=lambda x: x[1], reverse=True):
    print(f"  {cities[i]}: {deg}")