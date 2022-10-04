# RacerML
Exploring a very basic AI to navigate a racing route

The idea is to have a small "racer" - described by a triangular sprite - navigate a somewhat simple procedurally generated route.

The racer will be controlled be a simple Neural Network with eight inputs and four outputs. 
- Inputs will be rays cast out in a circle, 45 degrees apart, with a max distance or, if they intersect with the route boundaries, the distance to the route boundary.
- Outputs will be the choice to accelerate in one of four directions, forward, backward, left, right. At a given timestep, the racer may only choose one direction to accelerate in.

Penalties/Rewards:
- The racer will be given a maximum penalty for colliding with the route boundary. Due to hitbox limitations, this collision will not be as strict as it can be
- The racer will be rewarded based on its proximity to the endpoint
- The racer will also be rewarded based on the number of timesteps it took to reach the end position (not necessarily the endpoint, if it dies)

