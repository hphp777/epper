# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
# 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
# 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

# 괄호가 열리기 전에 닫히면 안됨

iter = int(input())
sentence = []

for i in range(iter):
    new = input()
    sentence.append(new)

for n in range(iter):
    open = 0
    close = 0
    answer = 0

    flag = False

    for i in range(len(sentence[n])):
        if answer < 0: 
            print("NO")
            flag = True
            break
        if sentence[n][i] == '(':
            answer += 1
        else:
            answer -= 1

    if flag == False:
        if answer == 0:
            print("YES")
        else:
            print("NO")

