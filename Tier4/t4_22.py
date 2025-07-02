def check_nums(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum  

nums = [10, 20, 30, 40, 50]

total, avg, highest, lowest = check_nums(nums)

print(f"Sum: {total}")
print(f"Average: {avg}")
print(f"Max: {highest}")
print(f"Min: {lowest}")