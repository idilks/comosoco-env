# Author: @idil_sahin; scaffold provided by CS76 faculty
# Date: 11 oct 2024
# Purpose: CS76 Lab defining the Mazeworld problem class 

from Maze import Maze
from time import sleep

class MazeworldProblem:
    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        self.start_state = tuple([0] + maze.robotloc)
        self.num_robots = len(maze.robotloc) / 2

    def __str__(self):
        return "Mazeworld problem: "
        
        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)


    def get_successors(self, state):
        successors = []

        # determine indices of the current robot's state to modify
        ix = 2 * state[0] + 1    # x-coordinate for the current robot
        iy = 2 * state[0] + 2    # y-coordinate for the current robot

        north = list(state)
        north[iy] += 1
        south = list(state)
        south[iy] -= 1
        east = list(state)
        east[ix] += 1
        west = list(state)
        west[ix] -= 1
        successors += [north, south, east, west]
        successors = self.filter_successors(successors, ix, iy)

        # recall that the robot could always choose to not move
        stay_put = list(state)
        stay_put[0] = int((stay_put[0] + 1) % self.num_robots)
        stay_put = tuple(stay_put)

        return successors + [stay_put]

    # helper function to filter successors by legality
    def filter_successors(self, successors, ix, iy):
        valid_successors = []

        for successor in successors:
            x = successor[ix]
            y = successor[iy]

            if self.maze.is_floor(x, y):
                if not self.is_collision(successor, ix, iy):
                    successor[0] = int((successor[0] + 1) % self.num_robots)

                    # convert back to tuple and add to valid successors
                    valid_successors.append(tuple(successor))

        return valid_successors

    # helper function to check for collisions between robots, similar to has_robot but does not modify states
    def is_collision(self, successor, ix, iy):
        x = successor[ix]
        y = successor[iy]

        robot_positions = successor[1:ix] + successor[iy + 1:]

        for i in range(0, len(robot_positions), 2):
            if robot_positions[i] == x and robot_positions[i + 1] == y:
                return True

        return False

    # helper function to check if the current state meets the goal
    def goal_test(self, state):
        return state[1:] == self.goal_locations

    # manhattan distance heuristic
    def manhattan_heuristic(self, state):
        dist = 0
        state = state[1:]
        for i in range(len(self.goal_locations)):
            dist += abs(self.goal_locations[i] - state[i])

        return dist

    # Calculate the transition cost for A* search
    def get_transition_cost(self, next_state, curr_state):
        # Return 1 if the robot has moved
        if next_state[1:] != curr_state[1:]:
            return 1
        # Return 0 if the robot stayed in place
        return 0

    # Animate the path by resetting the robot locations and printing the maze
    def animate_path(self, path):
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test.py code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((1, 1, 1, 2, 1, 3, 1, 4)))
