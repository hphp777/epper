# 플로이드 워셜 알고리즘
# 모든 노드를 중간 노드로 설정 

maps = []

def solution(n, s, a, b, fares):

    # n: 지점갯수
    # s: 출발지점
    # a,b: 도착지점
    # fares: 엣지정보

    s -= 1
    a -= 1
    b -= 1

    answer = 100000000

    for i in range(n):
        maps.append([100000000]*n)

    for i in range(len(fares)):
        indexY = fares[i][0]-1
        indexX = fares[i][1]-1
        maps[indexY][indexX] = fares[i][2]
        maps[indexX][indexY] = fares[i][2]
    
    for i in range(n):
        maps[i][i] = 0 # 자기 자신과의 거리는 0

    # Fill Graph
    for k in range(n): # 중간노드
        for y in range(n): # from
            for x in range(n): # to
                maps[y][x] = min(maps[y][x], maps[y][k] + maps[k][x])

    # 각 노드까지 함께 가는 경우를 고려해서 최소비용 도출
    for i in range(n):
        pay = maps[s][i] + maps[i][a] + maps[i][b]
        if pay < answer :
            answer = pay
    
    return answer

if __name__ == "__main__":

    n = 6
    s = 4
    a = 6
    b = 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	

    answer = solution(n,s,a,b,fares)

    print(answer)