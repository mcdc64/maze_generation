# maze_generation
A set of programs that generate mazes using Prim's Algorithm.
Tested with Python 3.7.3, but any version of Python 3 should work.

Requires matplotlib and numpy Python modules.

To generate a maze, run maze_gen.py or maze_gen_opt.py.
maze_gen.py uses a direct implementation of Prim's algorithm, that is not very efficient, to generate a maze.
maze_gen_opt.py uses an optimised version of this algorithm which takes advantage of the square grid structure of the maze points.

To generate a maze of different height and width, change the "xwidth" and "ywidth" variables at the beginning of the programs.

To compare the times to generate mazes, run each program a few times for different maze sizes. The data points will be output to
text files. Running graph.py will use the data in those files and output a graph. The graphing assumes the mazes are square (that
the height equals the width), since the "maze size" is actually the width of the maze.
