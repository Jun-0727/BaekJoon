# 1. 중간값 변수(mid) 선언 및 leftHeap(최대힙) & rightHeap(최소힙)을 생성
# 2. 입력값 < mid 이면 left_heap에, 입력값 ≥ mid 이면 right_heap에 push
# 3. 이 때 len(lheap)과 len(rheap)의 차이가 2 이상이면 mid값 재설정
#    - left_heap에 있는 원소의 개수가, right_heap에 있는 원소의 개수보다 2개이상 많아지면
#       - mid 를 right_heap에 push & left_heap의 최대값을 mid로
#    - 반대면
#       - mid 를 left_heap에 push & right_heap의 최소값을 mid로
# 4. 외친 값이 짝수개인 경우 중간에 있는 두 수 중 작은 수를 뽑아야 함
#    - lheap, rheap의 길이에 차이가 생기는 순간이 짝수개일 때임
#    - len(rheap) > len(lheap)인 경우 : 문제 없음
#    - len(rheap) < len(lheap)인 경우 : 현재 mid값을 rheap에 push, lheap의 최댓값을 중간값으로 재설정
import sys
import heapq

input = sys.stdin.readline
N =  int(input())
lheap = []  # Left_Heap
rheap = []  # Right_Heap
result = []

    
# 첫번째 입력 
mid = int(input())
result.append(mid)

for _ in range(N-1):
    value = int(input())

    # 입력값이 중간값보다 작으면 입력값을 왼쪽힙에, 크거나같으면 오른쪽 힙에 넣음
    if mid > value:
        heapq.heappush(lheap, -value)
    else:
        heapq.heappush(rheap, value)
    
    # 원소가 left_heap에 쏠리면 중간값 및 heap 재설정  
    # __OR__
    # 원소의 총 개수가 짝수개일 때 중간값을 가운데 두 수 중 작은 값으로 설정
    if ((len(lheap)-len(rheap) == 2) or (len(lheap) > len(rheap))):
        heapq.heappush(rheap, mid)
        mid = -heapq.heappop(lheap)

    # 원소가 right_heap에 쏠리면 중간값 및 heap 재설정
    if len(rheap)-len(lheap) == 2: 
        heapq.heappush(lheap, -mid)
        mid = heapq.heappop(rheap)
    
    # 중간값 저장
    result.append(mid)

for x in result:
    print(x)