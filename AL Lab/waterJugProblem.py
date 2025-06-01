from collections import deque

def water_jug_bfs():
    visited = set()
    queue = deque()

    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        print(f"5L: {x} | 3L: {y}")
        visited.add((x, y))

        if x == 4:
            print("Reached goal state!")
            return

        next_states = [
            (5, y),    
            (x, 3),
            (0, y),    
            (x, 0),     
            (x - min(x, 3 - y), y + min(x, 3 - y)),  
            (x + min(y, 5 - x), y - min(y, 5 - x))  
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("No solution found.")

water_jug_bfs()
