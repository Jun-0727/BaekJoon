import sys
input = sys.stdin.readline

def func(target):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        
        if a[mid] < target:
            start = mid + 1
        elif a[mid] > target:
            end = mid - 1
        else:
            return print(1)
        
    return print(0)

N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

a.sort()

for i in range(M):
    func(b[i])