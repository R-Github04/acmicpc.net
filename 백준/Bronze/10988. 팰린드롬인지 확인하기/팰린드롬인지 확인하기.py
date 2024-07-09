s = input()

def func(s) : 
    for i in range((len(s)//2)) : 
        if s[i] == s[(-1*(i+1))] : pass
        else : return 0
    return 1

print(func(s))