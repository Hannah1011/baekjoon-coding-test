# 상수가 세자리 두개 칠판에 씀. 
A,B = input().split()

# 거꾸로 읽음
A = int(A[::-1])
B = int(B[::-1])

# 큰 수 말함
print (A) if A>B else print(B)