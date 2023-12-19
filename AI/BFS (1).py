from collections import deque

def bfs(graph, start, end):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        if vertex == end:
            return path

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in range(len(graph[vertex])):
                if graph[vertex][neighbor] == 1:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    return None


# Define the graph as an adjacency matrix
graph = [
    [0,1,1,0,0,0,0,0],
    [1,0,1,1,1,0,0,0],
    [1,1,0,1,0,0,1,0],
    [0,1,1,0,1,0,0,1],
    [0,1,0,1,0,0,0,1],
    [0,0,0,0,0,0,0,1],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,1,1,0,0]
]

vertices = ['devgad','malvan','kankavli', 'kudal','vengurla','dodamatg','vaibhavwadi','sawantwadi']

start_vertex =int(input("Enter Your Start location index value: ")) 
end_vertex = int(input("Enter Your destination location index value: ")) 

result = bfs(graph, start_vertex, end_vertex)

if result:
    print(f"Path from {vertices[start_vertex]} to {vertices[end_vertex]}:")
    for i, vertex in enumerate(result):
        print(vertices[vertex], end='')
        if i < len(result) - 1:
            print(' -> ', end='')
    print()
else:
    print(f"No path found from {vertices[start_vertex]} to {vertices[end_vertex]}")
