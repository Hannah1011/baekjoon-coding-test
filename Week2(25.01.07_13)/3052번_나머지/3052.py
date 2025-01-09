numbers = set()

for _ in range(10):
    n = int(input())
    numbers.add(n%42)

print(len(numbers))