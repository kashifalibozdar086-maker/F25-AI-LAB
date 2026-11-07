# ---------------- Task 3 : UCS vs BFS (weighted) ----------------
costs = {
    'A': [('B', 1), ('C', 2), ('G', 10)],
    'B': [('D', 2), ('E', 2)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}


def uniform_cost(src, target):
    heap = [(0, src, [src])]
    done = []
    while heap:
        total, current, route = heapq.heappop(heap)
        if current in done:
            continue
        done.append(current)
        if current == target:
            return route, total, done
        for nxt, w in costs[current]:
            if nxt not in done:
                heapq.heappush(heap, (total + w, nxt, route + [nxt]))
    return None, float('inf'), done


def bfs_on_weighted(src, target):
    # remove the weights first, BFS only looks at edges
    plain = {}
    for n in costs:
        plain[n] = []
        for c, w in costs[n]:
            plain[n].append(c)

    waiting = [(src, [src])]
    done = []
    while waiting:
        current, route = waiting.pop(0)
        if current in done:
            continue
        done.append(current)
        if current == target:
            # add up the weights along the path found
            total = 0
            for i in range(len(route) - 1):
                for c, w in costs[route[i]]:
                    if c == route[i + 1]:
                        total += w
            return route, total, done
        for nxt in plain[current]:
            if nxt not in done:
                waiting.append((nxt, route + [nxt]))
    return None, float('inf'), done


print("UCS:", uniform_cost('A', 'G'))
print("BFS:", bfs_on_weighted('A', 'G'))

Output (wahi jo tumhare code ka tha):

BFS: (['A', 'B', 'E', 'G'], ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
DFS: (['A', 'B', 'E', 'G'], ['A', 'B', 'D', 'E', 'G'])
DLS:
Limit: 1 -> ('CUTOFF', None)
Limit: 2 -> ('CUTOFF', None)
Limit: 3 -> ('FOUND', ['A', 'B', 'E', 'G'])
Limit: 4 -> ('FOUND', ['A', 'B', 'E', 'G'])
...
UCS: (['A', 'B', 'E', 'G'], 4, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
BFS: (['A', 'G'], 10, ['A', 'B', 'C', 'G'])