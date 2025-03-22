from typing import Set, Callable, Dict

def gen_next_pos(s, a, S: Set):
    '''Generates the next state if action a is implemented at state s'''
    i, j = s
    moves = {"UP": (i-1, j), "DOWN": (i+1, j), 
             "LEFT": (i, j-1), "RIGHT": (i, j+1)}
    return moves[a] if moves[a] in S else s # return new position unless crossing boundary


def reward_func_generator(reward_states: Dict, boundary_penalty, S: Set) -> Callable:
    '''
    Defines a Reward function (input for value iteration) given a 
    dictionary of rewards for chosen states s from S (set of states)
    '''
    def R(s, a):
        '''Function to calculate reward when action a is performed at state s.'''
        s_next = gen_next_pos(s, a, S) # find new state
        if s_next == s: # penalty if we cross the grid boundary
            return -boundary_penalty 
        # default reward is 0 unless otherwise specified
        return reward_states[s_next] if s_next in reward_states else 0
    return R

def prob_func_generator(intended_move_prob, S: Set, A: Set) -> Callable:
    '''
    Defines a transition probability function (input for value iteration)
    given the deterministic/stochastic probability of moving in the intended
    direction. There are three unintended directions 
    (if there are 4 actions U, L, D, R).
    '''
    def P(sp, s, a):
        '''Function to determine transition probability of moving to 
        state s' given we perform action a at state s.'''
        unintended_A = A.copy() # set of unintended actions
        unintended_A.remove(a) # remove intended action
        if sp == gen_next_pos(s, a, S):
            return intended_move_prob # if we go in the intended direction
        elif sp in [gen_next_pos(s, a_alt, S) for a_alt in unintended_A]:
            return (1-intended_move_prob)/3 # equal probability for each unintended direction
        else:
            return 0 # landing in other states that cannot be reached in one move
        
    return P


