from queue import PriorityQueue

# Function to calculate the 'heuristic'
def h(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def A_star(maze, start, goal):

    # Priority queue for the nodes to visit
    queue = PriorityQueue()
    queue.put((0, start))

    # Dictionary to keep track of where we came from
    came_from = {}
    came_from[start] = None

    # Dictionary to keep track of the cost to reach each node
    cost_so_far = {}
    cost_so_far[start] = 0

    while not queue.empty():
        _, current = queue.get()

        # Goal reached
        if current == goal:
            break

        # Check all neighbors
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_node = (current[0] + dx, current[1] + dy)
            new_cost = cost_so_far[current] + 1

            # If the next node is not a wall and it's either not been visited or
            # we have a cheaper way to visit it now
            if maze[next_node[0]][next_node[1]] != '#' and (next_node not in cost_so_far or new_cost < cost_so_far[next_node]):
                cost_so_far[next_node] = new_cost
                priority = new_cost + h(next_node, goal)
                queue.put((priority, next_node))
                came_from[next_node] = current

    # Reconstruct the path
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path

# Define a simple maze
maze = [
    ['S', '.', '.', '#', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '.', 'G']
]

# Find the path
start = (0, 0)
goal = (5, 7)
path = A_star(maze, start, goal)
for position in path:
    if maze[position[0]][position[1]] == '.':
        maze[position[0]][position[1]] = '*'
for row in maze:
    print(' '.join(row))
