from itertools import permutations


dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
cities = list(range(n))
min_cost = float('inf')
best_path = []


for perm in permutations(cities[1:]):
    path = [0] + list(perm) + [0]  
    cost = 0
    for i in range(n):
        cost += dist[path[i]][path[i+1]]

    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Minimum cost:", min_cost)
print("Best path:", best_path)
