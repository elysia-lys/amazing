def main():
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
