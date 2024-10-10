#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Crosby Nash
# email: crosbyn@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: N/A
# partner's email: N/A
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        value = 0
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                self.tiles[row][col] = digitstr[value]
                value += 1
                
        for x in range(len(digitstr)):
            if digitstr[x] == '0':
                self.blank_r = x // 3
                self.blank_c = x % 3
        
    ### Add your other method definitions below. ###
    
    def __repr__(self):
        ''' Returns a string of a Board object
            Input self is a Board object'''
        s = ''
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == '0':
                    s += '_ '
                
                else:
                    s += self.tiles[row][col] + ' '
                
            s += '\n'
            
        return s
    
    def move_blank(self, direction):
        """ Returns True or False to indicate whether the requested move was possible
            Input direction is a string with values of only 'up', 'down', 'left' or 'right', self is a Board object"""
            
            
        if direction == 'up':
            if (self.blank_r - 1 < 0):
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r - 1][self.blank_c]
                self.tiles[self.blank_r - 1][self.blank_c] = '0'
                self.blank_r -= 1
                return True
            
        elif direction == 'down':
            if (self.blank_r + 1 > (len(self.tiles[0]) - 1)):
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r + 1][self.blank_c]
                self.tiles[self.blank_r + 1][self.blank_c] = '0'
                self.blank_r += 1
                return True  
            
        elif direction == 'left':
            if (self.blank_c - 1 < 0):
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c - 1]
                self.tiles[self.blank_r][self.blank_c - 1] = '0'
                self.blank_c -= 1
                return True
            
        elif direction == 'right':
            if (self.blank_c + 1 > (len(self.tiles[0]) - 1)):
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c + 1]
                self.tiles[self.blank_r][self.blank_c + 1] = '0'
                self.blank_c += 1
                return True
            
        else:
            return False
        
    def digit_string(self):
        ''' Returns a string of digits that corresponds to the current contents of the called Board object's tiles attribute
            Input self is a Board object'''
        s = ''
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                s += self.tiles[row][col]
                
        return s
    
    def copy(self):
        ''' Returns a newly-constructed Board object that is a deep copy of the called object
            Input self is a Board object'''
        
        return Board(self.digit_string())
    
    def num_misplaced(self):
        ''' Returns the number of tiles in the called Board object that are not where they should be in the goal state
            Input self is a Board object'''
            
        num = 0
            
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == '0':
                    num = num
                else:
                    if self.tiles[row][col] != GOAL_TILES[row][col]:
                        num += 1
                        
        return num
    
    def tiles_away(self):
        ''' Returns the number of tiles in the called Board object that represents how far the tile is from its intended position in the goal state
            Input self is a Board object'''
            
        num = 0
 
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] != (GOAL_TILES[row][col] and '0'):
                    if (abs(int(self.tiles[row][col]) // 3) != row) and (abs(int(self.tiles[row][col]) % 3) != col):
                        num += abs((int(self.tiles[row][col]) // 3) - row) + abs((int(self.tiles[row][col]) % 3) - col)
                        
                    elif abs(int(self.tiles[row][col]) // 3) != row:
                        num += abs((int(self.tiles[row][col]) // 3) - row)
                        
                    elif abs(int(self.tiles[row][col]) % 3) != col:
                        num += abs((int(self.tiles[row][col]) % 3) - col)
                
        return num
                
    def __eq__ (self, other):
        ''' Returns True if the called object (self) and the argument (other) have the same values for the tiles attribute, returns False otherwise
            Input self and other are Board objects'''
            
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] != other.tiles[row][col]:
                    return False
                
        return True

