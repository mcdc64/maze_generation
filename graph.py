'''
Cian McDonnell 2020
This reads the files generated by maze_gen and maze_gen_opt and outputs a graph that compares the time taken for the different programs to generate mazes of different sizes.

To see the comparison, run the other two programs for different maze sizes (works best for square mazes). Every time they are run, they will add the time taken to generate a maze of a certain size.
After running those programs a suitable number of times, run graph.py and it will plot the data. A scatter plot is used by default because that way the maze sizes don't need to be in the right order for the plot
to work, but this can of course be changed.
'''
import matplotlib.pyplot as plt
import numpy as np
file = open("times.txt",'r')
times_text = file.readlines()
times = []
sizes = []
for line in times_text:
    line_list = line.split(",")
    sizes.append(float(line_list[0]))
    times.append(float(line_list[1]))

plt.scatter(sizes,times,label="Unoptimised Algorithm")
plt.xlabel("Maze Size")
plt.ylabel("Generation Time / s")

file2 = open("opt_times.txt",'r')
opt_times_text = file2.readlines()
times_2 = []
sizes_2 = []
for line in opt_times_text:
    line_list = line.split(",")
    sizes_2.append(float(line_list[0]))
    times_2.append(float(line_list[1]))

plt.xlim(10,34)
plt.scatter(sizes_2,times_2,color="#e36172",label="Optimised Algorithm")
plt.legend(loc="best")
plt.show()