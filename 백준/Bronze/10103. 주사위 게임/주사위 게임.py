n = int(input())
li = []
ra, rb = 100, 100
for _ in range(n) : 
    a, b = map(int, input().split())
    if a == b : pass
    elif a > b : 
        rb -= a
    elif b > a : 
        ra -= b
print(ra)
print(rb)