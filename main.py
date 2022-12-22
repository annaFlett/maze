import matplotlib.patches
import numpy as np
import matplotlib.pyplot as plt
import random
from collections import defaultdict


maze_width = 10
maze_height = 10
maze = np.array([[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
                 [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                 [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                 [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]])

copy_maze = maze.copy()
print(maze)


def find_start_and_end():
    for indx, tile in enumerate(maze[0]):
        if tile == 0:
            start = (0, indx)

    for indx, tile in enumerate(maze[-1]):
        if tile == 0:
            end = (maze_height - 1, indx)

    return start, end


def make_node_array(start, end):
    for i in range(maze_height):
        for j in range(maze_width):
            right = (i, j + 1)
            left = (i, j - 1)
            up = (i - 1, j)
            down = (i + 1, j)
            check = [right, left, up, down]
            if (i, j) == start or (i, j) == end:
                copy_maze[i][j] = -3

            for x, y in check:
                try:
                    if maze[x][y] == 0 and maze[i][j] == 0:
                        copy_maze[x][y] -= 1
                except IndexError:
                    pass


def algorithm_setup():
    start, end = find_start_and_end()
    make_node_array(start, end)
    # checks for nodes hit lots of time (nodes), and sets up a boolean array
    node_maze = np.vectorize(lambda s: s <= -3)(copy_maze)
    # checks for any tile which can be walked on
    used_maze = np.vectorize(lambda s: s < 1)(copy_maze)

    return (copy_maze, node_maze, used_maze, start, end)


mazes = algorithm_setup()
fig, ax = plt.subplots()
for i in range(maze_height):
    for j in range(maze_width):
        if maze[i][j] == 1:
            rect = matplotlib.patches.Rectangle((i, j), 1, 1, color="k")
            ax.add_patch(rect)


def move(mazes):
    node_maze, used_maze, = mazes[1], mazes[2]
    current, end = mazes[3], mazes[4]
    nodes, travelled_to = [], [current]
    fails = 0
    print(current, end)
    while current != end:
        colour = (random.random(), random.random(), random.random())
        ax.scatter(current[0] + 0.5,current[1] +0.5, color=colour)
        print(used_maze, current, nodes)
        if node_maze[current[0]][current[1]] == True and (current[0], current[1]) not in nodes:
            print("adding node")
            nodes.append((current[0], current[1]))
        moved = False
        print("running check")
        try:
            if used_maze[current[0] + 1][current[1]] == True and moved == False:
                used_maze[current[0]][current[1]] = False
                current = (current[0] + 1, current[1])
                print("moved_down")
                moved = True
            else:
                print("failed")
        except IndexError:
            pass
        try:
            if used_maze[current[0]][current[1] + 1] == True and moved == False:
                used_maze[current[0]][current[1]] = False
                current = (current[0], current[1] + 1)
                moved = True
                print("moved_right")
            else:
                print("hello", used_maze[current[0]][current[1] + 1], moved)
        except IndexError:
            pass
        try:
            if used_maze[current[0]][current[1] - 1] == True and moved == False:
                used_maze[current[0]][current[1]] = False
                current = (current[0], current[1] - 1)
                moved = True
                print("moved_left")
        except IndexError:
            pass
        try:
            if used_maze[current[0] - 1][current[1]] == True and moved == False:
                used_maze[current[0]][current[1]] = False
                current = (current[0] - 1, current[1])
                moved = True
                print("moved_up")
        except IndexError:
            pass
        if moved == False:
            used_maze[current[0]][current[1]] = False
            fails += 1
            if fails > 3:
                current = nodes[-fails + 2]
                travelled_to.append((current[0], current[1]))
            else:
                current = nodes[-1]
                travelled_to.append((current[0], current[1]))
        else:
            fails = 0
            travelled_to.append((current[0], current[1]))
            print("end")
        print("end2")
    print("done", current)
    print(travelled_to)

    for x in range(len(travelled_to)):
        for x in range(len(travelled_to)):
            try:
                end_idx = travelled_to.index(travelled_to[x], x + 1)
            except ValueError:
                pass
            else:
                del travelled_to[x:end_idx]
                break

    print(travelled_to)

    x = [item[0] + 0.5 for item in travelled_to]
    y = [item[1] + 0.5 for item in travelled_to]
    plt.plot(x, y, color="b", lw=4)
    plt.scatter(x, y, color="k")

    plt.show()


move(mazes)
