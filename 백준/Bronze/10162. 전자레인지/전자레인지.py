a, b, c = 300, 60, 10
t = int(input())

if t % c != 0 : print(-1)
else : 
    print(t//a, (t%a)//b, (t%a%b)//c)