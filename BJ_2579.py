# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. 
# <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.
# 계단 오르는 데는 다음과 같은 규칙이 있다.
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 
# 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.
# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

# 각 계단의 현재 위치에서의 최댓값을 구함
# 각 인덱스는 현재 계단의 위치를 나타냄
# 계단의 갯수가 1,2개일수도 있음
# 다이나믹 프로그래밍

n = int(input()) # number of staires
staires = [0] * (n+1)
points = [0] * (n+1)

# value of staires
for i in range(n):
    staires[i+1] = int(input())

# 첫쨋칸의 최댓값 = 첫째칸을 밟은 경우
points[1] = staires[1]
# 둘쨋칸의 최댓값 = 첫째를 밟고 둘째를 밟은 경우
if n >= 2:
    points[2] = staires[1] + staires[2]

# 셋째 칸 부터의 최댓값: 두가지 경우 비교
# 두 칸을 옮기고 나서부터는 해당칸의 최댓값을 사용할 수 있음
if n >= 3:
    for i in range(3, n+1):
        op1 = staires[i] + points[i-2]
        op2 = staires[i] + points[i-3] + staires[i-1]
        points[i] = max(op1, op2)

print(points[n])