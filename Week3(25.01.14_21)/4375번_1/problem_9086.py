import sys
# 입력 첫 줄 테스트 케이스 개수 T
T = int(input())

#각 테스트 케이스 한줄에 하나의 문자열
S = []
for i in range(T):
    S_in = sys.stdin.readline().rstrip('\n')
    S.append(S_in)
for i in range(T):
    print(S[i][0] + S[i][len(S[i])-1])