import sys

sys.setrecursionlimit(10**8)

answer = []

def checkNum(sudoku, row, col):

    check = [0] * 9

    for n in range(9):
        index1 = sudoku[row][n] - 1
        index2 = sudoku[n][col] - 1
        if index1 >= 0:
            check[index1] = 1
        if index2 >= 0:
            check[index2] = 1

    # box
    boxY = row // 3
    boxX = col // 3

    for y in range(boxY*3, boxY*3+3):
        for x in range(boxX*3, boxX*3+3):
            index = sudoku[y][x] - 1
            if index >= 0:
                check[index] = 1

    return check

def isComplete(sudoku):
    
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                return False

    return True

def dfs(sudoku, level, flag):

    if isComplete(sudoku):
        answer = sudoku
        return sudoku, True    

    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                check = [0] * 9
                # mark used num
                # print(y, x)
                check = checkNum(sudoku, y, x)
                mark = False
                for n in range(9):
                    if check[n] == 0:
                        sudoku[y][x] = n+1
                        mark = True # 채울 숫자 있음
                        sudoku, flag = dfs(sudoku,level+1, flag)
                        if flag == True:
                            return sudoku, flag
                        sudoku[y][x] = 0
                        mark = False

                if mark == False: # 만약 채울 숫자가 없으면
                    return sudoku, False

    return sudoku, False


def solution(sudoku):

    answer = [[0]*9 for _ in range(9)]      # 정답 = 현재의 상태를 저장하는 리스트

    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                answer, flag = dfs(sudoku,0, False)

    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    output = solution(sudoku)
    for line in output:
        for num in line:
            print(num, end=' ')
        print()