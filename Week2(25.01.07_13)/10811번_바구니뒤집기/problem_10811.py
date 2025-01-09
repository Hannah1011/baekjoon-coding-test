N,M = map(int, input().split())
arr = [i+1 for i in range(N)]
    
for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1:j]=arr[i-1:j][::-1] #역순 처리

print(*arr)