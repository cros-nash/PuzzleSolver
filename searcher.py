#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Crosby Nash
# email: crosbyn@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: N/A
# partner's email: N/A
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    def __init__(self, depth_limit):
        ''' Constructs a new Searcher object by initializing the inputs as attributes
            Input depth_limit is an integer specifing how deep in the state-space search tree the Searcher will go'''
            
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def add_state(self, new_state):
        ''' Appends list self.states with input new_state
            Input new_state is a State object, self is a Searcher object'''
            
        self.states += [new_state]

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def should_add(self, state):
        ''' Returns True if the called Searcher should add state to its list of untested states, and False otherwise
            Input state is a State object, self is a Searcher object'''
            
            
        if (self.depth_limit != -1) and (state.num_moves > self.depth_limit):
            return False
        
        elif state.creates_cycle() == True:
            return False
        
        else:
            return True
        
    def add_states(self, new_states):
        ''' Processes the elements of new_states to see if it should be added to list of states
            Input new_states is a list of State objects, self is a Searcher object'''
            
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        ''' Performs a full state-space search that begins at the specified initial state
            Input init_state is a State object, self is a Searcher object'''
            
        self.add_state(init_state)
        
        while len(self.states) > 0:
            s = self.next_state()
            self.num_tested += 1

            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
                
        return None
        

### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    ''' Performs breadth-first search (BFS) instead of random search.
        Inherits methods from Searcher class'''

    def next_state(self):
        ''' Replaces the inherited next_state method and follows FIFO ordering
            Input self is a State object'''
            
        s = self.states[0]
        self.states.remove(s)
        return s
        
class DFSearcher(Searcher):
    ''' Performs depth-first search (DFS) instead of random search.
        Inherits methods from Searcher class'''
        
    def next_state(self):
        ''' Replaces the inherited next_state method and follows LIFO ordering
            Input self is a State object'''

        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    ''' Computes and returns an estimate of how many additional moves are needed to get from state to the goal state
        Input state is a State object'''
    
    return state.board.num_misplaced()

def h2(state):
    ''' Computes and returns an estimate of how many additional moves are needed to get from state to the goal state
        Input state is a State object'''
        
    return state.board.tiles_away()

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def __init__(self, heuristic):
        ''' Constructs a new GreedySearcher's object and overrides inherited one
            Input self is a GreedySearch object and heuristic is a reference to a hueristic function'''
        self.heuristic = heuristic
        super().__init__(-1)
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def add_state(self, state):
        ''' Overrides inherited add_state method and adds a sublist instead of a state
            Input self is a GreedySearcher object, state is a State object'''
            
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        ''' Overrides the inherited next_state method and instead chooses state with highest priority
            Input self is a GreedySearcher object'''
            
        s = max(self.states)
        self.states.remove(s)
        return s[1]
        
### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    ''' Like greedy search, A* is an informed search algorithm that assigns a priority to each state based on a heuristic function, 
        and that selects the next state based on those priorities but also takes into account the cost that has been expended to get to 
        that state'''
        
    def priority(self, state):
        ''' Computes and returns the priority of the specified state,
            based on the heuristic function used by AStarSearcher as well as cost expended to get to goal state
            Input self is a AStarSearcher object, state is a State object'''
            
        return -1 * (self.heuristic(state) + state.num_moves)
        
