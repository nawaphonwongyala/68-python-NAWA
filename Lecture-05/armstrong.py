def is_armstrong(numbers):
    str_num = str(numbers)
    all = len(str_num)
    total = sum(int(digit) ** all for digit in str_num)
    result = " + ".join(f"{digit}^{all})" for digit in str_num)
    return print(total == numbers, f"({total} = {result})")

is_armstrong(153)
is_armstrong(9474)
is_armstrong(123)