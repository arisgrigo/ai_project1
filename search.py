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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
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
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    nodeStack = util.Stack()  # stack to place nodes to be discovered
    pathStack = util.Stack()  # stack to place path to each node that is discovered
    path = []  # used to keep track of the path to current node
    discovered = set()  # list where every discovered node is placed

    # inititialize both stacks (nodeStack with the starting state and pathStack with an empty list)
    nodeStack.push(problem.getStartState())
    pathStack.push(path)

    while not nodeStack.isEmpty():
        currNode = nodeStack.pop()  # current node that will be explored
        path = pathStack.pop()  # path to current node from start state

        if currNode in discovered:  # if node is discovered, explore next node
            continue

        discovered.add(currNode)  # if not explore current one and add it to discovered list

        if problem.isGoalState(currNode):  # if current node is the goal state then return path to node
            return path

        # successor[0] is the node and successor[1] is the path from current node to successor
        for successor in problem.expand(currNode):
            if successor[0] not in discovered:
                succPath = path + [successor[1]]  # succPath is the path from start state to current successor
                nodeStack.push(successor[0])
                pathStack.push(succPath)

    if nodeStack.isEmpty():
        return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    nodeQueue = util.Queue()  # same as dfs but with Queues instad of Stacks
    pathQueue = util.Queue()
    path = []
    discovered = set()

    nodeQueue.push(problem.getStartState())
    pathQueue.push(path)

    while not nodeQueue.isEmpty():
        currNode = nodeQueue.pop()
        path = pathQueue.pop()

        if currNode in discovered:
            continue

        discovered.add(currNode)

        if problem.isGoalState(currNode):
            return path

        for successor in problem.expand(currNode):
            if successor[0] not in discovered:
                nodeQueue.push(successor[0])
                succPath = path + [successor[1]]
                pathQueue.push(succPath)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    nodePQ = util.PriorityQueue()
    pathPQ = util.PriorityQueue()
    path = []
    discovered = []

    priority = 0
    nodePQ.push(problem.getStartState(), priority)
    pathPQ.push(path, priority)

    while not nodePQ.isEmpty():
        currNode = nodePQ.pop()
        path = pathPQ.pop()

        if currNode in discovered:
            continue
        discovered.append(currNode)

        if problem.isGoalState(currNode):
            return path

        # priority in astar is based on cost of path to the node + heuristic in use

        for successor in problem.expand(currNode):
            if successor[0] not in discovered:
                succPath = path + [successor[1]]
                priority = (problem.getCostOfActionSequence(succPath) + heuristic(successor[0], problem))
                nodePQ.push(successor[0], priority)
                pathPQ.push(succPath, priority)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
