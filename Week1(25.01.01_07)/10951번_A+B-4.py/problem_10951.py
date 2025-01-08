results = []
while True: 
    try: 
        A,B = map (int, input().split())
        results.append(A+B)
    except: 
        break
        
for result in results:
    print(result)