import sys
input = sys.stdin.readline

N = int(input())
member = []
for i in range(1,N+1):
    age, name = input().split()
    member.append([int(age), i, name])

member.sort()

for i in range(N):
    print(member[i][0], member[i][2])
