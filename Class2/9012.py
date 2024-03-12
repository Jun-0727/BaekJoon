# 괄호

import sys
input = sys.stdin.readline


def solve(lst):
    check = []

    for i in range(len(lst)):
        if lst[i] == '(':
            check.append(1)
        else:
            if len(check) == 0:
                return 'NO'
            check.pop()

    if len(check) > 0:
        return 'NO'
    else:
        return 'YES'
    

N = int(input())
ex = []
for _ in range(N):
    ex.append(input().strip())

results = []
for i in range(N):
    results.append(solve(ex[i]))

for result in results:
    print(result)