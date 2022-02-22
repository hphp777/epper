# 상근이와 선영이가 다른 사람들이 남매간의 대화를 듣는 것을 방지하기 위해서 대화를 서로 암호화 하기로 했다. 그래서 다음과 같은 대화를 했다.

# 상근: 그냥 간단히 암호화 하자. A를 1이라고 하고, B는 2로, 그리고 Z는 26으로 하는거야.
# 선영: 그럼 안돼. 만약, "BEAN"을 암호화하면 25114가 나오는데, 이걸 다시 글자로 바꾸는 방법은 여러 가지가 있어.
# 상근: 그렇네. 25114를 다시 영어로 바꾸면, "BEAAD", "YAAD", "YAN", "YKD", "BEKD", "BEAN" 총 6가지가 나오는데, BEAN이 맞는 단어라는건 쉽게 알수 있잖아?
# 선영: 예가 적절하지 않았네 ㅠㅠ 만약 내가 500자리 글자를 암호화 했다고 해봐. 그 때는 나올 수 있는 해석이 정말 많은데, 그걸 언제 다해봐?
# 상근: 얼마나 많은데?
# 선영: 구해보자!
# 어떤 암호가 주어졌을 때, 그 암호의 해석이 몇 가지가 나올 수 있는지 구하는 프로그램을 작성하시오.

def solution(text):

    length = len(text)
    dp = [0] * 10000
    MOD = 10**6

    # 입력이 없는 데이터
    if length == 0:
        return 0

    # 처음 0으로 시작하는 경우에는 해석 불가
    if text[0] == '0':
        return 0
    
    # 첫글자 하나는 1개로만 해석 가능
    dp[0] = dp[1] = 1 # 0는 더미인덱스

    # 중간에 x0인데 x가 3보다 크거나 0이면 해석 불가
    # x0인데 앞이 1,2이면 무조건 1개로만 해석 가능
    
    for i in range(2, length+1):
        
        cur = i-1 # text를 접근하기 위한 인덱스
        
        if text[cur] == '0' and (text[cur-1] < '1' or text[cur-1] > '2'):
            return 0
        # 바로 앞의 문자가 별개의 문자로 해석될 수 있는 경우
        if text[cur] != '0': 
            dp[i] += dp[i-1]
        # 앞앞의 문자가 별개의 문자로 해석될 수 있는 경우
        if text[cur-1] == '1' or (text[cur-1] == '2' and text[cur] <= '6'): # text[i] == 0인 경우도 여기에 포함됨
            dp[i] += dp[i-2]
        
        dp[i] %= MOD

    answer = dp[length]

    return answer
             


if __name__ == "__main__":

    text = input()
    answer = solution(text)
    print(answer)