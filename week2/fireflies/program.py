from sys import stdin as inp

n, h = list(map(int, inp.readline().strip().split()))
obstacles = [int(inp.readline().strip()) for i in range(n)]


d = {i: 0 for i in range(h)}

lower = [0]*(h)
higher = [0]*(h)


for i in range(n):
    if i % 2 == 0:
        lower[obstacles[i]] += 1
    if i % 2 == 1:
        higher[obstacles[i]] += 1


values = [0]*(h)
values[0] = n//2


for i in range(1, h):
    values[i] = values[i-1] - lower[i] + higher[h-i]
    

print(min(values), values.count(min(values)))


