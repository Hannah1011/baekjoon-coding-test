d = input()

if len(d) <= 50 and len(d) > 0 :
    if all(char.islower() for char in d):
        print(d + "??!")