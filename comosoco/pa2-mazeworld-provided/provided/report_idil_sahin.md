Idil Sahin, COSC 76
PS2 - MazeWorld
18 Oct 24

# Code Description 🎉️ 

## MazeworldProblem.py



The main function of this class is the `get_successors()` function: every state is represented as a tuple where the first element `state[0]` identifies which robot to move, and the subsequent pairs of elements represent different robots' x-y coordinates. It generates potential moves in the north, south, east, west directions, as well as the option to stay put based on which robot's turn it is and its coordinates.

The helper function `filter_successors()` processes these moves to ensure they are legal through checking two conditions: whether `self.maze.is_floor()` returns true, and ensuring that there are no collisions with another robots using the `is_collision()` helper function. This function is similar to `has_robot()` from `Maze.py`, but it doesn't require updating the maze before checking, implemented for debugging reasons. As the output `get_successors()` returns a list of legal successor states.`manhattan_heuristic()` to compute Manhattan distances and `get_transition_cost()` to calculate the cost of transitions between states also exist as helper functions in this file as functions of the mazeworldproblem class.


## SensorlessProblem.py

Recall that we are trying to effectively infer the real location of the robot among all possible options - thus all_states is simply what is given by is_floor() over all possible states. We iterate over all successor states similar to mazeworld problem and add them the same procedure as A*, following two different heuristics. I implemented the heuristic on how they infuence the potential event space (higher priority lower successors) -- this is explained in more detail in the following section. Subsequently the code terminates when we get a single state, where goal_test() returns true.

## Heuristic

I used the manhattan distance heuristic, calculated as the absolute value of all coordinate differences between the current and the goal state for the mazeworld problem.

I implemented and tested two heuristics for the blind robot problem set, upon discussion with my friend Lisa Samoylov and Yawen Xue, eliminate_four() and halve_successors() to order potential successor states.

## astar_search.py

A* search processes the priority queue through repeatedly removing the node with the lowest priority, then explores its successors (from `get_successors()` in Mazeworld.py), calculates their costs, and updates the `visited_cost` dictionary to ensure their priorities are accurately represented. Once the goal is reached, it returns a `SearchSolution` with the path and relevant details

# Testing 👀️

## test_mazeworld.py, test_sensorless.py 

I tested this with mazes of different sizes as provided in the folder. This was useful for debugging, especially using the small maze (maze 2). Manhattan distance worked better than the null heuristic, and eliminate_four() and halve_successors() had similar results.

# Discussion Questions 🚀️ 

#### **1.** If there are k robots, how would you represent the state of the system? Hint – how many numbers are needed to exactly reconstruct the locations of all the robots, if we somehow forgot where all of the robots were? Further hint. Do you need to know anything else to determine exactly what actions are available from this state?

Similar to the original example, I would use a uple of size 2k+1. The first element would indicate which robot's turn it would be.

#### **2.** Give an upper bound on the number of states in the system, in terms of n and k.

Assuming n is the size of the maze (that is, number of squares), upper bound is k*(n^k) -- there are k possibilities for which robot's turn it is to move, and n^k possibilities for the number of occupied coordinates. This is an overestimate as it's more rigorously (n^k)((n-1)^k)((n-2)^k)... and so on, as the possible square for each robot to occupy decrements by 1.

#### **3.** Give a rough estimate on how many of these states represent collisions if the number of wall squares is w, and n is much larger than k.

Note that this gives us n-w floor spaces and k robots. All states, regardless of collisions is (n-w-1+k)!/(n-w-1)!(k)! = C(n-w-1+k, k) (balls and sticks combinatorics problem), subtracting the ones that do not have any collusions: C(n-w-1+k, k) - P(n-w, k).

#### **4.** If there are not many walls, n is large (say 100x100), and several robots (say 10), do you expect a straightforwards breadth-first search on the state space to be computationally feasible for all start and goal pairs? Why or why not?

This would not be feasible as BFS would take a lot of memory.

#### **5.** Describe a useful, monotonic heuristic function for this search space. Show that your heuristic is monotonic. See the textbook for a formal definition of monotonic.

The Manhattan distance is a reliable monotonic heuristic given it consistently underestimates costs: note that it is monotonic as the distance (|x-x'| + |y-y'|) either increases or stays the same along the path, given both these quantities are lengths and by definiton, non-negative. More rigourously, h(n) is always less than or equal to g(n') + c(n, n') + h(n') where h(n') is the successor. 


# Acknowledgements

Discussion with friends Yawen Xue and Lisa Samoylov, https://trevorstandley.com/papers/Standley_AAAI10.pdf this paper for pathfinding problems and heuristic inspiration.
