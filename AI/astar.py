import heapq

def astar(graph, start, goal):
    open_set = []  
    heapq.heappush(open_set, (0, start))  
    came_from = {}  

    while open_set:
        _, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = reconstruct_path(came_from, start, goal)
            print("Path found:", ' -> '.join(path))
            return

        for neighbor in graph[current_node]:
            if neighbor not in came_from:
                heapq.heappush(open_set, (0, neighbor))
                came_from[neighbor] = current_node

    print("No path found")

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path[::-1]

city_graph = {
    'Delhi': {'Mumbai', 'Jaipur', 'Lucknow'},
    'Mumbai': {'Delhi', 'Chennai', 'Bangalore'},
    'Chennai': {'Mumbai', 'Bangalore'},
    'Bangalore': {'Mumbai', 'Chennai', 'Hyderabad'},
    'Hyderabad': {'Bangalore', 'Chennai'},
    'Jaipur': {'Delhi', 'Lucknow'},
    'Lucknow': {'Delhi', 'Jaipur'}
}

start_city = input("Enter the start city in India: ")
goal_city = input("Enter the goal city in India: ")

print(f"Finding path from {start_city} to {goal_city} using A* algorithm:")
astar(city_graph, start_city, goal_city)
