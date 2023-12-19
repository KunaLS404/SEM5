def iterative_best_first_search(graph, start, goal):
    stack = [(start, float('inf'))]
    path = []

    while stack:
        current, f_limit = stack[-1]

        if current == goal:
            return path + [current]

        successors = [neighbor for neighbor in graph[current] if neighbor not in path]

        if not successors:
            stack.pop()
            path.pop()
        else:
            next_node = successors[0]
            stack.append((next_node, min(f_limit, float('inf'))))
            path.append(next_node)

    return None

# Example graph representing cities in India and their connections
graph = {
    'Delhi': {'Mumbai', 'Jaipur', 'Lucknow'},
    'Mumbai': {'Delhi', 'Chennai', 'Bangalore'},
    'Chennai': {'Mumbai', 'Bangalore'},
    'Bangalore': {'Mumbai', 'Chennai', 'Hyderabad'},
    'Hyderabad': {'Bangalore', 'Chennai'},
    'Jaipur': {'Delhi', 'Lucknow'},
    'Lucknow': {'Delhi', 'Jaipur'}
}

# Take input from the user for start and goal cities
start_city = input("Enter the start city in India: ")
goal_city = input("Enter the goal city in India: ")

# Run Iterative Best-First Search algorithm
path = iterative_best_first_search(graph, start_city, goal_city)

if path is not None:
    print(f"Found path from {start_city} to {goal_city}: {' -> '.join(path)}")
else:
    print("No path found")
