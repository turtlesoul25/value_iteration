def gen_next_pos(s, a, S):
    '''Generates the next state if action a is implemented at state s'''
    i, j = s
    moves = {"UP": (i-1, j), "DOWN": (i+1, j), 
             "LEFT": (i, j-1), "RIGHT": (i, j+1)}
    return moves[a] if moves[a] in S else s # return new position unless crossing boundary


def reward_func_generator(reward_states, boundary_penalty, S):
    '''
    Defines a Reward function (input for value iteration) given a 
    dictionary of rewards for chosen states s from S (set of states)
    '''
    def R(s, a):
        s_next = gen_next_pos(s, a, S)
        if s_next == s:
            return -boundary_penalty # penalty if we cross the grid boundary
        return reward_states[s_next] if s_next in reward_states else 0
    return R

def prob_func_generator(intended_move_prob, S, A):
    '''
    Defines a transition probability function (input for value iteration)
    given the deterministic/stochastic probability of moving in the intended
    direction. There are three unintended directions 
    (if there are 4 actions U, L, D, R).
    '''
    def P(sp, s, a):
        unintended_A = A.copy()
        unintended_A.remove(a)
        if sp == gen_next_pos(s, a, S):
            return intended_move_prob
        elif sp in [gen_next_pos(s, a_alt, S) for a_alt in unintended_A]:
            return (1-intended_move_prob)/3
        else:
            return 0
        
    return P


