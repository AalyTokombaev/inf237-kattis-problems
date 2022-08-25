from copy import deepcopy
from sys import stdin as inp


inf = float('inf')
def solve(m, heights):

    if sum(heights) % 2 == 1:
        print("IMPOSSIBLE")
        return 
    
    if len(heights) == 1:
        print('IMPOSSIBLE')
        return

    max_height = sum(heights) // 2  + 2
    #print(f"maxheight: {max_height}")
    dp = [[inf]*m for i in range(max_height)]
    dp[heights[0]][0] = heights[0] # dp[y][x] = max height on x y


    stacc = {dp[heights[0]][0]}
    another = set()

    for i in range(1, m):
        h = heights[i]
        # empty the stack here
        while stacc:
            element = stacc.pop()
            value = dp[element][i-1]
            
            if element + h < max_height:
                dp[element + h][i] = min(dp[element + h][i], max(element + h, value))
                another.add(element + h)

            if element - h >= 0:
                if dp[element - h][i]:    
                    dp[element - h][i] = min(value, dp[element - h][i])

                else:
                    dp[element - h][i] = value

                another.add(element - h)

        stacc = deepcopy(another)
        another = set()

    # backwards traversal 
    backwards = heights[::-1]
    string = ''
    last = dp[0][m-1]
    if  last == inf:
        print('IMPOSSIBLE')
        return 

    

    start = 0
    i = 1 
    while i < m:
        h = backwards[i-1]
        ft = start + h
        fb = start - h
        index = m - i - 1

        if index < 0:
            break

        ## if both exists 
        if ft < max_height and fb >= 0:
            if dp[ft][index] < dp[fb][index]:
                string = 'D' + string
                start = ft
            else:
                string = 'U' + string
                start = fb
        # else only one exists (hopefully)
        else:
            # this one?
            if fb >= 0 and ft >= max_height:
                string = 'U' + string
                start = fb
                # or this one?
            if fb < 0 and ft < max_height:
                string = 'D' + string 
                start = ft
        i+= 1





 

    print('U'+string, flush=True)


    



n = int(inp.readline().strip())

for _ in range(n):
    m = int(inp.readline().strip())
    heights = [int(i) for i in inp.readline().strip().split()]
    solve(m, heights)