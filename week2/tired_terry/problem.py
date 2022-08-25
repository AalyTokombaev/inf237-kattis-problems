from sys import stdin as inp

n, p ,d = map(int, inp.readline().split())

pattern = list(map(lambda c: {"W": 0, "Z": 1}.get(c), inp.readline().strip()))*2

tiredness = 0
s = sum(pattern[n-p:n])

for i in range(n, 2*n):
    start =  i - p + 1 
    end = i 
    out = start - 1
    s += pattern[end] - pattern[out]

    if s < d:
        tiredness += 1


print(tiredness, flush=True)

