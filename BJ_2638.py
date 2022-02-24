# N×M의 모눈종이 위에 아주 얇은 치즈가 <그림 1>과 같이 표시되어 있다. 
# 단, N 은 세로 격자의 수이고, M 은 가로 격자의 수이다. 
# 이 치즈는 냉동 보관을 해야만 하는데 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다. 
# 그런데 이러한 모눈종이 모양의 치즈에서 각 치즈 격자(작 은 정사각형 모양)의 4변 중에서 적어도 2변 이상이 실내온도의 공기와 
# 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다. 
# 따라서 아래 <그림 1> 모양과 같은 치즈(회색으로 표시된 부분)라면 C로 표시된 모든 치즈 격자는 한 시간 후에 사라진다.

# <그림 2>와 같이 치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다. 
# 그러므 로 이 공간에 접촉한 치즈 격자는 녹지 않고 C로 표시된 치즈 격자만 사라진다. 
# 그러나 한 시간 후, 이 공간으로 외부공기가 유입되면 <그림 3>에서와 같이 C로 표시된 치즈 격자들이 사라지게 된다.

# 모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다. 
# 입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 구하는 프로그램을 작성하시오.

# 외부공기, 내부공기를 구분할 때 치즈가 아닌 공기를 기준으로 깊이 우선 탐색을 해야한다
# 치즈를 한번에 녹여야 한다

def outside(sizeY, sizeX,y,x, board):
    
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]

    if y < 0 or y >= sizeY or x < 0 or x >= sizeX or board[y][x] != 0: return
    board[y][x] = -1 # outside air
    for i in range(4):     
        outside(sizeY, sizeX, y + dy[i], x + dx[i], board)

def melt(sizeY, sizeX, board):

    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    time = 0
    
    while True : 

        points = []  

        for y in range(sizeY):
            for x in range(sizeX):

                if board[y][x] == 1: # if there is a cheese

                    count = 0 # num of sides which faces outside air
            
                    for n in range(4):
                        ddy = y + dy[n]
                        ddx = x + dx[n]
                        if ddy < 0 or ddy >= sizeY or ddx < 0 or ddx >= sizeX:
                            continue
                        if board[ddy][ddx] == -1:
                            count += 1
            
                    if count >= 2:
                        points.append([y,x])

        # melt cheese
        if len(points) > 0:
            for n in range(len(points)):
                s = points[n]
                yy = s[0]
                xx = s[1]
                board[yy][xx] = -1
                outside(sizeY, sizeX,yy,xx,board)
        else: 
            break

        time += 1

    return time

def solution(y, x, board):
    
    # mark outside air
    outside(y, x, 0, 0,board)

    # if a cheese faces 2 sides with the outside air, melt them at once
    return melt(y, x, board)

if __name__ == "__main__":

    board = []
    y,x = map(int, input().split())
    
    for i in range(y):
        temp = list(map(int, input().split()))    
        board.append(temp)

        answer = solution(y, x)
        
        print(answer)

