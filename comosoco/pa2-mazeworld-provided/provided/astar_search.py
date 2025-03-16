# Author: @idil_sahin; scaffold provided by CS76 faculty
# Date: 10 oct 2024
# Purpose: CS76 Lab implementing A* search algorithm

from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
    # recall that each search node (except the root) has a parent node and all search nodes encapsulate a state object but are not the states themselves

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.state = state
        self.heuristic = heuristic  # h(n) heuristic function
        self.parent = parent
        self.transition_cost = transition_cost  # g(n) transition custs

    def priority(self):
        # f(n) = h(n) + g(n)
        return self.heuristic + self.transition_cost

    # comparison operator for heapq functions to work with AstarNode objects // we can simply pass it along in comparision. magic function
    def __lt__(self, other):
        return self.priority() < other.priority()

# follows parent nodes backwards to the root, collecting states and reverses the list of states to construct the final path
def backchain(node):
    path = []
    current = node
    while current:
        path.append(current.state)
        current = current.parent
    path.reverse()
    return path

def astar_search(search_problem, heuristic_fn):
    # create initial node, add it to queue
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "A* with heuristic " + heuristic_fn.__name__)

    # tracks the lowest known cost to reach each visited state through the heuristic
    visited_cost = {start_node.state: 0}

    # continue while there are nodes to process in the priority queue
    while pqueue:

        # get the node with the lowest priority
        curr_node = heappop(pqueue)
        solution.nodes_visited += 1

        # if goal is reached, backchain to find the solution path
        if search_problem.goal_test(curr_node.state):
            solution.cost = curr_node.transition_cost
            solution.path = backchain(curr_node)
            return solution

        # update visited cost for the current node
        visited_cost[curr_node.state] = curr_node.transition_cost

        # explore each successor of the current node
        for next_state in search_problem.get_successors(curr_node.state):

            # xalculate the new transition cost for the successor
            next_transition_cost = curr_node.transition_cost + search_problem.get_transition_cost(next_state, curr_node.state)
            next_node = AstarNode(next_state, heuristic_fn(next_state), parent=curr_node, transition_cost=next_transition_cost)

            # if successor has not been visited or found with a cheaper cost add it to the queue
            if next_state not in visited_cost or next_transition_cost < visited_cost[next_state]:
                visited_cost[next_state] = next_transition_cost
                heappush(pqueue, next_node)

    return solution
