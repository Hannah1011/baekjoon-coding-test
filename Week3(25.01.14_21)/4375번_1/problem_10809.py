# 첫째 줄 단어 S 
S = list(input())

c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in S:
        print(S.index(i), end = ' ')
    else:
        print(-1, end = ' ')