# 숫자 1까지 2초 한칸씩 이동할 때마다 1초
# 아스키코드 ord()

#1. 문자열 대문자로 받기 
#2. 아스키 코드로 바꾸기
#3. 각 숫자에 대해 2, 3,4,,, 이렇게 됨. 즉. 숫자에 +1 함. 
S = input()
sa =[]
for i in S:
    if i == 'A' or i == 'B' or i == 'C' :
        sa.append(2)
    elif i == 'D' or i == 'E' or i == 'F' :
        sa.append(3)
    elif i == 'G' or i == 'H' or i == 'I' :
        sa.append(4)
    elif i == 'J' or i == 'K' or i == 'L' :
        sa.append(5)
    elif i == 'M' or i == 'N' or i == 'O' :
        sa.append(6)
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S' :
        sa.append(7)
    elif i == 'T' or i == 'U' or i == 'V' :
        sa.append(8)
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z' :
        sa.append(9)
sum=0
for j in sa:
    j = int(j)
    if j != 0:
        sum = sum + j+1
    else:
        sum = sum + 11
print(sum)


