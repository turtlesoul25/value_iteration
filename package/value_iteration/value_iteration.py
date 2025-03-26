# Import packages
from typing import Set, Callable, Dict

# Define the value iteration algorithm as a function
def value_iteration(S: Set, A: Set, P: Callable, R: Callable, gamma: float, max_iterations: int, 
                    V_init: Dict = None, theta: float = None) -> Dict:
    '''
    Implements the value iteration algorithm to solve a MDP with given
    set of states and actions, transition probabilities, reward function, 
    and discount factor (gamma)

    Arguments
    -----------
    S: set of states for the MDP.
    A: set of actions for the MDP.
    P: a function which calculates P(s'|s,a), the probability of transitioning
        to state s' given we are in state s and execute action a.
    R: a function which calculates R(s,a), the reward obtainined if action a is 
        executed while in state s.
    gamma: discount factor for calculating the next value function in the MDP.
    max_iterations: maximum number of iterations of value function calculations.
    V_init: a dictionary to store the initialised values for all states.
    theta: threshold value to check convergence of the value function 
        to ensure minimum value function update across all states per iteration.

    Output
    -----------
    output_dict: dictionary containing the optimal policy dictionary and final value function dictionary for all states
    '''

    # Dictionaries containing value function entries for each state
    Vk = dict([(s, 0) for s in S]) if V_init is None else V_init
    V_next = dict([(s, 0) for s in S])

    # Dictionary to store optimal policy for each state
    policy = dict([(s, 0) for s in S])

    k = 0 # iteration counter

    while k < max_iterations: # Iteration termination condition
        delta = 0       # Factor to check convergence of value function
        k = k+1         # Increment iterations
        for s in S:     # Update value function for each state in new iteration
            V_next[s] = max([(R(s,a) + (gamma*sum([(P(s_next, s, a)*Vk[s_next]) for s_next in S]))) for a in A])
            delta = max(delta, abs(V_next[s] - Vk[s]))
        Vk = V_next      # Update penultimate value function for all states for next iteration

        if theta != None and delta < theta: # Convergence (termination) condition for value function (if applicable)
            break

    for s in S: # Store optimal policy for each state
        policy[s] = max(A, key = lambda a: (R(s,a) + (gamma*sum([(P(s_next, s, a)*V_next[s_next]) for s_next in S]))))

    return {"optimal_policy": policy, "value_function": V_next}