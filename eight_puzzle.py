#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Crosby Nash
# email: crosbyn@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: N/A
# partner's email: N/A
#

from searcher import *
from timer import *
from multiprocessing import Pool


def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
       searcher = BFSearcher(param)
    elif algorithm == 'DFS':
       searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
       searcher = GreedySearcher(param)
    elif algorithm == 'A*':
       searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
def process_file(filename):
    ''' Opens the file with the specified filename for reading, and uses a loop to process the file one line at a time.
        Each move is fed into the specified algorith with the specified paramater, and the results of each puzzle, along with the whole file, are printed 
        Input filename (string) is the name of a text file with each line is a digit string for an eight puzzle
              algorithm (string) specifies which state-space search algorithm to be used
              param (integer or string) is either a depth limit or a choice of heuristic function'''
     
    moves = []
    amount = 0
    avg_move = 0
    avg_state = 0

    algorithm = 'Greedy'
    param = h1
              
    with open(filename, 'r') as f:
        for line in f:
            line = line[:-1]
            moves += [line]
    
    for x in moves:
        b = Board(x)
        s = State(b, None, 'init')
        searcher = create_searcher(algorithm, param)
        
        print(x + ': ', end='')
        
        soln = None
        try:
            soln = searcher.find_solution(s)
        except KeyboardInterrupt:
            print('search terminated, ', end='')
            
        if soln == None:
            print('no solution')
            
        else:
            amount += 1
            print(soln.num_moves, 'moves,', searcher.num_tested, 'states tested')
            avg_move += soln.num_moves
            avg_state += searcher.num_tested
        
    if amount == 1:
        print('\n' + 'solved', amount, 'puzzle')
        
    else:
        print('\n' + 'solved', amount, 'puzzles')
    
    if amount != 0:
        avg_move /= amount
        avg_state /= amount
        print('averages:', avg_move, 'moves,', avg_state, 'states tested')
        return ('averages:', avg_move, 'moves,', avg_state, 'states tested')

if __name__ == '__main__':
    with Pool(12) as p:
        print(p.map(process_file, ['18_moves.txt', '24_moves.txt', '27_moves.txt']))

process_file('18_moves.txt', 'Greedy', h1)
process_file('24_moves.txt', 'Greedy', h1)
process_file('27_moves.txt', 'Greedy', h1)
process_file('27_moves.txt', 'A*', h1)
