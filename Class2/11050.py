
# 이항 계수
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i

    return int(ans)

ans = factorial(N)//(factorial(K)*factorial(N-K))
print(ans)