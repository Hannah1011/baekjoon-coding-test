T = int(input())
array = []

for _ in range(T):
    A,B = map(int, input().split())
    array.append(A+B)

for i in range(T):
    print(f"Case #{i}", end = ": ")
    print(array[i])