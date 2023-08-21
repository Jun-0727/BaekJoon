import sys
from collections import deque

M, N, K = map(int,input().split())

visit = [[False] * N for _ in range(M)]
results = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(y1, y2):
        for y in range(x1, x2):
            visit[x][y] = True

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visit[x][y] = True
    count = 0

    while(que):
        x,y = que.popleft()
        count += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if not visit[nx][ny]:
                que.append((nx,ny))
                visit[nx][ny] = True
    
    return count

for i in range(M):
    for j in range(N):
        if not visit[i][j]:
            results.append(bfs(i,j))

results.sort()
print(len(results))
print(*results)