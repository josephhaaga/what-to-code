WALL = 1
SPACE = 0

HORIZONTAL_WALL = "*" # "="
VERTICAL_WALL = "*" # "|"

simple_maze = [
    [WALL, WALL, SPACE, WALL],
    [WALL, SPACE, SPACE, WALL],
    [WALL, SPACE, WALL, WALL],
]

larger_maze = [
    [WALL, WALL, WALL, WALL, WALL, SPACE, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL, SPACE, SPACE, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, SPACE, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, SPACE, WALL],
    [WALL, WALL, WALL, WALL, WALL, SPACE, SPACE, WALL],
    [WALL, WALL, WALL, WALL, WALL, SPACE, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL, SPACE, WALL, WALL],
]

def print_maze(maze):
    for i in maze[0]:
        if i == WALL:
            print(HORIZONTAL_WALL, end='')
        else:
            print(" ", end='')
    print()
    for row in maze[1:-1]:
        for col in row:
            if col == WALL:
                print(VERTICAL_WALL, end='')
            else:
                print(" ", end='')
        print()
    for i in maze[-1]:
        if i == WALL:
            print(HORIZONTAL_WALL, end='')
        else:
            print(" ", end='')
    print()

print_maze(larger_maze)
