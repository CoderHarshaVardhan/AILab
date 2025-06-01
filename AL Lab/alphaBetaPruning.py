

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or isinstance(node, int):  
        return node

    if maximizing_player:
        max_eval = float('-inf')
        for child in node:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return max_eval
    else:
        min_eval = float('inf')
        for child in node:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval




game_tree = [
    [3, 5, 6],         
    [9, 1, 2],         
    [0, -1, -10]       
]

# Initial values
depth = 2
alpha = float('-inf')
beta = float('inf')
maximizing_player = True

# Run alpha-beta pruning
best_value = alpha_beta_pruning(game_tree, depth, alpha, beta, maximizing_player)
print("Best value:", best_value)
