matrix = []
for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

max = -1
row, col = 0, 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max:
            max = matrix[i][j]
            row, col = i, j
print(max)
print(row+1, col+1)