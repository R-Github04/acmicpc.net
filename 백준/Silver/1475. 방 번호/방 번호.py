s = input()

li = [
s.count("0"),
s.count("1"),
s.count("2"),
s.count("3"),
s.count("4"),
s.count("5"),
s.count("6"),
s.count("7"),
s.count("8"),
s.count("9")
]

six_nine_sets = (li[6] + li[9] + 1) // 2
max_other_sets = max(li[:6] + li[7:9] + li[10:])

result = max(six_nine_sets, max_other_sets)

print(result)