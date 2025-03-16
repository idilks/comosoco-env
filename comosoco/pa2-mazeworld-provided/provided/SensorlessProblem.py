# author: @idil sahin; scaffolding by cs76 faculty
# date: 17 oct. 24
# purpose: cs76 lab mazeworld problem class

from Maze import Maze
from time import sleep

class SensorlessProblem:

    ## You write the good stuff here:
    def __init__(self, maze):
        self.maze = maze
        self.start_state = tuple(self.all_belief_states())
        self.num_robots = 1

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))
    
    def all_belief_states(self):
        all_beliefs_list = []
        
        for x in range(0, self.maze.width):
            for y in range(0, self.maze.height):
                if self.maze.is_floor(x, y):
                    all_beliefs_list.append(x)
                    all_beliefs_list.append(y)

        return all_beliefs_list

    def __str__(self):
        string =  "Blind robot problem: "
        return string
        
    # given a sequence of states (including robot turn), modify the maze and print it out.
    #  (Be careful, this does modify the maze!)
    
    def get_successors(self, state):
        successors = []
        visited_beliefs = set()  # Keep track of visited positions

        # possible movement directions: north, south, east, west
        directions = [
            [0, 1],   # north
            [0, -1],  # south
            [1, 0],   # east
            [-1, 0]   # west
        ]

        # check each direction and get potential successors
        for dx, dy in directions:
            self.update_successors(successors, state, dx, dy, visited_beliefs)

        return successors
        
    
    def update_successors(self, successors, state, dx, dy, visited_beliefs):
        updated_beliefs = []

        for i in range(0, len(state), 2):
            current_belief = [state[i], state[i + 1]]  # (x, y)

            # calculate the next position after moving in the given direction
            next_belief = [current_belief[0] + dx, current_belief[1] + dy]

            # if the next position is valid (robot can move there)
            if self.maze.is_floor(next_belief[0], next_belief[1]):
                if tuple(next_belief) not in visited_beliefs:
                    updated_beliefs.append(next_belief[0]) 
                    updated_beliefs.append(next_belief[1])
                      # add the new position to updated beliefs
                    visited_beliefs.add(tuple(next_belief))  # mark as visited
            
            # if the next position is invalid, retain the current belief
            elif tuple(current_belief) not in visited_beliefs:
                updated_beliefs.append(current_belief[0]) 
                updated_beliefs.append(current_belief[1])  #keep current position
                visited_beliefs.add(tuple(current_belief))  # mark as visited

        # in case there are changes add the updated beliefs to successors
        if updated_beliefs:
            successors.append(tuple(updated_beliefs))


    def goal_test(self, curr_belief_states):
        if len(curr_belief_states) == 2:
            return True
        else: 
            return False

    # heuristic functions
    def eliminate_four(self, successors):
        return max(len(successors) - 4, 0)  # ensure non-negative

    def halve_successors(self, successors):
        return len(successors) // 2  # use integer division

    # calculate transition cost for search function
    def get_transition_cost(self, next_state, curr_state):
        return 1

    


## A bit of test code

if __name__ == "__main__":

    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
    initial_state = (0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4)
    print(test_problem.get_successors(initial_state))
