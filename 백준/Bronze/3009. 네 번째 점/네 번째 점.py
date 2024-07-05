x_li = []
y_li = []
for i in range(3) : 
    x, y = map(int, input().split())
    x_li.append(x)
    y_li.append(y)

print(x_li[0] ^ x_li[1] ^ x_li[2])
print(y_li[0] ^ y_li[1] ^ y_li[2])