# 행렬 크기 N과 M이 주어진다. 
N, M = map(int, input().split())
# 행렬 만들기 
A, B = [], []

for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)
    
for i in range(N):
    b = list(map(int, input().split()))
    B.append(b)

for i in range(N):
    for j in range(M):
        result = A[i][j] + B[i][j]
        print(result, end = " ")
    print()


# 📍Key Point: 2차원 행렬 이해 