# 직각삼각형
import sys
input = sys.stdin.readline

def solve(a, b, c):
    if c*c == a*a + b*b:
        return 'right'
    else:
        return 'wrong'

results = []
while(True):
    a, b ,c = map(int, input().split())
    if a == 0:
        break
    big = max(a,b,c)

    if a == big:
        a = c
        c = big
    elif b == big:
        b = c
        c = big
        
    results.append(solve(a,b,c))

for result in results:
    print(result)