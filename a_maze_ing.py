from config import read_config, convert_config, error_handling
from generate_maze import generate_perfect_maze, generate_imperfect_maze, print_maze


def main():
    try:
        config = read_config("config.txt")
        convert_config(config)
        error_handling(config)
    except (ValueError, KeyError) as e:
        print("Configuration error:", e)
        return

    print("=== Welcome to A-Maze-Ing===")
    print("Please Select A Mode:")

    choice = int(
            input(
                "1. Generate Maze\n"
                "2. Slove Maze\n"
                "3. Display Maze\n"
                "4. Save Maze To File\n"
                "Please Select 1 to 5\n"
                )
            )
    if choice == 1:
        print("=== Generating Maze ===")
        try:
            if config["PERFECT"]:
                maze = generate_perfect_maze(
                    config["WIDTH"],
                    config["HEIGHT"],
                    config["ENTRY"],
                    config["EXIT"]
                )
            else:
                maze = generate_imperfect_maze(
                    config["WIDTH"],
                    config["HEIGHT"],
                    config["ENTRY"],
                    config["EXIT"]
                )
            print_maze(maze, config["WIDTH"], config["HEIGHT"])
        except ValueError as e:
            print("Generation error:", e)

    elif choice == 2:
        print("=== Solving Maze ===")
    elif choice == 3:
        print("=== Displaying Maze ===")
    elif choice == 4:
        print("=== Saving Maze to file ===")
    else:
        print("uhoh wrong choice")


if __name__ == "__main__":
    main()
