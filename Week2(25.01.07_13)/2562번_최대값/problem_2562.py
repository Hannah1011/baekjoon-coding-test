arr = []
for _ in range(9):
    arr.append(int(input()))

max_Val = max(arr)

for i in range(9):
    if arr[i] == max_Val:
        print(max_Val)
        print(i+1)