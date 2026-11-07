# ---------------- Task 2 : Minimax with leaf counter ----------------
def minimax_counted(node, is_max, counter):
    if isinstance(node, int):
        counter[0] = counter[0] + 1
        return node

    results = []
    for child in node:
        results.append(minimax_counted(child, not is_max, counter))

    if is_max:
        return max(results)
    else:
        return min(results)


game_tree = [[3, 5], [2, 9], [12, 5]]
leaf_counter = [0]

print("Minimax Value:", minimax_counted(game_tree, True, leaf_counter))
print("Leaves Evaluated:", leaf_counter[0])