import png
import numpy as np
import matplotlib.pyplot as plt
import random

class maze_reader():

    def __init__(self):
        r = png.Reader(filename="maze (3).png")
        self.maze_width, self.maze_height, pixel, extra = r.read()
        self.maze = np.ndarray([self.maze_width, self.maze_height])
        self.pixel_array = (np.array(list(pixel)))
        self.convert_to_array()

    def convert_to_array(self):
        for idx, item in enumerate(self.pixel_array):
                for idx2, x in enumerate(range(0, self.maze_width * 4, 4)):
                    if item[x] == 0:
                        self.maze[idx][idx2] = 1
                    else:
                        self.maze[idx][idx2] = 0

    def find_start_and_end(self):
        for x in range(self.maze_height):
            if self.maze[x][0] == 0:
                start = (x, 0)

            if self.maze[x][self.maze_width - 1] == 0:
                end = (x, self.maze_width - 1)

        return start, end
    


class maze_solver():

    def __init__(self,mazes,ax):
        self.mazes = mazes
        self.node_maze, self.used_maze, = self.mazes[1], self.mazes[2]
        self.current, self.end = self.mazes[3], self.mazes[4]
        self.nodes, self.travelled_to = [], [self.current]
        self.fails, self.ax = 0 , ax

    def solve(self):
        while self.current != self.end:
            self.moved = False
            self.map_maze()
            self.movement()
        self.check_end()
        self.map()
        return self.travelled_to


    def map_maze(self):
        checks = ((self.current[0]+1,self.current[1]),(self.current[0],self.current[1]+1),(self.current[0],self.current[1]-1),(self.current[0]-1,self.current[1]))
        colour = (random.random(), random.random(), random.random())
        self.ax.scatter(self.current[1] +0.5,-(self.current[0] - 0.5), color=colour)

        if self.node_maze[self.current[0]][self.current[1]] == True and (self.current[0], self.current[1]) not in self.nodes:
            self.nodes.append((self.current[0], self.current[1]))
        for x,y in checks:
            try:
                if self.used_maze[x][y] == True and self.moved == False:
                    self.used_maze[self.current[0]][self.current[1]] = False
                    self.current, self.moved = (x, y), True
            except IndexError:
                pass

    def movement(self):
        if self.moved == False:
            self.used_maze[self.current[0]][self.current[1]] = False
            self.fails += 1
            if self.fails > 3:
                self.current = self.nodes[-self.fails + 2]
            else:
                self.current = self.nodes[-1]
        else:
            self.fails = 0
        self.travelled_to.append((self.current[0], self.current[1]))

    def check_end(self):
        for x in range(len(self.travelled_to)):
            for x in range(len(self.travelled_to)):
                try:
                    end_idx = self.travelled_to.index(self.travelled_to[x], x + 1)
                except ValueError:
                    pass
                else:
                    del self.travelled_to[x:end_idx]
                    break


    def map(self):
        x = [-1*(item[0] - 0.5) for item in self.travelled_to]
        y = [item[1] + 0.5 for item in self.travelled_to]
        plt.plot(y,x, color="b", lw=4)
        plt.scatter(y,x, color="k")

        plt.savefig("process.png")
        plt.show()
    

