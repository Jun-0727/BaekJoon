import sys
sys.setrecursionlimit(10**6)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs1(color, x,y):
    graph1[x][y] = 'X'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph1[nx][ny] == color:
            dfs1(color, nx, ny)

def dfs2(color, x,y):
    graph2[x][y] = 'X'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph2[nx][ny] == color:
            dfs2(color, nx, ny)

input = sys.stdin.readline
N = int(input())

graph1 = []
graph2 = []
for _ in range(N):
    buff = list(map(str, input()))    
    graph1.append(list(map(str, buff)))
    graph2.append(list(map(str, buff)))

for i in range(N):
    for j in range(N):
        if graph2[i][j] == 'R':
            graph2[i][j] = 'G'

result = []
count = 0
for i in range(N):
    for j in range(N):
        if graph1[i][j] != 'X':
            color = graph1[i][j]
            dfs1(color, i, j)
            count += 1
result.append(count)

count = 0
for i in range(N):
    for j in range(N):
        if graph2[i][j] != 'X':
            color = graph2[i][j]
            dfs2(color, i, j)
            count += 1
result.append(count)

print(*result)