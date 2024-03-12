# 스택
import sys
input = sys.stdin.readline

def solve(cmd, num, stack):
    if cmd == 'push':
        stack.append(num)
    
    if cmd == 'pop':
        if len(stack) > 0:
            x = stack.pop()
            return x
        else:
            return -1
    
    if cmd == 'size':
        return len(stack)
    
    if cmd == 'empty':
        if stack:
            return 0
        else:
            return 1
        
    if cmd == 'top':
        if stack:
            return stack[-1]
        else:
            return -1
        
N = int(input())
cmd = []
stack = []

for i in range(N):
    cmd.append(input().split())

results = []    
for i in range(N):
    if cmd[i][0] == 'push':
        solve(cmd[i][0], int(cmd[i][1]), stack)
    else:
        results.append(solve(cmd[i][0], 0, stack))

for result in results:
    print(result)