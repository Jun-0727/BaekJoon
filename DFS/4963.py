import sys
sys.setrecursionlimit(10**6)

dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,0,1,-1,0,1,-1]

def dfs(x,y):
    graph[x][y] = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= h or ny < 0 or ny>= w:   # 가로세로 헷갈림. 정리를 한번 하고 가야겠음
            continue
            
        if graph[nx][ny] == 1:
            dfs(nx,ny)

input = sys.stdin.readline
results = []

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                count += 1

    results.append(count)

print(*results)
