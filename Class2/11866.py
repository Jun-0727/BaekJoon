# 요세푸스 문제 0

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
josephus = []

tmp = []
for i in range(1,N+1):
    tmp.append(str(i))

current = 0
divide = N
while(len(tmp) > 0):
    current = current + K-1
    if current >= len(tmp):
        current = current%len(tmp) 
    josephus.append(tmp[current])
    tmp.pop(current)

print('<'+', '.join(josephus)+'>')