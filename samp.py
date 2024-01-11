import collections
import copy
start = [[1,2,3],[0,4,6],[7,5,8]]
goal = [[1,2,3],[4,5,6],[7,8,0]]
q = collections.deque([start])
visited = set()
while(q):

    for i in range(len(q)):
        curr = q.popleft()
        visited.add(curr)
        
        for r in range(len(curr)):
            for c in range(len(curr[0])):
                if curr[r][c]==0:
                    row,col = r,c
        if r==1 and c==1:
            up = copy.deepcopy(curr)
            down = copy.deepcopy(curr)
            right = copy.deepcopy(curr)
            left = copy.deepcopy(curr)
            up[r][c],up[r-1][c] = up[r-1][c],up[r][c]
            down[r][c],down[r+1][c] = down[r+1][c],down[r][c]
            right[r][c],right[r][c+1] = right[r][c+1],right[r][c]
            left[r][c-1],left[r][c] = left[r][c-1],left[r][c]
            print("up ",up)
            print("curr ",curr)
            
            q.append(up)
            q.append(down)
            q.append(right)
            q.append(left)
            
        elif r!=1 and c!=1:

        else:

        





