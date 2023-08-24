import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int , input().split())

# 지도를 입력받기 위한 graph 리스트
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))

# 경로의 수를 저장하기 위한 dp 리스트
dp = [[-1] * N for _ in range(M)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# dp를 사용하기 위해 dfs의 return 값을 무엇으로 두어야 할지가 관건!
def dfs(x,y):
    count = 0

    # 목적지에 도달하면 1을 반환
    if x == M-1 and y == N-1:
        return 1

    # 지나온 길이라면 저장해둔 값을 반환    
    if dp[x][y] != -1:
        return dp[x][y]
    
    current = graph[x][y]   # 현재 길 높이
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= M or ny >=N:
            continue

        next = graph[nx][ny]    # 다음 행선지 길 높이

        # 내리막 길 이라면 count값 + 다음 dfs()
        if current > next:      
            count += dfs(nx,ny)

    dp[x][y] = count    
    return count        

print(dfs(0,0))