# author: @idil_sahin; scaffolding by cs76 faculty
# date: 17 oct. 24
# purpose: cs76 lab sensorless problem testing



# You write this:

from SensorlessProblem import SensorlessProblem
from Maze import Maze

from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0



# Test problems
test_maze3 = Maze("maze3.maz")
test_maze2 = Maze("maze2.maz")
test_maze1 = Maze("maze1.maz")

test_mp = SensorlessProblem(test_maze3)
test_mp2 = SensorlessProblem(test_maze2)
test_mp1 = SensorlessProblem(test_maze1)




# default test problems, similar to test_mazeworld

# print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)
#test_mp.animate_path(result.path)

# this should do a bit better: (custom heuristic functions)
result = astar_search(test_mp, test_mp.eliminate_four)
print(result)






# print(astar_search(test_mp2, null_heuristic))
# print(astar_search(test_mp2, test_mp2.eliminate_four))
# print(astar_search(test_mp2, test_mp2.halve_successors))



# print(astar_search(test_mp1, null_heuristic))
# print(astar_search(test_mp1, test_mp1.eliminate_four))
# print(astar_search(test_mp1, test_mp1.halve_successors))