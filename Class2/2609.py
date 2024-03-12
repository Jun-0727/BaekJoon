# 최대 공약수와 최소 공배수

import sys
input = sys.stdin.readline

a,b = map(int, input().split())
d, m = 2, min(a,b)
tmp = [1]

while(d <= m):
    if a%d == 0 and b%d == 0:
        tmp.append(d)
        a = a//d
        b = b//d
        m = min(a,b)
        d = 2
    else:
        d += 1

print(tmp,a,b)

ans = 1
for x in tmp:
    ans *= x
print(ans, ans*a*b)