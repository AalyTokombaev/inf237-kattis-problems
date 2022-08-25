from sys import stdin as inp

def traverse(table, cost):
    #print('cost:', cost)
    if not table[cost]:
        print('Impossible',flush=True)
        return

    last = table[cost]
    numbers = list() # the numbers we visit
    # easy cases
    if not last:
        print('Impossible')
        return
    if len(last) > 1:
        print('Ambiguous')
        return
    
    while last:
        # again if we come to a capacity that isn't reachable we can't really make it happen
        if not last:
            print('Impossible')
            return
        # if we can reach the capacity in multiple ways it becomes ambigious
        if len(last) > 1:
            print('Ambiguous')
            return

        numbers.append(last[0])
        cost = cost - last[0]
        last = table[cost]
        
    return numbers
    

if __name__ == '__main__':
    n = int(inp.readline().strip())
    prices = list(map(int, inp.readline().strip().split()))
    m = int(inp.readline().strip())
    costs = list(map(int, inp.readline().strip().split()))
    max_cost = max(costs) # this is used to calcualte the capacity of the dp
    
    dp = [[] for i in range(max_cost+1)] # dp[c] where is capacity = price that can be used to reach c
    convert = dict()
    #making a dictionary to calculate output
    i = 1
    for price in prices:
        convert[price] = i
        i+=1
    
    for price in prices:
        for capacity in range(price, max_cost + 1):
            # if we're at index price we just add the price to it
            if capacity - price == 0:
                dp[capacity].append(price)
            
            # if we there's something in the value hopped price times backwards we add it here
            if dp[capacity - price]:
                dp[capacity].append(price)
            

    # actual solution 
    for cost in costs:
        g = traverse(dp, cost)
        if g:
            l = [convert.get(i) for i in g]
            l.sort()
            print(' '.join(list(map(str, l))), flush=True)
