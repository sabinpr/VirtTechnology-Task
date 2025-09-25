"""
Travelling Salesman Problem
A salesman must visit 6 cities: A, B, C, D, E, F.
The distances (in kilometers) between the cities are given below:

From / To   A   B   C   D   E   F
A           0  10  15  20  25  30
B          10   0  35  25  17  28
C          15  35   0  30  28  40
D          20  25  30   0  22  16
E          25  17  28  22   0  35
F          30  28  40  16  35   0

Task:
The salesman must:
1. Start from City A.
2. Visit each city exactly once.
3. Return to City A.

👉 Question: What is the shortest possible route the salesman can take, and what is the total
distance?
"""

# Solution using brute-force approach
import itertools

distances = {
    "A": {"A": 0, "B": 10, "C": 15, "D": 20, "E": 25, "F": 30},
    "B": {"A": 10, "B": 0, "C": 35, "D": 25, "E": 17, "F": 28},
    "C": {"A": 15, "B": 35, "C": 0, "D": 30, "E": 28, "F": 40},
    "D": {"A": 20, "B": 25, "C": 30, "D": 0, "E": 22, "F": 16},
    "E": {"A": 25, "B": 17, "C": 28, "D": 22, "E": 0, "F": 35},
    "F": {"A": 30, "B": 28, "C": 40, "D": 16, "E": 35, "F": 0},
}


def tsp_solution(start_city, all_cities):

    other_cities = []
    for city in all_cities:
        if city != start_city:
            other_cities.append(city)

    all_permutations = itertools.permutations(other_cities)

    shortest_distance = float("inf")
    shortest_route = None

    for permutation in all_permutations:
        current_distance = 0
        current_route = (start_city,) + permutation + (start_city,)

        for i in range(len(current_route) - 1):
            from_city = current_route[i]
            to_city = current_route[i + 1]
            current_distance += distances[from_city][to_city]

        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_route = current_route

    return shortest_route, shortest_distance


cities = ["A", "B", "C", "D", "E", "F"]
start = "A"

route, distance = tsp_solution(start, cities)

print(f"The shortest possible route is: {' -> '.join(route)}")
print(f"The total distance is: {distance} km")
