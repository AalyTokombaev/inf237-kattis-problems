from sys import stdin as inp 

X = int(inp.readline().strip())
N = int(inp.readline().strip())
numbers = [int(inp.readline().strip()) for i in range(N)]

s = X

for i in numbers:
    s -= i
    s += X

print(s)
