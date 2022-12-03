# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
"""
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # """
    "*** YOUR CODE HERE ***"
    closed = []  # list to keep track of expanded nodes
    frindge = util.Stack()  # stack with each element a {"node":"path to node"}
    # frindge1=[]
    frindge.push((problem.getStartState(), []))  # pushing start to stack
    # frindge1.append(problem.getStartState)
    while (frindge.isEmpty() is False):  # loop until stack is empty
        # print ("frindge: ",frindge.list)
        node, actions = frindge.pop()  # Setting node and path
        # frindge1.pop()
        # print ("node: ",node, actions, problem.getSuccessors(node))
        if (problem.isGoalState(node)): return actions  # checking if goal is reached
        if (node not in closed):
            closed.append(node)  # adding node to closed set
            # print("closed2: ", closed)
            for next, action, cost in problem.getSuccessors(node):
                # for loop to visit all next states after expanding the node
                # if(next not in frindge1):
                #     frindge1.append(next)
                # if actions is not None:
                # print("hello: ",next, actions+[action])
                frindge.push((next, actions + [action]))  # adding node and path to frindge
                # else:
                #     # print("hello1: ",next, [action])
                #     frindge.push((next, [action])) # adding node and path to frindge
    else:
        return
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    closed = []  # list to keep track of expanded nodes
    frindge = util.Queue()  # queue with each element a {"node":"path to node"}
    # frindge1=[problem.getStartState()] #it is used to check if the same node exsits in open set
    frindge.push((problem.getStartState(), []))  # pushing start to queue
    # frindge1.append(problem.getStartState)
    while (frindge.isEmpty() is False):  # loop until queue is empty
        # print ("frindge: ",frindge.list)
        node, actions = frindge.pop()  # Setting node and path
        # frindge1.remove(node)
        # print ("node: ",node, actions, problem.getSuccessors(node))
        if (problem.isGoalState(node)): return actions  # checking if goal is reached
        if (node not in closed):
            closed.append(node)  # adding node to closed set
            # print("closed2: ", closed)
            for next, action, cost in problem.getSuccessors(node):
                # for loop to visit all next states after expanding the node
                # if(next not in frindge1):
                #     frindge1.append(next)
                # if actions is not None:
                # print("hello: ",next, actions+[action])
                frindge.push((next, actions + [action]))  # adding node and path to frindge
                # else:
                #     # print("hello1: ",next, [action])
                #     frindge.push((next, [action]))  # adding node and path to frindge
    else:
        return
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    closed = []  # list to keep track of expanded nodes
    frindge = util.PriorityQueue()  # prioriy queue with each element a {"node":"path to node"} with priority defined by cost
    # frindge1=[] it is used to check if the same node exsits in open set
    frindge.push((problem.getStartState(), []), 0)  # pushing start to queue
    # frindge1.append(problem.getStartState)
    costs = {problem.getStartState(): 0}  # dictionary to store costs to get to each node
    while (frindge.isEmpty() is False):  # loop until queue is empty
        # print ("frindge: ",frindge.heap, costs)
        node, actions = frindge.pop()  # Setting node and path
        # frindge1.pop()
        # print ("node: ",node, actions, problem.getSuccessors(node))
        if (problem.isGoalState(node)): return actions  # checking if goal is reached
        if (node not in closed):
            closed.append(node)  # adding node to closed set
            # print("closed2: ", closed)
            for next, action, cost in problem.getSuccessors(node):
                # for loop to visit all next states after expanding the node
                # if(next not in frindge1):
                #     frindge1.append(next)
                dist = costs[node] + cost  # updating the cost to reach to that particular node
                costs[next] = dist  # updating the costs dictionary with child nodes
                # if actions is not None:
                # print("hello: ",next, actions+[action])
                frindge.push((next, actions + [action]), dist)  # adding node and path to frindge
                # else:
                #     # print("hello1: ",next, [action])
                #     frindge.push((next, [action]),dist)  # adding node and path to frindge
    else:
        return
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    closed = []  # list to keep track of expanded nodes
    frindge = util.PriorityQueue()  # prioriy queue with each element a {"node":"path to node"} with priority defined by cost + heurisitc
    # frindge1=[] it is used to check if the same node exsits in open set
    frindge.push((problem.getStartState(), []),
                 heuristic(problem.getStartState(), problem))  # pushing start to queue
    # frindge1.append(problem.getStartState)
    # costs = {problem.getStartState(): 0}  # dictionary to store costs to get to each node
    while (frindge.isEmpty() is False):  # loop until queue is empty
        # print ("frindge: ",frindge.heap, costs)
        node, actions = frindge.pop()  # Setting node and path
        # print ("node: ",node, actions, problem.getSuccessors(node))
        if (problem.isGoalState(node)): return actions  # checking if goal is reached
        if (node not in closed):
            closed.append(node)  # adding node to closed set
            # print("closed2: ", closed)
            for next, action, cost in problem.getSuccessors(node):
                # for loop to visit all next states after expanding the node
                # if(next not in frindge1):
                #     frindge1.append(next)
                costs = problem.getCostOfActions(actions + [action])  # getting the cost to travel to next node
                dist = costs + heuristic(next, problem)  # updating the cost+heuristic of that particular node
                # print ("dist: ",dist)
                # if actions is not None:
                # print("hello: ",next, actions+[action])
                frindge.push((next, actions + [action]), dist)  # adding node and path to frindge
                # else:
                #     # print("hello1: ",next, [action])
                #     frindge.push((next, [action]), dist)  # adding node and path to frindge
    else:
        return
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
