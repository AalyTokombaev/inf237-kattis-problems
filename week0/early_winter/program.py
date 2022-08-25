from sys import stdin as inp

n, d_m = [int(i) for i in inp.readline().strip().split()]
numbers = [int(i) for i in inp.readline().strip().split()]

k = None
for i in range(len(numbers)):
    if numbers[i] <= d_m:
        k = i
        break
    

if k != None:
    print(f"It hadn't snowed this early in {k} years!")
else:
    print("It had never snowed this early!")
