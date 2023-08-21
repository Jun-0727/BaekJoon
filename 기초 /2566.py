import sys
input = sys.stdin.readline

max_num = 0
x, y = 1, 1
for i in range(9):
    arr = list(map(int, input().split()))
    tmp = max(arr)

    if max_num < tmp:
        x = i+1
        y = arr.index(tmp)+1
        max_num = tmp

print(max_num)
print(x, y)