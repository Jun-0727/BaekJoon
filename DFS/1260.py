import sys
from collections import deque

input = sys.stdin.readline
N,M,V = map(int, input().split())

#--- 방법 1 ---#
"""
graph1 = [[False] * (N+1) for _ in range(N+1)]  # 간선 리스트 초기화
visit1 = [False] * (N+1)                        # 방명록 초기화

# 간선 리스트 입력
for _ in range(M):
    x,y = map(int, input().split())
    graph1[x][y] = True
    graph1[y][x] = True

def dfs1(V):
    visit1[V] = True
    print(V, end=' ')
    for i in range(1,N+1):
        if not visit1[i] and graph1[V][i]:
            dfs1(i)

dfs1(V)
"""

#--- 방법 2 ---#

graph2 = [[] * (N+1) for _ in range(N+1)]  # 간선 리스트 초기화
visit2 = [False] * (N+1)                        # 방명록 초기화

# 간선 리스트 입력
for _ in range(M):
    x, y = map(int, input().split())
    graph2[x].append(y)
    graph2[y].append(x)


# 여러개의 간선 중 작은 노드와 연결된 것 부터 조회
for x in graph2:
    x.sort()

def dfs2(V):
    visit2[V] = True
    print(V, end=" ")
    for i in graph2[V]:
        if not visit2[i]:
            dfs2(i)

dfs2(V)


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