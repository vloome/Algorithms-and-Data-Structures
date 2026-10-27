import random
def build_ba_network(m0=3, new_nodes=1000, m=2, seed=42):
    random.seed(seed)
    # Начальная полная сеть: вершины 0, 1 и 2 соединены друг с другом.
    graph = {v: set() for v in range(m0)}
    for u in range(m0):
        for v in range(u + 1, m0):
            graph[u].add(v)
            graph[v].add(u)
    # Каждый новый узел выбирает m разных старых узлов.
    for new_node in range(m0, m0 + new_nodes):
        candidates = list(graph.keys())
        targets = []
        while len(targets) < m:
            weights = [len(graph[v]) for v in candidates]
            target = random.choices(candidates, weights=weights, k=1)[0]
            if target not in targets:
                targets.append(target)
        graph[new_node] = set()
        for target in targets:
            graph[new_node].add(target)
            graph[target].add(new_node)
    return graph

if __name__ == "__main__":
    graph = build_ba_network()
    hubs = sorted(
        ((len(neighbors), node) for node, neighbors in graph.items()),
        reverse=True,
    )
    print("Топ-5 узлов-концентраторов:")
    for degree, node in hubs[:5]:
        print(f"Узел {node}: степень {degree}")
