from collections import namedtuple
import heapq
from sys import stdin as std
from sys import exit


n, m, f, s, t = map(int, std.readline().strip().split())

inf = float('inf')
adj_list = dict()
dist = [inf]*n
visited = [False]*n

Edge = namedtuple('Edge', ['weight', 'fro', 'to'])

nodes = set()

for _ in range(m):
    i, j, c = map(int, std.readline().strip().split())
    if not i in adj_list:
        adj_list[i] = {Edge(c, i, j)}
    else:
        adj_list[i].add(Edge(c, i, j))
    
    if not j in adj_list:
        # adj_list[j] = {Edge(c, j, i)}
        adj_list[j] = {(c, j, i)}
    else:
        # adj_list[j].add(Edge(c, j, i))
        adj_list[j].add((c, j, i))

    nodes.put(i)
    nodes.put(j)


airplanes = []

for _ in range(f):
    u, v = map(int, std.readline().strip().split())
    if not u in adj_list:
        #adj_list[u] = {Edge(0, u, v,)}
        adj_list[u] = {(0, u, v)}
    else:
        # adj_list[u].add(Edge(0, u, v))
        adj_list[u].add((0, u, v))
    
    airplanes.append(u)




def dijkstra(graph, start):
    global n
    #queue = [Edge(-1, start, 0)]
    queue = [start]
    dist = [float('inf')]*n
    visited = [False]*n
    visited[0] = True
    dist[0] = 0

    heapq.heapify(queue)
    
    while queue != []:
        node = heapq.heappop(queue)
        



if n == 0:
    print(0)
    exit()

initial_dikstra = dijkstra(adj_list, 5)

print(initial_dikstra[t])



