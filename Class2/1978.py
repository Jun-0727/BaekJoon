import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

check = [0] * 1001
check[2] = 1

for i in range(2,1001):
    for j in range(2,i):
        if i == j+1:
            check[i] = 1

        if i%j == 0:
            break
sum = 0
for i in range(N):
    sum += check[num[i]]

print(sum)