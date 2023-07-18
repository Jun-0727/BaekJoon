import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input())

que = PriorityQueue()
result = 0

# 우선순위 큐에 입력 데이터 초기화
for _ in range(N):
    que.put(int(input()))

while(True):
    tmp1 = que.get()
    
    # 큐가 비어있으면(더할 값이 없으면) 지금까지 계산한 result를 출력 후 종료
    if que.empty():
        print(result)
        break
    
    tmp2 = que.get()

    # 큐에서 가장 작은 두 수를 반환하여, 두 수를 더한 값을 다시 큐에 입력
    sum = tmp1 + tmp2
    result += sum
    que.put(sum)


# 우선순위 큐
# from queue import PriorityQueue
# 선언 : que = PriorityQueue()
# 입력 : que.put(1)
# 반환 : que.get() --> 가장 작은 값을 반환하고 큐에서 삭제
# 조건 : que.empty() --> 비어있으면 True를 반환