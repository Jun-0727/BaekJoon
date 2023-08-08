import sys
import copy
sys.setrecursionlimit(10**6)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 인자로 높이, 좌표가 들어가는 dfs 함수
# "조건 : graph[x][y] > h" 를 만족하는 위치를 탐색
def dfs(h,x,y):
    graph[x][y] = h
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] > h:
            dfs(h,nx,ny)

input = sys.stdin.readline
N = int(input())

reset = [list(map(int, input().split())) for _ in range(N)]
results = []

# 가장 높은 지역 탐색
highest = 0
for i in range(N):
    highest = max(highest, max(reset[i]))

# 강수량 : 0 ~ 가장높은지역 까지 일 때를 순차적으로 탐색
for h in range(highest):
    graph = copy.deepcopy(reset)    # 그래프(지도) 초기화
    count = 0   # 횟수 초기화
    
    # 좌표 순차 탐색
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h:
                dfs(h,i,j)
                count += 1
    results.append(count)

print(max(results))