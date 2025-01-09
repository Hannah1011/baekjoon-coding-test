'''N = int(input())
all = list(map(int, input().split()))

print(min(all), max(all))'''


## 만약 min , max 을 사용하지 못한다면 아래처럼 진행.
N = int(input())
all = list(map(int, input().split()))
min_val, max_val = float('inf'), float('-inf')

for a in all:
    if a < min_val: 
        min_val  = a
    if a > max_val: 
        max_val = a

print(min_val, max_val)