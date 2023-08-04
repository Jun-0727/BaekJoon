#--- DFS ---#
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
result = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    count = 0

    graph[x][y] = 0
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        if graph[nx][ny] == 1:
            count += dfs(nx,ny)
    
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(dfs(i,j))

print(len(result))
result.sort()
for i in result:
    print(i)


#--- BFS ---#

"""
from collections import deque

N = int(input())

graph = [list(map(int, input())) for _ in range(N)]
result = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    graph[x][y] = 0
    count = 0

    while que:
        x,y = que.popleft()
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                continue
            
            if graph[nx][ny] == 1:
                que.append([nx,ny])
                graph[nx][ny] = 0
                
    
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(i,j))

result.sort()

print(len(result))
for i in result:
    print(i)
"""