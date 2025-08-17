import math

def greatest_divisor(numbers):
    result = numbers[0]
    for a in numbers[1:]:
        result = math.gcd(result, a)
    return result

n = int(input())
arr = list(map(int, input().split()))

print(greatest_divisor(arr))
