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
    visited = [False] * n
    mst = []
    total = 0
    pq = [(0, start, -1)]
    
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

# Имена вершин
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
n = 8

# Рёбра в формате (вес, u, v)
edges = [
    (6, 0, 1), # A-B
    (4, 0, 2), # A-C
    (8, 0, 3), # A-D
    (2, 1, 2), # B-C
    (5, 1, 3), # B-D
    (7, 1, 4), # B-E
    (5, 1, 5), # B-F
    (3, 2, 3), # C-D
    (5, 3, 4), # D-E
    (5, 3, 5), # D-F
    (6, 3, 6), # D-G
    (4, 4, 5), # E-F
    (3, 4, 7), # E-H
    (2, 5, 6), # F-G
    (8, 5, 7), # F-H
    (5, 6, 7)  # G-H
]

# Список смежности для Прима
adj = {i: [] for i in range(n)}
for w, u, v in edges:
    adj[u].append((w, v))
    adj[v].append((w, u))

mst_k, total_k = kruskal(n, edges)
mst_p, total_p = prim(n, adj, start=0)

print(f"Краскал: суммарный вес = {total_k}")
print("Рёбра MST (Краскал):", [(names[u], names[v], w) for u, v, w in mst_k])

print(f"\nПрим: суммарный вес = {total_p}")
print("Рёбра MST (Прим):", [(names[u], names[v], w) for u, v, w in mst_p])