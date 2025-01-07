import sys

sys_input = lambda : sys.stdin.readline().rstrip()

T = int(sys_input())
array = []
for _ in range(T):
    A, B = map(int, sys_input().split())
    array.append(A+B)

for result in array:
    print(result)