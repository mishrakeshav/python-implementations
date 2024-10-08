import heapq


# Dijkstra's algorithm using dictionary
def dijkstra_dict(graph, start):
    # Priority queue to store (distance, node) tuples
    queue = []
    heapq.heappush(queue, (0, start))

    # Dictionary to store the shortest path to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Dictionary to store the previous node in the path
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # If the distance is already greater than the known shortest, skip
        if current_distance > distances[current_node]:
            continue

        # Explore the neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes


def shortest_path(graph, start, goal):
    distances, previous_nodes = dijkstra_dict(graph, start)
    path = []
    current_node = goal

    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    return path, distances[goal]


# Example usage:
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }
#
# start_node = 'A'
# goal_node = 'D'
#
# path, cost = shortest_path(graph, start_node, goal_node)
# print(f"Shortest path from {start_node} to {goal_node}: {path} with total cost {cost}")


# Dijkstra's algorithm using adjacency matrix

def dijkstra_matrix(graph, start):
    n = len(graph)  # Number of nodes in the graph
    distances = [float('infinity')] * n  # Initialize distances
    distances[start] = 0
    previous_nodes = [None] * n  # To store the path

    # Priority queue to store (distance, node) tuples
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # If the distance is already greater than the known shortest, skip
        if current_distance > distances[current_node]:
            continue

        # Explore the neighbors
        for neighbor in range(n):
            if graph[current_node][neighbor] != 0:  # Check if there's a connection
                distance = current_distance + graph[current_node][neighbor]

                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes


def shortest_path_matrix(graph, start, goal):
    distances, previous_nodes = dijkstra_matrix(graph, start)
    path = []
    current_node = goal

    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    return path, distances[goal]

# Example usage:
# graph_matrix = [
#     [0, 1, 4, 0],
#     [1, 0, 2, 5],
#     [4, 2, 0, 1],
#     [0, 5, 1, 0]
# ]
#
# start_node = 0  # Starting from node 'A' (index 0)
# goal_node = 3  # Goal is node 'D' (index 3)
#
# path, cost = shortest_path_matrix(graph_matrix, start_node, goal_node)
# print(f"Shortest path from {start_node} to {goal_node}: {path} with total cost {cost}")




def bellman_ford(graph, V, source):
    # Step 1: Initialize distances from source to all vertices as infinity
    # Distance to source is 0
    dist = [float('inf')] * V
    dist[source] = 0

    # Step 2: Relax all edges V-1 times
    for _ in range(V-1):
        for u, v, w in graph:  # u is source, v is destination, w is weight
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 3: Check for negative-weight cycles
    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return


########## Floyd Warshall #####################


def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]  # Create a copy of the graph

    # Initialize the distance matrix
    for i in range(V):
        for j in range(V):
            if i != j and dist[i][j] == 0:
                dist[i][j] = float('inf')

    # Main algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Example usage
# graph = [
#     [0, 5, float('inf'), 10],
#     [float('inf'), 0, 3, float('inf')],
#     [float('inf'), float('inf'), 0, 1],
#     [float('inf'), float('inf'), float('inf'), 0]
# ]
#
# result = floyd_warshall(graph)
# for row in result:
#     print(row)


########## ----------------------- #####################