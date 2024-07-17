t = int(input())
li = []

while t : 
    ali, bli = [], []
    n = int(input())
    for _ in range(n) : 
        a, b = input().split()
        ali.append(a)
        bli.append(int(b))
    li.append(ali[bli.index(max(bli))])
       
    t -= 1

for i in li : print(i)