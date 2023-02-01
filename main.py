import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    queue = [(0, start)]


    while queue:
        (distance, current) = heapq.heappop(queue)
        if distance > distances[current]:
            continue
        for neighbor, weight in graph[current].items():
            distance = distances[current] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current
                heapq.heappush(queue, (distance, neighbor))
    path, current = [], end
    while current:


        path.append(current)
        next_vertex = previous_vertices[current]
        current = next_vertex
    path = path[::-1]
    return (distances[end], path)

graph = {
    'A': {'B': 6, 'D': 4},
    'B': {'C': 3},
    'C': {'E': 4, 'H': 5},
    'D': {'C': 5, 'H': 3},
    'E': {'G': 4},
    'F': {'H': 5},
    'G': {'J': 2, 'I': 4},
    'H': {'G': 3, 'I': 7},
    'I': {'J': 1},
    'J': {},


}

print(dijkstra(graph, 'A', 'J'))
