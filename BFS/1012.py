# 1. 그래프 작성
# 2. 시작 노드를 큐에 push & graph = 0
# 3. 큐에 남아있는 원소가 없을 때 까지
#    - 큐에서 원소 pop
#    - 해당 원소의 이웃 노드 push
# 4. 큐에 있는 모든 원소가 pop되면 종료

import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    que = deque([])
    que.append((x,y))
    graph[x][y] = 0

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N :
                continue
            if graph[nx][ny] == 1:
                que.append((nx,ny))
                graph[nx][ny] = 0

input = sys.stdin.readline
T = int(input())
results = []

for _ in range(T):
    M,N,K = map(int, input().split())

    graph = [[0] * N for _ in range(M)]
    worm = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i,j)
                worm += 1
    results.append(worm)

print(results)