Introduction

I have developed a maze-solving agent using the Python
programming language. The agent's objective is to navigate through a 20x20 maze
environment, avoiding walls, and finding an optimal path from the start state to the goal
state. Our implementation uses Depth-First Search (DFS) and Breadth-First Search
(BFS) algorithms in order to achieve this goal.

Formulation of the Search Problem

Initial State: The initial state is the starting position of the agent within the maze.
Goal State: The goal state is the destination position that the agent aims to reach within
the maze.
State Space:.The state space consists of all possible maze configurations, or positions
hat the agent can occupy.
Operators: The operators define the actions that the agent can take to navigate
through the maze. These actions include moving in these directions (left, right,
backward or forward).
Assumptions:
- The maze is represented as a grid with discrete cells.
- Each cell in the maze can either be empty or contain a wall.
- The agent cannot move through walls and must find a path around them.
- The agent has perfect knowledge of its immediate surroundings but does not
have information about the entire maze layout.
- The maze environment is static, meaning it does not change during the agent's
navigation process.
- The agent's goal is to find the shortest path from the initial state to the goal state.

Interface Visualization:


<img src="https://github.com/AmarAlrifaie/MazeSolver/assets/169054714/71ec333f-5c70-4c9d-9f28-1d996da4d288" alt="Description of image" width="500">
