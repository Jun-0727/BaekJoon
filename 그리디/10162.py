T = int(input())

A, B, C = 0, 0, 0

if T%10 != 0:
    print(-1)
else:
    T /= 10
    if T >= 30:
        A = T/30
        T %= 30
    if T >= 6:
        B = T/6
        T %= 6
    if T >= 1:
        C = T

    print("%d %d %d" %(A, B, C))