# IndexError -> BFS로 제출

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

M,N,K = map(int, input().split())

graph = [[False]*(N) for _ in range(M)]
results = []

for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = True

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    count = 1
    graph[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue
        if not graph[nx][ny]:
            count += dfs(nx,ny)
    
    return count

for i in range(N):
    for j in range(M):
        if not graph[j][i]:
            results.append(dfs(i,j))

results.sort()
print(len(results))
print(*results)