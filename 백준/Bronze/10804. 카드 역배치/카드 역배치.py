li = [i for i in range(1, 20 + 1)]
for _ in range(10) : 
    a, b = map(int, input().split())
    li = li[:a - 1] + list(reversed(li[max(a - 1, 0):b])) + li[b:]
    
for i in li : 
    print(i, end = " ")