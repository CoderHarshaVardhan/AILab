from collections import deque


goal_state = "123456780"  


moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


def swap(state, i, j):
    state = list(state)
    state[i], state[j] = state[j], state[i]
    return ''.join(state)


def solve(start_state):
    queue = deque()
    visited = set()

    queue.append((start_state, []))  
    visited.add(start_state)

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [state]

        zero_index = state.index("0")  

        for move in moves[zero_index]:
            new_state = swap(state, zero_index, move)
            if new_state not in visited:
                queue.append((new_state, path + [state]))
                visited.add(new_state)

    return None  


start = "123406758" 
solution = solve(start)

if solution:
    print("Steps to solve:")
    for s in solution:
        for i in range(0, 9, 3):
            print(s[i:i+3])
        print("---")
else:
    print("No solution found.")
