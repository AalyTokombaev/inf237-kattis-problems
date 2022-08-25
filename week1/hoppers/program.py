from collections import deque
# from queue import Queue # Hot garbage
import sys

N, M = map(int, sys.stdin.readline().split())


colors = {}
neighbourhood = {}
marked = {}
for i in range(1,N+1):
    colors[i] = None
    marked[i] = False
    neighbourhood[i] = []



for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    neighbourhood[u].append(v)
    neighbourhood[v].append(u)


last_color = False
def bfs(start):
    """Bfs search to single out components ant tell us if they're bipartite"""
    global last_color
    bipart = True

    if marked[start]:
        return 

    queue = deque()
    queue.append(start)

    colors[start] = last_color
    last_color = not last_color

    while  queue:
        node = queue.popleft()
        marked[node] = True

        for child in neighbourhood[node]:
            if colors[node] == colors[child]:
                bipart = False

            if marked[child]:
                continue

            colors[child] = not colors[node]
            marked[child] = True
            queue.append(child)

    return bipart


# check for components
components = []
for node in neighbourhood.keys():
    component = bfs(node)

    if component != None:
        components.append(component)



if False in components:
    print(len(components)-1)
else:
    print(len(components))