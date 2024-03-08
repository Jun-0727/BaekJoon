
# RGB 거리

# 가장 저렴한 비용 찾기
#   - 몇 번 째 집인지 저장
#   - 무슨 색으로 칠했는지 저장
# n번째 집 제외 - 다음으로 가장 저렴한 비용 찾기
#   - 위의 이미 색칠한 집과의 관계 비교
#   - 몇 번 째 집인지 저장
#   - 무슨 색으로 칠했는지 저장

# 시도1
# house 리스트, cost변수 선언
# house[c] : index: i번째 집 / 어떤 color로 칠했는지
# total : 집을 칠하는데 드는 비용
# 1. 전체 중 가장 낮은 cost 찾기 
#   - 집을 칠한 뒤 (total += cost)
#   - 해당 라인의 cost를 모두 1001로 수정
# 2. 다음으로 가장 낮은 cost 찾기
#   - 주변집(윗집, 아랫집)이 칠해져 있는지 확인
#   - 안칠해져 있다면 집을 칠한 뒤 cost를 모두 1001로 수정
#   - 칠해져 있다면 무슨색으로 칠해졌는지 확인(1 or 2 or 3)
#   - 가장 낮은 cost가 이미 칠한 색이라면....잠깐만
#        100 | 2 | 100    
# ...근데 100 | 1 | 100 이라면 위의 방법으로 하면 안되네
#        100 | 3 | 100


# 시도2
# 집을 3개씩 세트로 묶으면 123, 234, 456, ... 이렇게
# 4번째 집을 어떤 색으로 칠할지가 되면 1번 집은 이미 확정
# 3집씩 묶어서 가격을 비교하면..
# 너무 복잡해진다..
"""
best = 0
comp = []
comp[1] = cost[1][1] + cost[2][2] + cost[3][1]
comp[2] = cost[1][1] + cost[2][2] + cost[3][3]
comp[3] = cost[1][1] + cost[2][3] + cost[3][1]
comp[4] = cost[1][1] + cost[2][4] + cost[3][2]

comp[5] = cost[1][2] + cost[2][1] + cost[3][2]
comp[6] = cost[1][2] + cost[2][1] + cost[3][3]
comp[7] = cost[1][2] + cost[2][3] + cost[3][1]
comp[8] = cost[1][2] + cost[2][3] + cost[3][2]

comp[9] = cost[1][3] + cost[2][1] + cost[3][2]
comp[10] = cost[1][3] + cost[2][1] + cost[3][3]
comp[11] = cost[1][3] + cost[2][2] + cost[3][1]
comp[12] = cost[1][3] + cost[2][2] + cost[3][3]
"""
# 답지
# 너무 복잡하게 생각했나
# 현재 집을 칠하는 기준으로 그 전까진의 비용을 계산 -> DP
# 2번째 집을 칠할건데 
# Step1. 1번집/red + 2번집 최소비용 vs 1번집/green + 2번집 최소비용 vs 1번집/blue + 2번집 최소비용
# Step2. 1+2번집 최소비용...

# 이거 처음에 생각했던건데 이러면 
# 100 99 100 : step1
# 100 1 100  : step2
# 100 3 100  : step3

# 가장 작은 수 부터 찾는 뱡식
# 99 -> 100 -> 3
# 정답은
# 100 -> 1 -> 100

# 위에를 선택하고 밑을 보는게 아니라
# 밑에 기준에서 위를 보는거야

# step2 에서 : 어디보자.. step1 중 뭘 골라야 최선이지?
# step3 에서 : 어디보자.. stpe2 중 뭘 골라야 최선이지?

import sys
input = sys.stdin.readline

def solution(N, cost):
    dp = [[0]*3 for row in range(N)]
    dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

    for i in range(1,N):
        dp[i][0] = min(cost[i][0]+dp[i-1][1], cost[i][0]+dp[i-1][2])
        dp[i][1] = min(cost[i][1]+dp[i-1][0], cost[i][1]+dp[i-1][2])
        dp[i][2] = min(cost[i][2]+dp[i-1][0], cost[i][2]+dp[i-1][1])

    return min(dp[N-1][0], dp[N-1][1], dp[N-1][2])

N = int(input())

cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

print(solution(N, cost))