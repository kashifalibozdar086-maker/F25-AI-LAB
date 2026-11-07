# ---------------- Task 1 : BFS and DFS ----------------
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


def bfs_search(src, target):
    waiting = [(src, [src])]          # simple list used as a queue
    done = []
    while len(waiting) > 0:
        current, route = waiting.pop(0)
        if current in done:
            continue
        done.append(current)
        if current == target:
            return route, done
        for nxt in tree[current]:
            if nxt not in done:
                waiting.append((nxt, route + [nxt]))
    return None, done


def dfs_search(src, target):
    pile = [(src, [src])]             # list used as a stack
    done = []
    while len(pile) > 0:
        current, route = pile.pop()
        if current in done:
            continue
        done.append(current)
        if current == target:
            return route, done
        # reverse so that the first child is taken out first
        for nxt in tree[current][::-1]:
            if nxt not in done:
                pile.append((nxt, route + [nxt]))
    return None, done


print("BFS:", bfs_search('A', 'G'))
print("DFS:", dfs_search('A', 'G'))

