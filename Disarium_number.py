def is_disarium(number):
    digits = list(str(number))
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(digits))
    return disarium_sum == number

# Test the function
n=int(input())
if is_disarium(n):
    print(True)
else:
    print(False)