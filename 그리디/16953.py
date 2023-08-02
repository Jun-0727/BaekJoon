A,B = map(int, input().split())
cnt = 1

while A != B:
    temp = B
    if B%10 == 1:
        B //= 10
    elif B%2 == 0:
        B//=2

    cnt += 1

    if temp == B:
        print(-1)
        break
else:  
    print(cnt)

# while-else : break 가 수행되면 else문이 실행되지 않는다

