def two_sum(numbers, x):
    count = 0
    seen = set()

    for num in numbers:
        if x - num in seen and x - num != num:
            count += 1
        seen.add(num)

    return count

# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

# 결과 출력
result = two_sum(numbers, x)
print(result)