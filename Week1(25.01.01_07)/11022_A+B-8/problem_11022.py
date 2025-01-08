'''
T = int(input())
Aa = []
Ba= []
results = []
for _ in range(T):
    A,B = map (int, input().split())
    Aa.append(A)
    Ba.append(B)
    results.append(A+B)
    
for i in range(T):
    print(f"Case #{i+1}: {Aa[i]} + {Ba[i]} = {results[i]}")
'''

# Another solution
T = int(input())
cases = []
for _ in range(T):
    A,B = map(int, input().split())
    cases.append((A,B)) #A와 B를 튜플로 저장

for i, (A,B) in enumerate(cases, start=1):
    print(f"Case #{i}: {A} + {B} = {A+B}")