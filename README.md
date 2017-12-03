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
  b. Padding data so that each training example has the same sequence length

2. RNN Model <br>
  a. Train the model with the newly padded data (for a single plane) <br>
  b. Change the output of the model (change number time steps that the model predicts)

3. Policy Prediction (potential options): <br>
  a. Hard code a manual policy when NMAC is detected <br>
  b. Q-learning --> Reinforcement learning algorithm to create policy for action selection
