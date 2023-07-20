import sys
import heapq

input = sys.stdin.readline
N = int(input())

nums = [int(input()) for _ in range(N)]

heap = []
for num in nums:
    if num == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)*(-1))
    else:
        heapq.heappush(heap, num*(-1))