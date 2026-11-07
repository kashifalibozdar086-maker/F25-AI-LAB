# ---------------- Task 3 : Alpha-Beta Pruning ----------------
def alpha_beta(node, a, b, is_max, counter):
    if isinstance(node, int):
        counter[0] = counter[0] + 1
        return node

    if is_max:
        best = float('-inf')
        for child in node:
            score = alpha_beta(child, a, b, False, counter)
            if score > best:
                best = score
            if best > a:
                a = best
            if a >= b:
                break          # prune the remaining children
        return best
    else:
        best = float('inf')
        for child in node:
            score = alpha_beta(child, a, b, True, counter)
            if score < best:
                best = score
            if best < b:
                b = best
            if a >= b:
                break          # prune the remaining children
        return best


game_tree = [[3, 5], [2, 9], [12, 5]]

leaf_counter = [0]
print("Original Order:")
print("Value:", alpha_beta(game_tree, float('-inf'), float('inf'), True, leaf_counter))
print("Leaves Evaluated:", leaf_counter[0])

leaf_counter = [0]
game_tree.reverse()

print("\nReversed Order:")
print("Value:", alpha_beta(game_tree, float('-inf'), float('inf'), True, leaf_counter))
print("Leaves Evaluated:", leaf_counter[0])