#--- BFS ---#
import sys
from collections import deque

input = sys.stdin.readline
N,M,V = map(int, input().split())

#---  방법 1 ---#

graph1 = [[False]*(N+1) for _ in range(N+1)]
visit1 = [False] * (N+1)

for _ in range(M):
    x,y = map(int, input().split())
    graph1[x][y] = True
    graph1[y][x] = True

def bfs1(V):
    que = deque([V])
    visit1[V] = True
    while que:
        V = que.popleft()
        print(V, end=" ")
        for i in range(1,N+1):
            if not visit1[i] and graph1[V][i]:
                que.append(i)
                visit1[i] = True

bfs1(V)


#--- 방법 2 ---#

graph2 = [[]*(N+1) for _ in range(N+1)]
visit2 = [False] * (N+1)

for _ in range(M):
    x,y = map(int, input().split())
    graph2[x].append(y)
    graph2[y].append(x)

def bfs2(V):
    que = deque([V])
    visit2[V] = True
    while que:
        V = que.popleft()
        print(V, end=" ")
        for i in graph2[V]:
            if not visit2[i]:
                que.append(i)
                visit2[i] = True

bfs2(V)


#--- 문제풀이 ---#

import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

def dfs(V):
    visit[V] = True         # 방명록 싸인
    print(V, end=' ')
    for i in graph[V]:      # 갖고있는 간선 중
        if not visit[i]:    # 방문 안한 곳 있으면
            dfs(i)          # 재귀

def bfs(V):
    que = deque([V])
    visit[V] = True
    while que:
        V = que.popleft()           # 다음~
        print(V, end=" ")
        for i in graph[V]:          # 갖고 있는 간선 중
            if not visit[i]:        # 방문 안한 곳 있으면
                que.append(i)       # 대기열 추가
                visit[i] = True     # 방명록 싸인

visit = [False] * (N+1)
dfs(V)
print()
visit = [False] * (N+1)
bfs(V)