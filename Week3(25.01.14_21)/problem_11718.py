# 입력 받은 대로 그대로 출력
# 🍀 코딩테스트 팁!!! : 별도의 조건 없이 입력값만 나열된 경우, EOF Error 를 통해 break 한다. 
while True:
    try:
        print(input())
    except EOFError:
        break