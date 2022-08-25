
from copy import deepcopy
from math import inf
from statistics import median, mean
import sys

from numpy import True_

n, m, k = map(int, input().split())

initial_scores = list(map(int, input().split()))

cool = deepcopy(initial_scores) # for getting the index later

initial_scores.sort()
people_needed = int(k/10)
goal = k/n
# split into two
larger = initial_scores[-people_needed:]
smaller = initial_scores[:people_needed-1]


scores = []
scores.append(min(larger))
smaller.remove(min(larger))

slider = True
while larger and smaller:
    if mean(scores) >  goal:
        if slider:
            scores.append(max(smaller))
            smaller.remove(max(smaller))

        else:
            scores.append(min(smaller))
            smaller.remove(min(smaller))
    else:
        if slider:
            scores.append(max(larger))
            larger.remove(max(larger))

        else:
            scores.append(min(larger))
            larger.remove(min(larger))


print(smaller, larger)
l = (scores + larger + smaller)

print([cool.index(i)+1 for i in l])
















