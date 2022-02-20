# 5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 
# 이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.

# 숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.

picture = []
visited = [0] * 1000000
answer = 0

def dfs(y, x, level, num):
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]


    if level == 6:
        visited[num] = 1
        return

    for n in range(4):
        ddx = x + dx[n]
        ddy = y + dy[n]
        if (ddx >= 0 and ddx < 5 and ddy >= 0 and ddy < 5):
            dfs(ddy,ddx,level+1,num*10 + picture[ddy][ddx])


for i in range(5):
    picture.append(list(map(int, input().split()))) # 배열을 입력받아서 붙이면 분리돼서 들어간다.


for y in range(5):
    for x in range(5):
        if y == 2 and x == 3:
            stop = 1
        dfs(y, x, 1,picture[y][x])

for i in range(len(visited)):
    if visited[i] == 1:
        # print(i)
        answer += 1

print(answer)