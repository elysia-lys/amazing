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


def has_open_3x3(maze, width, height):
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
                return True

    return False


def get_logo_cells(width, height):
    if width < 7 or height < 5:
        print("Error: Maze is too small to fit 42 pattern")
        return []
    pattern = [
        "#...###",
        "#.....#",
        "###.###",
        "..#.#..",
        "..#.###"
    ]

    start_x = (width - 7) // 2
    start_y = (height - 5) // 2

    logo_cells = []

    for y in range(5):
        for x in range(7):
            if pattern[y][x] == "#":
                logo_cells.append((start_x + x, start_y + y))

    return logo_cells


def generate_perfect_maze(width, height, logo_cells=None):
    maze = create_maze(width, height)
    visited = visited_creation(width, height)
    stack = []

    if logo_cells is None:
        logo_cells = get_logo_cells(width, height)
    for x, y in logo_cells:
        visited[y][x] = True

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
    logo_cells = get_logo_cells(width, height)
    maze = generate_perfect_maze(width, height, logo_cells)
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
        if (x, y) in logo_cells:
            continue

        connections = 0

        for direction in ["N", "E", "S", "W"]:
            if maze[y][x][direction] == 0:
                connections += 1

        if connections < 2:
            neighbors = get_neighbors(x, y, width, height)

            for direction in neighbors:
                nx, ny = x, y
                if direction == "E":
                    nx += 1
                elif direction == "W":
                    nx -= 1
                elif direction == "N":
                    ny -= 1
                elif direction == "S":
                    ny += 1

                if (nx, ny) in logo_cells:
                    continue

                if maze[y][x][direction] == 1:
                    open_wall(maze, x, y, direction)
                    connections += 1

                if connections == 2:
                    break

    # Open random walls
    for y in range(height):
        for x in range(width):
            if (x, y) in logo_cells:
                continue
            neighbors = get_neighbors(x, y, width, height)

            for direction in neighbors:
                if direction == "E":
                    nx, ny = x + 1, y
                elif direction == "W":
                    nx, ny = x - 1, y
                elif direction == "N":
                    nx, ny = x, y - 1
                elif direction == "S":
                    nx, ny = x, y + 1

                if (nx, ny) in logo_cells:
                    continue

                if maze[y][x][direction] == 1 and opened < extra_walls:
                    if random.choice([True, False]):
                        open_wall(maze, x, y, direction)

                        # Check for a fully open 3x3 area
                        if has_open_3x3(maze, width, height):
                            close_wall(maze, x, y, direction)
                        else:
                            opened += 1

    # Remove deadends
    dead_ends = count_deadends(maze, width, height)
    for dead_x, dead_y in dead_ends:
        closed_walls = []
        neighbors = get_neighbors(dead_x, dead_y, width, height)

        for direction in neighbors:
            nx, ny = dead_x, dead_y

            if direction == "E":
                nx += 1
            elif direction == "W":
                nx -= 1
            elif direction == "N":
                ny -= 1
            elif direction == "S":
                ny += 1

            if (nx, ny) in logo_cells:
                continue

            if maze[dead_y][dead_x][direction] == 1:
                closed_walls.append(direction)

        if closed_walls:
            direction = random.choice(closed_walls)
            open_wall(maze, dead_x, dead_y, direction)

            if has_open_3x3(maze, width, height):
                close_wall(maze, dead_x, dead_y, direction)

    return maze


# for debudding
def print_maze(maze, width, height):

    for y in range(height):
        # Print north walls
        for x in range(width):
            print("+---" if maze[y][x]["N"] == 1 else "+   ", end="")
        print("+")

        # Print west and east walls
        for x in range(width):
            if all(maze[y][x][d] == 1 for d in ("N", "E", "S", "W")):
                print("| # ", end="")
            else:
                print("|   " if maze[y][x]["W"] == 1 else "    ", end="")
        print("|" if maze[y][width - 1]["E"] == 1 else " ")

    # Print bottom walls
    for x in range(width):
        print("+---" if maze[height - 1][x]["S"] == 1 else "+   ", end="")
    print("+")


if __name__ == "__main__":
    try:
        maze = generate_perfect_maze(7, 5)
        print_maze(maze, 7, 5)
    except ValueError as e:
        print(e)
