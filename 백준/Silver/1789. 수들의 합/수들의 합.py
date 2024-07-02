s = int(input())
n = 1
while n != 0 :
    n += 1
    if n**2 + n > 2*s :
        print(n-1)
        break