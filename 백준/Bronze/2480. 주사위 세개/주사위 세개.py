a, b, c = map(int, input().split())  # 백준에서 런타임에러 남

if a == b == c :
    prize = 10000 + a * 1000
elif a == b :
    prize = 1000 + a * 100
elif a == c :
    prize = 1000 + a * 100
elif b == c :
    prize = 1000 + b * 100
else :
    prize = max(a, b, c) * 100
    
print(prize)