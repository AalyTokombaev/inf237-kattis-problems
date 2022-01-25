from queue import Queue
n, m, d = [int(s) for s in input().split()]

sceptisism = dict()

for i in range(n):
    name, s = input().split()
    sceptisism[name] = int(s)


mark_list = {}

adj_list = {}
for i in range(m):
    a, b = input().split()
    if a in adj_list:
        adj_list[a].append(b)
    else:
        adj_list[a] = [b]
    
    if b in adj_list:
        adj_list[b].append(a)
    else:
        adj_list[b] = [a]
    if not (a in mark_list):
        mark_list[a] = False
        mark_list[b] = False
    if not b in mark_list:
        mark_list[b] = False

alice = input()
mark_list[alice] = True

# queue = []
queue = Queue()
rumors = 0
queue.append(alice)
t = 0


def mark_children(node):
    global adj_list, rumors, mark_list
    if not adj_list.get(node):
        return
    for child in adj_list.get(node):
        if not mark_list.get(child):
            rumors += 1
            mark_list[child] = True


while queue and t < d:
    for i in range(queue.qsize()):
        start = queue.get()
        mark_children(start)
        if not adj_list.get(start):
            continue
        for child in adj_list.get(start):
            sceptisism[child] -= 1
            if sceptisism.get(child) == 0:
                queue.put(child)
    t += 1

print(rumors)