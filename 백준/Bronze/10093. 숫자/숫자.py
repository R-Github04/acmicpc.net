def print_numbers_between(a, b):
    if (not (a == b)) or (a - b != 1) or (b - a != 1) : 
        start, end = min(a, b), max(a, b)
        numbers = list(range(start + 1, end))
        
        print(len(numbers))
        if len(numbers) > 0:
            print(*numbers)
    else : print(0)

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
print_numbers_between(a, b)