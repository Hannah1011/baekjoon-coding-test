results = []
while True: 
    A,B = map (int, input().split())
    if A==0 and B==0 : break
    else:
        results.append(A+B)
        
for result in results:
    print(result)