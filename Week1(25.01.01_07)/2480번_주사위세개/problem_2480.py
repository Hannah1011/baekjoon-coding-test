# 첫 시도 코드 (맞음. 하지만 비효율적이라고 판단됨)
'''
a,b,c = map(int, input().split())

if ( a == b == c):
    print(10000 + a * 1000)
elif ( a == b and b != c):
    print(1000 + a * 100)
elif ( b == c and c != a) :
    print(1000 + b * 100)
elif ( a == c and c != b) :
    print(1000 + a * 100)
else:
    print(max(a,b,c)*100)
'''

# 최적화된 코드 버전1  : 빈도를 사용하는 코드
'''
from collections import Counter

a,b,c = map(int, input().split())

count = Counter([a,b,c]) # 주사위 값의 빈도 계산
if 3 in count.values() : # 값이 3개 모두 같은 경우
    print(10000 + a * 1000)
elif 2 in count.values() : # 값이 2개만 같은 경우
    same_num = [key for key, value in count.items() if value == 2][0]
    print(1000 + same_num * 100)
else: # 모두 다른 경우
    print(max(a,b,c)*100)
'''


# 최적화된 코드 버전 2: 정렬 활용하는 코드
a,b,c = sorted(map(int, input().split()))

if a == c: # 값이 다 같은 경우
    print(10000 + a * 1000)
elif a == b or b == c : # 두 값이 같은 경우
    print(1000 + b * 100)
else: # 모두 다른 경우
    print(c * 100) 