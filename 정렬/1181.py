#단어정렬
import sys
input = sys.stdin.readline

N = int(input())
words = []

for i in range(N):
    words.append(input().strip())

tmp = set(words)
words = list(tmp)
words.sort()
words.sort(key=len)

for word in words:
    print(word)