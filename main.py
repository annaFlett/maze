import matplotlib.patches
import numpy as np
import matplotlib.pyplot as plt
import png

from classes import maze_reader,maze_solver

#basic setup, convert the png to numpy array of 1s and 0s. Also finds start + end points of the maze
reader = maze_reader()
maze,maze_width,maze_height = reader.maze,reader.maze_width,reader.maze_height
copy_maze = maze.copy()
start,end = reader.find_start_and_end()

# setup the arrays to encode the maze + its nodes
def make_node_array(start, end):
    for i in range(maze_height):
        for j in range(maze_width):
            check = [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)] ## right, left, up ,down
            if (i, j) == start or (i, j) == end:
                copy_maze[i][j] = -3

            for x, y in check:
                try:
                    if maze[x][y] == 0 and maze[i][j] == 0:
                        copy_maze[x][y] -= 1
                except IndexError:
                    pass


def algorithm_setup():
    make_node_array(start, end)
    # checks for nodes hit lots of time (nodes), and sets up a boolean array
    node_maze = np.vectorize(lambda s: s <= -3)(copy_maze)
    # checks for any tile which can be walked on
    used_maze = np.vectorize(lambda s: s < 1)(copy_maze)
    return (copy_maze, node_maze, used_maze, start, end)


maze_info = algorithm_setup()
fig, ax = plt.subplots()
ax.axis('off')

for i in range(maze_height):
    for j in range(maze_width):
        if maze[i][j] == 1:
            # j and i swapped + -1, so that the grid is in the right orientation
            rect = matplotlib.patches.Rectangle((j, -i), 1, 1, color="k")
            ax.add_patch(rect)

solver = maze_solver(maze_info,ax)
travelled_to = solver.solve()

## Draw out the solved maze
p =[[]] * len(reader.pixel_array)
for idx,j in enumerate(reader.pixel_array):
    for x in range(len(j)):
        if x % 4 != 3:
            p[idx].append(j[x])

for pair in travelled_to:
    p[pair[0]][pair[1]*3],p[pair[0]][pair[1]*3 + 1],p[pair[0]][pair[1]*3 + 2] = 52, 204, 235
w = png.Writer(maze_width,maze_height,greyscale=False)
f = open("solvedmaze.png","wb")
w.write(f,p)

