import random


class MazeGenerator:
    def __init__(
            self, width: int, height: int,
            entry: tuple[int, int], exit: tuple[int, int],
            perfect: bool, seed: int
            ) -> None:
        self.maze: list[list[dict[str, int]]] = []
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.seed = seed

    def create_maze(self) -> list[list[dict[str, int]]]:
        self.maze = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append({
                    "N": 1,
                    "E": 1,
                    "S": 1,
                    "W": 1,
                    })
            self.maze.append(row)
        return self.maze

    def open_entrance_exit(self) -> None:
        entry_x, entry_y = self.entry
        exit_x, exit_y = self.exit

        if entry_x == 0:
            self.maze[entry_y][entry_x]["W"] = 0
        elif entry_x == self.width - 1:
            self.maze[entry_y][entry_x]["E"] = 0
        elif entry_y == 0:
            self.maze[entry_y][entry_x]["N"] = 0
        elif entry_y == self.height - 1:
            self.maze[entry_y][entry_x]["S"] = 0

        if exit_x == 0:
            self.maze[exit_y][exit_x]["W"] = 0
        elif exit_x == self.width - 1:
            self.maze[exit_y][exit_x]["E"] = 0
        elif exit_y == 0:
            self.maze[exit_y][exit_x]["N"] = 0
        elif exit_y == self.height - 1:
            self.maze[exit_y][exit_x]["S"] = 0

    def open_wall(self, x: int, y: int, direction: str) -> None:
        if direction == "E":
            self.maze[y][x]["E"] = 0
            self.maze[y][x + 1]["W"] = 0
        elif direction == "W":
            self.maze[y][x]["W"] = 0
            self.maze[y][x - 1]["E"] = 0
        elif direction == "N":
            self.maze[y][x]["N"] = 0
            self.maze[y - 1][x]["S"] = 0
        elif direction == "S":
            self.maze[y][x]["S"] = 0
            self.maze[y + 1][x]["N"] = 0

    def close_wall(self, x: int, y: int, direction: str) -> None:
        if direction == "E":
            self.maze[y][x]["E"] = 1
            self.maze[y][x + 1]["W"] = 1
        elif direction == "W":
            self.maze[y][x]["W"] = 1
            self.maze[y][x - 1]["E"] = 1
        elif direction == "N":
            self.maze[y][x]["N"] = 1
            self.maze[y - 1][x]["S"] = 1
        elif direction == "S":
            self.maze[y][x]["S"] = 1
            self.maze[y + 1][x]["N"] = 1

    def get_neighbors(self, x: int, y: int) -> list[str]:
        neighbors = []

        if x < self.width - 1:
            neighbors.append("E")

        if x > 0:
            neighbors.append("W")

        if y < self.height - 1:
            neighbors.append("S")

        if y > 0:
            neighbors.append("N")

        return neighbors

    def visited_creation(self) -> list[list[bool]]:
        visited = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(False)

            visited.append(row)

        return visited

    def get_unvisited_neighbors(
            self, x: int, y: int,
            visited: list[list[bool]]
            ) -> list[str]:
        neighbors = self.get_neighbors(x, y)
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

    def count_deadends(
            self, logo_cells: list[tuple[int, int]]
            ) -> list[tuple[int, int]]:
        list_deadends = []

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in logo_cells:
                    continue
                connections = 0
                if self.maze[y][x]["E"] == 0:
                    connections += 1
                if self.maze[y][x]["W"] == 0:
                    connections += 1
                if self.maze[y][x]["N"] == 0:
                    connections += 1
                if self.maze[y][x]["S"] == 0:
                    connections += 1

                if connections == 1:
                    list_deadends.append((x, y))

        return list_deadends

    def has_open_3x3(self) -> bool:
        for row in range(self.height - 2):
            for col in range(self.width - 2):
                fully_open = True

                for r in range(row, row + 3):
                    for c in range(col, col + 2):
                        if self.maze[r][c]["E"] == 1:
                            fully_open = False

                for r in range(row, row + 2):
                    for c in range(col, col + 3):
                        if self.maze[r][c]["S"] == 1:
                            fully_open = False

                if fully_open:
                    return True

        return False

    def get_logo_cells(self) -> list[tuple[int, int]]:
        if self.width < 7 or self.height < 5:
            print("Error: Maze is too small to fit 42 pattern")
            return []
        pattern = [
            "#...###",
            "#.....#",
            "###.###",
            "..#.#..",
            "..#.###"
        ]

        start_x = (self.width - 7) // 2
        start_y = (self.height - 5) // 2

        logo_cells = []

        for y in range(5):
            for x in range(7):
                if pattern[y][x] == "#":
                    logo_cells.append((start_x + x, start_y + y))

        return logo_cells

    def generate_perfect_maze(
            self,
            logo_cells: list[tuple[int, int]] | None = None
            ) -> list[list[dict[str, int]]]:
        random.seed(self.seed)
        self.maze = self.create_maze()
        visited = self.visited_creation()
        stack = []

        if logo_cells is None:
            logo_cells = self.get_logo_cells()
        for x, y in logo_cells:
            visited[y][x] = True

        x = 0
        y = 0

        visited[y][x] = True

        while True:
            neighbors = self.get_unvisited_neighbors(x, y, visited)
            if neighbors:
                stack.append((x, y))
                direction = random.choice(neighbors)

                self.open_wall(x, y, direction)
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

        self.open_entrance_exit()
        return self.maze

    def generate_imperfect_maze(self) -> list[list[dict[str, int]]]:
        logo_cells = self.get_logo_cells()
        self.maze = self.generate_perfect_maze(logo_cells=logo_cells)
        corners = [
            (0, 0),
            (self.width - 1, 0),
            (0, self.height - 1),
            (self.width - 1, self.height - 1)
        ]
        center = (self.width // 2, self.height // 2)
        important_cells = corners + [center]

        extra_walls = (self.width * self.height) // 4
        opened = 0

        # Ensure corners and center have at least 2 connections
        for x, y in important_cells:
            if (x, y) in logo_cells:
                continue

            connections = 0

            for direction in ["N", "E", "S", "W"]:
                if self.maze[y][x][direction] == 0:
                    connections += 1

            if connections < 2:
                neighbors = self.get_neighbors(x, y)

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

                    if self.maze[y][x][direction] == 1:
                        self.open_wall(x, y, direction)
                        connections += 1

                    if connections == 2:
                        break

        # Open random walls
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in logo_cells:
                    continue
                neighbors = self.get_neighbors(x, y)

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

                    if (
                            self.maze[y][x][direction] == 1
                            and opened < extra_walls
                            ):
                        if random.choice([True, False]):
                            self.open_wall(x, y, direction)

                            # Check for a fully open 3x3 area
                            if self.has_open_3x3():
                                self.close_wall(x, y, direction)
                            else:
                                opened += 1

        # Remove deadends
        dead_ends = self.count_deadends(logo_cells)
        for dead_x, dead_y in dead_ends:
            closed_walls = []
            neighbors = self.get_neighbors(dead_x, dead_y)

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

                if self.maze[dead_y][dead_x][direction] == 1:
                    closed_walls.append(direction)

            if closed_walls:
                direction = random.choice(closed_walls)
                self.open_wall(dead_x, dead_y, direction)

                if self.has_open_3x3():
                    self.close_wall(dead_x, dead_y, direction)

        return self.maze

    # for debudding
    def print_maze(self) -> None:

        for y in range(self.height):
            # Print north walls
            for x in range(self.width):
                print("+---" if self.maze[y][x]["N"] == 1 else "+   ", end="")
            print("+")

            # Print west and east walls
            for x in range(self.width):
                if all(self.maze[y][x][d] == 1 for d in ("N", "E", "S", "W")):
                    print("| # ", end="")
                else:
                    print(
                            "|   " if self.maze[y][x]["W"] == 1
                            else "    ", end=""
                            )
            print("|" if self.maze[y][self.width - 1]["E"] == 1 else " ")

        # Print bottom walls
        for x in range(self.width):
            print(
                    "+---" if self.maze[self.height - 1][x]["S"] == 1
                    else "+   ", end=""
                    )
        print("+")
