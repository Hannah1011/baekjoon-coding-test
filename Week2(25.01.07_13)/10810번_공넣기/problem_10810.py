N, M = map(int, input().split())
ball = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i-1, j):
        ball[n] = k

for b in ball:
    print(b, end=" ")