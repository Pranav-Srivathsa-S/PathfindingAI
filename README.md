# PathfindingAI
This repository implements the A* algorithm for efficient pathfinding. Find the shortest path between two points on a grid, used in AI and game development.

# A* Pathfinding Algorithm

This project implements the A* pathfinding algorithm in Python, using it to find the shortest path in a 2D maze.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Design Decisions](#design-decisions)
- [Challenges and Learning](#challenges-and-learning)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## Introduction
The A* algorithm is one of the most effective and efficient pathfinding algorithms. It finds the shortest path from a start node to a goal node in a graph. This project uses A* to solve a maze represented as a 2D grid.

## Prerequisites
You need Python 3.x to run this project. No additional libraries are required.

## Usage
Define your maze as a list of lists of characters, where 'S' is the start, 'G' is the goal, '#' is a wall, and '.' is an open path. Then, call the `A_star` function with the maze, the start node, and the goal node as arguments.

## Code Explanation
The code includes a helper function to calculate the Manhattan distance between two points, which is used as a heuristic in the A* algorithm. The main function, `A_star`, implements the A* algorithm using a priority queue to store the nodes to be visited and two dictionaries to store the parent and the cost of each node. The algorithm visits each node by considering its neighbors, and updates the parent and cost of each neighbor if a cheaper path to it is found. Once the goal is reached, the function reconstructs and returns the path from the start to the goal.

## Design Decisions
The choice of A* for pathfinding showcases the algorithm's efficiency and versatility. The use of a priority queue and dictionaries ensures optimal performance. The Manhattan distance was chosen as the heuristic due to its simplicity and effectiveness in grid-based problems.

## Challenges and Learning
Understanding and implementing the A* algorithm was a challenging yet rewarding experience. The project required a solid grasp of graph theory, priority queues, and heuristics. Handling different types of nodes (start, goal, wall, open path) appropriately was also an important part of the project.

## Future Improvements
This project can be extended to handle 8-connected or 3D grids, different types of terrain, and could also benefit from a graphical interface for visualizing the algorithm.

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [Contributing Guidelines](CONTRIBUTING.md) for more information.

