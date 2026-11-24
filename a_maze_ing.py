from config import read_config, convert_config, error_handling
from generate_maze import MazeGenerator

import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        return
    try:
        config = read_config(sys.argv[1])
        convert_config(config)
        error_handling(config)
    except (ValueError, KeyError) as e:
        print("Configuration error:", e)
        return

    print("=== Generating Maze ===")
    try:
        if config["PERFECT"]:
            maze = generate_perfect_maze(
                config["WIDTH"],
                config["HEIGHT"],
                config["ENTRY"],
                config["EXIT"],
                seed=config["SEED"]
            )
        else:
            maze = generate_imperfect_maze(
                config["WIDTH"],
                config["HEIGHT"],
                config["ENTRY"],
                config["EXIT"],
                seed=config["SEED"]
            )
        print_maze(maze, config["WIDTH"], config["HEIGHT"])
    except ValueError as e:
        print("Generation error:", e)

    print("=== A-Maze-Ing ===")
    print("1. Re-generate a new maze")
    print("2. Show / Hide the shortest path")
    print("3. Rotate wall colors")
    print("4. Quit")

    while True:
        try:
            answer = int(input("Choice? (1-4): "))

            if (answer < 1 or answer > 4):
                print("Please enter a number 1-4: ")
                continue
            break
        except ValueError:
            print("Please enter a number: ")

    if answer == 1:
        print("=== Regenerating New Maze ===")
    elif answer == 2:
        print("=== Show / Hide Shortest Path ===")
    elif answer == 3:
        print("=== Rotate Wall Colors ===")
    elif answer == 4:
        print("=== Quit ===")
        return

if __name__ == "__main__":
    main()
