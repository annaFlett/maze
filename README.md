# Maze Solver

Here you find a maze solver which takes in images (generated from https://keesiemeijer.github.io/maze-generator/#generate, wall size = 1) and is able to find a solution from the start on the left-hand side of the maze, over to the opening on the right hand side. The method in which is does this, is piecing together the main path by joining "nodes", which are cells with mulitple exits (so 3+ open sides). We then perform a depth first search, backtracking where necessary until the exit is found. The program then saves an image of the solved maze, as well as an image showing the working of the algorithms (the dots represent a tile on which the algorithm has stepped on at the some point). 

A few way I could take this project further is to make the reading in of the maze far more flexible so a wider variety of input images can be accepted, as at the moment the mazes need to be in a standard form. It would also be interested to explore some other algorithms for solving the mazes, and compare their performances in different scenarios. 

An example of a maze solved by the program:  
(blurry as I have enlarged the size of the png)

![solved maze](https://github.com/annaFlett/maze/blob/main/solvedMaze.png?raw=true)





The working to reach the solution: 

![working](https://github.com/annaFlett/maze/blob/main/process.png?raw=true)
