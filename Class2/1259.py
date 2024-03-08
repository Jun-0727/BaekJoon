import sys
input = sys.stdin.readline

def solve(num):
    s = list(str(num))
    cmp = list(reversed(s))
    if s == cmp:
        print('yes')
    else:
        print("no")


candis = []

while True:
    x = int(input())
    if x == 0:
        break
    candis.append(x)

for i in candis:
    solve(i)
