n = int(input())
c = 0
for i in range(n) : 
    v = int(input())
    if v == 1 : c += 1

if n - c > c : print("Junhee is not cute!")
else : print("Junhee is cute!")