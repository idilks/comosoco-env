# Author: @idil_sahin; scaffold provided by CS76 faculty
# Date: 11 oct 2024
# Purpose: testing for mazeworld problem

from MazeworldProblem import MazeworldProblem
from Maze import Maze

from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
# print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)
print(test_mp.animate_path(result.path))



# this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

# Your additional tests here:

# test_maze3 = Maze("maze3.maz")


# test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
# # test_mp4 = MazeworldProblem(test_maze4, (1, 4, 1, 3, 1, 2, 1, 1))


# # Your additional tests here:
# 1 robot, small maze


# test_maze2 = Maze("maze2.maz")
# test_mp2 = MazeworldProblem(test_maze2, (3, 1))
# print(astar_search(test_mp2, null_heuristic))
# print(astar_search(test_mp2, test_mp2.manhattan_heuristic))