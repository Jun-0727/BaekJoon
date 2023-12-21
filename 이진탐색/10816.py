import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
candis = list(map(int, input().split()))

result = []
dic = {}

for card in cards:
    if card in dic:
        dic[card] += 1
    else :
        dic[card] = 1

for candi in candis:
    result.append(dic.get(candi,0))

print(*result)


"""
def solve():
    res = []
    input()
    x = dict()
    for num in input().split():
        if num in x:
            x[num]+=1
        else:
            x[num] = 1
    input()
    for n in input().split():
        res.append(x.get(n,0))
    sys.stdout.write('\n'.join([str(r) if r else '0' for r in res]))


if __name__ == '__main__':
    solve()
"""