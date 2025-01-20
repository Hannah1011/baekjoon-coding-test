import sys

#입력 처리
input = sys.stdin.read().split()

for num in input:
    n = int(num)
    number = 1
    digit = 1
    
    while number % n !=0:
        number = number *10 +1
        digit += 1
    
    print(digit)