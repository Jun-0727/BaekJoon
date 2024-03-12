import sys
input = sys.stdin.readline
from collections import deque

def solve(cmd, num, queue):
    if cmd == 'push':
        queue.append(num)

    if cmd == 'pop':
        if queue:
            x = queue.popleft()
            return x
        else:
            return -1
    
    if cmd == 'size':
        return len(queue)
    
    if cmd == 'empty':
        if queue:
            return 0
        else:
            return 1
        
    if cmd == 'front':
        if queue:
            return queue[0]
        else:
            return -1
        
    if cmd == 'back':
        if queue:
            return queue[-1]
        else:
            return -1
        
N = int(input())
queue = deque()
cmd = []
for i in range(N):
    cmd.append(input().split())

result = []
for i in range(N):
    if cmd[i][0] == 'push':
        solve(cmd[i][0], int(cmd[i][1]), queue)
    else:
        result.append(solve(cmd[i][0], 0, queue))

for x in result:
    print(x)