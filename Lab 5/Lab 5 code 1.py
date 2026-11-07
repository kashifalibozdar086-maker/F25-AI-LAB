# ---------------- Task 1 : Minimax ----------------
def minimax_value(node, is_max):
    # a number means we reached a leaf
    if isinstance(node, int):
        return node

    results = []
    for child in node:
        results.append(minimax_value(child, not is_max))

    if is_max:
        return max(results)
    else:
        return min(results)


game_tree = [[3, 5], [2, 9], [12, 5]]
print("Minimax Value:", minimax_value(game_tree, True))
