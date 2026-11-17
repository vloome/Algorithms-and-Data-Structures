import heapq

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


def prim(n, adj, start=0):
    '''adj: {u: [(weight, v), ...]}'''
    visited = [False] * n
    mst = []
    total = 0
    pq = [(0, start, -1)]  # (weight, vertex, parent)
    
    while pq and len(mst) < n - 1:
        w, u, p = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if p != -1:
            mst.append((p, u, w))
            total += w
        for weight, v in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v, u))
    return mst, total


# Входные данные для Задания 3 (8 подстанций, индексация от 0 до 7)
n = 8
edges_sub = [
    (7, 0, 1), # 1-2
    (4, 0, 2), # 1-3
    (9, 0, 3), # 1-4
    (9, 1, 2), # 2-3
    (3, 1, 4), # 2-5
    (2, 1, 5), # 2-6
    (5, 2, 3), # 3-4
    (2, 2, 4), # 3-5
    (7, 3, 5), # 4-6
    (5, 3, 6), # 4-7
    (4, 4, 5), # 5-6
    (6, 4, 7), # 5-8
    (3, 5, 6), # 6-7
    (2, 5, 6), # параллельное ребро 6-7
    (5, 5, 7), # 6-8
]

# Создаем список смежности для алгоритма Прима
adj_sub = {i: [] for i in range(n)}
for w, u, v in edges_sub:
    adj_sub[u].append((w, v))
    adj_sub[v].append((w, u))

# Запуск алгоритма Краскала
mst_k3, total_k3 = kruskal(n, edges_sub)

# Запуск алгоритма Прима
mst_p3, total_p3 = prim(n, adj_sub, start=0)

# Вывод результатов
print(f"--- Алгоритм Краскала ---")
print(f"Общая стоимость: {total_k3}")
print("Рёбра MST:", [(u+1, v+1, w) for u, v, w in mst_k3])

print(f"\n--- Алгоритм Прима ---")
print(f"Общая стоимость: {total_p3}")
print("Рёбра MST:", [(u+1, v+1, w) for u, v, w in mst_p3])