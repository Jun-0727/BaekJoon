S = int(input())

sum = 0

for i in range(S+2):
    sum += i
    if sum > S:
        print(i-1)
        break