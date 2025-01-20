# 테스트 케이스 개수 T
# 각 테스트 케이스는 반복회수 R , 문자열 S가 공백으로 구분되어 주어짐. 
T = int(input())

for _ in range(T):
    cnt, word = input().split()
    for x in word:
        print(int(cnt) * x, end='')
    print()