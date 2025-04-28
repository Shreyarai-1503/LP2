class KruskalMST:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        self.edges.sort(key=lambda edge: edge[2])
        parent = {i: i for i in range(self.vertices)}
        rank = {i: 0 for i in range(self.vertices)}  # Tracks the height
        mst = []

        for u, v, weight in self.edges:
            root_u, root_v = self.find(parent, u), self.find(parent, v)
            if root_u != root_v:
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        return mst

kruskal = KruskalMST(5)
edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7)]
for u, v, w in edges:
    kruskal.add_edge(u, v, w)

print("Kruskal's MST:", kruskal.kruskal())

# Output:
'''
Kruskal's MST: [(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)]
'''