
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

# solution_1

cards = deque()

for i in range(1,N+1):
    cards.append(i)

while len(list(cards)) > 1:
    cards.popleft()
    tmp = cards.popleft()
    cards.append(tmp)

print(cards.popleft())


# stack은 list로
# push: list.append(value)
# pop : list.pop()
# top : [-1]

# list 삭제
# index : list.pop(index) / del list[index]
# value : list.remove(value)
# 모두제거: list.clear()

#--------------------------------------------------#

# queue를 list로 (FIFO)
# 삽입 : list.append(value) / list.insert(0, value)
# 삭제 : list.pop(0)        / list.pop()

# list는 무작위 접근에 최적화 된 자료구조임

#--------------------------------------------------#

# queue를 collections 모듈의 deque 클래스로

# from collections import deque
# queue = deque()
# 삽입 : queue.append(value) /  queue.appendleft(value)
# 삭제 : queue.popleft()     /  queue.pop()

# dequeue는 무작위 접근의 시간 복잡도가 O(n)

#--------------------------------------------------#

# queue를 queue 모듈의 Queue클래스로

# from queue import Queue
# que = Queue()
# 삽입 : que.put(value)
# 삭제 : que.get()

# 멀티쓰레드 환경, 내부 locking을 지원