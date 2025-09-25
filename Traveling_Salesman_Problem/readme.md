## Traveling Salesman Problem (TSP) Solver

This repository contains a Python script that solves a specific instance of the Traveling Salesman Problem (TSP) using a brute-force approach.

## Problem Description

A salesman must find the shortest possible route to visit six cities (A, B, C, D, E, F), starting and ending in City A, while visiting each city exactly once. The distances between the cities are provided in a distance matrix.

## Solution Approach

The script employs a brute-force method to find the optimal solution. This involves:

1. Identifying all possible routes: The code uses the itertools.permutations function to generate every possible sequence of the cities to be visited. Since the start and end city is fixed (A), the permutations are calculated for the remaining five cities (B, C, D, E, F).

2. Calculating the total distance for each route: For each permutation, the script calculates the total distance by summing the distances between consecutive cities in the route.

3. Finding the shortest route: The code keeps track of the shortest distance found so far and the corresponding route. After checking all possible permutations, it returns the route with the minimum total distance.

This approach is effective for a small number of cities. However, the time complexity of a brute-force solution grows factorially (n), making it impractical for a large number of cities.

## How to Run the Script

1. Ensure you have Python installed.

2. Run the script from your terminal:

```
python tsp_solver.py
```

## Output

The script will print the shortest possible route and its total distance to the console.

```
The shortest possible route is: A -> B -> F -> D -> E -> C -> A
The total distance is: 119 km
```
