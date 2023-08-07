#--- DFS ---#
# Recursion_Error #
import sys

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    graph[x][y] = 0

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N :
            continue
        if graph[nx][ny] == 1:
            dfs(nx,ny)

input = sys.stdin.readline
T = int(input())
results = []

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * N for _ in range(M)] # graph = [ [0] * 세로 for _ in range(가로)]
    worm = 0

    for i in range(K):
        x, y = map(int, input().split()) 
        graph[x][y] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                dfs(i,j)
                worm += 1
    results.append(worm)

for result in results:
    print(result)