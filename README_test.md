# `value_iteration`

- [Description](#description)
- [Installation](#installation)
- [Example](#example)
  - [Simple 2-state MDP example](#simple-2-mdp-example)
- [License](#license)
- [GitHub Repository](#github-repository)
- [Contributors](#contributors)
- [References](#references)

## **Description**

The value_iteration python package provides an implementation of the value iteration algorithm. This algorithm is a well-known solution method for finding the optimal policy of a Markov Decision Process (MDP). 

For a range of problems that can be modelled as MDPs, the value iteration algorithm finds the optimal policy by maximising a value function iteratively. 

To learn more about MDPs and the value iteration algorithm, the user can refer to Sections [9.5](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.html) and [9.5.1](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.SS1.html) of [Artificial Intelligence: Foundations and Computational Agents 2nd edition](https://artint.info/2e/html2e/ArtInt2e.html)

**Key Features**
- Implements the value iteration function described by the pseudocode in Figure 9.16 within [Section 9.5.2](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.SS2.html) of [Artificial Intelligence: Foundations and Computational Agents 2nd edition](https://artint.info/2e/html2e/ArtInt2e.html).
- Includes an example of a GridWorld problem which is solved using the `value_iteration` function included in this package.
- Can be used for any MDP with appropriate definitions of states, actions, transition probabilities, reward functions, discount factors, and termination conditions.


## **Installation**

This python package can be installed from github with pip
#### installing from github with pip
```python -m pip install "git+https://github.com/turtlesoul25/value_iteration"```

## **Example**

### Simple 2-state MDP example
This example is taken from [Example 9.27](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.html#Ch9.Thmciexamplered27) from [Artificial Intelligence: Foundations and Computational Agents 2nd edition](https://artint.info/2e/html2e/ArtInt2e.html). 

Suppose Sam wanted to make an informed decision about whether to party or relax over the weekend. Sam prefers to party, but is worried about getting sick. Such a problem can be modeled as an MDP with two states, _healthy_ and _sick_, and two actions, _relax_ and _party_. Thus, the set of states is 
$$S = \{\textit{healthy}, \textit{sick} \}$$

The set of actions is 
$$A = \{\textit{relax}, \textit{party} \}$$

Based on experience, Sam estimates that $P(s' \vert s, a)$ is given by 

| S   | A  | Probability of $s' =$ _healthy_   |
|----|----|---------------------------------------------|
| healthy  | relax   | 0.95  |
| healthy  | party   | 0.7  |
| sick  | relax   | 0.5  |
| sick  | party   | 0.1  |

Sam estimates his immediate rewards to be:

| S   | A  | Reward   |
|----|----|---------------------------------------------|
| healthy  | relax   | 7  |
| healthy  | party   | 10  |
| sick  | relax   | 0  |
| sick  | party   | 2  |


Thus, Sam always enjoys partying more than relaxing. However, Sam feels much better overall when healthy, and partying results in being sick more than relaxing does.

**The problem is to determine what Sam should do each weekend.**


``` python
S = {"sick", "healthy"} # set of states
A = {"relax", "party"}  # set of actions
def P(sp, s, a): # function to calculate transition probabilities
    if s == "healthy":
        if a == "relax":
            if sp == "healthy":
                return 0.95
            else:
                return 0.05
            
        elif a == "party":
            if sp == "healthy":
                return 0.7
            else:
                return 0.3
            
    elif s == "sick":
        if a == "relax":
            return 0.5
        
        elif a == "party":
            if sp == "healthy":
                return 0.1
            else:
                return 0.9
            

def R(s, a): # function to calculate rewards for a state, action pair
    if s == "healthy":
        if a == "relax":
            return 7
        elif a == "party":
            return 10
        
    elif s == "sick":
        if a == "relax":
            return 0
        elif a == "party":
            return 2

# Implementing the value iteration algorithm to solve the MDP
results = Value_iteration(S, A, P, R, 0.8, 1000)    # implement algorithm
optimal_policy = results["optimal_policy"]          # optimal policy
value_function = results["value_function"]          # final value function

for s in S: # print results
    print(f"If {s}, then Sam should {optimal_policy[s]}.")

```

## License

Copyright (C) 2025 Niharika Reddy Peddinenikalva

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.txt>.

## GitHub Repository

Source files for the packages can be found at
<https://github.com/turtlesoul25/value_iteration>

## Contributors

- Niharika Reddy Peddinenikalva: [email](mailto:n.peddinenikalva@lancaster.ac.uk) (**Author**)
  (**Maintainer**) (**Creator**) (**Translator**)

## References

Poole, D. L., & Mackworth, A. K. (2017). Artificial Intelligence: Foundations of Computational Agents (2nd ed.). Cambridge: Cambridge University Press.
