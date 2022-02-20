import sys
import queue

# size = list(map(int, input().split()))

picture = [ [1, 1, 1, 0], 
            [1, 2, 2, 0], 
            [1, 0, 0, 1], 
            [0, 0, 0, 1], 
            [0, 0, 0, 3], 
            [0, 0, 0, 3]]

def solution(m,n,picture):

    max_size = 0
    num_area = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    # queue generation
    que = queue.Queue() 

    for i in range(m):
        for j in range(n):
            if picture[i][j] != 0:
                color = picture[i][j] # type
                # put that in the queue
                que.put((i,j))
                # increase number of area
                num_area += 1
                # increase size
                size = 1
                # visited
                picture[i][j] = 0

                while que.qsize() > 0:
                    # standard point
                    y, x = que.get()
                    for s in range(4):
                        xl = x + dx[s]
                        yl = y + dy[s]
                        if xl >= 0 and xl < n and yl >= 0 and yl < m:
                            if picture[yl][xl] == color:
                                que.put((yl,xl))
                                picture[yl][xl] = 0 # visited
                                size += 1
                                print("points: ",yl,xl)
                
                if size > max_size:
                    max_size = size
    
    return num_area, max_size

print(solution(6, 4, picture))