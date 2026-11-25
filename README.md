# A-Maze-ing

*This project has been created as part of the 42 curriculum by yeliew, lanusri-.*

## 1. Description

A-Maze-ing is a Python project that generates configurable perfect and imperfect mazes based on user-defined settings.

The generator supports custom dimensions, entry and exit positions, random seeds and a 42 pattern. It also provides a reusable `MazeGenerator` class that can be imported into other Python projects.

### Features
- Perfect maze generation using DFS with backtracking.
- Imperfect maze generation with additional routes.
- Custom maze dimensions, entry and exit positions.
- Reproducible generation using a random seed.
- 42 pattern integration.
- Reusable Python module and package distribution.

## 2. Instructions

### Requirements
- Python 3.10+
- pip

### Installation

```bash

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt
```

### Execution

```bash
python3 a_maze_ing.py config.txt
```

### Makefile Commands

| Command | Description |
|---|---|
| `make install` | Install project dependencies |
| `make run` | Run the program |
| `make debug` | Run the program in debug mode |
| `make clean` | Remove generated files |
| `make lint` | Run Flake8 and Mypy |
| `make lint-strict` | Run strict code checks |
| `make build` | Build the reusable package |

## 3. Configuration File

The program uses a `KEY=VALUE` configuration file.

### Example

```ini
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=False
SEED=42
```

### Parameters

| Parameter | Description |
|---|---|
| `WIDTH` | Maze width |
| `HEIGHT` | Maze height |
| `ENTRY` | Starting coordinates (`x,y`) |
| `EXIT` | Ending coordinates (`x,y`) |
| `OUTPUT_FILE` | Output file path |
| `PERFECT` | `True` for perfect, `False` for imperfect |
| `SEED` | Random seed for reproducible generation |

Blank lines and lines beginning with `#` are ignored. Dimensions and coordinates are validated before generation.

## 4. Maze Generation Algorithm

### Perfect Maze — DFS with Backtracking

The perfect maze uses Depth-First Search (DFS) with backtracking. Starting from a cell, the algorithm visits unvisited neighbours and removes the wall between connected cells. When no unvisited neighbours remain, it backtracks until all cells have been visited.

This algorithm was chosen because it is straightforward to implement, requires relatively simple data structures and naturally produces a connected maze with a unique path between any two cells.

### Imperfect Maze

The imperfect maze starts with a perfect maze. Additional walls are opened to create loops and alternative routes while respecting the maze constraints.

### Random Seed

A random seed controls the random choices made during generation. Using the same seed and configuration allows the same maze to be reproduced.

## 5. Reusable Code

The reusable component is located in `generate_maze.py`, which contains the standalone `MazeGenerator` class.

Other Python projects can import the class and create maze generators with custom dimensions and settings.

### Example

```python
from generate_maze import MazeGenerator

generator = MazeGenerator(
    width=20,
    height=15,
    entry=(0, 0),
    exit=(19, 14),
    perfect=True,
    seed=42
)
```
# Generate the maze
if generator.perfect:
    maze = generator.generate_perfect_maze()
else:
    maze = generator.generate_imperfect_maze()

The maze is generated using the MazeGenerator class. 
It provides two methods: generate_perfect_maze() and generate_imperfect_maze(). 
The generated maze is returned as a 2D list and can be accessed through the maze variable. 
Each cell contains four directional walls (North, East, South and West), 
where 1 represents a closed wall and 0 represents an open wall.
The module is packaged as `mazegen` and distributed in both `.tar.gz` and `.whl` formats. It is released under the MIT License to permit reuse and distribution in other projects.

## 6. Teamwork and Project Management

### 6.1 Division of Responsibilities

The project was divided between two team members according to the main components of the application.

| Component | yeliew | lanusri- |
|---|---|---|
| Perfect maze generation | ✓ | |
| Imperfect maze generation | ✓ | |
| DFS and backtracking | ✓ | |
| Maze structure and wall management | ✓ | |
| 42 pattern generation | ✓ | |
| Configuration reading and validation | ✓ | |
| Reusable `MazeGenerator` class | ✓ | |
| Python package and distribution | ✓ | |
| Hexadecimal output format | | ✓ |
| Output file generation | | ✓ |
| Maze visualisation | | ✓ |
| User interaction | | ✓ |
| Integration and final testing | ✓ | ✓ |

### 6.2 Project Planning

The initial plan was to divide the project into maze generation and maze presentation. Each member would develop their assigned components before integrating them into the main application.

The development process took longer than initially expected due to debugging,
refining the maze generation logic, and integrating both parts of the project. 
Yeliew part required additional testing, especially for handling dead ends, 
opening extra paths in imperfect mazes, and ensuring the 42 pattern did not 
interfere with maze generation.

Lanusri- also needed time to implement and refine the hexadecimal output format, 
maze visualisation, and user interaction. 
Some adjustments were made along the way as issues were 
discovered during integration and testing. 

Overall, more time was spent debugging and ensuring both parts worked together 
correctly than originally planned.

### 6.3 What Worked Well

- Dividing responsibilities allowed both members to work on separate components.
- Separating maze generation into its own module improved code organisation and reusability.
- Testing individual components helped identify issues during development.

### 6.4 What Could Be Improved

- Earlier integration could reduce compatibility issues between components.
- More time could be allocated for testing edge cases and larger mazes.
- Clearer initial planning could help manage development time.

### 6.5 Tools Used

| Tool | Purpose |
|---|---|
| Flake8 | Code style checking |
| Mypy | Static type checking |
| pip | Dependency management |
| Python Build | Package distribution |

## 7. Resources

### Documentation
- [Python Documentation](https://docs.python.org/3/)
- [Python Random Module](https://docs.python.org/3/library/random.html)
- [Python Typing Documentation](https://docs.python.org/3/library/typing.html)
- [Python Packaging Guide](https://packaging.python.org/)
- [License.md template](https://github.com/spatie/temporary-directory/blob/main/LICENSE.md)

### AI Usage

ChatGPT was used as a learning and development assistant throughout the project.

It helped with:
- Understanding Python concepts, classes and data structures.
- Learning DFS and backtracking.
- Discussing maze generation approaches and constraints.
- Understanding type annotations and resolving Flake8 and Mypy errors.
- Debugging unexpected behaviour and exploring possible solutions.
- Understanding Python packaging and reusable modules.
- Organising project documentation.

AI suggestions were reviewed and tested before being incorporated into the project.
