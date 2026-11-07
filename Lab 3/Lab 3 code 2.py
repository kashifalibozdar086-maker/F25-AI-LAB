# ---------------- Task 2 : DLS and IDDFS ----------------
def depth_limited(curr, target, depth_left, route=None):
    if route is None:
        route = [curr]

    if curr == target:
        return "FOUND", route

    if depth_left == 0:
        if len(tree[curr]) > 0:
            return "CUTOFF", None
        return "FAILURE", None

    was_cut = False
    for nxt in tree[curr]:
        if nxt in route:
            continue
        state, found = depth_limited(nxt, target, depth_left - 1, route + [nxt])
        if state == "FOUND":
            return state, found
        if state == "CUTOFF":
            was_cut = True

    if was_cut:
        return "CUTOFF", None
    return "FAILURE", None


def iterative_deepening(src, target, max_depth):
    d = 0
    while d <= max_depth:
        state, route = depth_limited(src, target, d)
        print("Limit:", d, "| Status:", state, "| Path:", route)
        if state == "FOUND":
            return route
        if state == "FAILURE":
            return None
        d += 1
    return None


print("DLS:")
for lim in range(1, 5):
    print("Limit:", lim, "->", depth_limited('A', 'G', lim))

print("\nIDDFS:")
for m in range(1, 5):
    print("\nMaximum depth:", m)
    iterative_deepening('A', 'G', m)