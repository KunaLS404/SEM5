import sqlite3

# Create a database connection and cursor
connection = sqlite3.connect("visited_places.db")
cursor = connection.cursor()

# Create a table to store visited places
cursor.execute('''CREATE TABLE IF NOT EXISTS visited_places
                (vertex TEXT PRIMARY KEY, visit_order INTEGER)''')
connection.commit()

def dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(vertices[start])  # Append the actual place name

    # Store visited place in the database
    vertex_name = vertices[start]
    visit_order = len(path)
    
    # Check if the vertex already exists in the table
    cursor.execute("SELECT * FROM visited_places WHERE vertex = ?", (vertex_name,))
    existing_row = cursor.fetchone()

    if existing_row is None:
        # If the vertex doesn't exist, insert it
        cursor.execute("INSERT INTO visited_places (vertex, visit_order) VALUES (?, ?)",
                       (vertex_name, visit_order))
    else:
        # If the vertex already exists, update the visit_order
        cursor.execute("UPDATE visited_places SET visit_order = ? WHERE vertex = ?",
                       (visit_order, vertex_name))

    connection.commit()

    if start == end:
        return path

    for neighbor in range(len(graph[start])):
        if graph[start][neighbor] == 1 and neighbor not in visited:
            new_path = dfs(graph, neighbor, end, visited, path)
            if new_path:
                return new_path

    path.pop()
    visited.remove(start)

    return None

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
vertices = ['Devgad','Malvan','Kankavli', 'Kudal','Vengurla','Dodamargh','Vaibhavwadi','Sawantwadi']

start_vertex = int(input("Enter your Start index value: "))
end_vertex =int(input("Enter your destination index value: "))

result = dfs(graph, start_vertex, end_vertex)

if result:
    print(f"Path from {vertices[start_vertex]} to {vertices[end_vertex]}:")
    print(' -> '.join(result))  # Join the place names with ' -> ' separator
else:
    print(f"No path found from {vertices[start_vertex]} to {vertices[end_vertex]}")

# Close the database connection
connection.close()
