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
    'I': {'J': 1, 'H': 7, 'G': 4},
    'J': {'G': 2},
    'H': {'F': 4, 'D': 3, 'C': 5},
    'G': {'H': 3, 'E': 4},
    'F': {'D': 2},
    'E': {'C': 4},
    'D': {'A': 4},
    'C': {'D': 5, 'B': 3},
    'B': {'A': 6},
    'A': {},


}


distance = dijkstra(graph, 'I', 'A')
print('Оптимальное расстояние :', distance)



