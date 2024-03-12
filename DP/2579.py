# 계단 오르기

# 시도_1
# 반대로 내려간다고 생각하기

"""
import sys
input = sys.stdin.readline

def solution(n, stair):
    can_go_one_stair = True
    current = n

    score = stair[current]

    while(current > 0):
        if can_go_one_stair:
            if stair[current-1] >= stair[current-2]:
                score += stair[current-1]
                current -= 1
                can_go_one_stair = False
            else:
                score += stair[current-2]
                current -= 2
                can_go_one_stair = True
        else:
            score += stair[current-2]
            current -= 2
            can_go_one_stair = True
        
    return score

n = int(input())
stair = [0]
for _ in range(n):
    stair.append(int(input()))

print(solution(n, stair))

# 반례 10 / 200 / 100 / 25 / 10 / 20
"""


# 시도_2
# 1149 풀고 깨달음.. DP로 풀자

# DP는 점화식이다
# 해당 step에만 집중해서 문제를 풀어야함
# 이번 문제는 마지막 계단을 무조건 밟아야 한다 + 세 계단 연속으로 못밟는다 가 힌트

import sys
input = sys.stdin.readline

def solve(N):
    stair = []
    for _ in range(N):
        stair.append(int(input()))

    dp = [0 for row in range(N)]

    if N == 1:
        return stair[0]
    
    if N == 2:
        return stair[0]+stair[1]
    
    dp[0] = stair[0]
    dp[1] = max(stair[0]+stair[1], stair[1])
    dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])

    return dp[N-1]

N = int(input())
print(solve(N))
