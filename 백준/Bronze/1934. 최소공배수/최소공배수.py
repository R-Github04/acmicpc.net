def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

li = []
t = int(input())
for i in range(t) : 
    a, b = map(int, input().split())
    li.append(lcm(a, b))
for i in li : 
    print(i)