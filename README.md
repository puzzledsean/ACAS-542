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
- [x] Data Collection <br>
  a. Scraping and downloading data <br>
  b. Download data onto scc servers 

- [x] RNN Model <br>
  a. Padding data so that each training example has the same sequence length <br>
  b. Train the model with the newly padded data (for a single plane) <br>
  c. Change the output of the model (change number of time steps that the model predicts)

- [ ] Policy Prediction <br>
  a. Rewrite NMAC data cleaner to get ~10 time steps before collision <br>
  b. Feed NMAC data of both planes to the model to predict each plane's trajectory <br>
  c. Verify that the model correctly visualizes/predicts a collision <br>
  d. Manually code a policy for both planes to prevent them from colliding <br>
  

~~3. Policy Prediction (potential options): <br>
  a. Hard code a manual policy when NMAC is detected <br>
  b. Q-learning --> Reinforcement learning algorithm to create policy for action selection~~
  
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
