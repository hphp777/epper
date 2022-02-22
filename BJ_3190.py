from collections import deque # 양 끝에서 삽입, 제거

def playGame(n, board, cmd):
    
    dy = [0,-1,0,1] # 우 상 좌 하 반시계방향으로 90도씩 회전
    dx = [1,0,-1,0]

    t = 0 # time
    board[0][0] = 1
    head = 0 # 방향
    snake = deque() # 뱀의 몸통을 표시하는 좌표들
    snake.appendleft([0,0]) # 머리가 가장 왼쪽에 위치

    while(True):

        t += 1

        ny = snake[0][0] + dy[head]
        nx = snake[0][1] + dx[head]

        # exit
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            break
        if board[ny][nx] == 1:
            break

        if board[ny][nx] != 2: #사과를 먹지 않은 경우
            y,x = snake.pop() # 맨뒤(오른쪽좌표) 꼬리
            board[y][x] = 0

        snake.appendleft([ny,nx])
        board[ny][nx] = 1
        a = 10

        if cmd.get(t) == 'L': 
            head = (head + 1) % 4 # 현재의 머리방향에서 좌
        elif cmd.get(t) == 'D' : 
            head = (head + 3) % 4 # 현재의 머리방향에서 하

    return t


if __name__ == "__main__":
    
    board = []
    map_size = int(input())

    for i in range(map_size):
        board.append([0]*map_size)

    apple = int(input())
    if apple > 0:
        for i in range(apple):
            y, x = map(int, input().split())
            board[y-1][x-1] = 2 # apple

    turn_num = int(input())

    time = []
    rotation = []

    for i in range(turn_num):
        t, r = map(str,input().split())
        time.append(int(t))
        rotation.append(r)



    cmd = dict(zip(time,rotation))

    answer = playGame(map_size,board,cmd)

    print(answer)