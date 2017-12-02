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


### TODO:
- clean data more? (zig zags) might not be necessary
- predict more than 1 future timestep (how many?)
- train hyperparameters by using many different combinations on training data and then getting the ones that perform the best with the validation set
- train model on scc with all data
- get model (doesn't have to be well-trained), take multiple planes as input, and predict if future collision
- hard code plane action when NMAC detected (base case)
- use RNN Q-learning to create a policy for when NMAC detected
