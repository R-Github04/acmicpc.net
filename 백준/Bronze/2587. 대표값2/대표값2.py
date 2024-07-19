def calculate_median_and_mean(numbers):
    # Sort the numbers
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    # Calculate median
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    
    # Calculate mean
    mean = sum(numbers) / n
    
    return median, mean

# Input numbers
numbers = []
for _ in range(5) : 
    numbers.append(int(input()))

# Calculate median and mean
median, mean = calculate_median_and_mean(numbers)

# Print results
"""
print(f"입력값: {numbers}")
print(f"중앙값: {median}")
print(f"평균: {mean}")
"""

print(int(mean))
print(int(median))