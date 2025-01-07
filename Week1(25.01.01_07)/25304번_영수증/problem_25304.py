X = int(input())
N = int(input())
money = []
for i in range(N):
    a,b = map(int, input().split())
    money.append(a*b)

sum = 0
for mon in money:
    sum += mon

if sum == X:
    print("Yes")
else:
    print("No")
    


## clean code ##
'''
X = int(input())
N = int(input())

total = sum(int(a)*int(b) for a,b in (input().split() for _ in range(N)))

print("Yes" if total == X else "No")
'''