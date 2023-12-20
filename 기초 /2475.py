# 검증수
import sys
import math
input = sys.stdin.readline

arr = list(map(int, input().split()))

sum = 0
for i in range(5):
    sum += pow(arr[i], 2)

print(sum%10)