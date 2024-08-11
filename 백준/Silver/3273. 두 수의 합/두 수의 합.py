def two_sum(n, numbers, x):
    numbers.sort()  # 수열을 오름차순으로 정렬
    count = 0
    left, right = 0, n - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == x:
            # 같은 수가 여러 개 있을 수 있으므로 중복 처리
            if numbers[left] == numbers[right]:
                count += (right - left) * (right - left - 1) // 2
                break
            else:
                # 왼쪽과 오른쪽에서 같은 수가 몇 개 있는지 확인
                same_left, same_right = 1, 1
                while left + 1 < right and numbers[left] == numbers[left + 1]:
                    same_left += 1
                    left += 1
                while right - 1 > left and numbers[right] == numbers[right - 1]:
                    same_right += 1
                    right -= 1
                count += same_left * same_right
                left += 1
                right -= 1
        elif current_sum < x:
            left += 1
        else:
            right -= 1

    return count

# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

# 결과 출력
result = two_sum(n, numbers, x)
print(result)