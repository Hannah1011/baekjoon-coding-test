N, M = map (int, input().split())
ball = [0]*N
for i in range(N):
    ball[i] = i+1
for _ in range(M):
    i, j = map(int, input().split())
    ball[i-1], ball[j-1] = ball[j-1], ball[i-1]
    
for b in ball:
    print(b, end=' ')