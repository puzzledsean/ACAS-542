# CS542 Project for Aircraft Collision Avoidance System

### Members
Tyrone Hou, Mark Bestavros, Brian Siao, Sean Zhang

### Resources
Robust Airborne Collision Avoidance through Dynamic Programming </br>
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.207.7337&rep=rep1&type=pdf

Policy Compression for Aircraft Collision Avoidance Systems </br>
https://web.stanford.edu/group/sisl/references/2016/julian2016.pdf

Reinforcement Learning: An Introduction </br>
http://ufal.mff.cuni.cz/~straka/courses/npfl114/2016/sutton-bookdraft2016sep.pdf


### Next steps:
1. Data Collection <br>
  a. Scraping and downloading data <br>
  b. Download data onto scc servers 

2. RNN Model <br>
  a. Padding data so that each training example has the same sequence length <br>
  a. Train the model with the newly padded data (for a single plane) <br>
  b. Change the output of the model (change number of time steps that the model predicts)

3. Policy Prediction (potential options): <br>
  a. Hard code a manual policy when NMAC is detected <br>
  b. Q-learning --> Reinforcement learning algorithm to create policy for action selection
  
### Specifics of Q-learning model
Pieces that we will need to implement:
- Q function: Defines the *expected future reward* of taking action a in state s
  - Approximated using a Neural network model
  - input: state of plane
  - output: list of probabilities/rewards of the possible actions in the given state
- Transition Function:
  - p(s, a, s') := probability of transitioning to state s' given you are currently in state s and you take action a
  - Define deterministic probabilities
- Simulation for us to "poke" the q function to train and learn the best rewards based on transition function
  - Already given a simulation, need to look into how to use
