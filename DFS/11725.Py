import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 탐색으로 트리를 조회하면서
# 2~N번 노드의 부모 노드를 result 리스트에 저장하는 함수
def dfs(v):
    global parent
    visit[v] = True
    results[v-2] = parent

    for i in graph[v]:
        if not visit[i]:
            parent = v
            dfs(i)

N = int(input())
graph = [[]*(N+1) for _ in range(N+1)]      # 간선을 저장하는 graph
visit = [False] * (N+1)         # 방명록 초기화
results = [0] * (N-1)           # 2~N번 노드의 부모 노드를 저장하는 리스트

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


parent = 1  # 시작 부모 노드(root)
dfs(1)      # dfs 탐색으로, 각 노드의 부모노드 리스트 작성

for result in results:
    print(result)

"""
parent = 1
def dfs(current, find):
    global parent
    visit[current] = True

    if current == find:
        results.append(parent)
        return

    for i in graph[current]:
        if not visit[i]:
            parent = current
            dfs(i, find)

for i in range(2,N+1):
    visit = [False] * (N+1)
    dfs(1,i)

for result in results:
    print(result)
"""