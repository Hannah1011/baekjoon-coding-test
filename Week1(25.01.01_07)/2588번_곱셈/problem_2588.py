n1 = int(input())
n2 = list(map(int, input())) 

n3 = n1 * n2[2]
n4 = n1 * n2[1]
n5 = n1 * n2[0]

result = n3 + n4*10 + n5*100
print(n3)
print(n4)
print(n5)
print(result)