g = input()
g_li = ["D", "C", "B", "A"]
g_li2 = ["-", "0", "+"]

s = 0.0

for i in range(len(g_li)) : 
    if g[0] == g_li[i] : 
        s = i+1

for i in range(len(g_li2)) : 
    try : 
        if g[1] == g_li2[i] : 
            s_ = 0.3 * (i - 1)
    except :
        s_ = 0.0

print(s + s_)