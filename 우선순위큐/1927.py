import sys
import heapq

input = sys.stdin.readline
N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

heap = []
for num in nums:
    # x가 0이면 heap에서 최솟값 반환 및 출력
    if num == 0:
        # heap이 비어있으면 0을 출력
        if not heap:
            print(0)
        # 비어있지 않다면 heap 최소값 반환 및 삭제
        else:
            print(heapq.heappop(heap))
    # x가 0이 아니라면 heap에 추가
    else:
        heapq.heappush(heap,num)
