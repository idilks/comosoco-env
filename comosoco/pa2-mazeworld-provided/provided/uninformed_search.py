#author: @idil_sahin; scaffolding by cs76 faculty
#date: 03 oct 2024
#purpose: cs76 lab fox problem class

from collections import deque
from SearchSolution import SearchSolution
from collections import deque  # importing deque


# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        self.parent = parent
        self.state = state
        # you write this part


# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions


def bfs_search(search_problem):
    
    # initialization of our variables
    start_state = search_problem.start_state
    start_node = SearchNode(start_state)
    solution = SearchSolution(search_problem, "BFS")
    frontier = deque([start_node])

    # initialize a set to keep track of explored states // memoizing
    explored = set()
    explored.add(start_state)


    # continue the search until the frontier is empty or goal is found
    while frontier:
        
        # pop from left (front of the frontier)
        current_node = frontier.popleft()
        current_state = current_node.state
        solution.nodes_visited += 1

        # check if the current state matches the goal state
        if search_problem.goal_test(current_state):
            # if so, backchain and re-create the path
            solution.path = backchain(current_node, start_node)
            solution.path.reverse() # reverse path for consistency 

            return solution

        else:
            # get successor states for the current state
            successors = search_problem.get_successors(current_state)

            # iterate over successor states
            for next_state in successors:
                
                if next_state not in explored:
                    explored.add(next_state) # this helps us get rid of duplicate states more quickly
                    # create a new node for each unexplored successor state and add it to the frontier
                    frontier.append(SearchNode(next_state, current_node))

    return solution




def backchain(current_node, start_node):
    backlist = [current_node.state] ## keeping track of states


    while current_node.state != start_node.state:
        current_node = current_node.parent
        backlist.append(current_node.state)

    return backlist


# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded

def dfs_search(search_problem, depth_limit=100, node=None, solution=None):

    # initialize variables
    if node is None:
        node = SearchNode(search_problem.start_state)  
        solution = SearchSolution(search_problem, "DFS")  
        search_problem.solved = False # Global variable indicating whether the solution is found


    current_state = node.state  # Get the current state from the search node
    solution.nodes_visited += 1  # Increment the count of visited nodes
    solution.path.append(current_state)  # Add the current state to the solution's path


    # check if the current state is the goal state
    if search_problem.goal_test(current_state):
        search_problem.solved = True  # mark the problem as solved -> globally we leave the loop thusly
        return solution  

    if len(solution.path) == 1 and solution.nodes_visited > 1:
        # print(solution)
        solution.path = []
        return solution

    # if there are successors and depth limit is not reached, cont searching 
    elif depth_limit > 0:
        successors = search_problem.get_successors(current_state)

        for next_state in successors:
            # path checking to prevent loops
            if next_state not in solution.path:
                next_node = SearchNode(next_state, node)  # Create a new search node for the next state
                # recursively explore the next state 
                curr = dfs_search(search_problem, depth_limit - 1, next_node, solution)
                if search_problem.solved:
                    return curr  # if the problem is solved, return the result to parent recursions. break out of recursion.
                else:
                    solution.path.pop()# remove the state from the path after it leads to a dead-end (the neighbors will be explored recursively). this keeps us keep track of the path and be efficent.

        if len(solution.path) == 1 and solution.nodes_visited > 1:
            # print(successors)
            solution.path.pop() # no solution found, reset the list
            return solution






def ids_search(search_problem, depth_limit=100):
    # perform (IDS) by gradually increasing the depth limit
    search_problem.solved = False

    for limit in range(depth_limit + 1):
        # initialize a Depth-First Search (DFS) with the current depth limit
        result = dfs_search(search_problem, limit)

        # if a solution is found (result is not None), stop searching and break out of the loop
        if result and len(result.path) != 0:
            break

    # return the result (either the solution or None if no solution was found within the depth limit)
    result.search_method = "IDS"  # Renaming the search method.
    return result


