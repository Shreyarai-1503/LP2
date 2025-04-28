import heapq

def dijkstra(graph, start):
    pq = [(0, start)]  
# (distance, node) Dijkstra expects to prioritize by distance first, so the elements in the priority queue should be (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 1), ('B', 2), ('D', 8)],
    'D': [('B', 5), ('C', 8)]
}

start_node = 'A'
print("Shortest distances:", dijkstra(graph, start_node))

# Output:
'''
Shortest distances: {'A': 0, 'B': 3, 'C': 1, 'D': 8}
'''