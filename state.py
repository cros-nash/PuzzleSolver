#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: Crosby Nash
# email: crosbyn@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: N/A
# partner's email: N/A
#

from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
        
    def __init__(self, board, predecessor, move):
        ''' Constructs a new State object by initalizing the input attributes
            Input board is a reference to the Board object
                  predecessor is a reference to the previous state prior to the current sequence of moves
                  move is a string representing the move needed to transition from the predeccesor state to the current state'''
                  
        self.board = board
        self.predecessor = predecessor
        self.move = str(move)
        
        if predecessor == None:
            self.num_moves = 0
            
        else:
            self.num_moves = int(predecessor.num_moves) + 1
        

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
    
    def is_goal(self):
        ''' Returns True if the called State object is a goal state, and False otherwise
            Input self is a State object'''
            
        for row in range(len(self.board.tiles)):
            for col in range(len(self.board.tiles[0])):
                if self.board.tiles[row][col] != GOAL_TILES[row][col]:
                    return False
            
        return True
                
    def generate_successors(self):
        ''' Returns a list of State objects for all successor states of the called State object
            Input self is a State object'''
        successors = []
        b = self.board.copy()
        
        for x in MOVES:
            if b.move_blank(x) == True:
                successors.append(State(b, self, x))
                b = self.board.copy()
                
        return successors
    
    def print_moves_to(self):
        ''' Prints the sequence of moves that lead from the initial state to the called State object
            Input self is a State object'''
            
        if self.move == 'init':
            print('initial state:')
            print(self.board)
            
        else:
            pre = self.predecessor
            pre.print_moves_to()
            print('move the blank', self.move + ':')
            print(self.board)
            
