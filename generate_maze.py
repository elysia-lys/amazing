import random

def create_maze(width, height):
    maze = []

    for y in range(height):
        row = []

        for x in range(width):
            row.append({
                "N": 1,
                "E": 1,
                "S": 1,
                "W": 1,
                })

        maze.append(row)

    return maze


def open_wall(maze, x, y, direction):
    if direction == "E":
        maze[y][x]["E"] = 0
        maze[y][x + 1]["W"] = 0
    elif direction == "W":
        maze[y][x]["W"] = 0
        maze[y][x - 1]["E"] = 0
    elif direction == "N":
        maze[y][x]["N"] = 0
        maze[y - 1][x]["S"] = 0
    elif direction == "S":
        maze[y][x]["S"] = 0
        maze[y + 1][x]["N"] = 0


def close_wall(maze, x, y, direction):
    if direction == "E":
        maze[y][x]["E"] = 1
        maze[y][x + 1]["W"] = 1
    elif direction == "W":
        maze[y][x]["W"] = 1
        maze[y][x - 1]["E"] = 1
    elif direction == "N":
        maze[y][x]["N"] = 1
        maze[y - 1][x]["S"] = 1
    elif direction == "S":
        maze[y][x]["S"] = 1
        maze[y + 1][x]["N"] = 1


def get_neighbors(x, y, width, height):
    neighbors = []

    if x < width - 1:
        neighbors.append("E")

    if x > 0:
        neighbors.append("W")

    if y < height - 1:
        neighbors.append("S")

    if y > 0:
        neighbors.append("N")

    return neighbors


def visited_creation(width, height):
    visited = []

    for y in range(height):
        row = []
        for x in range(width):
            row.append(False)

        visited.append(row)

    return visited


def get_unvisited_neighbors(x, y, width, height, visited):
    neighbors = get_neighbors(x, y, width, height)
    unvisited = []

    for direction in neighbors:
        if direction == "E":
            if not visited[y][x + 1]:
                unvisited.append("E")
        if direction == "W":
            if not visited[y][x - 1]:
                unvisited.append("W")
        if direction == "N":
            if not visited[y - 1][x]:
                unvisited.append("N")
        if direction == "S":
            if not visited[y + 1][x]:
                unvisited.append("S")

    return unvisited


def count_deadends(maze, width, height):
    list_deadends = []

    for y in range(height):
        for x in range(width):
            connections = 0
            if maze[y][x]["E"] == 0:
                connections += 1
            if maze[y][x]["W"] == 0:
                connections += 1
            if maze[y][x]["N"] == 0:
                connections += 1
            if maze[y][x]["S"] == 0:
                connections += 1

            if connections == 1:
                list_deadends.append((x, y))

    return list_deadends

def generate_perfect_maze(width, height):
    maze = create_maze(width, height)
    visited = visited_creation(width, height)
    stack = []

    x = 0
    y = 0

    visited[y][x] = True

    while True:
        neighbors = get_unvisited_neighbors(x, y, width, height, visited)
        if neighbors:
            stack.append((x, y))
            direction = random.choice(neighbors)

            open_wall(maze, x, y, direction)
            if direction == "E":
                x += 1
            elif direction == "W":
                x -= 1
            elif direction == "N":
                y -= 1
            elif direction == "S":
                y += 1
        else:
            if not stack:
                break
            x, y = stack.pop()

        visited[y][x] = True
    return maze


def generate_imperfect_maze(width, height):
    maze = generate_perfect_maze(width, height)

    corners = [
        (0, 0),
        (width - 1, 0),
        (0, height - 1),
        (width - 1, height - 1)
    ]
    center = (width // 2, height // 2)
    important_cells = corners + [center]

    extra_walls = (width * height) // 4
    opened = 0

    # Ensure corners and center have at least 2 connections
    for x, y in important_cells:
        connections = 0

        for direction in ["N", "E", "S", "W"]:
            if maze[y][x][direction] == 0:
                connections += 1

        if connections < 2:
            neighbors = get_neighbors(x, y, width, height)

            for direction in neighbors:
                if maze[y][x][direction] == 1:
                    open_wall(maze, x, y, direction)
                    connections += 1

                if connections == 2:
                    break

        print((x, y), "connections:", connections)

    # Open random walls
    for y in range(height):
        for x in range(width):
            neighbors = get_neighbors(x, y, width, height)

            for direction in neighbors:
                if maze[y][x][direction] == 1 and opened < extra_walls:
                    if random.choice([True, False]):
                        open_wall(maze, x, y, direction)

                        # Check for a fully open 3x3 area
                        open_area = False

                        for row in range(height - 2):
                            for col in range(width - 2):
                                fully_open = True

                                for r in range(row, row + 3):
                                    for c in range(col, col + 2):
                                        if maze[r][c]["E"] == 1:
                                            fully_open = False

                                for r in range(row, row + 2):
                                    for c in range(col, col + 3):
                                        if maze[r][c]["S"] == 1:
                                            fully_open = False

                                if fully_open:
                                    open_area = True

                        if open_area:
                            close_wall(maze, x, y, direction)
                        else:
                            opened += 1

    # check for deadends
    dead_ends = count_deadends(maze, width, height)
    print("before_deadends:",dead_ends)
    for x, y in dead_ends:
        closed_walls = []
        neighbors = get_neighbors(x, y, width, height)
        for direction in neighbors:
            if maze[y][x][direction] == 1:
                closed_walls.append(direction)
        if closed_walls:
            direction = random.choice(closed_walls)
            open_wall(maze, x, y, direction)

    dead_ends = count_deadends(maze, width, height)

    # Count total connections
    total_connections = 0

    for y in range(height):
        for x in range(width):
            if maze[y][x]["E"] == 0:
                total_connections += 1
            if maze[y][x]["S"] == 0:
                total_connections += 1

    print("Total connections:", total_connections)
    print("Extra connections:", total_connections - (width * height - 1))
    print("after_deadends:",dead_ends)
    print("deadends:", len(count_deadends(maze, width, height)))

    return maze


if __name__ == "__main__":
    maze = generate_imperfect_maze(10, 10)

    for row in maze:
        for cell in row:
            print(cell, end=" ")
        print()
