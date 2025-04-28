import heapq
from collections import defaultdict

class PrimsMST:
    def __init__(self, vertices):
        self.vertices = vertices
        #self.graph = {i: [] for i in range(vertices)}
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))  # Since the graph is undirected

    def prim(self):
        mst, visited, edges = [], set(), [(0, 0, 0)]  # (weight, from, to)
        heapq.heapify(edges)

        while edges and len(visited) < self.vertices:
            weight, frm, to = heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                if frm != to:
                    mst.append((frm, to, weight))

                for next_weight, next_to in self.graph[to]:
                    if next_to not in visited:
                        heapq.heappush(edges, (next_weight, to, next_to))

        return mst

# Example Usage
prims = PrimsMST(5)
edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7)]
for u, v, w in edges:
    prims.add_edge(u, v, w)

print("Prim's MST:", prims.prim())

# Output:
'''
Prim's MST: [(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)]
'''