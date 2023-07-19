# 우선순위큐(pq)에는 N개의 데이터 밖에 못 들어감
# 한 줄씩 큐에 넣을 건데
# 넣으려는 리스트(테이블 한 줄)중 가장 큰 값(listMax)과, 큐에 존재하는 가장 작은 값(queMin) 비교
# 리스트에서 가장 큰 값 pop / pq에서 가장 작은 값 pop
# listMax > queMin 이면 listMax를 큐에 put
# listMax ≤ queMin 이면 queMin를 큐에 put

# 시간 초과 --> listMax를 구하는 대신 '현재 넣으려는 리스트 값(listCurrent)' 으로 대체
# 그래도 시간초과

# queque 대신 heapq를 사용해보자
# 선언 : 리스트 선언과 동일 (리스트를 마치 최소힙처럼 다룰 수 있게 해줌, 때문에 함수를 호출할 떄마다 리스트(힙)를 인자로 넘거야 함 )
# 원소 추가 : heappush(대상 리스트, 원소) 
# 원소 삭제 : heappop(대상 리스트) -> 루트에 위치한 원소(가장 작은 값) 삭제
# pop하지 않고 최솟값 조회 : heap[0]

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())


heap = []       # 힙(리스트) 선언

for _ in range(N):
    values = list(map(int, input().split()))    # 리스트에 n번째 줄 입력

    # heap이 비어있으면 리스트에 있는 값 넣기
    if not heap:    
        for value in values:
            heappush(heap, value)
    # heap이 비어있지 않다면 힙의 최솟값과 리스트의 값을 비교         
    else:
        for value in values:
            # 힙의 최솟값보다 리스트에 들어있는 값이 크면 최솟값 삭제 & 힙에 리스트값 추가
            if heap[0] < value:
                heappop(heap)
                heappush(heap,value)

print(heap[0])

"""
from queue import PriorityQueue

que = PriorityQueue()   # 우선순위큐 선언

# N * N 데이터 입력
for _ in range(N):
    values = list(map(int, input().split()))
    if que.empty():
        for i in range(N):
            que.put(values[i])
    else:
        for i in range(N):
            current = values[i]
            queMin = que.get()

            if current > queMin :
                que.put(current)
            else:
                que.put(queMin)

print(que.get())
"""
