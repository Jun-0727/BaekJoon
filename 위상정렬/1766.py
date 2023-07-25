
# 1. 먼저 풀어야 좋은 문제의 번호를 우선순위, 그 후에 풀어야 좋은 문제의 번호를 값 으로 하는 최소힙 생성
# 2. 문제가 모두 입력되면 최소힙에 저장된 원소를 pop하는데
# 3. pop한 원소 리스트에 '값'이 존재한다면 값만 push

import sys
import heapq
"""
input = sys.stdin.readline
N, M = map(int, input().split())

# 1~N번까지 문제 생성
questions = []
for i in range(N):
    questions.append(i+1)

# 먼저 풀어야 할 문제 & 그 다음에 풀어야 할 문제 쌍으로 최소힙 생성
# 이때 입력된 문제는 전체 문제 리스트에서 삭제
order = []
for _ in range(M):
    A,B = map(int,input().split())
    questions.remove(A)
    questions.remove(B)
    heapq.heappush(order, (A,B))

# 쌍이 없는 문제들을 최소힙에 입력
for x in questions:
    heapq.heappush(order, (x, 0))

# 난이도(번호)가 낮은 순서대로 힙에서 꺼냄
result = []
for _ in range(N):
    x = heapq.heappop(order)
    result.append(x[0])

    if x[1] != 0:
        heapq.heappush(order, (x[1],0))

print(*result)
"""



# 위상정렬
# 사이클이 없는 방향 그래프(DAG)
#   - 큐, 
#   - 스택, DFS
# 큐를 이용한 위상정렬 알고리즘 동작 과정
# 1. 진입차수가 0인 모든 노드를 큐에 넣는다
# 2. 큐가 빌 때까지 다음의 과정을 반복한다
#   - 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다
#   - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다
# 3. 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다
import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
heap = []
result = []

for _ in range(M):
    A,B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1

for i in range(1, N+1):
    if inDegree[i] == 0:
        heapq.heappush(heap,i)

while heap:
    temp = heapq.heappop(heap)
    result.append(temp)

    for i in graph[temp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(heap, i)

print(*result)
